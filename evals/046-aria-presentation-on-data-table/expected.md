# Eval 046: a data table marked role="presentation"

Input: `input.html`. A library "Opening hours" page with a real data table: a caption, column headers, and row headers.

Intended defect: the `table` has `role="presentation"`. Under WAI-ARIA 1.2 that removes the table role and, because rows and cells are its required owned elements, the roles of `thead`, `tbody`, `tr`, `th`, `td`, and the `caption` too. The headers and the row and column relationships the table shows visually are no longer exposed.

Everything else is clean:
- `header`, `nav` named "Site" (with `aria-current="page"` on the current link), `main`, and `footer`, all at the top level.
- One `h1`, a `title`, `lang`, visible focus, link text that says where it goes.
- Text and borders are #1a1a1a and #767676 on white or #f2f2f2: well over 4.5:1 for text, at least 3:1 for borders. Links are #0b4f9c.

## Expected findings

1. **[Definite]** The data table's structure is removed by `role="presentation"`.
   - Criterion: WCAG 2.2 SC 1.3.1 Info and Relationships (Level A), tier 1, from `knowledge/wcag/sc-1.3.1-info-and-relationships.md` ("`role="presentation"` or `role="none"` on an element that carries meaning, such as a data table. Definite. F92").
   - Role entry: `knowledge/aria/roles/presentation.md`, which explains that the rows, cells, headers, and caption lose their roles too.
   - Where: `table[role="presentation"]`.
   - Acceptable fix directions: remove the role. As a direction, not a patch.

## Also acceptable

- Naming `knowledge/html/tables.md` for how the table should be built.
- A note that the caption, `scope` attributes, and `th` elements are otherwise correct.
- A note that axe may report this under a table or ARIA rule, or not at all, with the rule named.
- Manual-review notes that a criterion appears met and needs a browser check.

## Must not

- Report the defect more than once: under 1.3.1 and again under 4.1.2, or once for the table and again for each header or the caption.
- Call `role="presentation"` the same as `aria-hidden="true"`, or say the table's text is hidden.
- Report the landmarks, the `nav` name, `aria-current`, headings, contrast, focus, or language as failures.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Say what a screen reader user would hear or experience.
- Rewrite the page.

## Automated scan

axe-core 4.14 may or may not flag a data table with `role="presentation"`; whether it did is recorded in `RESULTS.md`. The finding does not depend on it.

## Pass condition

Finding 1 is present as definite under SC 1.3.1 (Level A), tier 1, once, and nothing from the Must not list appears.
