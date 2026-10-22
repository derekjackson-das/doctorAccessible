# Eval results

One row per run. Newest first. A run is an axe pass, a verifier pass, or both, against one eval. Record what happened, not what should have happened.

| Date | Eval | Tool | Version | Result | Notes | By |
|---|---|---|---|---|---|---|
| 2026-10-22 | 001-missing-label | verifier, blind | verifier.md at commit a6e1767, run as a general-purpose agent with the file body as instructions (project agent not registered mid-session) | Pass: one definite finding, SC 4.1.2 (Level A), tier 1, sourced to the entry, at `#q`; 1.3.1 and 3.3.2 cross-referenced as no entry yet; shared word "Search" raised as manual review; nothing from the must-not list | Full report in `001-missing-label/run-2026-10-22-verifier.md`. Observation: a contrast threshold was stated from memory in a pass observation; consider tightening the rule. | Derek Jackson with Claude Code |
| 2026-10-22 | 001-missing-label | axe CLI | axe-core 4.14.0, Chrome for Testing 156.0.8078.47 | Pass: one violation, `label` on `#q`, impact critical, tags include `wcag412`; 21 rules passed, 0 incomplete | Matches `expected.md`. The `wcag412` tag matches the knowledge entry for SC 4.1.2. Nothing from the must-not list fired. | Derek Jackson with Claude Code |
