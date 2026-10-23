# Runs 2026-10-23: verifier on eval 031, after the follow-ups

- Why: `patterns/autocomplete.md` now points to `aria/patterns/autocomplete.md` for the APG roles, states, and keys (commit fda27db).
- axe, both runs: axe-core 4.14.0, Chrome for Testing 156.0.8078.47, WCAG 2.2-tagged: 0 violations, as the key expects.
- Verifier: general-purpose agent carrying `verifier.md`, given the axe result, answer key off limits. A prompt test, not a fresh-session load.

## Run 1, at fda27db: pass against the key, and a real second defect found

- Finding 1, SC 4.1.2 (Level A), tier 1, definite, the highlighted option never exposed: present.
- **A second definite finding, correct:** SC 2.5.2 Pointer Cancellation (Level A), F101. Options were chosen on `mousedown`, so a pointer user could not abort by moving off. The key did not list it, so the run did not break the must-not list, but the page was not the one-defect page the key claimed. The three earlier runs of 031 had missed it; this was the first to open the 2.5.2 entry.
- Fix at 051599b: `mousedown` now only calls `preventDefault` (to keep focus in the field), and choosing happens on `click`. The key now says 2.5.2 is met.

## Run 2, at 051599b: pass

- One definite finding, SC 4.1.2 (Level A), tier 1, citing the 4.1.2 entry and `aria/patterns/autocomplete.md`. No pointer finding; the result count left as a human judgment under 4.1.3; nothing from the must-not list.
