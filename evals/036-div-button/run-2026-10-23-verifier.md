# Run 2026-10-23: axe and verifier on eval 036

- axe: `@axe-core/cli`, axe-core 4.14.0, Node.js 24.22.1, Chrome for Testing 156.0.8078.47 (explicit `--chromedriver-path` and `--chrome-path`, see `evals/README.md`). Default and `--tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa`: **0 violations** in both, as the key expects.
- Verifier: `.claude/agents/verifier.md`, knowledge at commit 78efd19, run as a general-purpose agent carrying the verifier text (not the registered agent). Given the axe result; told not to open `expected.md`, run files, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- Result: **pass.** Graded against the key as amended after review at the next commit (both criteria to be named in one finding), which this run already met.

## Graded against `expected.md`

- Finding 1, definite, on `div.reserve` (line 25) and its handler, naming SC 2.1.1 Keyboard and SC 4.1.2 Name, Role, Value (both Level A), tier 1, in one finding (F42, F54), citing both entries and `html/buttons.md`: present.
- Fix: a native `button type="button"`. Acceptable.
- The status region was judged correct under 4.1.3; the clean axe run was not treated as a pass.
- Must not: nothing from the list.

Observations: contrast was not computed, and no claim was made about it. A content manual-review note that the script has no failure path.
