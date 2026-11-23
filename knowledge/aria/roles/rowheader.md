# Role: rowheader

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "rowheader role", https://www.w3.org/TR/wai-aria-1.2/#rowheader. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `th` and `td`, https://www.w3.org/TR/html-aria/#el-th
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.137, https://www.w3.org/TR/html-aam/#el-th-rowheader
- Practice (tier 2): ARIA Authoring Practices Guide, "Table Pattern" and "Structural Roles" (no date on the pages), https://www.w3.org/WAI/ARIA/apg/patterns/table/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: rowheader role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/rowheader_role
- Related entries: `aria/roles/table.md`, `aria/roles/row.md`, `aria/roles/columnheader.md`, `aria/roles/cell.md`, `aria/roles/treegrid.md`, `html/tables.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="rowheader"` on a `th` that heads a row is redundant and never a finding.

## What it is

The header cell for a row. WAI-ARIA 1.2: "A cell containing header information for a row."

## The native element

A `th` that is a row header or row group header (HTML-AAM 3.5.137). `scope="row"` makes that explicit (`html/tables.md`).

## When writing the role is justified

Only inside a `row` of an ARIA `table`, `grid`, or `treegrid`: on `div` or `span` elements, or on a `th` whose table had its semantics removed by CSS `display` (`aria/roles/table.md`).

## What the spec asks of authors

- "Authors MUST ensure elements with role rowheader are contained in, or owned by, an element with the role row."
- "authors SHOULD NOT use aria-expanded, aria-readonly, or aria-required in a rowheader that descends from a table". They apply in a `grid` or `treegrid` only.
- Setting `aria-selected` on the header does not select the row's cells: "An author MAY choose to propagate selection in this manner depending on the specific application."
- A note in the role says the working group plans to prohibit `aria-disabled` on a row header outside a `grid` or `treegrid` in a later version.
- Naming: required ("Accessible Name Required: True"), from the content or the author. The header's text is its name.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `row`.
- Required owned elements: none. Required states and properties: none.
- Supported states and properties: `aria-expanded`, `aria-sort`, plus those it inherits from `cell` and `gridcell`: `aria-colindex`, `aria-colspan`, `aria-rowindex`, `aria-rowspan`, `aria-readonly`, `aria-required`, `aria-selected`.
- Prohibited states and properties: none. No global attribute is marked deprecated on this role.
- Naming: name from contents or author; **required**.

**The whole component.** See `aria/roles/table.md`. MDN: a row should hold one row header.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `th` in a table, grid, or treegrid (redundant, "NOT RECOMMENDED").
- **Allowed:** a `th` or `td` whose table is not exposed as a `table`, `grid`, or `treegrid`, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** a `td` inside a table exposed as a `table`, `grid`, or `treegrid` (it takes `cell` or `gridcell` only; use a `th`); `li`; `h1` to `h6`; `button`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

On a `th`, any other role removes the header, and the cells in its row lose it.

## How it fails in code

- The first cell of each row names the row but is a `cell`, or a `td`: the header is not marked as one. `wcag/sc-1.3.1-info-and-relationships.md`, definite per that entry (F91) once a person confirms the cell is what identifies the row.
- A `rowheader` outside a `row`: breaks the WAI-ARIA MUST. `wcag/sc-1.3.1-info-and-relationships.md`, likely.
- `aria-expanded` on a row header in a plain `table`: breaks the WAI-ARIA SHOULD NOT. Advice; then check whether the row really does expand, in which case the component is a `treegrid`.

## How to check

Every `role="rowheader"` is in a `row` and has text. In the browser's accessibility tree, pick a data cell and confirm this header is listed for it. axe: `aria-required-parent` covers a `rowheader` outside a `row` (mapped to 1.3.1; `knowledge/axe-rules.md`).
