# SC 1.3.1 Info and Relationships

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 1 Perceivable / 1.3 Adaptable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#info-and-relationships
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Information, structure, and relationships conveyed through presentation can be programmatically determined or are available in text.

## What it requires, in our words

Whatever the visual design tells a sighted reader about structure must also be in the code. If something looks like a heading, it is marked up as a heading. If cells line up as a table, they are a real table with header cells. If a label sits beside a field, the two are connected. If a group of radio buttons shares a question, the group and its question are marked up as one. If a word is bold because it is important, the markup says so or the text does. Assistive technology reads the code, not the layout, so the code must carry the same information. This is the single most frequently cited criterion in audits, because it covers headings, lists, tables, and forms all at once.

## How it fails in code

- Text styled to look like a heading (bold, larger) without a heading element or heading role. Definite. F2.
- Data in a table without any `th` header cells, or header cells not marked as such. Definite. F91.
- A `table` used for layout that carries `th`, `caption`, or a summary. Definite. F46.
- A form control with visible label text that is not associated with it. Definite. Shared with SC 4.1.2; see that entry for how to report once. F111.
- A group of related controls, such as radio buttons under one question, with no `fieldset` and `legend` or equivalent grouping. Likely; definite when the question is not otherwise associated.
- A list presented visually as a list but made of `div` or `br` elements, or list items outside a list element. Definite.
- `role="presentation"` or `role="none"` on an element that carries meaning, such as a data table. Definite. F92.
- `headers` attributes pointing at cells that are not headers, or at ids that do not exist. Definite. F90.
- Whitespace characters used to fake columns or tables in plain text. Definite. F33, F34.
- Tabular data in a `pre` element. Definite. F48.

## How to meet it

- Native HTML first. Technique H42, "Using h1-h6 to identify headings". Technique H48, "Using ol, ul and dl for lists or groups of links". Technique H51, "Using table markup to present tabular information", with H63, "Using the scope attribute to associate header cells with data cells", and H39 for captions. Technique H44, "Using label elements to associate text labels with form controls". Technique H71, "Providing a description for groups of form controls using fieldset and legend elements". Technique H101, "Using semantic HTML elements to identify regions of a page". Technique H97, "Grouping related links using the nav element".
- Technique G115, "Using semantic elements to mark up structure", together with H49, "Using semantic markup to mark emphasized or special text".
- Technique G117, "Using text to convey information that is conveyed by variations in presentation of text", when markup cannot carry it.
- ARIA only when no native element does the job: ARIA11 and ARIA13 for landmarks and their names, ARIA12 for heading roles, ARIA17 for grouping form controls, ARIA16 for naming controls, ARIA24 for font icons, ARIA26 for `aria-current`.
- Technique H43, "Using id and headers attributes", for complex tables where `scope` is not enough.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`). An unassociated label fails both; report one finding and name both.
- SC 1.3.2 Meaningful Sequence (entry in this package). Order, as distinct from structure.
- SC 2.4.6 Headings and Labels (no entry yet). Whether a heading is descriptive, as distinct from whether it is a heading.
- SC 1.4.1 Use of Color (entry in this package). Color conveying structure needs a text or markup equivalent too.

## Automated coverage (tier 3)

axe-core tags many rules to this criterion, including `list`, `listitem`, `definition-list`, `dlitem`, `td-headers-attr`, `th-has-data-cells`, `td-has-header`, `table-fake-caption`, `p-as-heading`, `aria-required-children`, `aria-required-parent`, and `aria-hidden-body`. axe catches malformed lists and tables and some fake headings. It cannot tell that a `div` grid is really a table, that a bold line is really a heading in context, or that radio buttons belong to one question. Those remain manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
