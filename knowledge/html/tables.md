# HTML: Tables

- Tier 1: HTML Living Standard, §4.9 Tabular data (§4.9.1 The table element, §4.9.2 The caption element, §4.9.10 The th element), accessed 2026-10-23. https://html.spec.whatwg.org/multipage/tables.html
- Tier 1: ARIA in HTML, W3C Recommendation 11 August 2026, rows for `table`, `caption`, `th`, `td`. https://www.w3.org/TR/html-aria/
- Tier 2: WAI Tutorials, "Tables Tutorial" (updated 16 February 2023), "Tables with one header" and "Caption & Summary" (both updated 27 July 2019). https://www.w3.org/WAI/tutorials/tables/
- Related: `patterns/` none; `aria/patterns/date-picker.md` (a table as a grid), `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-1.3.2-meaningful-sequence.md`, `wcag/sc-1.4.10-reflow.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

This entry says how to build it. Whether code fails WCAG is decided by the `wcag/` entries named below; report a failure once, under its criterion, at that entry's confidence.

## The native approach

- **A table is for data with a logical relationship in rows and columns** (WAI tutorial). Mark header cells with `th` and data cells with `td`.
- **Say which way headers point** with `scope="col"` or `scope="row"` when it is not obvious; for headers spanning groups, `scope="colgroup"` or `"rowgroup"`; for headers that cannot be tied in a straight line, `id` and `headers` (WAI tutorial).
- **A `caption` as the first child of the `table`**, a short heading for the table that most screen readers announce, and the main way to find a table in a screen reader's tables mode (WAI tutorial).
- **A summary only for complex tables**, inside the caption or linked with `aria-describedby`, not repeating the caption (WAI tutorial).

## Not for layout

The HTML Standard says tables must not be used as layout aids: it is non-conforming, tools extracting data get confusing results, and screen reader users are likely to find such pages very difficult to navigate. It points to CSS grid, flexbox, multi-column layout, and positioning instead (§4.9.1).

## What the native approach satisfies by default

Header and data cells, and the relationship between them, are exposed with no ARIA, so a screen reader reads each cell with its headers (`wcag/sc-1.3.1-info-and-relationships.md`).

## Where people go wrong

- A data table with no `th`, or headers styled with bold `td`: relationships not exposed (`wcag/sc-1.3.1-info-and-relationships.md`, eval 004).
- A `table` used to lay out a form or a page: non-conforming HTML, and the reading order follows rows, which may not be the visual order (`wcag/sc-1.3.2-meaningful-sequence.md`). If a layout table cannot be removed at once, `role="presentation"` on it stops it being exposed as a table (ARIA in HTML allows any role on `table`); the fix is CSS.
- A grid of `div`s styled as a table: no table semantics at all (`wcag/sc-1.3.1-info-and-relationships.md`).
- A wide table in a scrolling container that cannot be scrolled by keyboard. Reflow permits a data table to scroll in its own container (`wcag/sc-1.4.10-reflow.md`), but the container must still be operable by keyboard (`wcag/sc-2.1.1-keyboard.md`).

## When ARIA is genuinely needed

- `role="presentation"` on a layout table that cannot yet be replaced.
- `aria-describedby` for a summary.
- An interactive grid, where cells take focus and arrow keys move between them: `role="grid"`, as in `aria/patterns/date-picker.md`. A table that only shows data needs none of this.
