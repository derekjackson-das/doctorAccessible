# Verifier runs, 2026-10-22, eval 008, tightened prompt

Two blind runs through the registered `verifier` agent, dispatch omitting the axe command and the scratch directory.

## Run 1, verifier.md at commit 0cb0488: pass on the key, partial on the numbers rule

One Definite finding, SC 2.3.1 Three Flashes or Below Threshold (Level A), tier 1, at `.alert` and `@keyframes flash`, with G19 as the fix; 2.2.2 correctly ruled out at four seconds; tags flag used unprompted. Nothing from the must-not list.

But the report stated a pixel-area figure for the general flash threshold and credited it to the Understanding document. The agent's transcript shows it never opened that document; the figure was from memory, labeled with a source the agent believed it came from. The new rule said a remembered figure not in an entry is left out or marked unverified, and the agent did neither. Better than the earlier run, which credited the entry itself, and still not right. One sentence was added to the rule: a figure from any document you did not open in this run is from memory, whatever document you believe it came from; naming that document does not make it a citation.

## Run 2, verifier.md at commit f93f693: pass, numbers rule held

One Definite finding, same criterion, same location, same fix. The report says: "The entry does not state the numeric area or luminance thresholds, so none are stated here beyond the observation that a large element alternating light and dark qualifies in the entry's own words." Every number given is marked as computed from the code: cycle duration, flashes per second, total run, relative luminance of the two colors by the Recommendation's formula, element dimensions from the CSS. SC 2.2.2 ruled out with the computation shown (0.2 s times 20 is 4.0 s). SC 1.4.3 checked with the entry's thresholds named and the ratios computed. A manual-review note on `role="alert"` applied to static content, explicitly marked as not a WCAG failure from code. No "would announce" language. Scratch files in a temp directory. Nothing from the must-not list. No file modified.

axe, both runs: 0 violations, 0 incomplete, with the tags flag. The report states the clean run is not a pass because the 2.3.1 entry says axe has no rule for flash rate.
