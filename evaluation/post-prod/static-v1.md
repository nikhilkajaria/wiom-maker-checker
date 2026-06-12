# Post-Production Check — STATIC (v1.0)

**Owner:** Shiva (`@shivakimothi-design`) · **Status:** draft for ratification
**Companion to:** the video-oriented post-prod v1.0 in [`/evaluation/agents/README.md`](../agents/README.md)
and the gate rules in [`/evaluation/g1g2-logic/v1.md`](../g1g2-logic/v1.md).
**Source framework:** [`Wiom_Creative_Static_Evaluation_Framework.docx`](Wiom_Creative_Static_Evaluation_Framework.docx)
(the 6-dimension scoring model).

Runs on the **rendered static art** (the delivered 1:1 image), **before spend**. Order matters:
**gate first, disqualifiers second, score third.** A static that fails an earlier stage never
reaches a later one.

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
- **A7 Mobile legibility:** 6-element text budget · one-idea-once · 3-second phone-size test ·
  smallest-text-rule (small lines move to the caption).

---

## STAGE 2 — 6-dimension score (rendered art)

Weighted score from the source framework (Section C):

| Dimension | Weight |
|---|---|
| Audience | 15% |
| Motivation | 30% |
| Promise | 20% |
| Recharge-Mechanic visibility | 15% |
| CTA | 10% |
| Thumb-Stop | 10% |

`Score = 0.15·Aud + 0.30·Mot + 0.20·Prom + 0.15·Mech + 0.10·CTA + 0.10·ThumbStop`

---

## Verdict

- **PASS** — clears Stage 0 + no Section A breach + score ≥ threshold. → goes live.
- **ITERATE** — a fixable Stage 0 / Section A issue, or a sub-threshold score. → fix and re-check.
- **KILL** — wrong frame or unfixable contamination. → logged, not nurtured. **Default bias = KILL.**

## ⏳ Open item for Shiva to ratify

The source framework gives weights but **no numeric pass bar.** The June L1 wave scored **6.3–8.2**
(scaled the ≥~7.0 set). **Shiva to set the threshold** (e.g. "≥7.0 to scale, 5.5–6.9 iterate, <5.5
kill") — left as TBD until ratified.
