# Creative Test & Analysis Framework

*The single, repeatable way we plan a creative test and read its data — by objective.*

- **Owner:** Shiva (`/evaluation/`)
- **Status:** v1 · working rule
- **Sits with:** Messaging System v1.3 (who we make for), the BFC-VOLUME Decision Rules (Scale fate engine), and *Before You Trust A Number* (reading discipline).

## Why this exists
So every test is **planned the same way** and **read the same way**. It stops the two failures that cost us decisions:
1. Starting from the biggest number instead of the decision.
2. Reading **Learning** data with **Scale** eyes (or the reverse) — they answer different questions and use different metrics.

Use **Part A** before a test goes live. Use **Part B** when the data comes in. **Part C** is the discipline that wraps both.

---

## Part A — Test Plan Format (fill before any test goes live)
No creative goes live without this one screen.

| Field | What to write |
|---|---|
| **Test ID / name** | e.g. `T-ART-02 · Language anchor` |
| **Who it's for** | Audience layer (L1 / L2 / L3) + need-state |
| **Creative(s) + link** | Each variant by concept ID **with a link to the rendered art**, so reviewers can *see* what's being tested |
| **Pre-launch score** | The 6-dimension scorecard (see "The creative scorecard" below) — recorded *before* launch so we can later test whether the score predicted the result |
| **Hypothesis** | "We believe **[X]** because **[Y]**." (a belief *and* its reason) |
| **The ONE variable** | The single thing changing (e.g. the anchor word) |
| **Held constant** | Everything else — story, protagonist, format, geo, art |
| **Campaign / objective** | **Learning** (clean read) *or* **Scale** (business quality) — and why |
| **Success metric** | The ONE metric that decides it (see Part B) |
| **Decision rule** | "If [metric] does [X] → [call]." Written *before* launch, not after |
| **Confidence gate** | *Relative, not a fixed number* — a call is allowed once the result is **clearly separated from the pool median** (far from the line → fewer bookings needed; hugging the line → keep collecting). Hard floor only: ignore any booking-cost built on ~2–3 bookings (one sale swings it). |
| **Decision deadline** | A date — decide on whatever data exists by then |
| **Guardrail / auto-kill** | Comprehension fail (e.g. reads as *mobile recharge*, or headline ends on "recharge") kills regardless of the numbers |

**Single-variable discipline:** change **one** axis at a time (story / protagonist / need-state / format). If two or more move together, you may **rank** the creatives but you **cannot attribute** the win to any one variable — say so explicitly.

---

## The creative scorecard (pre-launch) — and how we validate it
Every concept is scored before launch on the 6-dimension framework (Donald Miller / Maanas). Record the **weighted score and each dimension** in the test plan, next to the creative's link.

| Dimension | Weight | What it asks |
|---|--:|---|
| Audience | **15** | Does it speak to the right layer + need-state? |
| Motivation | **30** | Does it give a real reason to act? *(heaviest)* |
| Promise | **20** | Is the offer clear and specific? |
| Recharge-mechanic | **15** | Is "pay as you use / *ghar ka net*" legible? |
| CTA | **10** | Is the next step obvious? |
| Thumb-stop | **10** | Will it stop the scroll? |
| **Total** | **100** | → reported as a weighted score out of 10 |

**The score is a prediction, not a verdict.** Log it beside the realized outcome (CTR/hook, CPBL, recharge) for every creative. Across ~30+ creatives we then check whether the score actually predicts performance — and re-weight the dimensions if it doesn't. *(Early signal from the L1 wave: not yet predictive — the highest-scored creative was the pool's worst converter, so watch whether the rubric over-rewards craft and under-prices misread risk.)*

---

## Part B — How to analyse, by objective
The objective decides the metric *and* the lens. **Never mix them.**

### B1 · LEARNING objective — "which idea pulls?"
- **Question:** does the creative earn attention and pull the click? (A clean read of the creative itself.)
- **Metrics — RATES, not costs** (rates strip out auction/CPM noise and isolate the creative):
  - Stopping power → **CTR** (static) / **hook-rate** (video)
  - Pull-through → **install-per-click** (install rate)
  - Bookings / recharge → **directional only** (too little volume to be significant here)
- **How to read:**
  - Matched spend, **same ad-set**, single variable.
  - **Per-theme, never pooled** — compare static vs carousel *within* a theme, not across themes.
  - Powered by **engagement volume** (clicks/impressions) → readable in days.

### B2 · SCALE objective — "which one earns quality business?"
- **Question:** does it produce recharge-quality bookings at acceptable cost?
- **Metrics — walk the funnel, trust the deepest step that has volume:**
  `CPI → cost-per-booking (CPBL) → first-recharge quality`.
  The real verdict metric is **first-recharge at/under the CAC target**; CPBL is the proxy until recharge matures; CPI is the fallback when bookings are thin.
- **How to read — RELATIVE TO SIBLINGS, not absolute rupees:**
  Compare each creative to the **median** of its pool (same ad-set / geo). Lines (from the BFC-VOLUME rules):

  | Where it sits | Meaning | Call |
  |---|---|---|
  | ≤ **0.7×** median | a clear star | **SCALE / isolate** |
  | below median | better than typical | **CONTINUE** |
  | median → **1.2×** | middle of the pack | **MONITOR** |
  | ≥ **1.2×** median | much worse than typical | **KILL (efficiency)** |

  - **Geo-clean:** judge on the **mature geo** (Delhi); pool thin geos and never penalise a creative for a *geo's* intent/serviceability problem.
- **Confidence gate — relative, not a fixed count.** Trust a creative's booking cost once it sits **clearly on one side of the line** — i.e. its gap from the pool median is bigger than its small sample could swing. *Far* below the median → callable on a handful of bookings; *hugging* the median → needs many more before you believe it. Keep only a hard floor: a cost built on ~2–3 bookings is noise → MONITOR. (~₹20k spend ≈ enough to *produce* a callable number at typical cost — a useful spend floor — but it's the **separation from the line**, not the rupees, that licenses the call. ₹20k spent with ~0 bookings *is itself* a call — a kill.)
  - *Why not a fixed "5"?* The **median** answers "who's winning" (relative position); **confidence** answers "can I believe this number" (sample size) — two different jobs. A flat 5 ignores that a creative far from the line is provable on fewer bookings, while one near the line isn't provable even on 15. So gate on **distance-from-line vs sample-noise**, with a floor — not a frozen count.
- **Multi-theme caveat:** if every ad is a different theme (so theme co-varies with story / protagonist / art), Scale **ranks concepts** — it **cannot prove "theme X beats theme Y."** For a clean theme law, run a single-variable theme test in Learning, or brief **2–3 executions per theme** so the theme average becomes readable.

### The median, plainly (so the relative rules make sense)
- **Median** = line the numbers up smallest → biggest; the one in the **middle**. Half below, half above. "The typical creative."
- **Use median, not average:** one disaster drags the *average* up and makes the group look worse than it is; the median ignores *how extreme* an outlier is — it only cares about position.
- **The bar moves on purpose:** kill the worst creative and the median improves, so the "keeper" bar **auto-tightens** toward target. That's why the rule is **relative**, not a frozen rupee number — it's immune to cold-start and scaling noise.

---

## Part C — The reading discipline (run in this order)
*From* Before You Trust A Number. *The order is the point — the conclusion comes last, so you can't jump to it.*

1. **What decision are we making?** No decision attached → don't pull the number.
2. **What metric = success?** A creative can win CTR and lose the business.
3. **Where in the funnel did it move?** spend → impression → click → install → serviceable → booking → recharge.
4. **Which groups win / lose?** Top vs bottom — **never the average alone** (a few stars can carry a dead pool).
5. **Does it survive different cuts?** Geo / channel / segment; remove known distortions (e.g. serviceability) **before** comparing.
6. **Observation or explanation?** "X happened" is proven; "X happened *because* Y" is a hypothesis you still have to test.
7. **What decision changes?** End here, always. If nothing changes, it was reporting, not analysis.

---

## Part D — Logging the learning
Every result is logged as exactly one of:
- ✅ **Observation** — proven by the data.
- 🔶 **Hypothesis** — the "why." Must be backed by a **cultural nuance** or a **corroborating signal** (comprehension test, sales-call transcripts, cancellation reasons), not asserted from the metric alone. Name the data needed to confirm it.
- ❌ **Killed** — with the rule it failed.

Logged learnings live in `/learnings/`. The **rules** for *how* we test and read (this doc) live here in `/evaluation/`.
