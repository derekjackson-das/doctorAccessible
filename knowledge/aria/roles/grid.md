# Role: grid

- Category: widget (composite).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "grid role", https://www.w3.org/TR/wai-aria-1.2/#grid. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `table` (any role allowed), `tr`, `td`, and `th`, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `td` when its table has the grid role (3.5.130), https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Grid (Interactive Tabular Data and Layout Containers) Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/grid/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: grid role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/grid_role
- Related entries: `aria/roles/gridcell.md`, `aria/roles/treegrid.md`, `html/tables.md`, `aria/patterns/date-picker.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

An interactive table, or a two-dimensional layout of widgets, that the user moves through cell by cell with the arrow keys. WAI-ARIA 1.2: "A composite widget containing a collection of one or more rows with one or more cells where some or all cells in the grid are focusable by using methods of two-dimensional navigation, such as directional arrow keys."

## The native element

None. A `table` is a static table; adding `role="grid"` to it makes it interactive and the arrow keys must then be scripted. MDN: a plain HTML table is enough for many cases.

## When writing the role is justified

When cells are interactive and arrow-key movement is the point: a calendar (`aria/patterns/date-picker.md`), a spreadsheet, a list of items each with several actions. MDN warns users may not know to use the arrows; confirm a grid is the right choice.

## What the spec asks of authors

- "Authors MAY designate a cell as a row or column header by using either the rowheader or columnheader role in lieu of the gridcell role."
- "Authors MUST ensure elements with role gridcell, columnheader, or rowheader are owned by elements with role row, which are in turn owned by an element with role rowgroup, or grid."
- "To be keyboard accessible, authors SHOULD manage focus of descendants of a grid as described in Managing Focus."
- "When a user is navigating the grid content with a keyboard, authors SHOULD set focus as follows: If a gridcell contains a single interactive widget that will not consume arrow key presses when it receives focus, such as a checkbox, button, or link, authors MAY set focus on the interactive element contained in that cell."
- "Otherwise, authors SHOULD ensure the element that receives focus is a gridcell, rowheader, or columnheader element."
- "Authors SHOULD provide a mechanism for changing to an interaction or edit mode that allows users to navigate and interact with content contained inside a focusable cell if that focusable cell contains any of the following: [a list in the spec: a widget that needs the arrow keys, several interactive elements, or editable content]"
- "Authors MAY use a gridcell to display the result of a formula, which could be editable by the user."
- "An author MAY override the propagated value of aria-readonly for an individual gridcell element."
- "In a grid that provides cell content editing functions, if the content of a focusable gridcell element is not editable, authors MAY set aria-readonly to true on the gridcell element."
- "Authors MAY indicate that a focusable gridcell is selectable as the object of an action with the aria-selected attribute."
- "If the grid allows multiple gridcells to be selected, the author SHOULD set aria-multiselectable to true on the element with role grid."
- "When the author is reusing a native host language table element and needs a gridcell element to span multiple rows or columns, the author SHOULD apply the appropriate host language attributes instead of WAI-ARIA aria-rowspan or aria-colspan properties."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: `row`, `rowgroup → row`.
- Required states and properties: none.
- Supported states and properties: `aria-multiselectable`, `aria-readonly`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-haspopup`, `aria-invalid` as deprecated on this role.
- Naming: name from author; **required**.
- `aria-readonly`, `aria-multiselectable`, `aria-rowcount` and `aria-colcount` when not all rows or columns are in the page (APG).

**The whole component.** It must own `row` elements (directly or through `rowgroup`), which own `gridcell`, `columnheader`, or `rowheader` cells (WAI-ARIA 1.2 MUST). On an HTML `table` with `role="grid"` the rows and cells are implied. It needs a name and the keyboard below.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `table` and the elements that allow any role, such as `div`, `span`, `p`, and `table`. Inside it, `tr` takes `row` and `td` takes `gridcell` implicitly.
- **Not allowed:** `ul`, `ol`, `li`, headings, landmark elements, form fields, `button`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Grid Pattern (data grid): the arrows move one cell; Page Up and Page Down move several rows; Home and End go to the first and last cell in the row; Control+Home and Control+End to the first and last cell in the grid. Selection keys are common but optional. One tab stop for the grid. A cell holding a widget that needs the arrows (a combobox, a text field) needs Enter or F2 to go in and Escape to come out. Layout grids may wrap at row ends; data grids should not.

## What an explicit role takes away

- On a `table`, the table role becomes grid: the screen reader's table reading commands give way to the author's arrow keys, and only focusable content may be heard in some modes (MDN). A data table that is not interactive should stay a table.

## How it fails in code

- `role="grid"` on a static data table with no arrow keys: cells cannot be reached in focus mode. `wcag/sc-2.1.1-keyboard.md`, likely; and advice to remove the role.
- No arrow keys and cells out of the tab order: `wcag/sc-2.1.1-keyboard.md`, definite per that entry.
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- Rows and cells with no `row` and `gridcell` structure: `wcag/sc-1.3.1-info-and-relationships.md`, at that entry's confidence.

## How to check

Is it interactive? If not, remove the role. If so: one tab stop, the arrows move between cells, it has a name, and the structure is row and cell. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
