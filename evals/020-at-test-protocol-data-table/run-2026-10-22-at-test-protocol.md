# AT test protocol run, 2026-10-22, eval 020

Method: as for eval 019. The skill was at commit de80924, run by a general-purpose agent with the answer key off limits and no writes.

Result against `expected.md`: **pass**.

- **Modes:** sections for exactly the spec's five: JAWS with Chrome, VoiceOver on iOS, keyboard only, 400% zoom, and Contrast Themes.
- **Gaps stated:**
  - "no pattern entry" for data tables.
  - JAWS marked UNVERIFIED with the NVDA entry as the model. No JAWS keystrokes were given; the tester is told to take them from current JAWS documentation.
  - The scroll container's label has no entry, so it is manual review.
- **Table structure on both screen readers:** the caption is read; row and column headers are read with each cell; links make sense with their cell context. On iOS this uses the rotor's Tables setting.
- **The "full" rows:** checked by what is read in the Seats left cell and by what remains in forced colors. The script does not assert a 1.4.1 failure; the developer note says the "0" text is probably a sufficient cue unless the red means more.
- **Keyboard:** wide and narrow passes; the container is reachable with visible focus; arrows and Space scroll it; the run checks that focus can leave the table and is never hidden.
- **Zoom at 400%:** the table's own sideways scroll is recorded as the data-table exception; individual cells are still checked.
- **Forced colors:** a dark and a light theme, with the entry's status that forced-colors-only problems are manual review unless they fail a criterion another way.
- **Recording:** fields per mode.
- **Principle 7:** no predictions in the script.

Nothing from the Must not list.
