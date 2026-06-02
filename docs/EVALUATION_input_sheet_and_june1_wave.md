# Evaluation — Creative Input Sheet + June-1 Activation Wave

**Date:** 2026-05-28
**Inputs evaluated:**
- `Wiom_Creative_Input_and_Evaluation.xlsx` (Creative Input tab + Evaluation Criteria tab)
- `Wiom_Static_Test_Design_final.docx` (9 statics + 1 wording variant)
- `Wiom_7Scripts_Unfiltrr_25May.docx` (F1–F7: 3 live vox pop + 4 green-screen comparison)
- `Wiom_F11_F12_Scripts_final.docx` (2 comparison-frame videos)
- `Wiom_3Films_Obvious_AI_25May.docx` (3 AI films = F8/F9/F10)

**Benchmark:** Performance Creative Framework v0.9 (+ Principles, Context Note, Annexure).

Severity key: 🔴 structural error · 🟠 discipline risk · 🟡 minor / watch · ✅ aligned.

---

## PART A — The sheet vs the Performance Creative Framework

### A.0 Headline

The **Evaluation Criteria** tab is a faithful, near-complete encoding of the framework's Layer-1→4 architecture (gates → variables → determined params → outcome ladder → 3-way decision). It is in fact *more* operational than the framework doc, and it correctly captures things my Phase-1 checker defers (Hero, Hygiene, Objective discipline). Strong.

The **Creative Input** tab is the issue. It is really a **production-spec sheet** (everything you decide when making a creative), not a **test-variable taxonomy** — and it mixes the two. The framework is explicit that there are exactly **4 test variables** (story structure, protagonist & credibility, need-state, format), tested **one at a time**, kept **orthogonal** so outcomes attribute cleanly. The sheet adds five more columns (production style, recharge-model, category-bridge, hero-entry, plus Objective) and folds a production method into a test variable. For *tagging/description* that's fine; for *test design* it's dangerous, because a user could co-vary a non-orthogonal axis with need-state and break single-variable discipline.

**#1 recommendation:** visually separate the sheet into **TEST AXES (4, orthogonal, single-variable)** vs **PRODUCTION SPEC (determined params / gate inputs / execution detail)**. Everything below is downstream of this.

### A.1 Column-by-column

| Sheet column | Framework status | Verdict |
|---|---|---|
| Objective: Campaign / Test | Not in framework; operationalizes "test one variable at a time" | ✅ useful addition |
| Need-state (10 values) | Exact match, Framework Table 5 | ✅ |
| Story structure | 9 of the values match Table 5 **but adds "AI / Non AI"** | 🔴 see A.2 |
| Protagonist/Credibility (6, peer→authority) | Exact match, ordered correctly | ✅ |
| Format (10 values) | Exact match, Table 5 | ✅ |
| Production style | New 5th axis; **overlaps Format** (screen-record, motion graphic in both) | 🟠 see A.3 |
| Recharge-model understanding (6) | New; operationalizes G1 "recharge-shape clear" — useful, **but lists "implicit/buried" as a value** | 🟠 see A.4 |
| Category bridge (6) | New; operationalizes capture/convert; flags "WiFi = bridge only" correctly | ✅ (minor: flag mobile-data bridge's misread risk) |
| Hero entry point (7) | New; operationalizes user-as-hero + constraint-first opening | 🟡 overlaps Story Structure (see A.5) |
| CTA (3) | 2 match Table 8; **adds "Wiom try karo" with no stage** | 🟠 see A.6 |
| End-slate / caption anchors | The 3 locked anchors | ✅ |
| Length (4) | New; reasonable, but **60s drifts toward ToF** for activation | 🟡 |
| Funnel stage (warm/hot) | Match, Table 8; correctly excludes cold/ToF | ✅ |
| Target geography (capacity-ready gate) | Encodes Principles "capacity leads demand" NEVER-rule | ✅ strong addition |
| Kill-list words (5) | Match Gate 2; **missing "ISP"** | 🟡 |

### A.2 🔴 "AI / Non AI" is mis-filed under Story Structure

AI-render vs live-shoot is a **production method**, not a narrative structure. It is orthogonal to story structure and collinear with nothing in that list. Filing it there means a "story-structure test" could accidentally be an AI-vs-live test. It also *is* a real axis the wave deliberately tests (F1 live vs F8 AI). **Fix:** pull it out of Story Structure; make it its own axis ("Production method: live / AI-rendered") — which is also where it interacts with Protagonist & Credibility (see B.4 on AI vox-pop).

### A.3 🟠 "Production style" overlaps "Format"

`screen-record/demo` and `motion graphic` appear in **both** Format and Production style; "real-person formats" restates Format values (vox pop, UGC, testimonial). The framework collapsed exactly this kind of redundancy to keep 4 orthogonal variables. **Fix:** either fold Production style into Format, or scope it tightly to the one distinction Format doesn't carry — real-person vs polished, and live vs AI (i.e., merge with A.2).

### A.4 🟠 "Rule implicit / buried" is a gate-fail, not a creative choice

Listing "Rule implicit/buried" as a selectable value of "Recharge-model understanding" contradicts G1 ("recharge-shape clear, **not buried**") and Principles §7D ("the rule must appear clearly and early; earlier work buried it too deep"). A buried rule should **fail** the recharge-shape sub-check, not be an option on the menu. **Fix:** keep the column (the other 5 values are a genuinely useful gradation of *how* the rule is conveyed) but move "implicit/buried" to the G1 fail criteria as the negative condition.

### A.5 🟡 Hero-entry overlaps Story-structure

"Open on user's constraint" (hero entry) ≈ "constraint-first" (story structure). Mild collinearity. Acceptable if Hero-entry is treated as execution detail *within* a held story structure, not as an independent test axis. Don't test it against need-state.

### A.6 🟠 "Wiom try karo" CTA has no stage

The framework rule is **CTA is determined by stage** (warm = "Check Availability/Dekho", hot = "Get Wiom/Book Now"). "Wiom try karo" sits between them with no stage assignment — which breaks the determinism. (It appears in the framework's own §10 worked example as a *warm* CTA.) **Fix:** assign it to warm, or drop it. Separately: **the actual scripts specify no CTA at all** (they end on the locked anchor end-slate) — see B.6.

### A.7 Net on Part A

The sheet is a strong operational asset and mostly faithful. The fixes are: (1) separate test-axes from production-spec, (2) move AI/non-AI out of story structure, (3) de-dupe Production style vs Format, (4) move "rule buried" to the G1 fail list, (5) stage-assign or drop "Wiom try karo", (6) add ISP to kill-list. None of these are fatal; all sharpen attribution discipline.

---

## PART B — The creatives vs the framework / sheet

### B.0 The wave at a glance

10 films (F1–F10) + 2 add-ons (F11–F12) + 9 statics. The cross-doc test architecture:

| Test | Cells | Holds constant | Varies | Clean? |
|---|---|---|---|---|
| Need-state pull (vox pop) | F1 / F2 / F3 | format, story, protagonist | need-state | ✅ |
| Need-state pull (comparison) | F4–F5 vs F6–F7; +F11, F12 | format, story | need-state | ✅ |
| Protagonist axis | F4 vs F5; F6 vs F7 | need-state, format, story | peer vs narrator | ✅ clean |
| AI vs live | F1 vs F8 | everything | production method | ✅ (the key learning cell) |
| Static need-state sweep | 9 statics | format, story, protagonist | need-state | ✅ |

This is **disciplined single-variable design** — genuinely framework-honoring. Two exceptions in B.3.

### B.1 Independent gate read (Phase-1 checker run on the 3 highest-risk concepts)

I ran my Phase-1 G1/G2 checker (the tool in this repo) on the three concepts most likely to trip the primary misread, to cross-check the docs' self-scores:

| Concept | Doc self-score | Checker verdict | Takeaway |
|---|---|---|---|
| **F4** "bilkul mobile ki tarah" | G2 PASS (bridge) | **PASS** — clean mechanic-analogy bridge, sandwiched between ghar anchors | ✅ Confirms doc. De-risks the mobile-bridge watch. |
| **F2** top-up vox pop | misread risk Low-Medium, PASS | **PASS** — ghar pivot at 4-7s converts the mobile-data opening | ✅ Gates pass, but checker itself names mobile-data-product as the risk being *prevented* → highest residual misread risk of the videos (see B.2). |
| **Static-2 top-up variant** | "deliberate probe", G1 Pass-gated | **KILL** — in a sound-off single frame with a phone-data-over warning + "recharge" doing double duty, the mobile-data-product misread is the most likely first read; no single-line fix in a no-arc static | 🔴 **Divergence.** See B.2. |

### B.2 Misread-risk ranking (primary = mobile-data-product)

Highest → lowest:

1. 🔴 **Static-2 top-up wording variant** ("Mobile recharge ke kharche bachane hain?… recharge se chalana hai"). The static doc itself calls this "a category-confusion probe, not a tidy A/B" — `recharge` is used for *both* the mobile problem and the home solve, in a single sound-off frame with no arc to self-correct, over a phone-data-over visual. **The checker KILLs it.** This is the right call **for a Campaign objective.** Recommendation: deploy it **only** as an explicitly-labelled Test probe with comment monitoring — never as a scaled campaign static. If you want a clean top-up static, the visual must carry whole-home (not a phone) and the rule must be JDRUDN-verbatim, not "recharge se chalana hai."
2. 🟠 **F2 top-up vox pop** (video). Opens squarely in the mobile-data frame (data exhaustion, hotspot). The 4-7s ghar pivot + resolution corrects it, so gates pass — but it carries the most residual misread risk of the videos. The doc's "Low-Medium" is fair; treat F2 as the **must-watch-in-UAT** video, and watch comments exactly as the static doc prescribes for the top-up cells.
3. 🟡 **F4 / F5** "bilkul mobile ki tarah." Clean bridge per the checker (explains the *recharge mechanic*, not Wiom's identity, immediately re-anchored to ghar ka net). Keep, but it leans on the most-dangerous bridge — keep the ghar anchors tight around it.
4. 🟡 **F6 / F11** "baaki net waali companiyon." Generic (no branded competitor) so within G2, but nudges the *broadband*-comparison frame (secondary misread). The doc already flags watching UAT for this — agreed.
5. ✅ Everything else: Low. F1, F3, F7, F9, statics 1/4/5/6/7/8 are clean and well-anchored.

### B.3 Test-design discipline — two violations to fix

- 🔴 **Obvious AI Film 3 (F10) is mis-tagged / co-varies two need-states.** It is labelled **family simultaneity**, but the *spoken* need is **short-duration/seasonal**: "Garmiyon mein bachhe ghar pe… sab ka net chalu. Lekin jab school khule? Tab sirf weekend par kaam padta hai." The busy-multi-device B-roll gestures at simultaneity while the dialogue argues short-duration. You can't attribute its performance to either need-state. **Fix:** pick one. If it's the F10 family-simultaneity cell, the dialogue must be about *concurrent household load* (like static-9), not seasonal/weekend duration. As written it's a second short-duration film, not a simultaneity film.
- 🟡 **Static "hotspot" vs "family simultaneity" is not a clean need-state delta.** The doc is honest about this ("both are now hotspot-framed… read the delta as treatment/angle, not need-state"). Acceptable *because* it's disclosed — just don't draw need-state conclusions from that pair.

### B.4 AI on the protagonist axis (open brief item #4)

F8 (AI vox-pop, mirrors F1) is the wave's headline learning cell. But **vox-pop's entire credibility mechanism is "real public"** — candid, unscripted, "don't fake it" (F1 iteration notes). An AI-rendered "vox pop" is in tension with the axis it occupies: if the AI face reads even slightly synthetic/aspirational, it doesn't just score lower on credibility, it can *contaminate* (the Obvious AI doc's own "any aspirational drift breaks the films" guard). **Implication for the sheet:** this is why AI/non-AI must be its own axis (A.2) **and** why it interacts with Protagonist & Credibility — AI sits comfortably on *testimonial/peer* (F9, F10: a "character" is allowed) but uneasily on *vox-pop* (F8: realness is the point). Recommend resolving the brief's open item as: **AI ≈ narrator/peer-character credibility, NOT vox-pop-public credibility.** Score F8 against that expectation, not against F1's live-vox-pop credibility.

### B.5 Coverage gaps (sheet taxonomy vs what's been produced)

- **Story structure held at constraint-first across the *entire* wave.** The other 8 structures (rule-reveal, before/after, question-hook, household-conflict, Kyunki-isliye, explainer, comparison-as-structure, urgency-first) are **untested**. Deliberate (constraint-first is the validated hypothesis) — but the "story structure" test variable is currently unexercised. Plan a later flight that holds need-state and sweeps story structure.
- **Need-states: IPL/cricket and festival are absent** (cricket appears only as a *scenario* inside F7). The static doc deliberately excludes them as urgency-led (would break the evergreen constraint-first set) — sound reasoning, but it leaves urgency-first + those two need-states untested. They need their own urgency flight.
- **Protagonist: local-creator (peer-with-reach) and founder are untested**; celebrity is (correctly) excluded on principle.
- **Format: local-creator UGC, motion graphic, founder talk, screen-record/demo, meme/reel, WhatsApp-forward are untested.** This wave is vox-pop / comparison-frame / static / testimonial only.

These gaps are mostly intentional sequencing, not errors — but the sheet is "exhaustive" while the wave exercises maybe a third of it. Worth an explicit roadmap so the untested axes don't quietly never get tested.

### B.6 🟠 CTA is missing from every script

Every film ends on the **locked anchor end-slate** (JDRUDN + Chale aapke hisaab se + logo) with **no stage-matched CTA** ("Check Availability/Dekho"). The sheet's own Hygiene check requires "CTA matches funnel stage." Either:
- this wave is deliberately CTA-less / pure soft category-building (defensible for warm top-of-activation, and consistent with the Annexure's slow-CTA discipline) — in which case **state it**, so the Hygiene check doesn't fail every film; or
- it's an omission, and a warm CTA needs adding before deployment.

Confirm which. Right now there's a literal contradiction between the eval sheet (CTA required) and the scripts (no CTA).

### B.7 Smaller notes (already mostly caught by the docs)

- **F5** body close "apne hisaab se" ≠ locked "Chale aapke hisaab se." The doc catches this and recommends tightening — agreed (end-slate carries it verbatim, so not a hard fail, but fix the in-body inflection).
- **Static-9 family simultaneity** puts the recharge-shape only in the lockup ("Ghar ka net chale befikr" headline carries no recharge mechanic). Borderline on G1 "recharge-shape clear" — watch whether the lockup alone carries it at a glance.
- **F1/F2** introduce the category only at 10-13s — long pure-problem runway. Inherent to vox-pop; F7's early 0-3s ghar anchor is the better pattern where the format allows.

---

## Prioritized fix list

**Sheet (Part A):**
1. 🔴 Move "AI / Non AI" out of Story Structure into its own Production-method axis.
2. 🟠 Separate the tab into TEST AXES (4) vs PRODUCTION SPEC; de-dupe Production style against Format.
3. 🟠 Move "rule implicit/buried" from a Recharge-model *value* to a G1 *fail* condition.
4. 🟠 Stage-assign or drop "Wiom try karo"; add "ISP" to kill-list.

**Wave (Part B):**
5. 🔴 Do not run Static-2 top-up variant as a campaign static (checker KILL). Test-probe only, or rebuild with whole-home visual + JDRUDN-verbatim.
6. 🔴 Re-tag / rewrite Obvious AI Film 3 — it conflates family-simultaneity (visual) with short-duration (verbal); pick one need-state.
7. 🟠 Flag F2 as the must-watch-in-UAT video for mobile-data misread.
8. 🟠 Resolve the CTA question (B.6) — deliberate soft close, or add stage CTA.
9. 🟡 Set AI's protagonist-axis expectation (B.4): AI = peer/narrator-character, not vox-pop-public credibility; score F8 accordingly.
10. 🟡 Publish a coverage roadmap for the untested story-structures, need-states (IPL/festival/urgency), protagonists, and formats.
