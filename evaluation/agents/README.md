# Evaluation Agents

**Owner:** Shiva + Nikhil (`@shivakimothi-design` `@nikhilkajaria`) — shared engineering
**Status:** 🟡 G1/G2 agent exists (runs locally) · 🔴 post-prod agent not built · ⏸ auto-on-PR not armed

This folder holds the **plumbing that runs the gate rules** defined in
[`/evaluation/g1g2-logic/v1.md`](../g1g2-logic/v1.md). The rules are owned by Shiva; the
code that executes them is shared.

---

## What exists today

- A working **G1/G2 checker** lives in the repo (`layers/gate_checker/`, run via
  `scripts/run_gate_check.py`). It judges a single concept and returns PASS / ITERATE / KILL.
- It reads its context from the load-bearing `reference/context_layer.md`.
- **Post-prod is not built yet** (see below).

## The three agents (target state)

1. **G1 agent** — Category-Frame Integrity (layer-aware). Source: `g1g2-logic/v1.md` §Gate 1.
2. **G2 agent** — Contamination / Banned Words (layer-aware). Source: `g1g2-logic/v1.md` §Gate 2.
3. **Post-prod agent** — runs on the *finished* asset, not the concept text. **v1.0 below.**

> **Static vs video:** the v1.0 below is video-oriented. The **static** post-prod check —
> which puts a G1/G2 gate first, then Section-A disqualifiers, then a 6-dimension score — lives
> in [`/evaluation/post-prod/static-v1.md`](../post-prod/static-v1.md).

### Post-Production Check — v1.0 (video)

Runs on the rendered creative (video). Three lenses:

- **P1 — Multimodal re-run.** Re-run G1 + G2 on the finished asset across **all modalities**
  (visual + audio + on-screen captions). A concept can pass on paper but drift in the cut.
- **P2 — Craft hygiene** (each check traces to a field learning):
  - WiFi/net cue is the visually **dominant** element, not a decorative badge. *(Field Learning 1 & 2)*
  - **One** dominant cue, one message, one proof — no overload. *(Field Learning 10)*
  - Day-numbers shown **with the operating rule**, not as a bare menu/range. *(Field Learning 3 & 9)*
  - **No OTT / app-logo cluster** — show devices, not content brands. *(Field Learning 7)*
  - **Router is not the hero** visual. *(Field Learning 8)*
  - For L2 user-recognition assets: the on/off "zaroorat hai / zaroorat nahi" contrast reads
    at flash speed. *(L2 brief)*
- **P3 — Format hygiene** (ratios, durations, safe zones, caption rules):
  **⏸ depends on Nikhil's formats-spec** (`/wrapper/formats-spec/`, a 🔴 item). Documented
  placeholder until that lands — we don't fake it.

---

## How a concept is fed in

A "creative concept" is judged in the structured shape the engine expects (see
`tests/golden_concepts/concepts.json` for examples). Roughly:

```json
{
  "concept_id": "JUN-L1-001",
  "layer": "L1",
  "hook": "WiFi lene jaa rahe ho?",
  "body": "...",
  "close": "Recharge-wala ghar ka net. Jitne din recharge, utne din net.",
  "modality": "static | video | vox-pop"
}
```

The `layer` field is what selects the L1 / L2 / L3 strictness from `g1g2-logic/v1.md`.

---

## ❓ OPEN QUESTION FOR NIKHIL (decide in this PR)

**How do you want to run gate-checks?**

- **Option A — Auto-on-PR (recommended).** You open a PR with a concept; a GitHub Action
  runs the agents automatically, posts the verdict on the PR, and pings Shiva on a fail.
  You run nothing. Needs: (1) your finalised criteria — done, v1.1; (2) Shiva's
  `ANTHROPIC_API_KEY` added once as a GitHub **secret** by the repo admin; (3) arming the
  workflow template [`gate-check.workflow.yml`](gate-check.workflow.yml) — currently a
  switched-OFF template living here (not in `.github/workflows/`, so GitHub won't run it).
  Arming = copy it into `.github/workflows/gate-check.yml` and follow its header.
- **Option B — Local.** You run `python scripts/run_gate_check.py <concept>` on your own
  machine. Works today for G1/G2, but no auto-alert to Shiva.

Your answer decides whether we wire the GitHub Action or a local hook. Leave a comment on
the PR.

---

## Cost note

Each check is **one small Sonnet call ≈ a fraction of a cent**. At volume it draws on
Shiva's monthly API budget, so if auto-on-PR runs on every push, set a spend cap.
The key is stored as an encrypted GitHub secret — only the Action can read it.

## Escalation / "revert"

On a FAIL, CODEOWNERS already makes Shiva the required reviewer for `/evaluation/` and
`/messaging/`, so the PR **cannot merge** until she approves. "Revert" in practice =
request changes / block the PR (it bounces back to the maker). If something already merged
and is later found bad, a revert is a one-click "undo this change" PR.
