# Messaging Thesis

**Owner:** Shiva (`@shivakimothi-design`) · Approval required via CODEOWNERS
**Status legend:** ✅ in place · 🟡 scattered / needs extraction · 🔴 missing

What Wiom says: the L1/L2/L3 thesis, the expressions doctrine, and the locked memory anchors.
Anyone may propose changes (open a PR); they become official only when Shiva approves.

| Sub-folder | What lives here | Status |
|---|---|---|
| `thesis/` | L1/L2/L3 definitions, objectives, differentiators, bridges, must-not-do | ✅ `audience_layers.json` moved here |
| `expressions/` | Contrast doctrine, permitted/forbidden, destination tests | 🟡 extract from Contrast Doctrine v2.1 |
| `memory-anchors/` | Locked verbatim phrasing + JZUR routing | ✅ `memory_anchors.json` moved here |
| `explore/` | Open experiment sandbox (no required owner) | open posting |

**Source docs (moved here from `docs/source_docs/`):** `Wiom_Messaging_System_v1.3.docx`,
`Wiom_Category_Reset_Context_Note.docx`, `Wiom_Category_Reset_Outreach_Annexure.docx` —
the originals the thesis/expressions are distilled from.

> **Load-bearing note:** the live, compiled context the engine actually reads is
> `reference/context_layer.md` — it blends gate definitions (owned by `/evaluation/`) and
> memory anchors / audience layers (owned here). It stays in `reference/` because the code
> reads it by path. When messaging rules change, mirror them into that file in the same PR.
