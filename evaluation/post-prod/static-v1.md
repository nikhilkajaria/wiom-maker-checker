# Post-Production Check — STATIC (v1.0)

**Owner:** Shiva (`@shivakimothi-design`) · **Status:** draft for ratification · **scoring model: v2.0**
**Companion to:** the video-oriented post-prod v1.0 in [`/evaluation/agents/README.md`](../agents/README.md)
and the gate rules in [`/evaluation/g1g2-logic/v1.md`](../g1g2-logic/v1.md).
**Source framework:** [`Wiom_Creative_Evaluation_Framework_v2.0.docx`](Wiom_Creative_Evaluation_Framework_v2.0.docx)
(v2.0 — 6-**criterion** scoring; splits Hook/Thumb-Stop from Audience Relevance). *The v1 framework is
kept as a log in [`_archive/`](_archive/).*

Runs on the **rendered static art** (the delivered 1:1 image), **before spend**. Order matters:
**gate first, disqualifiers second, score third.** A static that fails an earlier stage never
reaches a later one.

> **This is the single, sufficient gate for a static.** Statics do **not** need a separate
> pre-production G1/G2 concept-gate — video does (because video production is expensive and worth
> protecting before you shoot). A static's art *is* the concept, so it's checked **once**, here,
> on the rendered art. See the two-track model in [`/evaluation/README.md`](../README.md).

---

## STAGE 0 — Gate pass (G1 + G2) on the rendered static  ← the encapsulation

This stage is exactly the [`g1g2-logic/v1.md`](../g1g2-logic/v1.md) gates, applied to the finished
image. A static **passes the gate only if both hold:**

- **G1 — Category-frame integrity:** ghar anchor present · **recharge-shape clear** (on a static
  this means the recharge mechanic is *visible* — durations `1 din | 7 din | 14 din` or the rule
  line, not merely implied) · no frame drift (does not land as cheap WiFi / mobile data / broadband).
- **G2 — Contamination / banned words:** no banned word used as Wiom's **identity** · the
  **destination noun lands on "net / ghar ka net," never "recharge" as the final word** · a
  comparison static lands on **Wiom's category** (the A5 carve-out), not "a different WiFi."

**Layer:** these statics are **L1** (capture-bridge, WiFi-as-launchpad). Apply the **dual-persona
range test** (would it also *not confuse* an L2 viewer?). **No L3 hooks** this round.

**A static that fails G1 or G2 is fixed or killed before scoring** — this is the pre-flight gate in
the June test plan (Doc 2, "Pre-flight, every concept").

> **Why this "encapsulates G1/G2":** Stage 0 *is* the G1/G2 gate run on the rendered art. Anything
> that clears Stage 0 has, by construction, passed G1 and G2 — Stages 1–2 only add craft + scoring
> on top. The mapping below shows every gate clause also has a redundant catch in Stage 1/2.

| Gate clause | Also enforced at |
|---|---|
| G1 — ghar anchor | Step 1 Audience · A6 (real home, user-as-hero) |
| G1 — recharge-shape visible | Step 4 Recharge-Mechanic Visibility · A1 positioning |
| G1 — no frame drift | A6 visual anti-patterns · A5 comparison destination |
| G2 — no banned word as identity | A3 vocabulary rules |
| G2 — destination = net, never recharge | A5 comparison rule · Contrast Doctrine v2.1 safety rule |

---

## STAGE 1 — Section A brand disqualifiers

Any breach = **disqualified regardless of score** (from the source framework):

- **A1 Positioning** — new category, recharge mechanic visible (not implied).
- **A3 Banned vocabulary** — WiFi, broadband, plan, monthly, validity, unlimited, subscription, quarterly.
- **A4 CTA** — primary CTA is **"Book Karein" + Play Store icon** (only approved primary).
- **A5 Comparison** — destination is Wiom's category, not just Wiom's name; not brand-switching.
- **A6 Visual anti-patterns (auto-fail):** speed-test / Mbps as hero · glowing routers, signal waves,
  fibre, data-centre imagery · stock corporate families in premium apartments · city skylines /
  abstract tech · app-UI screenshot as primary image.
  **(carve-out) The Wiom pink WiFi mark / category glyph is NOT an anti-pattern — it is the category
  launchpad (see the Stage-0 WiFi-symbol clarification). A6 bans generic telecom *signal* imagery
  (glowing routers, radiating waves, fibre, data-centre), never our glyph.** *(resolves the false-positive
  where a glyph-hero static cleared Stage 0 but died at A6.)*
- **A7 Mobile legibility:** 6-element text budget · one-idea-once · 3-second phone-size test ·
  smallest-text-rule (small lines move to the caption).

---

## STAGE 2 — 6-criterion score (v2.0, rendered art)

v2.0 **splits attention (Hook) from relevance (Audience)** so the two stop double-counting, and
rebalances the weights. Score each criterion **0–10, independently**, then weight.

| # | Criterion | Weight | Core question |
|---|---|---|---|
| 1 | **Hook / Thumb-Stop** | 15% | Will they pause & consume the next element? |
| 2 | **Audience Relevance** | 15% | Will the right person feel "this is for me"? |
| 3 | **Motivation** | 25% | Why care enough to reconsider or act? |
| 4 | **Product Promise** | 20% | What outcome / value do I get? |
| 5 | **Recharge Mechanic** | 15% | How does recharge-by-days actually work? |
| 6 | **CTA** | 10% | What do I do next? |

`Score = 0.15·Hook + 0.15·Audience + 0.25·Motivation + 0.20·Promise + 0.15·Mechanic + 0.10·CTA`

**Scoring rules (v2.0):**
- **Score the full sequence, not the headline alone** — the visual + next line can complete a job.
- **No double-counting attention** — a curiosity / character / celebrity hook is valid; don't mark
  **Hook** down for not naming the audience. Judge relevance on the *next line/visual* (the "relevance bridge").
- **Promise ≠ Mechanic** — Promise = *what I get* (outcome); Mechanic = *how it works* (recharge-by-days). Score separately.
- **One line may earn two scores** if it does two distinct jobs — state the distinct reason for each.
- For every criterion, write: the score · one sentence on *why it isn't higher* · one specific improvement.

### Per-criterion score bands (v2.0)

Anchors live here (in the `.md`) so rubric changes are reviewable and the reviewer agent reads them; the
docx stays the narrative source.

- **Hook / Thumb-Stop** — `0–2` generic / ignored · `3–4` surface interest, weak reason to continue ·
  `5–6` noticeable but predictable · `7–8` strong entry, earns the next line · `9–10` exceptionally
  distinctive, immediately processed, hard to ignore.
- **Audience Relevance** — `0–2` could be for anyone · `3–4` vaguely implied / forced · `5–6` some
  relevance but too much inference or generic · `7–8` the intended audience quickly gets why it matters ·
  `9–10` immediate self-recognition, minimal decoding.
  *(Relevance can be landed by **visuals, objects (router / recharge screen / day-chips), setting or copy** —
  a human in frame is neither necessary nor sufficient. Do not dock a no-human creative on Audience.)*
- **Motivation** — `0–2` no reason to care · `3–4` generic benefit / weak pain · `5–6` rational but not
  sharp or emotional · `7–8` clear pain, desire or economic benefit · `9–10` strong emotional trigger,
  fairness tension, or locked belief cracked (esp. L2).
- **Product Promise** — `0–2` confusing / wrong category vocab · `3–4` some benefit but unclear /
  undifferentiated · `5–6` understandable but generic or feature-led · `7–8` clear, on-category, valuable ·
  `9–10` instantly understood, strongly positions the new category.
- **Recharge Mechanic** — `0–3` absent or misunderstood (**fails the category requirement**) · `4–6`
  flexibility implied but recharge-by-days not concrete · `7–8` clearly explained or shown · `9–10`
  immediately clear **and** strengthened by proof, an exceptionally simple demonstration, or a
  **no-upfront-cost carve-out ("0 shuruaati kharcha")** — **NOT a plan / recharge price anchor** (a price
  anchor on a plan reads as "cheap plan" and is not credited).
- **CTA** — `0–2` none / misleading · `3–4` generic or weak · `5–6` present but icon, clarity or prominence
  missing · `7–8` correct CTA + expected cues · `9–10` clear CTA + useful supporting context, no clutter.

---

## Verdict — v2.0 interpretation bands

**Gate first** (Stage 0 + Section-A) — **any gate failure = rework, whatever the score.** Then the
weighted total:

| Weighted score | Verdict |
|---|---|
| **8.5–10.0** | **Strong test candidate** — clear strategic role, few structural weaknesses → test / scale |
| **7.0–8.4** | **Promising** — needs a specific improvement before/during testing → iterate |
| **5.5–6.9** | **Material weakness** — rework before media spend |
| **< 5.5** | **Weak / misaligned route** → kill |
| any gate failure | rework irrespective of score · **default bias = KILL** on wrong-frame / contamination |

> **Threshold note (your call):** v2.0 puts the "strong / scale" bar at **8.5** — earlier you ratified
> **8.0**. I've written it at **8.5 per the new doc**; say the word if you want to hold 8.0.
