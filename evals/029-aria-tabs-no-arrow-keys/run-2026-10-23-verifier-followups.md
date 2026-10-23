# Run 2026-10-23: verifier on eval 029, after the follow-ups

- Why: `patterns/tabs.md` now points to `aria/patterns/tabs.md` for roles, names, and states instead of restating them (commit fda27db).
- axe: axe-core 4.14.0, Chrome for Testing 156.0.8078.47, WCAG 2.2-tagged: 0 violations, as the key expects.
- Verifier: general-purpose agent carrying `verifier.md`, given the axe result, answer key off limits. A prompt test, not a fresh-session load.
- Result: **pass.** One definite finding, SC 2.1.1 (Level A), tier 1, inactive tabs unreachable, citing the 2.1.1 entry's roving-tabindex case and `aria/patterns/tabs.md`. Selected-tab cue judged not color alone; contrast computed and passing; nothing from the must-not list. The run followed the new pointer from `patterns/tabs.md` to the aria entry.
