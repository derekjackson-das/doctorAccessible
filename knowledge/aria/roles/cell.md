# Role: cell

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "cell role", https://www.w3.org/TR/wai-aria-1.2/#cell. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `td` and `th`, https://www.w3.org/TR/html-aria/#el-td
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows 3.5.129 (`td`) and 3.5.134 (`th` that is not a header), https://www.w3.org/TR/html-aam/#el-td
- Practice (tier 2): ARIA Authoring Practices Guide, "Table Pattern" and "Structural Roles" (no date on the pages), https://www.w3.org/WAI/ARIA/apg/patterns/table/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: cell role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/cell_role
- Related entries: `aria/roles/table.md`, `aria/roles/row.md`, `aria/roles/columnheader.md`, `aria/roles/rowheader.md`, `aria/roles/gridcell.md`, `html/tables.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="cell"` on a `td` in a table is redundant and never a finding.

## What it is

A cell in a table that is not a header. WAI-ARIA 1.2: "A cell in a tabular container." In a `grid` or `treegrid` the cell is a `gridcell` instead (`aria/roles/gridcell.md`).

## The native element

A `td` whose `table` is exposed as a `table` (HTML-AAM 3.5.129). A `th` that is not a column or row header maps to `cell` too (HTML-AAM 3.5.134).

## When writing the role is justified

Only inside a `row` of an ARIA `table`: on `div` or `span` elements, or on a `td` whose table had its semantics removed by CSS `display` (`aria/roles/table.md`).

## What the spec asks of authors

- "Authors MUST ensure elements with role cell are contained in, or owned by, an element with the role row."
- Naming: allowed, from the content or the author; not required.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `row`.
- Required owned elements: none. Required states and properties: none.
- Supported states and properties: `aria-colindex`, `aria-colspan`, `aria-rowindex`, `aria-rowspan`. The index attributes are needed only when some columns or rows are not in the page; the span attributes do the work of `colspan` and `rowspan` where `td` is not used (APG, "Table Pattern").
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; not required.

**The whole component.** See `aria/roles/table.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `td` in a table exposed as a `table` (redundant, "NOT RECOMMENDED").
- **Allowed:** `th` in such a table (also "NOT RECOMMENDED"; see below), a `td` or `th` whose table is not exposed as a `table`, `grid`, or `treegrid`, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `td` or `th` in a `grid` or `treegrid` (they take `gridcell`); `li`; `h1` to `h6`; `button`; `a` with `href`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

`role="cell"` on a `th` that is a column or row header replaces the header role. The cell is then exposed as data, and the cells under or beside it lose their header. ARIA in HTML allows it; that does not make it safe.

## How it fails in code

- `role="cell"` on a header `th`, or header text in a `div role="cell"`: the header is not marked as one. `wcag/sc-1.3.1-info-and-relationships.md`, definite per that entry (F91).
- A `cell` outside a `row`: breaks the WAI-ARIA MUST. `wcag/sc-1.3.1-info-and-relationships.md`, likely.
- A cell that spans columns or rows with no `aria-colspan` or `aria-rowspan` on a `div` table: its headers may be worked out wrongly. `wcag/sc-1.3.1-info-and-relationships.md`, manual review in the accessibility tree.

## How to check

Every `role="cell"` is in a `row`, and no header carries it. In the browser's accessibility tree, pick a data cell and confirm its column and row headers. axe: `aria-required-parent` fires on a `cell` outside a `row` (mapped to 1.3.1; observed with axe-core 4.14.0 on 2026-11-23; `knowledge/axe-rules.md`).
