# Restructure Spec — Ownership-Governed Layout

**Date:** 2026-06-10 · **Author:** Shiva (with Claude) · **Status:** proposed (this branch)

## Goal

Reorganise the repo by **ownership** so a `CODEOWNERS` file + branch protection can enforce
"anyone can propose, only the owner approves." The ownership structure is layered **on top of**
the working engine — the engine is not disturbed.

## Principles honoured

1. **Rearrange + add docs — don't edit code.** No source file's contents were changed.
2. **History preserved.** All relocations use `git mv` (shown as renames in the diff).
3. **Nothing breaks.** The load-bearing file the engine reads stays exactly where it is.
4. **Gaps stay visible.** Missing pieces become assigned README stubs (owner + 🔴 status),
   not silent absences.

## Three kinds of change

### 1. Pure additions (zero risk)
- New owned folders: `messaging/ wrapper/ evaluation/ briefs/ creative-library/ constitution/ learnings/ performance/` (+ sub-folders), each with a README declaring **owner + status**.
- Root governance: [`CODEOWNERS`](../../CODEOWNERS) + [`GOVERNANCE.md`](../../GOVERNANCE.md).
- Gate logic: [`evaluation/g1g2-logic/v1.md`](../../evaluation/g1g2-logic/v1.md) — **G1/G2 v1.1, layer-aware**.
- Agent stub: [`evaluation/agents/README.md`](../../evaluation/agents/README.md) — post-prod **v1.0** + the open question to Nikhil.
- Switched-OFF automation **template**: [`evaluation/agents/gate-check.workflow.yml`](../../evaluation/agents/gate-check.workflow.yml). Kept outside `.github/workflows/` so it never auto-runs and needs no special token scope; arming = copy it into `.github/workflows/`.
- Three source docs placed: two learnings + the L1/L2 creative briefs.

### 2. Safe moves (verified: zero code references)
| From | To |
|---|---|
| `reference/memory_anchors.json` | `messaging/memory-anchors/` |
| `reference/audience_layers.json` | `messaging/thesis/` |
| `reference/need_states.json` | `wrapper/test-variables/` |
| `reference/dangerous_misreads.json` | `evaluation/g1g2-logic/` |

A `grep` over all `*.py` confirmed none of these four are read by code before moving.

Source docs (also verified zero code references) moved from `docs/source_docs/` to their owners:
| From `docs/source_docs/` | To |
|---|---|
| `Wiom_Messaging_System_v1.3.docx` | `messaging/` |
| `Wiom_Category_Reset_Context_Note.docx` | `messaging/` |
| `Wiom_Category_Reset_Outreach_Annexure.docx` | `messaging/` |
| `Wiom_Performance_Creative_Framework_v0_9.docx` | `wrapper/` |
| `Wiom_Performance_Marketing_Principles.docx` | `constitution/` |

`experiments/` and `tests/` were **kept in place** — verified they ARE read/written by code
(`scripts/export_registry_to_json.py` writes `experiments/`; the checker reads
`tests/golden_concepts/concepts.json`).

### 3. Left 100% untouched
`layers/ shared/ scripts/ tests/ logs/ experiments/ docs/ README.md requirements.txt`
— and critically **`reference/context_layer.md`**, which the engine reads by path
([`layers/gate_checker/prompts.py:11`](../../layers/gate_checker/prompts.py)). It is a
*blend* of several owners' content, so it has no single clean home; `/evaluation/` and
`/messaging/` READMEs point to it instead of moving it.

## Key decisions (made during brainstorming)

- **Delivery:** as a Pull Request. Shiva's account has read-only access, so we **fork →
  push to fork → open PR** into `nikhilkajaria/wiom-maker-checker`. Built locally first for
  Shiva's review; nothing pushed until approved.
- **Code safety:** keep the running engine 100% untouched (this pass).
- **Agents:** document + stub now, **arm later** (criteria must be finalised first, and the
  API key + branch protection are Nikhil's one-time admin steps).
- **Gate logic v1.1:** layer-aware. Strictness dials **L3 (strict) → L1 (lenient)** because
  mobile-data-misread risk falls as the viewer already lives in the WiFi frame.

## Open items (carried forward)

- **Nikhil:** choose local vs auto-on-PR checking (baked into the PR description + agents README).
- **Nikhil (admin):** enable branch protection on `main` (else CODEOWNERS doesn't enforce);
  add `ANTHROPIC_API_KEY` secret when arming the agent.
- **Nikhil:** create the formats-spec (unblocks post-prod P3 hygiene).
- **Both leads:** agree the creative-library schema + the performance registry schema.
- **Replace** `@karishni-handle` in CODEOWNERS with the real username.
- **Phase 2:** split `context_layer.md` into per-owner sources + auto-rebuild, so the
  rules-doc and the engine's context stop needing manual sync.
