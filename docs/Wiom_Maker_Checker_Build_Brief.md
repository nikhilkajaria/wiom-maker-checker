# Wiom Maker-Checker System — Build Brief

**Status:** v0.4 — handoff brief for Claude Code
**Purpose:** This document is the spec Claude Code should use to begin building Wiom's activation creative maker-checker system. It captures context, source documents, system architecture, constraints, and build phases. Read it through once before starting. Re-read sections as you build.

---

## 1. What we're building

A **six-layer system** that produces production-ready activation creative for Wiom's performance marketing, enforces Wiom's locked creative standard automatically, and learns from deployed creative performance over time. The system replaces ad-hoc brief writing, manual QA, and reactive iteration with a structured workflow that humans approve at named gates.

**Users:**
- **Primary human in the loop:** Nikhil Kajaria (creative production lead), supported by Shiva (brand)
- **Agencies (Unfiltrr, Obvious AI, One47, etc.):** receive only system-approved production-ready briefs; they do not interact with the system directly
- **Deployment + measurement team:** consumes approved creative; feeds learnings back into the system

**Scope:** Activation creative only (paid performance ads for in-market audiences). Top-of-funnel category-creation work is owned by a different workstream and not in scope here.

---

## 2. Source documents to load first

These four documents define the standard the system enforces. Load and parse them before generating anything.

1. **`Wiom_Category_Reset_Context_Note.docx`** — Strategic foundation. Who the user is, what the category is, the dangerous misunderstanding (mobile-data product), language discipline.
2. **`Wiom_Category_Reset_Outreach_Annexure.docx`** — Five validated learnings from the outreach journey.
3. **`Wiom_Performance_Marketing_Principles.docx`** — Operating principles for performance marketing. Never-do list, four exercises, three-stage activation structure.
4. **`Wiom_Performance_Creative_Framework_v0_9.docx`** — The selection framework. Gates, test variables, outcome ladder, decision rule.

**Hierarchy:** Framework wins on selection mechanics, Principles win on operating rules, Context Note wins on strategic position, Annexure wins on historical learning.

---

## 3. System architecture — six layers

```
┌─────────────────────────────────────────────────────────────────┐
│  CONTEXT LAYER (knowledge store, read-only by all)              │
│  RWGKN strategy + Growth Function + Perf Mkt principles +       │
│  validated learnings buffer (updated by measurement layer)      │
└─────────────────────────────────────────────────────────────────┘
                              ↕ read
┌─────────────────────────────────────────────────────────────────┐
│  1. BRIEF LAYER — entry point                                   │
│  Human: "I need X creatives for Y objective by Z time"          │
│  System: structured brief + finite choices for audience × format│
│  Reads corpus + kill memory to bias toward unexplored cells     │
└─────────────────────────────────────────────────────────────────┘
                              ↓ structured brief
┌─────────────────────────────────────────────────────────────────┐
│  2. SCRIPT MAKER — concept + script + storyboard description    │
│  Single agent. Outputs viable static and video concepts.        │
└─────────────────────────────────────────────────────────────────┘
                              ↓ concept package
┌─────────────────────────────────────────────────────────────────┐
│  3. GATE-PASS CHECKER — G1 + G2 only                            │
│  Binary pass/fail. Iterate with script maker until pass.        │
│  HUMAN APPROVAL → production-ready brief assembled              │
└─────────────────────────────────────────────────────────────────┘
                              ↓ production-ready brief
                          [to agencies]
                              ↓ PPM submitted
┌─────────────────────────────────────────────────────────────────┐
│  4. CREATIVE EVALUATOR (pre-prod) — PPM evaluation              │
│  G1 + G2 re-run + contamination scan + brief-delta detector     │
│  HUMAN APPROVAL → shoot/produce                                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓ final cut delivered
┌─────────────────────────────────────────────────────────────────┐
│  5. CREATIVE EVALUATOR (post-prod) — final cut evaluation       │
│  Hygiene + creative quality + light contamination re-check      │
│  HUMAN APPROVAL → deploy                                        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                       [deployment team]
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  6. MEASUREMENT LAYER — outcomes + learnings                    │
│  Built by deployment team. Reads performance data.              │
│  Identifies patterns (3+ creatives in same cell converging).    │
│  HUMAN-GATED writeback into context layer (and other layers     │
│  if needed). Buffer prevents single-creative artifact chasing.  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Context layer

**Job:** Read-only knowledge store referenced by all other layers. Holds Wiom's strategic and operational truth. Updates only via human-gated writeback from measurement layer.

**What it carries:**
- Why the shift to RWGKN happened (Context Note distilled)
- What RWGKN is — both halves co-equal, the two layers of the proposition (value: JDRUDN/JZUR pending; mechanic: duration units; commitment granularity)
- Growth Function principles (subordinate to but informing performance marketing)
- Performance marketing operational context (capture/convert split, user-as-hero, never-do list)
- Memory anchors (locked three-rung stack — see below)
- Dangerous misreads list (mobile-data-product as primary, others secondary)
- Identity truths / optimization variables / temporary devices hierarchy
- Validated learnings buffer (populated by measurement layer over time)

**How it's accessed:** Cached system prompt segment that all layer agents prepend. Updated rarely. Cheap to read because of prompt caching.

### Memory anchor stack — locked

Three rungs, three jobs. Each does work the others can't.

| Rung | Anchor | Job | Status |
|---|---|---|---|
| Label | **Recharge-wala Ghar ka Net (RWGKN)** | Names the category | Locked, verbatim |
| Rule | **Jitne din recharge, utne din net (JDRUDN)** | States the operating logic (invariant — same for every user) | Locked, verbatim |
| Emotion | **Chale aapke hisaab se** | Names how it feels (user agency) | Locked, verbatim |

### Bridge — flexible benefit articulation

Between rule and emotion sits the benefit line — **Jitni zarurat utna recharge (JZUR)** — which explains *why the rule is useful*. JZUR is NOT a fourth rung. It is a benefit template that fills with each need-state:

- Exam season: "exam ke 15 din ka recharge"
- Match day: "match wale din ka recharge"
- Salary delay: "abhi 2 din, salary aane pe poora mahina"
- Family travel: "ghar par nahi, toh recharge nahi"

**Underlying principle: lock the constant, flex the contextual.** The rule is invariant (locked phrasing). The benefit is contextual (varies with need-state). RWGKN, JDRUDN, and Chale aapke hisaab se must appear in their locked forms when used. JZUR-shaped benefit lines flex per situation.

### Articulation flexibility around the rule and benefit

The script maker is not constrained to use JDRUDN and JZUR as the only ways to communicate the mechanic and benefit. Creatives may explain the operating logic through varied articulations:

- Visual demonstrations (app UI showing duration selection)
- Dialogue that walks through the decision ("toh phir 1 din ka recharge kar lete hain")
- Multi-person patterns (different people showing different recharge durations)
- Situational explanation ("aaj match hai — bas aaj ke liye kar lo")

What is required: JDRUDN must appear verbatim *at least once* in the creative (typically at end-slate or as a summary line), and the creative as a whole must communicate the locked rule and the contextual benefit. How it communicates them is open to creative judgment — articulation diversity is encouraged so creatives don't read as templated.

**Anti-pattern:** Do not make this layer a coordinator or router. It's a knowledge store. Each subsequent layer reads from it but does its own work.

### Structured-input schema for context layer updates

Context layer drifts unless updates are constrained. All writes to the context layer go through a structured-input schema — no free-text edits.

**Three update channels, each with a defined schema:**

**Channel 1 — Learnings buffer update** (Nikhil-owned)

```json
{
  "update_type": "learnings_buffer",
  "pattern_id": "L-2026-W22-001",
  "pattern_description": "Single sentence describing what was observed",
  "supporting_creatives": ["C-2026-W18-003", "C-2026-W19-007", "C-2026-W20-012"],
  "variable_cell": {"story_structure": "constraint-first", "protagonist": "peer", "need_state": "monthly-commitment_rejection"},
  "outcome_signal": "first_recharge_rate | mobile_to_bfc | d28_retention | misread_proxy",
  "magnitude": "directional | meaningful | strong",
  "implication_for_briefs": "Bias toward / Bias against / No change",
  "approved_by": "Nikhil",
  "approved_at": "ISO timestamp",
  "review_at": "Next review trigger — N more creatives in this cell"
}
```

**Channel 2 — Brief choices evolution** (Nikhil-owned)

```json
{
  "update_type": "brief_choices",
  "action": "add | modify | retire",
  "combination": {"audience": "...", "objective": "...", "format": "...", "compatible_need_states": [...]},
  "rationale": "Why this combination is being added/modified/retired",
  "approved_by": "Nikhil",
  "approved_at": "ISO timestamp"
}
```

**Channel 3 — Identity truths update** (Shiva-owned)

```json
{
  "update_type": "identity_truth",
  "target_section": "memory_anchors | dangerous_misreads | gates | category_definition",
  "current_value": "...",
  "proposed_value": "...",
  "rationale": "Why this change is needed — must reference specific evidence or strategic decision",
  "source_evidence": "Measurement pattern ID, founder decision, qualitative finding, etc.",
  "approved_by": "Shiva",
  "approved_at": "ISO timestamp"
}
```

**Schema rules:**
- All four required fields per channel (no nulls)
- `approved_by` must match the channel's owner — system rejects writes with mismatched owner
- Every update gets a timestamped audit log entry; the context layer maintains version history
- Free-text fields (rationale, pattern_description) are constrained by length and validated for clarity before commit
- No "miscellaneous" or "other" fields; if a write doesn't fit one of the three schemas, it requires schema extension first (which itself is a versioned change to this brief)

---

## 5. Brief layer (entry point)

**Job:** Translate human request into structured creative brief. Bias toward unexplored variable cells. Present finite choices for human decision-making.

### Input — from human

Free-form request like: "I need 8 new creatives for Considerer audience by next Friday for IPL final week" or "Need 3 statics + 5 videos for general Considerer pull this fortnight."

### What the brief layer does

1. Parses the human request for objective, audience, count, format split, timing
2. Reads current state (corpus + kill memory + active opportunity calendar)
3. Presents the human with a **finite set of choices** from a pre-defined config — audience tier × objective × format × need-state combinations curated to balance:
   - Coverage of unexplored variable cells (per corpus and kill memory)
   - Fit with current event calendar (IPL final, exam season ending, festivals)
   - Operational viability (capacity-ready zones, language, length constraints)
4. Human selects from offered combinations
5. Brief layer assembles structured brief per concept

### Configuration of finite choices

Choices live in a **pre-defined config file** (`reference/brief_choices.json`) that's hand-curated. New combinations are added manually as they get validated. Format:

```json
{
  "audience_tiers": ["T1.5_general_Considerer", "T2_warm_Considerer", "T3_retargeting", "..."],
  "objectives": ["pure_acquisition", "warm_to_hot_conversion", "category_clarity_lift", "..."],
  "formats": ["video_15s", "video_18s", "video_30s", "static_feed", "static_story", "carousel"],
  "need_states": ["hotspot_exhaustion", "IPL_or_cricket", "exam_season", "salary_delay", "..."],
  "valid_combinations": [
    {
      "audience": "T1.5_general_Considerer",
      "objective": "pure_acquisition",
      "format": "video_15s",
      "compatible_need_states": ["IPL_or_cricket", "monthly_commitment_rejection", "family_simultaneity"],
      "preferred_protagonist_axis": ["peer", "peer-with-reach"],
      "notes": "Currently over-saturated in scripted-narrator. Bias toward peer-proximate."
    }
  ]
}
```

### Output — structured brief (passes to script maker)

```json
{
  "brief_id": "B-2026-W21-001",
  "campaign_objective": "...",
  "audience_tier": "T1.5",
  "audience_descriptor": "...",
  "format": "video_15s",
  "language": "HI",
  "geography": "Delhi NCR",
  "need_state": "monthly-commitment rejection",
  "preferred_protagonist_axis": "peer | peer-with-reach",
  "preferred_story_structure": "constraint-first | open",
  "current_event_context": ["IPL final week"],
  "ops_constraints": ["no SLA mention", "no specific install timeline promise"],
  "human_directional_note": "Test peer-proximate protagonist; previous wave was scripted family",
  "corpus_avoid": ["concepts already tested with this combo, e.g. C-2026-W18-003"],
  "kill_memory_avoid": ["specific failure modes already established"]
}
```

### Anti-pattern

Brief layer optimizes for **learning per ad-rupee + creative diversity**, not for ease-of-measurement metrics. If two combinations have similar projected coverage, prefer the one with less prior testing.

---

## 6. Script maker

**Job:** Take a structured brief and produce a viable creative concept with script and storyboard description.

**Single agent (Sonnet 4.6).** Three-agent decomposition was considered and rejected as over-spec for v1.

### Inputs
- Structured brief from §5
- Context layer (cached)
- Memory anchors (cached)
- Dangerous misreads list (cached)

### Output per concept

Differentiated for static vs video. JSON:

```json
{
  "concept_id": "C-2026-W21-001",
  "brief_id": "B-2026-W21-001",
  "concept": "One-paragraph concept summary",
  "format": "video | static",

  "for_video": {
    "script": "Shot-by-shot script with Hindi dialogue and timing markers",
    "storyboard_description": "Per-shot visual description — setting, blocking, props, mood, key visual moments",
    "audio_notes": "Pacing, dialogue delivery, any diegetic sound, no music bed unless explicitly briefed"
  },
  "for_static": {
    "copy_blocks": "All text elements with hierarchy (primary, secondary, supporting)",
    "visual_description": "What the static depicts; composition; brand asset placement"
  },

  "tags": {
    "story_structure": "constraint-first | rule-reveal | before-after | ...",
    "protagonist_credibility": "real-customer | local-creator | vox-pop | founder | narrator | actor",
    "need_state": "...",
    "format_subtype": "..."
  },
  "memory_anchors_planned": {
    "label_RWGKN": "where Recharge-wala Ghar ka Net lands — verbatim, at least one moment",
    "rule_JDRUDN": "where Jitne din recharge, utne din net lands — verbatim, at least once (typically end-slate or summary line)",
    "emotion_chale_aapke_hisaab_se": "where Chale aapke hisaab se lands — verbatim",
    "benefit_articulation": "How the benefit (JZUR-shaped) is expressed in this creative — contextual to need-state (e.g., 'exam ke 15 din ka recharge', 'match wale din ka recharge'). Free articulation; not required verbatim.",
    "mechanic_articulation": "How the operating mechanic is communicated beyond the locked JDRUDN line — visual demo, dialogue walkthrough, multi-person pattern, situational explanation, etc."
  },
  "cta_intensity": "warm | hot",
  "rationale": "Why this concept, why this need-state, why this protagonist axis"
}
```

---

## 7. Gate-pass checker (Step 3)

**Job:** Run G1 + G2 on the script-maker's output. Binary pass/fail per gate. Iterate with script maker until both gates pass. Human approves before production-ready brief is assembled.

**Sub-agents:**
- **Gate-1 agent (Sonnet 4.6)** — category-frame integrity
- **Gate-2 agent (Sonnet 4.6)** — contamination check
- **Feedback synthesizer (Sonnet 4.6)** — turns gate output into structured feedback for script maker iteration

**Scope of v1:** G1 + G2 + user-as-hero. Memory anchor placement scoring, misread risk scoring, protagonist axis alignment, and constraint-first verification are explicitly **deferred to subsequent versions** per Nikhil's direction. Note: constraint-first is Wiom's current strongest hypothesis for story structure, not a hard gate — the maker is biased toward it but the checker does not fail non-constraint-first creative on that basis alone. v1 ships with the two binary gates plus the user-as-hero check, and human judgment on the rest.

### G1 — Category-frame integrity

Passes if all three hold:
- Ghar anchor present (household / whole-home explicit or unmistakable in visual or audio)
- Recharge-shape clear (pay-as-you-go / recharge behavior conveyed, not buried)
- No frame drift (creative doesn't land as cheap WiFi / flexible mobile data / budget broadband)

**Fail test:** "If a reviewer must supply the ghar anchor themselves to make the ad cohere, it fails."

**Scope note (creative vs landing page):** The creative's job is to capture intent and *begin* category anchoring. Per SD's three-stage activation model (Activation → Landing → Measurement), full category comprehension is completed downstream at the landing page, which re-anchors into RWGKN above the fold. Landing pages are outside this system's scope. G1 should therefore not be tuned to demand that a 15-second creative fully resolve comprehension on its own — it must establish the ghar anchor and recharge-shape, not complete the entire mental-model conversion.

### G2 — Contamination check (capture/convert split)

This is the gate most easily misjudged. The rule is not "no kill-list words ever." Per SD's Principles: **capture using the market's words, convert using Wiom's category.** Kill-list words (WiFi, broadband, fiber, speed plans, cheap internet) are permitted as a *capture bridge* and forbidden as *Wiom's identity*.

**Two distinct checks:**

1. **Capture-bridge use (ALLOWED):** A kill-list word appears in the user's own voice, at the hook/opening, as the language the in-market user already searches with. Examples: opening line "WiFi lene jaa rahe ho?"; a respondent saying "main WiFi dhoondh raha tha." The word is the bridge that meets the user where they are — it is not claimed as what Wiom *is*.

2. **Identity use (FORBIDDEN):** A kill-list word is used to define or describe Wiom itself. Examples: "Wiom — best cheap WiFi"; "Wiom ek WiFi service hai"; "WiFi jaisa, par sasta." Here the word becomes Wiom's category identity, which pulls the user back into the old frame.

**Fail test:** "Does the creative invite the user to compare Wiom against Jio/Airtel/broadband on their terms? If a kill-list word defines what Wiom IS (rather than what the user was looking for), it fails. If it only names the user's starting point and the creative then converts to RWGKN, it passes."

**Common error to avoid:** Do not blanket-fail any creative containing "WiFi." That over-rejection kills legitimate capture-bridge creative. Check the *role* the word plays — bridge (pass) vs identity (fail).

### User-as-hero check (v1)

Passes if the user (or household) is the emotionally central subject and Wiom is the enabler — not the hero.

**Fail test:** "If the product/brand is the emotional center of the creative — if Wiom is what the creative is *about* rather than what helps the user — it fails." Constraint disclosure, household reality, and user agency should carry the creative; the brand enters as the resolution, not the protagonist.

### Dangerous-misread weighting (note for the deferred misread-scorer)

When the misread-risk scorer is built (deferred past v1), **mobile-data-product is the primary misread to weight hardest** — the Context Note names it as the dangerous one, already showing up in mid-funnel. Broadband and cheap-WiFi misreads are secondary. The scorer should not weight all misreads equally; mobile-data-product carries the highest penalty.

### Verdict logic

- **PASS** — Both gates pass. → human approval → production-ready brief assembled
- **ITERATE** — One or both gates fail on structural-only issues (fixable by a four-word add or single-line rewrite). → back to script maker with structured feedback
- **KILL** — Gates fail on conceptual issues (concept built on wrong frame) OR script maker has iterated >3 times without passing. → concept logged to kill memory with reason

### Production-ready brief assembly (after PASS + human approval)

The system assembles a complete brief for the agency containing:

1. **Objective and audience context**
2. **Concept and rationale**
3. **Script with storyboard** (video) or **copy + visual description** (static)
4. **Format specs** — length, aspect ratios, file specs
5. **Callouts and notes** — specifics agency must preserve or avoid
6. **Pre-production instructions (video):**
   - Casting — protagonist axis required, physical description, age range, household segment markers
   - Location — setting type, household segment cues, segments to avoid
   - Environment / setting — lighting (natural vs cinematic), room tone, time of day
   - Art elements — props, set dressing, walls, table contents
   - Costumes — clothing register
   - Specifically forbidden visuals — anything that codes "broadband sale" or "mobile data product"
7. **Post-production do's and don'ts:**
   - Music — none unless explicitly briefed; diegetic/natural sound only by default
   - End-slate — locked brand spec (logo placement, hold duration, no glow, no emphasis)
   - Brand asset placement — Wiom logo small, quiet, bottom centre or bottom right
   - Captions — Hindi text, readable on phone, contrast preserved
   - CTA — exact wording per CTA intensity stage from brief
   - Dimensions — required deliverable formats and aspect ratios
   - Color palette — pink only on Wiom logo; black background for statics
   - Pacing — constraint-first opener must land in <3s; duration demonstration before 8s; memory anchor must land before typical drop-off point
   - Audio levels — dialogue must be audible without music bed
   - First-frame thumbnail composition — Meta auto-grabs frame 1; what's there matters

(File naming per Online Nomenclature doc, delivery deadline, production team contact, review-and-revision protocol, rights and usage — added per agency briefing norms.)

---

## 8. Creative evaluator — pre-prod and post-prod

### Pre-prod (Step 4)

**Job:** Evaluate the agency's PPM (pre-production materials — fleshed-out storyboards, casting choices, location selections, mood references, art direction) against the approved brief.

**Sub-agents:**
- **G1 + G2 re-runner (Sonnet 4.6)** — re-runs gates on PPM materials. Catches micro-decisions that broke the gates (wrong household segment in casting; aspirational kitchen in location; branded polo on protagonist).
- **Contamination scanner (Sonnet 4.6)** — explicit check for visual or audio elements that code "broadband sale," "premium ISP," "mobile data product," "cheap internet" — independent of G1+G2.
- **Brief-delta detector (Sonnet 4.6)** — flags any deviations the agency proposed from the approved brief.

**Verdict:**
- **PASS** — proceed to shoot
- **ITERATE** — specific PPM elements need revision
- **DEVIATION ESCALATION** — agency proposed changes from the brief. **Human-gated decision:** accept (route back to script maker for re-script per §6; full gate-pass cycle re-runs) or reject (agency reverts to approved brief)

### Post-prod (Step 5)

**Job:** Evaluate the final cut. Hygiene + creative quality + light contamination re-check.

**Sub-agents:**

**Hygiene checker (Haiku 4.5 + Sonnet 4.6 split):**
- Audio levels and clarity — dialogue audible, no clipping, brand name pronounced clearly
- Visual clarity — exposure, composition, no blur or compression artifacts
- Dimensions and file specs — deliverable formats present, aspect ratios correct
- End-slate and branding — Wiom logo placement, hold duration, color match to locked spec
- Captions — present, Hindi rendering correct, readable on phone, sync to dialogue
- CTA — visible and readable, including on 320x320 Meta thumbnail
- First-frame thumbnail — Meta auto-grab frame composition

**Creative quality checker (Sonnet 4.6):**
- Memory anchor *audibility* — caption-on and caption-off both (many viewers watch muted)
- Memory anchor *timing* against the actual cut — script said anchor at 7-12s; did the edit preserve that, or did it slide to 13-15s where fewer viewers see it
- Hindi pronunciation and clarity — brand name, the rule line, key duration words
- Pacing — does constraint-first opener land in <3s; does duration-flexibility demonstration happen before 8s
- Diegetic sound quality — room tone consistent, no out-of-frame artifacts

**Contamination re-check (Sonnet 4.6) — light:**
- Did any post-prod choice introduce contamination? (color grade coding "premium telecom"; sound design coding "promo offer"; etc.)
- Note: full G1 + G2 re-run on post-prod was considered and deferred per Nikhil's direction. The light contamination re-check is the v1 compromise.

**Verdict:**
- **PASS** — human approval → deploy
- **ITERATE** — specific post-prod elements need fixing
- **KILL** — final cut fails fundamental check; reshoot or scrap

---

## 9. Measurement layer (Step 6)

**Built by deployment team.** Not in scope for the maker-checker build directly, but the system must expose hooks for the measurement layer to feed learnings back, and must define how learnings are assimilated and ingested.

### What the measurement layer measures (five signal sources)

The demand engine is not measured by Meta performance alone. Per SD's docs (the compound primary metric, the dangerous-misread tracking, the pull-vs-push transition signals), the measurement layer must capture both quantitative and qualitative signals across five sources:

| # | Signal source | Type | What it captures | Origin |
|---|---|---|---|---|
| 1 | Platform performance | Quant | CTR, hook rate, completion rate, CPA, mobile→BFC | Meta / ad platforms |
| 2 | Conversion + recharge quality | Quant | Bookings, first-recharge rate, D7/D28 recharge cohorts | Product / billing system |
| 3 | Category comprehension | Qual | UAT misread rate; recharge-frame vs mobile-frame vs broadband-frame classification | UAT / surveys |
| 4 | Inbound language | Qual | CC call transcript classification (recharge-frame share); in-app help-query taxonomy | CC / app |
| 5 | Demand-engine health | Mixed | Branded-search trend; category-confusion trend (pull-vs-push transition indicators) | Search / brand tracking |

The compound primary metric (qualified bookings × first-recharge conversion) draws on sources 1 and 2. But a creative that wins on source 1 while failing source 3 (comprehension) is the exact failure mode the category reset is fighting — looking like it works on platform metrics while the mental model stays wrong. The measurement layer must therefore report comprehension and recharge-quality signals alongside platform performance, not as an afterthought.

### Learning assimilation and ingestion

**Ownership chain (single owner per node):**

1. **Karishni assimilates + proposes.** She takes raw measurement output (all five sources, quant and qual) and synthesizes it into structured candidate-learning entries. She proposes writebacks. This is real ownership — it builds her category judgment, with Nikhil as the safety net.
2. **Nikhil reviews + approves (gatekeeper).** He is the gatekeeper for what enters the system. He reviews each candidate, decides accept / reject / needs-more-evidence, and approves writebacks to the learnings buffer and brief_choices.json.
3. **Shiva owns identity truths.** Any candidate that proposes changing an identity truth (memory anchors, dangerous-misreads, gates, category definition) routes to Shiva to decide — boundary by content, not by step.

**Candidate-learning format (the pre-approval entry Karishni produces):**

Distinct from the committed-writeback schemas in §4. A candidate must carry:

```json
{
  "candidate_id": "CL-2026-W22-001",
  "signal_sources": ["platform_performance", "conversion_recharge", "comprehension", "..."],
  "raw_signals": "The specific data points — metrics, UAT findings, transcript classifications — this is built on",
  "variable_cell": {"story_structure": "...", "protagonist": "...", "need_state": "...", "format": "..."},
  "supporting_creatives": ["C-... ", "C-..."],
  "sample_size_or_confidence": "n creatives / n respondents / qualitative strength",
  "proposed_finding": "One sentence — what was observed",
  "competing_explanations_considered": "What else could explain this (confounds, IPL-was-running, small sample, etc.)",
  "proposed_destination": "context_layer_learnings_buffer | brief_choices | script_maker_examples | gate_definition | identity_truth",
  "proposed_by": "Karishni",
  "proposed_at": "ISO timestamp"
}
```

**Routing rules (which learning informs which destination):**

| Learning type | Routes to | Owner of decision |
|---|---|---|
| "Constraint/need-state X converts better than Y" | brief_choices (weighting) | Nikhil |
| "Format/protagonist X outperforms Y at matched cell" | brief_choices + learnings buffer | Nikhil |
| "Creatives doing X get misread as mobile-data-product" | script_maker negative example + gate-definition sharpening | Nikhil; Shiva if it touches gate definition |
| "Category comprehension shifting (misread rate moving)" | identity-truth-adjacent / strategic | Shiva |
| "A specific framing reliably fails in UAT" | script_maker negative example | Nikhil |

**Differentiated evidence thresholds (quant vs qual):**

Quant and qual have different evidence logics. One rule does not fit both.

- **Quant convergence:** 3+ creatives in the same variable cell converging on a finding before it updates the context layer or brief_choices. Single-creative quant results stay in the corpus as data points; they do not update beliefs. (Guards against single-creative artifact chasing.)
- **Qual conclusiveness:** a single well-run signal can justify action faster than quant convergence — e.g., a UAT showing 5/5 respondents misreading a specific framing is conclusive enough to add a script-maker negative example immediately, without waiting for 3 deployed creatives to fail. Qual that is suggestive but not conclusive (e.g., a handful of ambiguous CC transcripts) waits for corroboration.
- **The asymmetry is deliberate:** quant needs volume to overcome noise; a clean qual finding can be diagnostic on its own. Karishni's candidate must state which logic applies and why.

**Conflict resolution (when learnings contradict):**

Contradictions will happen — the Cricket case is the archetype (strong acquisition, questionable recharge quality). Rules:

- When a new learning contradicts an existing context-layer entry → flag to Nikhil; he decides whether it's a genuine conflict (escalate / re-examine) or a resolvable update (new evidence supersedes old).
- When quant and qual point opposite directions (e.g., great CPA but high UAT misread) → the quality/comprehension signal takes precedence over the efficiency signal, per SD's objective hierarchy (recharge-quality bookings, not booking volume). Nikhil applies this and documents the call.
- No contradiction is silently resolved by the system. Every conflict is surfaced to a human.

### Kill memory (lives in same database as corpus)

The kill memory is a flagged subset of the corpus, not a separate store.

- Schema: `corpus` table with `killed` boolean, `kill_reason` text, `killed_at_stage` enum (gate-checker | pre-prod | post-prod | post-deployment)
- Written to when a concept is KILLed at any gate, or when post-deployment data shows it failed (latter writeback is human-gated)
- Brief layer reads kill memory to avoid regenerating similar concepts
- Script maker reads kill memory to avoid producing scripts similar to killed ones

---

## 10. Cross-cutting concerns

### Roles and responsibilities

Single owner per node — no co-ownership. Eliminates accountability ambiguity, conflict, and decision lag.

| Person | Owns | Approves |
|---|---|---|
| **Shiva** (Comms lead) | Gates (G1, G2), contamination definitions, dangerous-misreads list, identity truths in context layer, growth function co-ownership with Guneet | Post-G1+G2 concept → production-ready brief assembly; pre-prod final approval → shoot; identity-truth changes proposed via learnings |
| **Nikhil** (Acquisition comms lead) | Context layer maintenance, brief layer, script maker, system tuning, performance interpretation | Brief finalization (operating his own layer, not a gate); post-prod final approval → deploy; gatekeeper-reviewer-approver for all learnings ingested into the system (learnings buffer + brief_choices.json writebacks) |
| **Karishni** (Junior, building context) | Agency/prod ops, deployment coordination, reference data hygiene (event_calendar.json, ops_constraints.json), corpus hygiene (tagging discipline, kill-memory reasons logged correctly), **assimilation of all learnings (quant + qual) from the measurement layer + proposing writebacks** | Agency-side iteration loops (PPM revisions; final-cut revisions). Does not make stage-advancement or writeback-approval decisions. |

**Per-concept sequence:**
1. Nikhil → brief finalized (operating brief layer; finite choices presented by system)
2. Script maker → output → gate-pass checker → **Shiva approves** → production-ready brief
3. Karishni → hands brief to agency, runs PPM iteration loop, gets to "ready-for-shoot" state
4. **Shiva approves** → shoot
5. Karishni → runs final-cut iteration loop, gets to "ready-for-deploy" state
6. **Nikhil approves** → deploy
7. Measurement layer produces raw data (5 signal sources) → **Karishni assimilates** quant + qual into structured candidate-learning entries → proposes writebacks
8. **Nikhil reviews + approves** candidate learnings (gatekeeper) → writeback to learnings buffer / brief_choices.json
9. If a candidate proposes changing an identity truth → request handed to **Shiva** to decide (boundary by content, not by step)

**Escalation paths:**
- System can escalate to the relevant owner at any layer if confidence is low (model uncertainty, gate verdict close to threshold, etc.)
- Agency deviations from approved brief (caught by brief-delta detector at pre-prod) → Karishni surfaces to Shiva; Shiva decides accept (routes back to Nikhil for re-script) or reject (revert to brief)
- Disagreements between Karishni and agency on iteration calls → Karishni escalates to whoever owns the next approval (Shiva for pre-prod loop, Nikhil for post-prod loop)

### Agency deviations from brief

If agency proposes changes at PPM stage:
- System flags via brief-delta detector
- Human-gated decision
- If accepted: deviation routes back to script maker (§6) for re-scripting; full gate-pass cycle re-runs on the modified script
- If rejected: agency reverts to approved brief

This prevents deviations from bypassing the standard.

---

## 11. Access, identity, and roles

The system is multi-user. It must know who is acting, attribute every action to a real person, and let an admin configure who can do what.

### Authentication

- **SSO via Google Workspace, restricted to wiom.in email IDs.** Sign-in uses the Wiom Google Workspace identity; the wiom.in email is the user identity. OAuth flow only — no passwords stored in the app. Non-wiom.in accounts are rejected at sign-in.
- This matches the constraint that account creation and password handling stay with the identity provider, not the app.

### Identity and attribution

- Every action (brief finalization, gate approval, agency iteration, writeback proposal, writeback approval, identity-truth change) is attributed to the signed-in user.
- The audit log ties every context-layer write, every approval, and every kill-memory entry to a real person and timestamp (the §4 schemas already require `approved_by` / `proposed_by` — these must match the authenticated user, and the system rejects writes where they don't).

### Role-based access (configurable, three roles seeded as defaults)

Roles are **configurable by the admin**, not hardcoded — the admin can create roles and assign permissions without a rebuild. The system ships with three default roles seeded to match the current team's ownership model:

| Default role | Permissions (seeded) | Current holder |
|---|---|---|
| **Guardrails owner** | Edit gate definitions, contamination/kill-list definitions, dangerous-misreads list, identity truths; approve identity-truth changes; approve post-G1+G2 concept and pre-prod | Shiva |
| **System gatekeeper** | Maintain context layer, brief layer, script maker; finalize briefs; approve post-prod → deploy; review + approve all learning writebacks | Nikhil |
| **Operator / assimilator** | Run agency iteration loops; maintain reference data + corpus hygiene; assimilate learnings + propose writebacks. No stage-advancement or writeback-approval authority | Karishni |

The role definitions encode the §10 ownership model as configurable permissions. If responsibilities shift or the team grows, the admin reassigns permissions rather than the system being rebuilt.

### Admin role

- The admin can add/remove users, assign roles, create new roles, and define per-role permissions (including which role can approve identity-truth changes, which can approve writebacks, which can advance stages).
- Admin actions are themselves audit-logged.
- At least one admin must exist at all times; the seeding sets the initial admin (to be designated at deployment).

---

## 12. Operational constraints

| Constraint | Value |
|---|---|
| Geography (current) | Delhi NCR only |
| Language (current) | Hindi only |
| Audience | In-market home internet users (Considerers) |
| Product trial | First 2 days of net are free |
| Pricing structure | 1 din / 2 din / 7 din / 14 din / 28 din recharges; current ₹23/₹45/₹140/₹305/₹565 — structure stable, prices may shift |
| Booking fee | ₹100 non-refundable |
| Security deposit | ₹300 refundable when user doesn't recharge for 15+ days AND voluntarily returns router; CSP-collected refund is slightly lower but nominal |
| Install timing | No SLA — CSP proposes a slot, customer accepts or requests another (handshake) |
| Capacity gating | Owned by Guneet's team; brief layer should not generate briefs for non-capacity-ready zones |
| Top-of-funnel | Not in scope; assumed handled separately |
| Production volume | 8-10 concepts to start, then ~5 ongoing per week |

---

## 13. Tech stack guidance

**Anthropic API** (not Claude Max — Max is per-user, doesn't work for multi-user programmatic apps).

**Model selection:**
- **Sonnet 4.6** — judgment-heavy agents (script maker, gate checkers, creative quality checker, feedback synthesizers, contamination scanner, brief-delta detector)
- **Haiku 4.5** — mechanical agents (hygiene checks, file spec validation, dimension checks, anchor presence detection)
- **Opus 4.7** — not needed for v1

**Anthropic API features:**
- **Prompt caching** — context layer is reused on every call across every layer. Cache aggressively.
- **Tool use** — structured JSON output and corpus lookups
- **Batch API** — async work (overnight corpus re-tagging, learning-layer runs)
- **Streaming** — human-facing checker feedback so reviewers see results progressively

**Stack suggestion (not prescriptive):** Python + FastAPI backend, React frontend, Postgres for corpus and kill memory, S3 or equivalent for media assets, Anthropic SDK for API calls. Claude Code can pick a different stack if it has reason to.

**Repo structure suggestion:**

```
wiom-maker-checker/
├── README.md
├── docs/
│   ├── Wiom_Category_Reset_Context_Note.docx
│   ├── Wiom_Category_Reset_Outreach_Annexure.docx
│   ├── Wiom_Performance_Marketing_Principles.docx
│   ├── Wiom_Performance_Creative_Framework_v0_9.docx
│   └── Wiom_Maker_Checker_Build_Brief.md (this file)
├── reference/
│   ├── context_layer.md            (compiled from source docs)
│   ├── brief_choices.json
│   ├── event_calendar.json
│   ├── ops_constraints.json
│   ├── dangerous_misreads.json
│   └── memory_anchors.json
├── layers/
│   ├── brief/
│   ├── script_maker/
│   ├── gate_checker/
│   ├── evaluator_preprod/
│   └── evaluator_postprod/
├── shared/
│   ├── prompts/
│   ├── corpus.py        (read/write corpus + kill memory)
│   └── anthropic_client.py
├── api/
│   └── routes.py
├── ui/
│   └── ...
└── tests/
    ├── golden_concepts/
    └── ...
```

---

## 14. Cost architecture

Rough order-of-magnitude estimate for 8-10 concepts per week with iterations:

- **Cached context layer:** ~8-12K tokens, cached with prompt caching — 90%+ cost reduction on repeat calls
- **Per-concept generation:** ~3-5 Sonnet calls
- **Per-concept gate-checking:** ~3-4 Sonnet calls + ~2-3 Haiku calls
- **Pre-prod evaluation:** ~3-4 Sonnet calls per PPM
- **Post-prod evaluation:** ~5-8 split between Sonnet and Haiku
- **Average iterations per concept before PASS:** ~2-3

Estimated monthly cost at this volume: **low double-digit dollars**, not hundreds. Validate against actual usage in week 1 and adjust model assignments if it exceeds.

Sonnet 4.6 is ~$3/Mtok input; Haiku 4.5 is ~$1/Mtok at the time of writing. Confirm current pricing at https://docs.claude.com when you start.

---

## 15. Open items / pending decisions

These need human input before specific build steps proceed. They do not block starting Phase 1.

1. **Operational substrate hosting** — where the deployed app lives. **Decision needed:** before Phase 6.
2. **Event calendar maintainer** — who keeps `reference/event_calendar.json` current. (Karishni per §10 ownership split, but workflow for surfacing upcoming events to Nikhil for brief planning needs definition.) **Decision needed:** before Phase 3.
3. **Corpus seeding** — initial set of past creatives to populate corpus. Available data files exist in working directory. Claude Code should ingest these. **Decision needed:** before Phase 3.
4. **Where AI-generated faces sit on the protagonist axis** — Obvious AI films are scripted but visually-rendered as real-feeling people. Treated as "narrator" or as something closer to "peer"? **Decision needed:** before script maker is wired into production use.
5. **`brief_choices.json` seed combinations** — initial hand-curated set. Claude Code can propose a v0 seed from current activity; Nikhil approves. **Decision needed:** before Phase 3.
6. **PPM submission format** — agencies submit PPMs in different formats (PDF, deck, Notion page, etc.). The pre-prod evaluator needs a defined intake format. **Decision needed:** before Phase 4.
7. **Initial admin designation** — who holds the admin role at deployment (can add/remove users, assign roles, define permissions per §11). **Decision needed:** before Phase 6.

---

## 16. Build phases

**Phase 1 (week 1) — Gate-pass checker minimum viable.** Single Sonnet agent running G1 + G2 on manually-written concepts. Returns structured feedback. No script maker yet. Validates gates are encoded tightly enough that two runs agree. Test against 10-15 golden examples.

**Phase 2 (week 2) — Script maker minimum viable.** Single Sonnet agent generates concept + script + storyboard description from a manually-written structured brief. Outputs JSON. Pass to Phase-1 checker. Iterate prompts until consistent quality.

**Phase 3 (week 3) — Brief layer.** Build the brief layer with `brief_choices.json` config. Brief layer reads corpus + kill memory + event calendar; presents finite choices; assembles structured brief for script maker.

**Phase 4 (week 4) — Pre-prod evaluator.** Build evaluator for PPM submissions. G1 + G2 re-run + contamination scan + brief-delta detector.

**Phase 5 (week 5) — Post-prod evaluator.** Build hygiene + creative quality + light contamination re-check on final cuts.

**Phase 6 (week 6) — Web app, auth, and human-in-loop UI.** Build the interface humans use to submit briefs, review outputs, approve or reject at named checkpoints. Includes SSO sign-in (wiom.in only), role-based access with the three seeded roles, and the admin role for user/role management (§11).

**Phase 7 (later) — Measurement layer hooks.** Corpus database with outcome tracking. Expose write hooks for the deployment team's measurement layer to feed back data.

**Phase 8 (later, separate workstream) — Learning layer.** Pattern detection over corpus performance data. Human-gated writebacks to context layer. Not v1 scope.

---

## 17. Success criteria for v1

The system is v1-ready when:

1. **Two independent runs of the gate-pass checker on the same concept produce the same verdict** at >90% consistency on a golden test set of 20 concepts.
2. **The script maker produces a PASS-verdict concept on first attempt** at >60% rate.
3. **Per-concept end-to-end cost** is in low-single-digit dollars or below.
4. **Human reviewer time per concept** drops from current baseline (30-60 min manual review) to <10 min for final approval on PASS, ~15-20 min on ITERATE.
5. **Zero KILL verdicts have made it past the system to agency production** in a one-month test period.
6. **Production-ready briefs generated by the system are accepted by agencies as-is** without back-and-forth on missing information.

---

## 18. Anti-goals (what this system is NOT)

- **Not a creative selection framework for live performance optimization.** That's Guneet's separate workstream — kill/scale/iterate based on outcome ladder data post-deployment. This system is pre-deployment only.
- **Not a top-of-funnel category creative generator.** Activation only.
- **Not a replacement for agency craft.** Agencies still shoot and edit. The system produces the brief and script they work from.
- **Not a learning system in v1.** Learning is a future workstream layered on top of the measurement layer's data.
- **Not a tool for top-down brief-without-human-input.** Every initiation requires a human brief; every approval gate requires a human signoff.

---

## End

Start with Phase 1 (gate-pass checker minimum viable). If anything in this brief is unclear or contradicts what you find in the source documents, surface it before building — don't infer. Open items in §14 do not block Phase 1.
