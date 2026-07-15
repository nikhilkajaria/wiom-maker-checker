# Creative Data Analyst — Run Report

**Window:** 2026-06-30 → 2026-07-13 (14 completed days, split 7v7 for trend)
**Generated:** 2026-07-15 · First production run
**Caveats:** install attribution for the last ~14 days is still maturing;
Google spend ₹11,32,690 excluded from creative ranking (no creative
taxonomy); all numbers are Meta only. Full tables: [tables.md](tables.md) ·
raw: [data.json](data.json)

---

## 1. BFC-VOLUME (the scale campaign) — the main read

### Delhi · Statics (5 qualified)

| Creative | CTR% | CVR% | CPI ₹ | Spend ₹ | Quadrant | Trend |
|---|---|---|---|---|---|---|
| T-064 | 0.512 (worst) | **11.0 (best)** | **60.0** | 60,101 | 🤝 honest-but-invisible | ⚠ fatigue |
| T-063 | **0.576 (best)** | 9.2 | 64.7 | 224,125 | 🏆 all-rounder | ⚠ fatigue |
| T-083 | 0.548 | 5.9 | 91.0 | 124,293 | 🎣 clickbait | |
| T-085 | 0.545 | 7.7 | 98.4 | 9,054 | 🤝 | |
| T-082 | 0.552 | 5.8 | 119.5 | 15,415 | 🎣 clickbait | |

### Delhi · Videos (3 qualified)

| Creative | Hook% | Hold% | CTR% | CVR% | CPI ₹ | Quadrant | Trend |
|---|---|---|---|---|---|---|---|
| C-076 | 12.7 | 19.6 | 0.367 | **25.1** | **86.0** | 🏆 all-rounder | |
| C-069 | 8.3 (worst) | 22.9 | 0.307 | 16.9 | 87.8 | 🤝 | ⚠ fatigue |
| C-077 | 12.2 | **23.1** | **0.443** | 11.1 | 126.6 | 🎣 clickbait | |

### Bharat · Statics (4 qualified)

| Creative | CTR% | CVR% | CPI ₹ | Spend ₹ | Quadrant | Trend |
|---|---|---|---|---|---|---|
| T-064 | 0.711 | **22.7** | **21.1** | 9,413 | 🏆 | ⚠ fatigue |
| T-063 | **0.733** | 18.0 | 22.2 | 63,429 | 🏆 | ⚠ fatigue |
| T-085 | 0.626 | 13.3 | 42.8 | 6,334 | ❌ weak | |
| T-083 | 0.647 | 10.0 | 44.8 | 10,882 | ❌ weak | |

### Bharat · Videos (12 qualified — ⚠ pool mixes BHARAT_ALL and city ad
sets; same concept appears once per ad set)

Top of pool: **H-004** (CPI ₹19.2–20.6 across both its ad sets, 1,652
installs combined, hook ~25–27%) but ⚠ fatigue-flagged in both. **C-076**
repeats its Delhi personality: worst hook (11.2%), best honesty (CVR
41.9%). H-002/H-003 at scale slip to 🎣 (CVR ~12%).

## 2. The cross-pool patterns (data-side observations)

1. **T-064 is the honesty champion in both geos** — CVR #1 in Delhi (11.0%)
   and Bharat (22.7%) with bottom-of-pool CTR in Delhi. Whatever it
   promises survives the store page.
2. **C-076 has the same personality in both geos** — worst hook, best CVR
   (25.1% Delhi / 41.9% Bharat). The most honest promise in the video pool,
   wrapped in the weakest opener.
3. **⚠ Fatigue is pool-wide, not creative-specific**: T-063, T-064 (both
   geos), C-069, H-004, H-002, H-003 all show 2nd-week CPI >1.3× 1st-week.
   When *everything* fatigues at once, suspect market/seasonal shift or
   auction change, not individual creative decay. Needs corroboration next
   run before acting.
4. **H-004's CVR differs by ad set** — 34.5% in its smaller ad set vs 21.0%
   in the bigger one. Same creative, different targeting → honesty is
   partly a targeting property. (Also why cross-ad-set caveats matter.)

## 3. Quadrant actions (BFC-VOLUME only)

- **Scale / keep**: T-063, T-064 (both geos), C-076, H-004 — but resolve
  the fatigue question first (point 3 above).
- **Fix the promise (keep the hook)**: T-083, T-082 (Delhi statics),
  C-077, H-002.
- **Rebuild the hook (keep the promise)**: C-069, C-076, H-001.
- **Kill / recycle**: T-085 & T-083 in Bharat (weak in that pool), H-005.

## 4. Divergence pairs — the content reads a human should do

| Pool | Pair (attention × conversion) | Question to answer looking at them |
|---|---|---|
| Delhi Static | **T-082 × T-064** | Near-equal CTR, 2× CVR gap: what expectation does T-064 set that T-082's click doesn't survive? |
| Delhi Video | **C-077 × C-069** | C-077 wins hook/hold/CTR, C-069 wins CVR/CPI: what does C-069 say about the offer that C-077's attention device hides? |
| Bharat Static | **T-063 × T-064** | Same family, tiny CTR gap, 4.7-pt CVR gap: isolate the promise element. |
| Bharat Video | **H-002 × C-076** | H-002 hook 26% / CVR 12; C-076 hook 11% / CVR 42: the cleanest hook-vs-honesty split in the account. |

## 5. Candidate learnings — PROPOSED, UNCONFIRMED

*(nothing below goes to `learnings/performance/` until a human confirms it
against the actual creatives)*

- **CL-1**: T-064 contains a promise/expectation element that converts
  clicks ~2× better than sibling statics in both geos. Identify it via the
  T-082 × T-064 read; graft onto higher-CTR statics.
- **CL-2**: C-076's script/promise is the most store-page-honest message in
  the video pool (CVR top in both geos); its opener wastes it. A re-hooked
  C-076 is the highest-expected-value video edit available.
- **CL-3**: The simultaneous fatigue flags across BFC-VOLUME are one
  market-level event, not six creative decays. (Verify next run; check
  against seasonality calendar.)

## 6. Questions for the human

1. 12 ad sets (`META_ACTIVECUSTOMERS_50MBPS_*`, `META_CSP_ROHIT_*`) have no
   geo prefix — which geography, and are existing-customer/partner reach
   campaigns even in scope for this framework?
2. Campaign `META_PR_MULTI_ABO_Aware_PM-AWARENESS_050626` — new family
   `PM-AWARENESS`? (Its video JUN26-PR-001: hook 64%, ThruPlay 23% —
   exceptional attention numbers, zero installs, aware objective.)
3. AWARENESS pool currently blends WARM / COLD / PROBE campaigns (different
   audiences). Should the family cut split them into sub-pools?
4. RETARGETING runs a Sales objective — CPI ₹207–532 and CVR 2.7–7.2% here
   are expected to look "bad" on install lenses. Keep reporting it this way,
   or wait for the booking lenses (CPBL) to judge it properly?
5. Mumbai: still zero spend anywhere in the window. Expected?

## 7. Seen but not judged

29 ad-rows below spend floor, 27 inactive (incl. the whole CREATIVE-TESTING
campaign — paused; its T-063/064/082/083/085 concepts now run inside
BFC-VOLUME instead). AWARENESS·Delhi install-lens numbers (CVR ≤0.4%, CPI
₹1,300+) reflect a LEARNMORE/website objective, not creative failure — read
that pool on hook/hold only (B-001: hook 39%, hold 29%; B-007: hook 52%).
