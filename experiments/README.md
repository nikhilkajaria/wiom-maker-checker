# Experiments mirror (versioned snapshot)

Diffable JSON mirror of the live Google Sheet **"June 1 - Performance Creative
Repository"** (ID `1ay8EBJ3fRjpx0U80ErEqMwJGXlY0ynh_FzTfGcTGXaA`).

The Sheet is the editing surface. These files are a generated, read-only audit
trail so creative concepts, experiments, and status changes become diffable in
git over time. This closes the gap that the operational registry (what we are
actually running) otherwise lives only in a mutable Sheet.

## Files
- `brief_registry.json`      - Tab 0: brief instances (agency x date)
- `creative_registry.json`   - Tab 1: one row per concept (the spine)
- `experiment_registry.json` - Tab 2: one row per test (T-NS-*, T-PR-*, T-SD-*, ...)
- `status_tracker.json`      - Tab 3: WIP + per-ratio asset file names / drive links
- `_snapshot_meta.json`      - source id, export timestamp, per-tab record counts

The Context & Legend tab (codes reference) is intentionally NOT mirrored - the
canonical code reference lives in `reference/` (`need_states.json`,
`audience_layers.json`, `memory_anchors.json`, ...).

## Do not hand-edit
Edit the Google Sheet, then regenerate:

1. Export the Sheet to xlsx (google-workspace MCP, or File > Download > Microsoft Excel).
2. `python scripts/export_registry_to_json.py "<path-to-export.xlsx>"`
3. Review `git diff experiments/` and commit.

## Caveat
This is a periodic snapshot, not a live sync - only as fresh as the last export.
Check `_snapshot_meta.json` -> `export_timestamp`.
