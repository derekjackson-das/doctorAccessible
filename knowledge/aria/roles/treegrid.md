# Role: treegrid

- Category: widget (composite).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "treegrid role", https://www.w3.org/TR/wai-aria-1.2/#treegrid. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `table` (any role allowed), `tr`, `td`, and `th`, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows for `td` and `th` when the table has the treegrid role, https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Treegrid Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/treegrid/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: treegrid role", last modified 30 September 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/treegrid_role
- Related entries: `aria/roles/grid.md`, `aria/roles/tree.md`, `aria/roles/gridcell.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A grid whose rows expand and collapse like a tree, such as an email thread list with replies under each message. WAI-ARIA 1.2: "A grid whose rows can be expanded and collapsed in the same manner as for a tree."

## The native element

None.

## When writing the role is justified

When rows have children that open and close and cells are interactive. Use `grid` when rows do not expand (MDN).

## What the spec asks of authors

- "An author MAY override the propagated value of aria-readonly for an individual gridcell element."
- "In a treegrid that provides content editing functions, if the content of a focusable gridcell element is not editable, authors MAY set aria-readonly to true on the gridcell element."
- "To be keyboard accessible, authors SHOULD manage focus of descendants for all instances of this role, as described in Managing Focus."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: `row`, `rowgroup → row`.
- Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-haspopup` as deprecated on this role.
- Naming: name from author; **required**.
- Parent rows have `aria-expanded` on the row or on one of its cells; other rows have none (APG).
- `aria-level`, `aria-setsize`, `aria-posinset` on rows; `aria-rowcount` and `aria-colcount` when not all are in the page.

**The whole component.** It must own `row` elements (directly or in `rowgroup`), which own `gridcell`, `columnheader`, or `rowheader` cells. APG: every row and cell is focusable or holds something focusable, because screen readers in application mode only hear what can take focus.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `table` and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `ul`, `ol`, `li`, headings, landmark elements, form fields, `button`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Treegrid Pattern: Right expands a collapsed row, or moves into the row's cells; Left collapses an expanded row, or moves from the first cell back to the row. Up and Down move by row or by cell; Home and End, Control+Home and Control+End, Page Up and Page Down as in a grid. Enter on the expandable cell toggles the row; elsewhere it performs the cell's action. Tab moves between focusable elements within the row, then out.

## What an explicit role takes away

- On a `table`, as for `grid`: table reading gives way to the author's keys.

## How it fails in code

- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- Parent rows without `aria-expanded`, or not updated: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry.
- Cells that cannot take focus, so their content is not heard: `wcag/sc-1.3.1-info-and-relationships.md`, likely.
- No arrow keys: `wcag/sc-2.1.1-keyboard.md`, definite per that entry if rows and cells are out of the tab order.

## How to check

One tab stop; arrows open, close, and move; parent rows expose `aria-expanded`. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
