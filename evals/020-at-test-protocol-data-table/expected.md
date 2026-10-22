# Eval 020: test script for a data table

Input: `request.md`. A developer describes a course schedule table with row and column headers, links, full courses marked by a red row background (the Seats left cell also shows "0"), and a scrolling container on narrow screens, and asks for a test script. The spec names JAWS with Chrome, VoiceOver on iOS, keyboard only, 400% zoom, and Windows Contrast Themes.

Intended outcome: a numbered script grouped by the spec's modes, built from `knowledge/testing/`, with the gaps stated honestly. There is no pattern entry for data tables and no JAWS-specific testing entry, and the script must say so rather than invent commands.

## Expected

1. **Uses the spec's list.** Sections for JAWS with Chrome, VoiceOver on iOS, keyboard only, 400% zoom, and forced colors (Contrast Themes). No sections for modes not on the list.
2. **States the gaps.**
   - No `patterns/` entry for data tables: says so and builds from the testing entries.
   - No JAWS testing entry: uses `testing/screen-reader-windows.md` as the model, says the JAWS commands are not from an entry, and marks those steps unverified. It does not present JAWS keystrokes as verified.
3. **Screen reader steps check the table's structure:** the caption is read; moving cell by cell reads the row header (course) and column header with each cell; the course links are reachable and read their text (`wcag/sc-1.3.1-info-and-relationships.md`). For VoiceOver on iOS: the rotor's Tables setting, and swiping through cells (`testing/screen-reader-apple.md`).
4. **The "full" state is tested** in more than one mode: a screen reader check that 0 seats is conveyed by the cell text; a forced-colors check that notes whether the red background remains and whether anything else marks a full course. Tied to `wcag/sc-1.4.1-use-of-color.md`. Because the "0" is shown as text, 1.4.1 may well pass; the script checks rather than asserts a failure. A note for the developer outside the script is acceptable, without fixing anything.
5. **Keyboard:** Tab reaches the scrolling container, with focus visible, and arrow keys scroll it; Tab reaches each course link (`wcag/sc-2.1.1-keyboard.md`, `sc-2.4.7-focus-visible.md`).
6. **Zoom at 400% / 320 CSS pixels:** the table may scroll sideways inside its container as an exception for tabular data, and the rest of the page reflows; header and caption stay readable (`wcag/sc-1.4.10-reflow.md`, `testing/zoom.md`).
7. **Forced colors setup** from `testing/forced-colors.md`: a dark and a light theme; focus on the container and links visible; with the status that forced-colors-only problems are manual review unless they fail a criterion another way.
8. **What to record** per the testing entries, including versions and the tester.
9. **Never speaks as a user** and never predicts announcements.

## Also acceptable

- A step to check whether the container's `aria-label` is read when the container receives focus.
- Proposing to add the script to "Open manual tests".

## Must not

- Write or change code.
- Present JAWS commands as verified when no entry supplies them.
- Predict what a screen reader will say, or describe what a user would experience.
- Treat the horizontal scroll of the table at 400% as a failure on its own.
- Assert that the red-background state fails SC 1.4.1 without checking the cell text.
- Call a forced-colors-only issue a WCAG failure without tying it to a criterion.

## Pass condition

Items 1 to 6, 8, and 9 are present, and nothing from the Must not list appears.
