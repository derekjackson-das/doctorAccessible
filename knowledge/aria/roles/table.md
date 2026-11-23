# Role: table

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "table role", https://www.w3.org/TR/wai-aria-1.2/#table. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `table`, `tr`, `td`, and `th`, https://www.w3.org/TR/html-aria/#el-table
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.127, https://www.w3.org/TR/html-aam/#el-table
- Practice (tier 2): ARIA Authoring Practices Guide, "Table Pattern" and "Structural Roles" (no date on the pages), https://www.w3.org/WAI/ARIA/apg/patterns/table/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: table role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/table_role
- Related entries: `html/tables.md`, `aria/roles/row.md`, `aria/roles/rowgroup.md`, `aria/roles/cell.md`, `aria/roles/columnheader.md`, `aria/roles/rowheader.md`, `aria/roles/grid.md`, `aria/roles/presentation.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="table"` on a `table` is redundant and never a finding.

## What it is

Data in rows and columns that the user reads but does not operate. WAI-ARIA 1.2: "A section containing data arranged in rows and columns." A table whose cells take focus and answer arrow keys is a `grid` (`aria/roles/grid.md`).

## The native element

`table` (HTML-AAM 3.5.127). ARIA in HTML allows any role on `table` and marks `role="table"` "NOT RECOMMENDED".

## When writing the role is justified

- A table built from `div` and `span` elements that cannot be rebuilt (`aria/using-aria.md`, rule 1).
- A real `table` whose CSS `display` was changed, for example to `grid`, `flex`, or `block` for a small-screen layout. MDN reports that this removes the table's native semantics, and that the ARIA table roles put them back. Every part then needs its role, not only the `table`.

APG adds a caution: the role arrived in WAI-ARIA 1.1, so test with each browser and assistive technology the project names.

## What the spec asks of authors

- "If the tabular container maintains a selection state, provides its own two-dimensional navigation, or allows the user to rearrange or otherwise manipulate its contents or the display thereof, authors SHOULD use grid or treegrid instead."
- "Authors SHOULD prefer the use of the host language's semantics for table whenever possible, such as the <table> element in [HTML]."
- Naming: required ("Accessible Name Required: True"), from the author. MDN says a name is strongly recommended but not required by ARIA. WAI-ARIA 1.2 says otherwise, and it is tier 1: name it. APG: `aria-labelledby` pointing at a visible label, otherwise `aria-label`; `aria-describedby` for a caption that is a description.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: `row`, or `rowgroup` holding `row`.
- Required states and properties: none.
- Supported states and properties: `aria-colcount`, `aria-rowcount`. Needed only when some columns or rows are not in the page; the cells then take `aria-colindex` and `aria-rowindex` (APG, "Table Pattern").
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; **required**.

**The whole component.** A `table` owns `row` elements, directly or inside a `rowgroup`. Each row owns `cell`, `columnheader`, or `rowheader` elements. Built on `div` elements, every one of those roles has to be written; a `role="table"` on its own exposes nothing as a table. It has no keyboard behavior: widgets inside its cells are separate tab stops (APG).

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `table` (redundant, "NOT RECOMMENDED").
- **Allowed:** the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `ul`, `ol`, `dl`; `section`, `main`, `nav`, and the other landmark elements; `fieldset`; `button`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- Any other role on a `table` replaces the table, and its parts go with it. ARIA in HTML gives `td` and `th` no corresponding role when the ancestor `table` is not exposed as a `table`, `grid`, or `treegrid`. `role="presentation"` is the case seen most (`aria/roles/presentation.md`).
- `role="grid"` on a `table` turns its `td` cells into grid cells and promises the grid's keyboard (`aria/roles/grid.md`).

## How it fails in code

- Tabular data in `div` elements with no table roles at all: the rows, columns, and headers are shown only visually. `wcag/sc-1.3.1-info-and-relationships.md`, likely; the entry lists header cells not marked as such as definite (F91), and a person confirms the content is a data table.
- `role="table"` whose header cells are plain `cell` elements, or not marked: `wcag/sc-1.3.1-info-and-relationships.md`, definite per that entry (F91).
- `role="table"` with no `row` inside: `wcag/sc-1.3.1-info-and-relationships.md`, likely.
- `role="table"` with no accessible name: breaks the WAI-ARIA requirement. Advice; not a WCAG failure by itself.
- `role="table"` on a structure the user operates with arrow keys: advice; use `grid`.

## How to check

For each `role="table"`: it has a name, rows, and cells, and its headers are `columnheader` or `rowheader`. For each `table` whose CSS changes `display`: look at the accessibility tree at that viewport width. In the browser's accessibility tree, confirm the table, its row and column counts, and each cell's headers. axe: `aria-required-children` and `aria-required-parent` cover the parts (mapped to 1.3.1; `knowledge/axe-rules.md`). Observed with axe-core 4.14.0 on 2026-11-23: no rule fired on a `role="table"` with no name.
