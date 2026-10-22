# Verifier run, 2026-10-22, eval 012

Blind run through the registered `verifier` agent (`verifier.md` at commit f93f693), dispatch omitting the axe command and the scratch directory.

Result against `expected.md`: **pass**. One Definite finding, SC 3.2.2 On Input (Level A), tier 1, at `select#dept` and its `onchange`, with G80 and G13 as fix directions. The agent read the instruction sentence, judged it a statement of purpose rather than a warning, reported Definite, and stated exactly what a reviewer would have to conclude for it to drop to Likely, listing that judgment under manual checks. It declined to report the same handler under 2.1.1, citing one finding per defect and noting the 2.1.1 entry does not list the pattern. Nothing from the must-not list. No file modified.

Rule check: tags flag unprompted; clean scan explicitly not treated as a pass, citing the 3.2.2 entry's note. Ratios computed and compared against opened entries (1.4.3, 1.4.11), stated as the agent's own computation. Reading-level coefficients flagged as from the agent's own knowledge rather than an entry, and the number marked weak evidence; honest, and a sign the rule is read strictly.

Report summary: finding as above; label visible and associated; title matches `h1`; `lang` declared. Manual checks: closed-select arrow behavior across browsers, Escape after arrowing in the open list, screen reader browse mode over the options, the advance-notice judgment, focus visibility, 400% reflow. axe: 0 violations, 11 passes, 0 incomplete.
