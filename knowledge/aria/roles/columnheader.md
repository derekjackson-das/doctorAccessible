# Role: columnheader

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "columnheader role", https://www.w3.org/TR/wai-aria-1.2/#columnheader. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `th` and `td`, https://www.w3.org/TR/html-aria/#el-th
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.136, https://www.w3.org/TR/html-aam/#el-th-columnheader
- Practice (tier 2): ARIA Authoring Practices Guide, "Table Pattern" and "Structural Roles" (no date on the pages), https://www.w3.org/WAI/ARIA/apg/patterns/table/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: columnheader role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/columnheader_role
- Related entries: `aria/roles/table.md`, `aria/roles/row.md`, `aria/roles/rowheader.md`, `aria/roles/cell.md`, `aria/roles/grid.md`, `html/tables.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="columnheader"` on a `th` that heads a column is redundant and never a finding.

## What it is

The header cell for a column. WAI-ARIA 1.2: "A cell containing header information for a column." The spec calls it "the structural equivalent to an HTML th element with a column scope."

## The native element

A `th` that is a column header or column group header (HTML-AAM 3.5.136). `scope="col"` makes that explicit (`html/tables.md`).

## When writing the role is justified

Only inside a `row` of an ARIA `table`, `grid`, or `treegrid`: on `div` or `span` elements, or on a `th` whose table had its semantics removed by CSS `display` (`aria/roles/table.md`).

## What the spec asks of authors

- "Authors MUST ensure elements with role columnheader are contained in, or owned by, an element with the role row."
- "authors SHOULD NOT use aria-required or aria-readonly in a columnheader that descends from a table". They apply in a `grid` only.
- Setting `aria-selected` on the header does not select the column's cells: "An author MAY choose to propagate selection in this manner depending on the specific application."
- A note in the role says the working group plans to prohibit `aria-disabled` on a column header outside a `grid` or `treegrid` in a later version.
- Naming: required ("Accessible Name Required: True"), from the content or the author. The header's text is its name; an empty header has none.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `row`.
- Required owned elements: none. Required states and properties: none.
- Supported states and properties: `aria-sort`, plus those it inherits from `cell` and `gridcell`: `aria-colindex`, `aria-colspan`, `aria-rowindex`, `aria-rowspan`, `aria-expanded`, `aria-readonly`, `aria-required`, `aria-selected`.
- Prohibited states and properties: none. No global attribute is marked deprecated on this role.
- Naming: name from contents or author; **required**.
- `aria-sort` goes on the header cell of the sorted column, not on the table (APG, "Table Pattern"). MDN: on one header at a time, and it can be set on a native `th` with no role written.

**The whole component.** See `aria/roles/table.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `th` in a table, grid, or treegrid (redundant, "NOT RECOMMENDED").
- **Allowed:** a `th` or `td` whose table is not exposed as a `table`, `grid`, or `treegrid`, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** a `td` inside a table exposed as a `table`, `grid`, or `treegrid` (it takes `cell` or `gridcell` only; use a `th`); `li`; `h1` to `h6`; `button`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

On a `th`, any other role removes the header. A sortable header is the usual case: `role="button"` on the `th` is not allowed and, where honored, leaves the column with no header. Put a `button` inside the `th` and keep `aria-sort` on the `th`.

## How it fails in code

- Header cells in an ARIA table marked `cell`, or not marked: `wcag/sc-1.3.1-info-and-relationships.md`, definite per that entry (F91).
- A `columnheader` outside a `row`: breaks the WAI-ARIA MUST. `wcag/sc-1.3.1-info-and-relationships.md`, likely.
- A sorted column whose order is shown only by an icon, with no `aria-sort`: the state is not exposed. `wcag/sc-1.3.1-info-and-relationships.md`, likely; the entry does not list this case.
- An empty `columnheader`: breaks the naming requirement. Advice (axe `empty-table-header`, best practice), unless the column's meaning is then unavailable, which is the F91 case above.

## How to check

Every `role="columnheader"` is in a `row`, has text, and sits at the top of the cells it describes. Sort the table and watch `aria-sort` change. In the browser's accessibility tree, pick a data cell and confirm this header is listed for it. axe: `aria-required-parent` fires on a `columnheader` outside a `row` (mapped to 1.3.1; observed with axe-core 4.14.0 on 2026-11-23; `knowledge/axe-rules.md`).
