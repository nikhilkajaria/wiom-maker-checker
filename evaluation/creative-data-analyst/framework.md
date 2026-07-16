# Creative Data Framework v1

*Owner: Shiva (evaluation/). Locked 2026-07-15. The method the
`creative-data-analyst` agent runs. Scope v1: ad-account metrics up to app
install. Booking (CPBL) and recharge lenses get added once those flows are
finalised — install-efficiency is NOT the business KPI, it is the furthest
clean signal available today.*

## Why this exists

Ad metrics are usually read as one leaderboard ("which ad has the best
CPI?"). That hides *why* an ad wins, and the why is the only thing you can
reuse in the next creative. This framework turns the ad account into
diagnosis: every metric is a lens on one specific ability of the creative,
and learnings come from comparing creatives whose abilities differ.

## Step 0 — Build clean pools (never compare across a pool boundary)

A pool = **campaign family × geography × format**, then two filters:

| Cut | Rule | Why |
|---|---|---|
| 1. Campaign family | BFC-VOLUME / RETARGETING / CREATIVE-TESTING / … auto-discovered from campaign names; new families get their own pool + a flag | Different objective & audience = different auction; cross-family numbers don't compare |
| 2. Geography | Delhi / Bharat / Mumbai (from ad-set prefix) | CPMs and audiences differ ~3× |
| 3. Spend floor | ₹5,000 (Delhi/Mumbai), ₹1,500 (Bharat) per 14 days, scaled to window; below floor = listed, never ranked | Rates on tiny spend are noise |
| 4. Format | Statics and Videos are separate pools, always | Different metrics exist, different jobs |
| + Active | Spend in the window's last 3 days | Paused ads are history, not options |

Default window: **last 14 completed days**, always split **first-7 vs
last-7** for the fatigue check. Custom windows allowed (pin to campaign
changes, not just calendars). Rationale: Meta's 7-day-click attribution and
weekly seasonality make 7-day blocks the judgment unit; >3 weeks blends
different market conditions (fee changes, festivals).

## Step 1 — Score five lenses (the formula)

| # | Lens | Formula | Question it answers | Where to look in the creative |
|---|---|---|---|---|
| 1 | **Hook** | 3-sec views ÷ impressions *(video)* | Did the first frame stop the scroll? | Opening frame, first spoken line, face/contrast |
| 2 | **Hold** | ThruPlays ÷ 3-sec views *(video)* | Did the story keep them? | Pacing, seconds 3–15, when the offer appears |
| 3 | **Pull (CTR)** | clicks ÷ impressions | Did the message make them want more? | Headline claim, curiosity gap, CTA |
| 4 | **Honesty (CVR)** | installs ÷ clicks | Did the promise survive the store page? | Expectation the ad sets vs what the store shows |
| 5 | **Efficiency (CPI)** | spend ÷ installs | Net cost — the scoreboard | Nothing directly: CPI = CPM ÷ (CTR × CVR) |

Notes:
- ThruPlay rate = Hook × Hold. Never read it blended — two ads can share a
  ThruPlay rate for opposite reasons (great opener/leaky story vs the
  reverse), and the fix is different for each.
- Statics get lenses 3–5 only (CTR doubles as their hook proxy).
- **Trust weight**: raw install count is a *budget* outcome, not a quality
  score (installs = spend ÷ CPI). Its use: <50 installs → read direction,
  not decimals; high spend at stable CPI → proven at scale.

## Step 2 — Collapse to two scores, place in the 2×2

- **Attention score** = mean rank on Hook + Hold + Pull (statics: Pull only)
- **Conversion score** = rank on Honesty (CVR)

| | High conversion | Low conversion |
|---|---|---|
| **High attention** | 🏆 All-rounder | 🎣 Clickbait profile |
| **Low attention** | 🤝 Honest-but-invisible | ❌ Weak |

## Step 3 — Action per quadrant

- 🏆 → scale; watch weekly CPI for scale-decay (fatigue flag = 2nd-half CPI
  >1.3× 1st-half)
- 🎣 → keep the hook, fix the promise (borrow one from a 🤝)
- 🤝 → keep the promise, rebuild the hook (borrow one from a 🎣)
- ❌ → kill; recycle elements only

## Step 4 — The insight loop (where learnings come from)

A learning is a PATTERN, never a single comparison. The loop:

1. **Notice** — inside a divergence pair (creatives whose ranks cross),
   spot a visible/verbal content difference.
2. **Hypothesize** — turn it into one plain sentence ("a person sharing
   his own problem stops more people than advice does").
3. **Test across the pool** — tag every creative in the SAME geo + format
   pool for that trait and check: do the high scorers have it and the low
   scorers lack it? One pair suggests; only the pool-wide check proves.
4. **Only a pattern that survives step 3 becomes a candidate learning** —
   and the final learning is still written manually by a human.

Rules for step 3:
- **Never test a pattern across geos.** Delhi and Bharat audiences differ
  culturally and by profile; a geo may *echo* a pattern (worth noting) but
  never counts as proof for the other geo.
- **Creator fame is its own trait.** A known local face lifts hook by WHO
  they are, not what the creative says — tag it separately so it isn't
  mistaken for a content effect.
- **Tag only what you're sure of.** Who is saying, how, what, design,
  expressions — many traits live in the voice-over or in taste. Machines
  tag what is visible; unsure traits go to the human as a tag sheet, not
  as guesses.

Benchmarks are reported as **best / median / worst** (p100 / p50 / p0) per
pool — the comparison lives at the extremes; the median only shows where
"normal" is.

Reports are written in plain language: short sentences, no jargon, every
term explained the first time it's used. The report exists to be consumed
and applied by others.

## Known limits (state them, don't hide them)

- Reads to install only (v1). A creative can win CPI and attract non-bookers.
- Google ads carry no creative taxonomy → excluded from creative ranking;
  their spend is reported as a line item.
- Attribution: installs are attributed within a 14-day window; the most
  recent days are still maturing.
- RETARGETING runs on a Sales objective — install-lenses may be the wrong
  read there; the agent flags this rather than pretending.
