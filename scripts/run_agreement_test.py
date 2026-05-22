"""Two-reviewer agreement test for Phase 1 gate-pass checker.

Runs each golden concept twice (independent calls, temperature 1.0) and reports:
- Overall-verdict agreement (run A vs run B) — target >= 90% per brief §17.
- G1-verdict agreement, G2-verdict agreement.
- Ground-truth accuracy per run.
- Total cost.

Output: logs/agreement_<timestamp>.jsonl (one line per run) + a human-readable summary on stdout.

Usage:
    python scripts/run_agreement_test.py
    python scripts/run_agreement_test.py --concepts_file tests/golden_concepts/concepts.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared.anthropic_client import get_client
from layers.gate_checker import run_gate_check
from layers.gate_checker.checker import estimate_cost_usd


def run_once(concept: dict, run_label: str, client) -> dict:
    result = run_gate_check(concept, temperature=1.0, client=client)
    return {
        "run_label": run_label,
        "concept_id": concept["concept_id"],
        "overall_verdict": result.overall_verdict,
        "g1_verdict": result.g1["verdict"],
        "g2_verdict": result.g2["verdict"],
        "g1_reasoning": result.g1["reasoning"],
        "g2_reasoning": result.g2["reasoning"],
        "g1_fix": result.g1["fix_suggestion"],
        "g2_fix": result.g2["fix_suggestion"],
        "overall_reasoning": result.overall_reasoning,
        "usage": result.usage,
        "estimated_cost_usd": estimate_cost_usd(result.usage),
        "latency_seconds": result.latency_seconds,
        "model": result.model,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--concepts_file",
        default=str(Path(__file__).resolve().parents[1] / "tests" / "golden_concepts" / "concepts.json"),
    )
    args = ap.parse_args()

    concepts = json.loads(Path(args.concepts_file).read_text(encoding="utf-8"))
    print(f"Loaded {len(concepts)} concepts from {args.concepts_file}")

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    log_dir = Path(__file__).resolve().parents[1] / "logs"
    log_dir.mkdir(exist_ok=True)
    log_path = log_dir / f"agreement_{timestamp}.jsonl"

    client = get_client()
    rows: list[dict] = []
    total_cost = 0.0

    with log_path.open("w", encoding="utf-8") as fh:
        for concept in concepts:
            cid = concept["concept_id"]
            print(f"  [{cid}] run A ...", end="", flush=True)
            row_a = run_once(concept, "A", client)
            print(f" {row_a['overall_verdict']} ({row_a['latency_seconds']:.1f}s)", flush=True)
            fh.write(json.dumps(row_a, ensure_ascii=False) + "\n")

            print(f"  [{cid}] run B ...", end="", flush=True)
            row_b = run_once(concept, "B", client)
            print(f" {row_b['overall_verdict']} ({row_b['latency_seconds']:.1f}s)", flush=True)
            fh.write(json.dumps(row_b, ensure_ascii=False) + "\n")

            total_cost += row_a["estimated_cost_usd"] + row_b["estimated_cost_usd"]
            rows.append(
                {
                    "concept_id": cid,
                    "gold_overall": concept["gold_overall_verdict"],
                    "gold_g1": concept["gold_g1"],
                    "gold_g2": concept["gold_g2"],
                    "a_overall": row_a["overall_verdict"],
                    "b_overall": row_b["overall_verdict"],
                    "a_g1": row_a["g1_verdict"],
                    "b_g1": row_b["g1_verdict"],
                    "a_g2": row_a["g2_verdict"],
                    "b_g2": row_b["g2_verdict"],
                }
            )

    n = len(rows)
    overall_agree = sum(1 for r in rows if r["a_overall"] == r["b_overall"])
    g1_agree = sum(1 for r in rows if r["a_g1"] == r["b_g1"])
    g2_agree = sum(1 for r in rows if r["a_g2"] == r["b_g2"])
    a_truth = sum(1 for r in rows if r["a_overall"] == r["gold_overall"])
    b_truth = sum(1 for r in rows if r["b_overall"] == r["gold_overall"])

    summary = {
        "n_concepts": n,
        "overall_verdict_agreement_pct": round(100 * overall_agree / n, 1),
        "g1_verdict_agreement_pct": round(100 * g1_agree / n, 1),
        "g2_verdict_agreement_pct": round(100 * g2_agree / n, 1),
        "run_a_ground_truth_accuracy_pct": round(100 * a_truth / n, 1),
        "run_b_ground_truth_accuracy_pct": round(100 * b_truth / n, 1),
        "total_estimated_cost_usd": round(total_cost, 4),
        "log_path": str(log_path),
        "passes_success_criterion_section_17_1": overall_agree / n >= 0.90,
    }

    print("\n=== Summary ===")
    print(json.dumps(summary, indent=2))

    print("\n=== Per-concept ===")
    print(f"{'concept_id':<12} {'gold':<8} {'run_A':<8} {'run_B':<8} {'agree?':<8} {'truth_A':<8} {'truth_B':<8}")
    for r in rows:
        agree = "✓" if r["a_overall"] == r["b_overall"] else "✗"
        truth_a = "✓" if r["a_overall"] == r["gold_overall"] else "✗"
        truth_b = "✓" if r["b_overall"] == r["gold_overall"] else "✗"
        print(
            f"{r['concept_id']:<12} {r['gold_overall']:<8} {r['a_overall']:<8} {r['b_overall']:<8} "
            f"{agree:<8} {truth_a:<8} {truth_b:<8}"
        )

    # Verdict distribution
    print("\n=== Verdict distribution ===")
    print(f"  Run A: {Counter(r['a_overall'] for r in rows)}")
    print(f"  Run B: {Counter(r['b_overall'] for r in rows)}")
    print(f"  Gold : {Counter(r['gold_overall'] for r in rows)}")

    # Write a summary JSON alongside the JSONL log
    summary_path = log_path.with_suffix(".summary.json")
    summary_path.write_text(json.dumps({"summary": summary, "rows": rows}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nDetailed rows -> {log_path}")
    print(f"Summary       -> {summary_path}")

    return 0 if summary["passes_success_criterion_section_17_1"] else 2


if __name__ == "__main__":
    sys.exit(main())
