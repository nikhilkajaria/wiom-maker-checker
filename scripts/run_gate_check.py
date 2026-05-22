"""CLI: run G1+G2 on a single concept from a concepts JSON file.

Usage:
    python scripts/run_gate_check.py tests/golden_concepts/concepts.json --concept_id PASS-01
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Make sibling packages importable when run as a script
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from layers.gate_checker import run_gate_check
from layers.gate_checker.checker import estimate_cost_usd


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("concepts_file")
    ap.add_argument("--concept_id", required=True)
    ap.add_argument("--temperature", type=float, default=1.0)
    args = ap.parse_args()

    concepts = json.loads(Path(args.concepts_file).read_text(encoding="utf-8"))
    concept = next((c for c in concepts if c["concept_id"] == args.concept_id), None)
    if concept is None:
        print(f"Concept {args.concept_id} not found in {args.concepts_file}")
        return 1

    result = run_gate_check(concept, temperature=args.temperature)
    cost = estimate_cost_usd(result.usage)

    print(json.dumps(
        {
            "concept_id": result.concept_id,
            "overall_verdict": result.overall_verdict,
            "overall_reasoning": result.overall_reasoning,
            "g1": result.g1,
            "g2": result.g2,
            "usage": result.usage,
            "estimated_cost_usd": round(cost, 6),
            "latency_seconds": round(result.latency_seconds, 2),
        },
        indent=2,
        ensure_ascii=False,
    ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
