# Creative Data Analyst

An agent that reads Wiom's ad-account data the way a diagnostician would:
every metric is a lens on one ability of the creative (Hook / Hold / Pull /
Honesty / Efficiency), creatives are placed in a 2×2
(attention × conversion), and the report tells you exactly which two
creatives to look at side-by-side to extract a learning.

- **Method**: [framework.md](framework.md) (locked v1 — read this first)
- **Data engine**: [fetch_and_score.py](fetch_and_score.py)
- **Agent**: `.claude/agents/creative-data-analyst.md` (repo root)
- **Runs land in**: `runs/<end-date>_<N>d/` → `data.json`, `tables.md`,
  `report.md`

## One-time setup

1. Get your personal dashboard token from Kashish (shared by DM, never in
   docs).
2. Put it in `C:\credentials\.env` (create the file if needed):
   `GROWTH_DASHBOARD_TOKEN=<token>`
   (`WIOM_DASHBOARD_TOKEN` also works — that's the name in Kashish's doc.)
3. Python 3.9+ on PATH. No packages needed (stdlib only).

## Using it

In Claude Code, from this repo:

> run the creative data analyst

Optionally with a window:

> run the creative data analyst for June
> run the creative data analyst, last 7 days

Or run the data engine directly (tables only, no narrative):

```
python evaluation/creative-data-analyst/fetch_and_score.py
python evaluation/creative-data-analyst/fetch_and_score.py --days 7
python evaluation/creative-data-analyst/fetch_and_score.py --start 2026-06-01 --end 2026-06-30
```

## The learning loop

Each run's report ends with **candidate learnings** (proposed, unconfirmed)
and **divergence pairs** — pairs of creatives whose data profiles cross
(one wins attention, the other wins conversion). A human looks at those two
creatives, decides what explains the gap, and confirms or rejects the
candidates. The final learning is then written into
`learnings/performance/` **manually, by its human owner, in their own
words** — the agent and the creative-director skill never write there.
Creativity is taste and judgment, owned by humans. That's how the system
compounds: data names the experiment, machines argue, humans own the
learning.

## Troubleshooting

- `credentials file not found` / token missing → step 1–2 above.
- DNS failure on JioFiber → handled automatically (resolves via 8.8.8.8 and
  pins the IP).
- 404 on a date → that day has no record yet; the engine only uses dates
  the API lists as available.
