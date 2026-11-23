# Role: row

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "row role", https://www.w3.org/TR/wai-aria-1.2/#row. ARIA in HTML, W3C Recommendation 11 August 2026, row for `tr`, https://www.w3.org/TR/html-aria/#el-tr
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.141, https://www.w3.org/TR/html-aam/#el-tr
- Practice (tier 2): ARIA Authoring Practices Guide, "Table Pattern" and "Structural Roles" (no date on the pages), https://www.w3.org/WAI/ARIA/apg/patterns/table/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: row role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/row_role
- Related entries: `aria/roles/table.md`, `aria/roles/rowgroup.md`, `aria/roles/cell.md`, `aria/roles/grid.md`, `aria/roles/treegrid.md`, `html/tables.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="row"` on a `tr` is redundant and never a finding.

## What it is

One row of cells in a table, grid, or treegrid. WAI-ARIA 1.2: "A row of cells in a tabular container."

## The native element

`tr` (HTML-AAM 3.5.141). ARIA in HTML marks `role="row"` on it "NOT RECOMMENDED".

## When writing the role is justified

Only as part of an ARIA `table`, `grid`, or `treegrid`: on `div` elements, or on a `tr` whose table had its semantics removed by CSS `display` (`aria/roles/table.md`).

## What the spec asks of authors

- "Authors MUST ensure elements with role row are contained in, or owned by, an element with the role table, grid, rowgroup, or treegrid."
- "authors MUST NOT apply aria-expanded, aria-posinset, aria-setsize, and aria-level to a row that descends from a table or grid". They belong to rows in a `treegrid` only (`aria/roles/treegrid.md`).
- A note in the role says the working group plans to prohibit `aria-disabled` on a row outside a `grid` or `treegrid` in a later version.
- Naming: allowed, from the content or the author; not required.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `table`, `grid`, `treegrid`, or `rowgroup`.
- Required owned elements: `cell`, `columnheader`, `gridcell`, or `rowheader`.
- Required states and properties: none.
- Supported states and properties: `aria-colindex`, `aria-rowindex`, `aria-selected`, and, in a `treegrid` only, `aria-expanded`, `aria-level`, `aria-posinset`, `aria-setsize`. It also inherits `aria-activedescendant`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; not required.
- `aria-rowindex` is needed only when some rows are not in the page. `aria-selected` is for rows in a `grid` or `treegrid`; MDN notes it has no meaning in a `table`.

**The whole component.** See `aria/roles/table.md`, or `aria/roles/grid.md` for the interactive kind.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `tr` (redundant, "NOT RECOMMENDED"). Inside a `table` exposed as a `table`, `grid`, or `treegrid`, a `tr` allows no other role.
- **Allowed:** a `tr` whose table is not exposed as one of those, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `li`, `ul`, `ol`; `section` and the other landmark elements; `td` and `th` inside a table; `button`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

A different role on a `tr` inside a real table is not allowed. Where a browser honors it, the cells in that row have no row to belong to, and their headers can no longer be worked out.

## How it fails in code

- A `row` outside a `table`, `grid`, `treegrid`, or `rowgroup`: breaks the WAI-ARIA MUST, and the cells are not part of any table. `wcag/sc-1.3.1-info-and-relationships.md`, likely.
- A `row` with no cells of the required roles: `wcag/sc-1.3.1-info-and-relationships.md`, likely.
- `aria-expanded`, `aria-level`, `aria-posinset`, or `aria-setsize` on a row in a `table` or `grid`: breaks the WAI-ARIA MUST NOT. Advice; then check whether the row really does expand, in which case the component is a `treegrid`.

## How to check

Every `role="row"` sits in one of its four context roles and holds cells. In the browser's accessibility tree, confirm each row is under the table and its cells are under it. axe: `aria-required-parent` fires on a `row` outside its context, and `aria-required-children` covers its cells (mapped to 1.3.1; `aria-required-parent` observed with axe-core 4.14.0 on 2026-11-23; `knowledge/axe-rules.md`).
