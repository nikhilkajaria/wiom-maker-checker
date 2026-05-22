"""System + user prompt builders for the Phase-1 gate-pass checker (G1 + G2)."""
from __future__ import annotations

from pathlib import Path

from shared.anthropic_client import project_root


def load_context_layer() -> str:
    """Return the compiled context layer markdown, used as a cached system-prompt segment."""
    path = project_root() / "reference" / "context_layer.md"
    return path.read_text(encoding="utf-8")


SYSTEM_PROMPT_PREAMBLE = """You are the Wiom gate-pass checker. You evaluate Wiom activation creative concepts against two binary gates: G1 (category-frame integrity) and G2 (contamination / kill-list).

Your job is narrow and disciplined:
- Apply the gates exactly as defined in the context below. Do not invent new gates.
- Do not assess story structure, protagonist axis, format quality, or production craft. Those are out of Phase-1 scope.
- Do not fail a creative on user-as-hero grounds in Phase 1. That is a script-maker input constraint, not a gate here.
- Do not fail a creative on constraint-first grounds — constraint-first is a hypothesis, not a gate.
- For G2, check the ROLE a kill-list word plays (capture-bridge vs identity), not its mere presence. Blanket-failing any creative containing "WiFi" is the most common error to avoid.

You must respond by calling the `report_gate_verdict` tool exactly once. Do not write a free-text response.
"""


def build_system_blocks() -> list[dict]:
    """Return the system-prompt blocks with prompt caching enabled on the context layer.

    The context layer is large and reused on every call — cache it. Anthropic prompt caching
    requires `cache_control: {"type": "ephemeral"}` on the block to cache.
    """
    context_layer = load_context_layer()
    return [
        {
            "type": "text",
            "text": SYSTEM_PROMPT_PREAMBLE,
        },
        {
            "type": "text",
            "text": "# Wiom context (reference)\n\n" + context_layer,
            "cache_control": {"type": "ephemeral"},
        },
    ]


GATE_CHECK_TOOL = {
    "name": "report_gate_verdict",
    "description": "Report the gate-pass verdict for a Wiom activation creative concept. Must be called exactly once.",
    "input_schema": {
        "type": "object",
        "additionalProperties": False,
        "required": ["g1", "g2", "overall_verdict", "overall_reasoning"],
        "properties": {
            "g1": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "verdict",
                    "ghar_anchor_present",
                    "recharge_shape_clear",
                    "no_frame_drift",
                    "reasoning",
                    "fix_suggestion",
                ],
                "properties": {
                    "verdict": {"type": "string", "enum": ["PASS", "FAIL"]},
                    "ghar_anchor_present": {"type": "string", "enum": ["PASS", "FAIL"]},
                    "recharge_shape_clear": {"type": "string", "enum": ["PASS", "FAIL"]},
                    "no_frame_drift": {"type": "string", "enum": ["PASS", "FAIL"]},
                    "reasoning": {
                        "type": "string",
                        "description": "2-4 sentences citing specific lines / visuals from the concept that drove each sub-check.",
                    },
                    "fix_suggestion": {
                        "type": "string",
                        "description": "If verdict is FAIL and the fix is a four-word add or single-line rewrite, state the exact fix. If FAIL is conceptual (no quick fix), state 'KILL: <one-sentence reason>'. If PASS, return an empty string.",
                    },
                },
            },
            "g2": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "verdict",
                    "kill_list_words_used",
                    "role_classification",
                    "reasoning",
                    "fix_suggestion",
                ],
                "properties": {
                    "verdict": {"type": "string", "enum": ["PASS", "FAIL"]},
                    "kill_list_words_used": {
                        "type": "array",
                        "description": "Exact kill-list words/phrases that appear in the concept. Empty if none.",
                        "items": {"type": "string"},
                    },
                    "role_classification": {
                        "type": "string",
                        "enum": ["none", "capture_bridge", "identity", "mixed"],
                        "description": "'none' if no kill-list words. 'capture_bridge' if used only in user's voice at the hook and the creative converts to RWGKN. 'identity' if any usage defines what Wiom IS. 'mixed' if both roles appear (treat as identity-violating).",
                    },
                    "reasoning": {
                        "type": "string",
                        "description": "2-4 sentences citing the specific line(s) where kill-list words appear and the role classification rationale.",
                    },
                    "fix_suggestion": {
                        "type": "string",
                        "description": "If FAIL and fixable, state the exact rewrite. If conceptual KILL, state 'KILL: <reason>'. If PASS, return an empty string.",
                    },
                },
            },
            "overall_verdict": {
                "type": "string",
                "enum": ["PASS", "ITERATE", "KILL"],
                "description": "PASS = both gates pass. ITERATE = one or both gates fail on a structural-only issue fixable by a four-word add or single-line rewrite. KILL = one or both gates fail on a conceptual issue (built on the wrong frame; primary mobile-data-product misread; cheap-WiFi identity).",
            },
            "overall_reasoning": {
                "type": "string",
                "description": "1-3 sentences justifying the overall verdict, especially the ITERATE-vs-KILL distinction when relevant.",
            },
        },
    },
}


def build_user_message(concept: dict) -> str:
    """Render a concept dict as the user message for the gate-pass call.

    Expected concept fields: concept_id, format, script_or_copy, visual_description, notes (optional).
    """
    lines = [
        "Evaluate this Wiom activation creative concept against G1 and G2.",
        "",
        f"**Concept ID:** {concept['concept_id']}",
        f"**Format:** {concept.get('format', 'unspecified')}",
        "",
        "**Script / copy:**",
        concept.get("script_or_copy", "(not provided)"),
        "",
        "**Visual description:**",
        concept.get("visual_description", "(not provided)"),
    ]
    if concept.get("notes"):
        lines += ["", "**Notes:**", concept["notes"]]
    lines += [
        "",
        "Call `report_gate_verdict` with your evaluation. Cite specific lines from the script and specific elements from the visual description in your reasoning.",
    ]
    return "\n".join(lines)
