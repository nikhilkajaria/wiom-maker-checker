# Open Items — Phase 1 build

**Last updated: 2026-06-03.** Items A–I were from the original Phase 1 build. Items J–N added after Taxonomy v1.3 and June-1 wave evaluation.

---

Tracked deviations and unresolved questions surfaced while building Phase 1. Update as items close.

## A. JZUR phrasing — RESOLVED, canonical with SD's rule-vs-benefit framing

**Item:** The brief §4 introduces "Jitni zarurat utna recharge" (JZUR) as the bridge benefit template. None of the four source docs contain this phrase. The closest is "Jitna chahiye utna recharge" in the Context Note ("Messaging direction" section, listed informally, not named as an anchor).

**Status: RESOLVED (2026-05).** Nikhil + Shiva + SD aligned in Slack thread. Canonical framing:

- **JDRUDN ("Jitne din recharge, utne din net") = the RULE.** Tells people *how this thing works*. Specific operating logic. Locked because invariant. Analogies SD wants the team to use verbatim:
  - "Ticket kharido → movie dekho."
  - "Button dabao toh paani niklega."

- **JZUR ("Jitni zarurat, utna recharge") = the BENEFIT.** Tells people *why this rule is useful*. Emotional / value explanation. Flexes per need-state. Analogies:
  - "Paise waste nahi honge."
  - "Jab pyaas lage tab use karo."

- **Both are needed in creatives.** Rule alone leaves no felt benefit; benefit alone leaves no understanding of how.

- **Locked memory line stays as JDRUDN (not Shiva's interim variant "Jitne din recharge, utne din ghar ka net").** The ghar anchor lives in RWGKN itself — the rule does not need to re-carry it. SD's final position.

- **Three-rung guard:** JZUR sits *between* the rule and the emotional anchor as the connective benefit line. It does NOT displace "Chale aapke hisaab se" (which does a different job — how-it-feels / user agency). Three rungs, three jobs. JZUR is the bridge, not a fourth rung.

**Updates made to the build:**
- `reference/context_layer.md` §2 expanded with SD's framing + analogies (used verbatim as teaching devices).
- `reference/memory_anchors.json` includes the rule-vs-benefit split with both analogy sets.

**Action items remaining:**
- Update Context Note and Outreach Annexure source docs to add JZUR explicitly. **Owner: Shiva.** The four reference .docx files in `docs/source_docs/` are pre-this-alignment snapshots.

---

## B. User-as-hero — deferred from Phase 1 gates; lives as a script-maker input constraint

**Item:** Brief §7 names user-as-hero as a v1 check. §16 Phase 1 omits it. Framework lists only G1 and G2 as binary gates; Principles §3 mandates user-as-hero as a strong rule but does not promote it to a binary gate.

**Resolution (this build):** Phase 1 is strictly G1 + G2. User-as-hero is encoded as a **strong input-level constraint on the script maker layer** (Phase 2) — the script maker is prompted to construct concepts that satisfy user-as-hero by design, rather than the gate-pass checker filtering for it post-hoc.

**Action items (Phase 2):**
- Encode user-as-hero in the script-maker system prompt as a hard constraint: "User / household is the emotional center. Wiom is the enabler. The product/brand is never the emotional center of the creative."
- Consider whether to add a Phase-2 "user-as-hero verification" sub-check inside the script-maker's self-review loop (not a checker gate, an output-validation step before handing to the gate-pass checker).

**Owner:** Nikhil.

---

## C. JDRUDN strictness softened from "everywhere" to "at least once verbatim"

**Item:** Source docs say repetition is the strategy — "said everywhere", "every surface reinforces them repeatedly". Brief §4 + §6 soften this to "verbatim at least once (typically end-slate)" + free articulation elsewhere.

**Resolution (this build):** Context layer in Phase 1 follows the brief's softer rule. G1 checks for ghar anchor + recharge-shape clarity but does not require JDRUDN verbatim multiple times in a 15-second creative.

**Action items:**
- Worth a brief SD review to confirm the softening is intentional. Defensible for short-format activation creative; not defensible if applied to longer-format films.
- Revisit when adding longer-format support.

**Owner:** Shiva.

---

## D. Two-run agreement test = model self-consistency, not true gate-tightness

**Item:** Brief §17 success criterion #1 reframes the Framework's "two reviewers" question as "two model runs." A model is more self-consistent than two independent humans would be, so passing this test does NOT prove gate definitions are tight enough to survive disagreement between two human reviewers.

**Resolution (this build):**
- Phase 1 agreement test runs each concept twice (the brief's criterion) AND reports ground-truth accuracy against gold labels (a stronger test of gate tightness).
- We accept the brief's success threshold (≥90% two-run agreement) but treat ground-truth accuracy as the diagnostic signal worth watching.

**Action items:**
- Once Phase 6 (web app + human reviewers) lands, re-run the gate-tightness test with two humans evaluating the same concepts. The Framework's original question is properly answered only there.

**Owner:** Nikhil (Phase 6 owner).

---

## E. Single-agent collapse for Phase 1 vs §7's three sub-agent target

**Item:** §7 specifies three Phase-1 sub-agents (G1 agent, G2 agent, feedback synthesizer). §16 Phase 1 says single agent. Phase 1 build collapses all three responsibilities into one Sonnet 4.6 call.

**Resolution (this build):** Single call. Tool-use enforces structured output covering all three responsibilities (G1 verdict + reasoning, G2 verdict + reasoning, overall verdict + reasoning, fix suggestions).

**Trigger to revisit:** If two-run agreement drops below 90% or per-gate reasoning quality degrades, split into separate G1 and G2 calls (with the feedback synthesizer as a third call). The prompt structure is already organized to make the split mechanical.

---

## F. Model id and API verification

**Item:** Phase 1 uses `claude-sonnet-4-6`. Per system info, this is the current Sonnet 4.6 model ID.

**Action items:**
- Confirm against `https://docs.claude.com` pricing page that input/output token rates are current. The cost estimator in `layers/gate_checker/checker.py` assumes $3/Mtok input, $15/Mtok output, cache-create 1.25x input, cache-read 0.1x input. Adjust if pricing has shifted.

**Owner:** Anyone running the build.

---

## H. Golden-set calibration — ITERATE-04 revised to KILL after first agreement run — PARTIALLY RESOLVED

**Item:** On the first run (2026-05-22), both independent runs of the gate-pass checker classified ITERATE-04 as KILL, with consistent and rigorous reasoning: the concept has no ghar anchor, no RWGKN conversion in the body, and no JDRUDN — three independent structural gaps that no four-word add or single-line rewrite can fix. The gold label was originally ITERATE (G2 PASS) on the rationale that "sasta WiFi" was a rhetorical-question capture-bridge.

**Resolution:** Gold label revised to **KILL / G1 FAIL / G2 FAIL**. The model's reasoning was correct: because the creative never converts away from the WiFi frame, "sasta WiFi" ends up *defining* the frame the user is left in — which is identity use, not capture-bridge use. The model is enforcing the gate definition more strictly than the original gold did.

**Action items:**
- Add a replacement genuine-ITERATE concept in the next golden-set iteration to preserve 4 PASS / 4 ITERATE / 4 KILL composition. Design: take a clean PASS-shaped concept and break exactly ONE element (e.g., omit the locked JDRUDN end-slate; otherwise leave ghar anchor and RWGKN body intact). That makes the fix a literal single-line rewrite, which is the canonical ITERATE case.
- Expand golden set from 12 to 20 concepts (the brief §17 #1 references 20). The marginal calls cluster around the ITERATE/KILL boundary — that's where more golden coverage adds the most signal.

**Owner:** Nikhil (this build).

---

## I. First-run results — 2026-05-22

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Overall verdict agreement (run A vs run B) | 100.0% (12/12) | ≥ 90% (brief §17 #1) | PASS |
| G1 verdict agreement | 100.0% | — | clean |
| G2 verdict agreement | 91.7% (11/12) | — | one disagreement on PASS-02 internally (overall still PASS in both runs) |
| Run A ground-truth accuracy | 91.7% (11/12) | informational | one disagreement on ITERATE-04 (now revised — see item H) |
| Run B ground-truth accuracy | 91.7% (11/12) | informational | same |
| Total cost | $0.3715 | — | ~$0.015 / call |
| Total latency | ~6.5 min | — | sequential; could be parallelized for production |

Log: `logs/agreement_20260522T105603Z.jsonl` + `.summary.json`.

After applying the item-H gold revision, ground-truth accuracy is effectively 100% on both runs.

---

## G. Anthropic SDK version pin

**Item:** `requirements.txt` pins `anthropic==0.40.0`. Verify this version supports `cache_control` on system blocks and tool-use with `tool_choice={"type":"tool","name":"..."}`.

**Action items:**
- If SDK version drift breaks the build, update the pin and adjust the call shape in `layers/gate_checker/checker.py`.

---

## J. Audience layers added to context_layer.md — RESOLVED (2026-06-03)

**Item:** The L1/L2/L3 audience-layer framework (Messaging System v1.3) was entirely absent from the context layer. The checker evaluated G1/G2 with no awareness of which layer a creative targets — meaning it could not apply layer-specific must-not-do rules, L3's "नेट as destination noun" rule, or detect L1 contamination risk.

**Resolution (2026-06-03):**
- `reference/context_layer.md` §8 added: full L1/L2/L3 layer definitions, objectives, bridges, must-not lists, proof structures, contamination risk, CTA intensity.
- `reference/context_layer.md` §9–12 added: craft rules (May sprint), JDRUDN/JZUR cash-vs-need routing, script-mixing convention, AI vox-pop credibility caveat.
- `reference/audience_layers.json` created: machine-readable layer definitions for Phase 2 script-maker.
- `reference/need_states.json` created: full need-state vocabulary including SDN-MULTI.
- `reference/memory_anchors.json` updated: cash-vs-need routing rule added.
- `Wiom_Messaging_System_v1.3.docx` added to `docs/source_docs/`.

**Action items remaining:**
- Add audience-layer checking to G1/G2 gate logic (Phase 2) — the checker currently evaluates gates without asking "which layer is this creative targeting?" A Phase 2 extension would require the concept brief to name its layer and the checker to apply layer-specific rules conditionally.
- **Owner:** Nikhil.

---

## K. L3 doctrine — in-context rule application — RESOLVED (2026-06-03)

**Item:** The "नेट must be the destination noun" rule for L3 was missing from the context layer, and when added must be framed as contextual (prior line/visual grounds the destination), not per-line mechanical. Evidence: S2 Variant was KILLed by the original checker using line-mechanical application; user override confirmed the creative passed because the prior PT line + lockup grounded the destination.

**Resolution (2026-06-03):**
- `reference/context_layer.md` §8 (L3 section) includes the rule with explicit IN-CONTEXT application language.
- `reference/audience_layers.json` L3 section includes `l3_critical_note` with override history.

**Action items remaining:**
- When Phase 2 adds L3-layer gate checking, implement the contextual test: "is there a prior line, visual, or lockup anywhere in the creative that grounds the घर-का-नेट destination?" — not "does this specific line use रिचार्ज as head noun?"
- **Owner:** Nikhil (Phase 2).

---

## L. SDN-MULTI added to vocabulary — RESOLVED (2026-06-03)

**Item:** SDN-MULTI (multi-occasion framing — multiple SDN sub-cases stacked in one creative) was missing from all reference files. Added to taxonomy v1.3 for F7 (script stacks cricket + exam).

**Resolution (2026-06-03):**
- `reference/need_states.json` SDN sub-cases includes SDN-MULTI with covariance flag.
- `reference/context_layer.md` mentions SDN-MULTI in §8 implicitly via the need_states reference.

**Covariance flag:** SDN-MULTI creative cannot be cleanly compared against a single-occasion creative without controlling for occasion-cardinality. Test T-PR-02 is flagged as 3-variable co-variance for this reason.

---

## M. Golden-set gaps — OPEN

**Item:** Multiple gaps in the golden set remain unaddressed:
1. No replacement genuine-ITERATE concept (after ITERATE-04 revised to KILL in item H).
2. Only 12 of target 20 concepts — 8 more needed, especially at ITERATE/KILL boundary.
3. No L3-layer concepts — all 12 are L1/L2-adjacent.
4. No SDN-MULTI concept.
5. No vox-pop format concepts.

**Action items:**
- Design and add 8 new golden concepts. Priority: 2 genuine-ITERATE (boundary cases), 2 L3 (TUF + HSE), 1 SDN-MULTI, 1 vox-pop PASS, 1 vox-pop ITERATE, 1 AI vox-pop to test the AI-credibility caveat.
- **Owner:** Nikhil.

---

## N. Real concept JSONs — stale / incomplete — OPEN

**Item:** `tests/real_concepts/` contains S1–S5, S7, S8 statics but:
1. S6 (SDN-WKC) is missing.
2. No film JSONs (F1–F12).
3. Naming convention mismatch: existing JSONs use `concept_id` like `JUN26-T-013-v1-produced`, not the canonical `JUN26-T-013`.
4. S2 Variant verdict in any related file would still say KILL — needs to reflect CRAFT REVIEW PASS override (Taxonomy v1.3).
5. F10 verdict if added would say INVALID — needs to reflect PENDING + override (Taxonomy v1.3).

**Action items:**
- Add S6 JSON.
- Add F1–F3, F8 film JSONs (these are Live in Meta; good to have in real_concepts for regression testing).
- Fix concept_id naming to match taxonomy primary key.
- Add a `verdict_overrides` field to the S2 Variant JSON noting the doctrine change.
- **Owner:** Nikhil.

---

## O. EVALUATION doc stale — OPEN

**Item:** `docs/EVALUATION_input_sheet_and_june1_wave.md` carries verdicts that are now outdated:
- S2 Variant: originally KILL, now CRAFT REVIEW PASS (Taxonomy v1.3, June 2026).
- F10: originally INVALID, now PENDING with override (Taxonomy v1.3, June 2026).
- T-PR-02: originally flagged as "compound contamination"; now upgraded to 3-VARIABLE CO-VARIANCE.

**Action items:**
- Update relevant sections of the EVALUATION doc to reflect the overrides.
- Add a "Revision trail" section at the top of the doc noting the update date and nature of changes.
- **Owner:** Nikhil.
