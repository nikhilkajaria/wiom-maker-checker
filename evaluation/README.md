# Evaluation Logic

**Owner:** Shiva (`@shivakimothi-design`) · Approval required via CODEOWNERS

The rules the AI checks creative against. Shiva owns the **rules**; the **agent code** that
runs them is shared (`agents/` is co-owned with Nikhil).

| Sub-folder | What lives here | Status |
|---|---|---|
| `g1g2-logic/` | G1 + G2 gate rules (layer-aware **v1.1**), banned-word trigger list, verdict rules, dangerous-misreads weighting | ✅ ratified |
| `agents/` | The plumbing that runs the rules + post-prod **v1.0** spec + the open question to Nikhil | 🟡 / 🔴 |

Start here: [`g1g2-logic/v1.md`](g1g2-logic/v1.md).

> **Load-bearing note:** the running engine reads `reference/context_layer.md` (§6, §7, §13
> hold the gate definitions). It stays in `reference/` because the code reads it by path.
> `g1g2-logic/v1.md` is the human-readable source of truth; keep the two in sync by hand
> until Phase-2 auto-rebuild lands.
