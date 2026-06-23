# Evaluation Logic

**Owner:** Shiva (`@shivakimothi-design`) · Approval required via CODEOWNERS

The rules the AI checks creative against. Shiva owns the **rules**; the **agent code** that
runs them is shared (`agents/` is co-owned with Nikhil).

| Sub-folder | What lives here | Status |
|---|---|---|
| `g1g2-logic/` | G1 + G2 gate rules (layer-aware **v1.1**), banned-word trigger list, verdict rules, dangerous-misreads weighting | ✅ ratified |
| `post-prod/` | Post-production checks on the rendered asset — **static v1.0** + pointer to video | ✅ static ratified |
| `agents/` | The plumbing that runs the rules + the open question to Nikhil | 🟡 / 🔴 |

Start here: [`g1g2-logic/v1.md`](g1g2-logic/v1.md).

## Two-track model — video vs static

The number of checks depends on production cost. Video is expensive to produce, so the **concept**
is gated *before* shooting; a static's art *is* the concept, so it's checked **once**, on the
rendered art.

| | Video | Static |
|---|---|---|
| Pre-production gate (G1/G2 on the concept) | ✅ protects expensive production | ❌ skip — nothing expensive to protect |
| Post-prod check (on rendered art) | ✅ video post-prod (multimodal re-run + craft) | ✅ **static post-prod = the single gate** (G1/G2 Stage 0 + Section-A + score) |
| Automated checkpoints | **2** | **1** |

## How to run a check — what to type

> **Honest status:** only the **concept-level G1/G2** checker is *built and runnable today*. The
> **post-prod** checks (video and static) are **ratified criteria, not yet wired into code** — they
> need the engine to actually *see* the rendered image/video (a vision step the current text-only
> checker doesn't have). See `agents/` for the build plan + Nikhil's local-vs-auto decision.

| Want to check… | What Nikhil types (or does) | Available? |
|---|---|---|
| **Concept against G1/G2** (the video pre-production gate) | `python scripts/run_gate_check.py <concepts.json> --concept_id <ID>` | ✅ today |
| **Finished video** (post-prod) | *not built yet* — future: `run_post_prod.py --type video --asset <file>` | 🔴 build |
| **Finished static** (post-prod = the single static gate) | *not built yet* — future: `run_post_prod.py --type static --asset <art.jpg>` | 🔴 build |

If Nikhil picks **auto-on-PR** (the open question in `agents/`), he types **nothing** — he opens a
PR with the concept/asset and the check runs itself.

> **Load-bearing note:** the running engine reads `reference/context_layer.md` (§6, §7, §13
> hold the gate definitions). It stays in `reference/` because the code reads it by path.
> `g1g2-logic/v1.md` is the human-readable source of truth; keep the two in sync by hand
> until Phase-2 auto-rebuild lands.
