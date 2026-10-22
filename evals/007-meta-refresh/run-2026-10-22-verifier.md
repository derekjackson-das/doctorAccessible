# Verifier run, 2026-10-22, eval 007

Blind run through the registered `verifier` agent (`verifier.md` at commit 6a54d17), given the file path, the index, the content standards, and the axe command, and told not to open `expected.md`, `RESULTS.md`, or any run file.

Result against `expected.md`: **pass**. One Definite finding, SC 2.2.1 Timing Adjustable (Level A), tier 1, sourced to the entry with F40 and F41 named, at `meta[http-equiv="refresh"]`, with removal in favor of the existing link as the fix direction. SC 3.2.5 and 2.2.4 set aside as Level AAA, not cited as failures. The "Continue" link, heading, contrast, and focus style were checked and declared passing. Nothing from the must-not list. axe inside the agent: one violation, `meta-refresh`. No file modified.

## Report as returned (findings and scan)

### [Definite] Timed redirect with no way to turn off, adjust, or extend it
- Where: `input.html` line 6, `meta[http-equiv="refresh"]`, content `20; url=/registration/step-2`
- What: The page sets a 20-second time limit after which it navigates to the next step on its own, and nothing on the page lets the user turn the limit off beforehand, lengthen it to at least ten times the default, or receive a warning and extend it; none of the exceptions apply to a registration confirmation.
- Criterion: WCAG 2.2 SC 2.2.1 Timing Adjustable (Level A), tier 1
- Source: knowledge/wcag/sc-2.2.1-timing-adjustable.md (lists this exact pattern as Definite, failures F40 and F41)
- Fix direction: Remove the `meta refresh` and let the existing "Continue to contact details" link be the way forward; if an automatic advance is wanted, it needs a visible control to turn it off or a warning with at least 20 seconds to extend it, repeatedly.

Related, not reported: SC 3.2.5 Change on Request and 2.2.4 Interruptions are Level AAA.

Checked and passing: `lang`, title matches `h1`, link text states its destination, contrast 17.40:1 and 7.14:1 with colors set together, focus outline declared, landmarks present.

Content: reading level about grade 2.0; heading describes the page; link text passes; first sentence carries the point. Manual review on whether the step vocabulary matches earlier steps not in the input.

Manual checks remaining: screen reader title and link list; focus outline in the project's browsers; if a timed advance is kept, test the warning and extension; confirm the destination exists and its title changes; 200% and 320px reflow.

Automated scan: axe-core 4.14.0, 1 violation, `meta-refresh`, at `meta[http-equiv="refresh"]`. Agrees with the reading.
