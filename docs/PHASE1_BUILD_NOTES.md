# Phase 1 Build Notes

## Scope shipped

- Single Sonnet 4.6 gate-pass checker (`layers/gate_checker/`).
- G1 (category-frame integrity) + G2 (contamination / capture-vs-identity) only.
- Structured JSON output via tool-use (the model must call `report_gate_verdict` exactly once; no free-text response).
- 12-concept hand-written golden set (`tests/golden_concepts/concepts.json`) covering 4 PASS / 4 ITERATE / 4 KILL.
- Two-run agreement test runner (`scripts/run_agreement_test.py`) — reports overall and per-gate verdict agreement plus ground-truth accuracy.
- Anthropic prompt caching on the context-layer system block (the bulk of input tokens; cached after first call).

## Scope explicitly NOT shipped

- User-as-hero check (deferred — see `OPEN_ITEMS.md` item B).
- Memory-anchor placement scoring.
- Misread risk scoring.
- Protagonist axis alignment.
- Constraint-first verification.
- Feedback synthesizer as a separate sub-agent (collapsed into the same call).
- Script maker, brief layer, evaluator pre/post-prod, measurement layer.
- Web app, auth, UI.

## Architecture decisions worth recording

1. **Single API call per concept.** Phase 1 collapses G1, G2, and feedback synthesis into one Sonnet call. Cleaner to validate two-run agreement against; trivial to split into three calls later if quality degrades.
2. **Tool-use over free-text JSON.** `tool_choice` forces the model to call `report_gate_verdict` exactly once with a strict schema (no JSON-mode parse failures, no missing fields).
3. **Temperature 1.0 for the agreement test.** Tests prompt stability under noise. A temperature-0 self-agreement test would be trivially passable and would NOT validate that the gate definitions are encoded tightly enough.
4. **Prompt caching on the context layer.** Context layer (~1200 tokens) is cached. After the first call in any batch, subsequent calls hit the cache at 10% of input pricing.
5. **G1 and G2 only — user-as-hero pushed up to script maker.** Per Nikhil's call. Phase 1 stays tight to the Framework's "two binary gates"; user-as-hero becomes a Phase-2 script-maker input constraint where it's enforced at generation time rather than filtered at gate time.

## Running the agreement test

```powershell
cd C:\Users\nikhi\wiom-maker-checker
.\.venv\Scripts\Activate.ps1
python scripts\run_agreement_test.py
```

Cost: 12 concepts × 2 runs = 24 calls. Cached context layer; each call is ~1.3k input (mostly cached) + ~0.5k output. Estimated total cost: under $0.10 USD.

## Success criteria (brief §17 #1)

> Two independent runs of the gate-pass checker on the same concept produce the same verdict at >90% consistency on a golden test set of 20 concepts.

Phase 1 ships with 12 concepts (the brief says 10-15 for Phase 1 testing; 12 is in range; the §17 criterion's reference to 20 concepts can be addressed by expanding the golden set in later iterations).

Pass threshold: **overall_verdict_agreement_pct >= 90.0**.

The agreement test script exits with code 0 if the threshold is met, code 2 if not.

## Failure modes to watch for in the first run

1. **G2 over-rejection on "WiFi" capture-bridge.** If PASS-02 and ITERATE-04 come back as FAIL on G2 with role_classification=identity, the prompt is over-indexed on word presence and not reading role. Tighten the G2 section of `reference/context_layer.md`.

2. **Mobile-data-product misread under-detection.** If KILL-01 comes back as ITERATE rather than KILL, the no_frame_drift check is not weighting mobile-data-product hard enough. Strengthen the dangerous-misread priority language.

3. **ITERATE vs KILL drift.** The most subjective call. If runs A and B disagree on ITERATE vs KILL at >2 concepts (out of 12), the prompt needs sharper language on "four-word fix possible" vs "concept built on wrong frame".

4. **Brand-as-hero (KILL-04) misclassified as ITERATE.** Concept has no ghar anchor at all. If returned as ITERATE, G1's reasoning is being too charitable. Strengthen "If a reviewer must supply the ghar anchor themselves to make the ad cohere, it fails."

## What to do if the test fails (<90% agreement)

1. Read the JSONL log: `logs/agreement_<timestamp>.jsonl`. Look at the rows where A and B disagreed.
2. For each disagreement, examine the per-run reasoning. The disagreements usually cluster around a specific edge-case the prompt is ambiguous on.
3. Sharpen the relevant section of `reference/context_layer.md` (or add an explicit clause to the relevant gate definition).
4. Re-run.

The two-run agreement test is fast (~3-4 min total) and cheap, so iteration is cheap.
