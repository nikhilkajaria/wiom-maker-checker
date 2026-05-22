# Wiom Maker-Checker — Phase 1

Phase 1 of the Wiom activation-creative maker-checker system per `docs/Wiom_Maker_Checker_Build_Brief.md` §16.

**Scope:** Gate-pass checker MVP only. G1 (category-frame integrity) + G2 (contamination / capture-vs-identity). Single Claude Sonnet 4.6 agent. Validates that two independent runs of the checker on the same concept agree on the verdict.

**Out of scope for Phase 1:**
- User-as-hero check (deferred to Phase 2 — applied as a script-maker input constraint, not a binary gate; see `docs/OPEN_ITEMS.md`).
- Script maker (Phase 2).
- Brief layer (Phase 3).
- Pre-prod evaluator (Phase 4).
- Post-prod evaluator (Phase 5).
- Web app, auth, UI (Phase 6).

## Setup

```powershell
cd C:\Users\nikhi\wiom-maker-checker
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

The Anthropic API key is loaded from `C:\credentials\.env` (`ANTHROPIC_API_KEY`). Do not put credentials in the project directory.

## Run

Check a single concept:
```powershell
python scripts\run_gate_check.py tests\golden_concepts\concepts.json --concept_id PASS-01
```

Run two-reviewer agreement test across the golden set:
```powershell
python scripts\run_agreement_test.py
```

Outputs land in `logs\` as timestamped JSONL.

## Architecture

- `reference/context_layer.md` — compiled context (cached as a system-prompt segment via Anthropic prompt caching). Verbatim memory anchors, dangerous-misreads priority, capture/convert split, gate definitions.
- `layers/gate_checker/prompts.py` — system + user prompt builders for the gate-pass agent.
- `layers/gate_checker/checker.py` — single Sonnet 4.6 call per concept; tool-use enforced structured JSON output.
- `tests/golden_concepts/concepts.json` — 12 hand-written concepts with ground-truth labels.
- `scripts/run_agreement_test.py` — agreement runner. Reports per-gate and overall verdict agreement across two independent runs of each concept, plus accuracy vs ground truth.

## Success criteria (from brief §17, applied to Phase 1)

1. Two independent runs of the gate-pass checker on the same concept produce the same overall verdict at ≥90% on the 12-concept golden set.
2. Ground-truth accuracy (each run vs gold label) reported as informational.
