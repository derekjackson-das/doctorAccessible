# Run 2026-10-23: axe and verifier on eval 037

- axe: `@axe-core/cli`, axe-core 4.14.0, Node.js 24.22.1, Chrome for Testing 156.0.8078.47. Default and `--tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa`: **0 violations** in both. The key says axe may or may not flag it; it did not.
- Verifier: `.claude/agents/verifier.md`, knowledge at commit 78efd19, run as a general-purpose agent carrying the verifier text (not the registered agent). Given the axe result; told not to open `expected.md`, run files, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- Result: **pass.** The key's must-not and also-acceptable lists were widened slightly after review (no second finding under 2.4.6 or 1.3.2; a reflow manual-review note allowed); this run did neither.

## Graded against `expected.md`

- Finding 1, SC 1.3.1 Info and Relationships (Level A), tier 1, definite, F46, on `table.layout`, its `caption` and `th` row, citing the 1.3.1 entry and `html/tables.md` (HTML Standard §4.9.1 as support): present.
- Fix: CSS grid or flexbox; at minimum remove `caption` and `th` and add `role="presentation"`. Acceptable.
- Labels, `autocomplete`, button, reading order (1.3.2 met), and contrast (computed: #4a4a4a about 8.9:1, #005a9c about 7.1:1) checked and not reported.
- Must not: nothing from the list.
