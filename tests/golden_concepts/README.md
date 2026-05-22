# Golden concepts — Phase 1

12 hand-written activation creative concepts, each labeled with the expected verdict (PASS / ITERATE / KILL) and the gate(s) that should fire. Used by `scripts/run_agreement_test.py` to validate that the gate-pass checker is encoded tightly enough that two independent runs agree on the verdict (success criterion §17 #1, target ≥90%).

## Composition

| Bucket | Count | What's being tested |
|--------|-------|---------------------|
| PASS | 4 | Clean RWGKN concepts. Both gates should pass cleanly. |
| ITERATE | 4 | Single fixable structural issue (missing ghar anchor; buried recharge mechanic; one identity-claim line; bridge that fails to convert). |
| KILL | 4 | Conceptually broken (mobile-data-product framing; cheap-WiFi identity; broadband comparison; brand-as-hero with no ghar). |

## Calibration notes

- **PASS-02** explicitly opens with "WiFi lene jaa rahe ho?" in the user's voice — tests that the checker does NOT blanket-fail concepts containing "WiFi" (the most common error per context_layer.md §7).
- **ITERATE-04** opens with a kill-list word in capture-bridge style but the body never converts to RWGKN — tests the harder G1 "no frame drift" judgement (G2 might pass, G1 should fail on drift).
- **KILL-01** is the primary dangerous misread (mobile-data-product). Should fire on G1 no_frame_drift + KILL verdict (not ITERATE — no four-word fix).
- **KILL-04** has no ghar anchor and Wiom as the emotional center — tests that Phase-1's G1 catches the absent ghar anchor even when the concept's deeper problem (user-as-hero violation) is a Phase-2 concern.

## Editing the golden set

Add concepts as new objects in `concepts.json`. Each concept must include:
- `concept_id` (unique)
- `format`
- `script_or_copy`
- `visual_description`
- `gold_overall_verdict` (PASS / ITERATE / KILL)
- `gold_g1` (PASS / FAIL)
- `gold_g2` (PASS / FAIL)
- `gold_notes` (1-2 sentence rationale)
