# Role: rowgroup

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "rowgroup role", https://www.w3.org/TR/wai-aria-1.2/#rowgroup. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `tbody`, `thead`, and `tfoot`, https://www.w3.org/TR/html-aria/#el-tbody
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows 3.5.128 (`tbody`), 3.5.138 (`thead`), 3.5.133 (`tfoot`), https://www.w3.org/TR/html-aam/#el-tbody
- Practice (tier 2): ARIA Authoring Practices Guide, "Table Pattern" and "Structural Roles" (no date on the pages), https://www.w3.org/WAI/ARIA/apg/patterns/table/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: rowgroup role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/rowgroup_role
- Related entries: `aria/roles/table.md`, `aria/roles/row.md`, `aria/roles/grid.md`, `aria/roles/presentation.md`, `html/tables.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="rowgroup"` on a `thead`, `tbody`, or `tfoot` is redundant and never a finding. Leaving the role out of an ARIA table is not a finding either: it is optional.

## What it is

A group of rows inside a table, grid, or treegrid. WAI-ARIA 1.2: "A structure containing one or more row elements in a tabular container." A note in the role says it does not tell a header group from a body group.

## The native element

`thead`, `tbody`, and `tfoot` (HTML-AAM 3.5.138, 3.5.128, 3.5.133). ARIA in HTML allows any role on them and marks `rowgroup` "NOT RECOMMENDED".

## When writing the role is justified

Only inside an ARIA `table`, `grid`, or `treegrid`, where the rows are wrapped in a container: on a `div`, or on a `thead`, `tbody`, or `tfoot` whose table had its semantics removed by CSS `display` (`aria/roles/table.md`).

## What the spec asks of authors

- "Authors MUST ensure elements with role rowgroup are contained in, or owned by, an element with the role grid, table, or treegrid."
- Naming: allowed, from the author; not required.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `table`, `grid`, or `treegrid`. MDN's description names only `table` and `grid`; WAI-ARIA 1.2 lists all three.
- Required owned elements: `row`.
- Required states and properties: none. Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.

**The whole component.** See `aria/roles/table.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `thead`, `tbody`, `tfoot` (redundant, "NOT RECOMMENDED").
- **Allowed:** the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** a `tr` inside a table exposed as a `table`, `grid`, or `treegrid`; `ul`, `ol`, `li`; `section` and the other landmark elements; `fieldset`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

ARIA in HTML allows any role on `thead`, `tbody`, and `tfoot`. A role there other than `rowgroup`, `none`, or `presentation` puts something that is not a row group between the table and its rows. ARIA in HTML allows it; check what the accessibility tree shows for the rows.

## How it fails in code

- A `rowgroup` outside a `table`, `grid`, or `treegrid`: breaks the WAI-ARIA MUST. `wcag/sc-1.3.1-info-and-relationships.md`, likely.
- A `rowgroup` with no `row` inside: `wcag/sc-1.3.1-info-and-relationships.md`, likely.

## How to check

Every `role="rowgroup"` sits in a `table`, `grid`, or `treegrid` and holds rows. In the browser's accessibility tree, confirm the rows are counted under the table. axe: `aria-required-parent` and `aria-required-children` both fire on a `rowgroup` with no table around it and no rows in it (mapped to 1.3.1; observed with axe-core 4.14.0 on 2026-11-23; `knowledge/axe-rules.md`).
