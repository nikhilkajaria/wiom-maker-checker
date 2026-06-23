# Governance — Wiom Maker-Checker

Who owns what, who can change what, and how changes get approved. This is the
plain-language companion to [`CODEOWNERS`](CODEOWNERS), which enforces it.

## The one rule to understand: access ≠ ownership

- Everyone on the team can **read** the whole repo and **propose** changes anywhere —
  post a learning, drop an experiment in Explore, open a change to any file.
- A change becomes **official only when the area's owner approves it.**
- "Ownership" = that approval right. It is **not** a locked door. Anyone can propose;
  the owner signs off.

This is enforced by **CODEOWNERS + branch protection**: changes to a protected path
can't merge until the listed owner reviews them.

## Who owns what

Plain version: **Shiva owns what we say and what passes. Nikhil owns how we build it
and what goes to the agency. Karishni turns results into learnings. The library and
constitution belong to both leads.**

| Area (repo path) | Owner | Meaning |
|---|---|---|
| Messaging thesis — `/messaging/` | Shiva | L1/L2/L3, expressions, memory anchors. Only Shiva approves edits. |
| Evaluation logic — `/evaluation/` | Shiva | The G1/G2 + post-prod rules the AI checks against. |
| Agent code — `/evaluation/agents/` | Shiva + Nikhil | The plumbing that runs the rules — shared engineering, not Shiva's alone. |
| Wrapper — `/wrapper/` | Nikhil | The four test variables, determined params, formats-spec. |
| Product briefs — `/briefs/` | Nikhil | The production-ready briefs sent to the agency. |
| Creative library — `/creative-library/` | Shiva + Nikhil | Shared. Either lead can approve. |
| Constitution — `/constitution/` | Shiva + Nikhil | Non-negotiables + brand guidelines. Both must approve. |
| Learnings — `/learnings/` | Open | Anyone posts; Karishni curates; the actual rule change is approved by the area owner where it lands. |
| Explore — `/messaging/explore/` | Open; Shiva governs promotion | Anyone posts experiments; Shiva approves what gets promoted into the thesis. |
| Performance — `/performance/` | Shiva + Nikhil | Deployed registry + tracking-sheet link. |

## How a change gets made

1. Anyone opens a change (a pull request) to any file.
2. The owner of that path is automatically requested for review (via CODEOWNERS).
3. The change merges only after the owner approves. For the constitution, **both leads** approve.
4. Learnings and Explore are open — post freely; the change only affects a *rule* once the
   owner edits the gated file it points to (the learning → change loop).

## What must be true for this to actually enforce

CODEOWNERS is only a notification list until the repo admin turns on **branch protection**.
Required settings on `main`:

- **Require a pull request before merging** (disable direct pushes to `main`).
- **Require review from Code Owners.**
- For the constitution's "both must approve": set **Required approvals = 2**.

**Owner: repo admin (Nikhil). One-time setup.**

## Notes

- The handles in CODEOWNERS are real: `@nikhilkajaria`, `@shivakimothi-design`, and Karishni
  is `@karishnipuri-star` (curates `/learnings/`, which is open — not a required reviewer).
  Make sure each listed owner has repo access.
- This file (and `CODEOWNERS`) are themselves owned by **both leads** — changing the
  governance needs both.
- Repo guardrails (this file) are separate from any future web-app user roles / SSO.
  Don't confuse the two.
