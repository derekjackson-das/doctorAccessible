# Eval results

One row per run. Newest first. A run is an axe pass, a verifier pass, or both, against one eval. Record what happened, not what should have happened.

| Date | Eval | Tool | Version | Result | Notes | By |
|---|---|---|---|---|---|---|
| 2026-10-22 | 001-missing-label | axe CLI | axe-core 4.14.0, Chrome for Testing 156.0.8078.47 | Pass: one violation, `label` on `#q`, impact critical, tags include `wcag412`; 21 rules passed, 0 incomplete | Matches `expected.md`. The `wcag412` tag matches the knowledge entry for SC 4.1.2. Nothing from the must-not list fired. | Derek Jackson with Claude Code |
