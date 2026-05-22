"""Single-call Sonnet 4.6 gate-pass checker for G1 + G2."""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, asdict
from typing import Any

from anthropic import APIError

from shared.anthropic_client import MODEL_SONNET, get_client
from .prompts import GATE_CHECK_TOOL, build_system_blocks, build_user_message


@dataclass
class GateCheckResult:
    concept_id: str
    overall_verdict: str  # PASS | ITERATE | KILL
    overall_reasoning: str
    g1: dict[str, Any]
    g2: dict[str, Any]
    raw_response: dict[str, Any]
    usage: dict[str, Any]
    latency_seconds: float
    model: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def run_gate_check(
    concept: dict,
    *,
    temperature: float = 1.0,
    max_tokens: int = 1500,
    client=None,
) -> GateCheckResult:
    """Run G1+G2 on a single concept. Returns a GateCheckResult.

    Args:
        concept: dict with keys concept_id, format, script_or_copy, visual_description, notes (optional).
        temperature: sampling temperature. Default 1.0 to test prompt stability under noise (per success criterion §17).
        max_tokens: cap on response length.
        client: optional Anthropic client (reused across calls to avoid re-init).
    """
    client = client or get_client()
    system_blocks = build_system_blocks()
    user_message = build_user_message(concept)

    started = time.time()
    last_err: Exception | None = None
    for attempt in range(3):
        try:
            resp = client.messages.create(
                model=MODEL_SONNET,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system_blocks,
                tools=[GATE_CHECK_TOOL],
                tool_choice={"type": "tool", "name": GATE_CHECK_TOOL["name"]},
                messages=[{"role": "user", "content": user_message}],
            )
            break
        except APIError as e:
            last_err = e
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    latency = time.time() - started

    # Extract the tool_use block
    tool_block = next((b for b in resp.content if b.type == "tool_use" and b.name == GATE_CHECK_TOOL["name"]), None)
    if tool_block is None:
        raise RuntimeError(
            f"Model did not call report_gate_verdict for {concept['concept_id']}. "
            f"Content blocks: {[b.type for b in resp.content]}"
        )

    payload = tool_block.input  # already a dict

    usage = {
        "input_tokens": resp.usage.input_tokens,
        "output_tokens": resp.usage.output_tokens,
        "cache_creation_input_tokens": getattr(resp.usage, "cache_creation_input_tokens", 0),
        "cache_read_input_tokens": getattr(resp.usage, "cache_read_input_tokens", 0),
    }

    return GateCheckResult(
        concept_id=concept["concept_id"],
        overall_verdict=payload["overall_verdict"],
        overall_reasoning=payload["overall_reasoning"],
        g1=payload["g1"],
        g2=payload["g2"],
        raw_response=payload,
        usage=usage,
        latency_seconds=latency,
        model=MODEL_SONNET,
    )


def estimate_cost_usd(usage: dict[str, Any]) -> float:
    """Rough Sonnet-4.6 cost estimate. Pricing per https://docs.claude.com."""
    # Sonnet 4.6 (approx, as of writing): $3/Mtok input, $15/Mtok output.
    # Cached reads are 0.1x input price; cache creation is 1.25x input price.
    input_cost = usage["input_tokens"] * 3.0 / 1_000_000
    output_cost = usage["output_tokens"] * 15.0 / 1_000_000
    cache_create_cost = usage.get("cache_creation_input_tokens", 0) * 3.75 / 1_000_000
    cache_read_cost = usage.get("cache_read_input_tokens", 0) * 0.30 / 1_000_000
    return input_cost + output_cost + cache_create_cost + cache_read_cost
