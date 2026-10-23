# Eval 037: a layout table that holds a form

Input: `input.html`. An "Ask a librarian" form laid out with a `table`.

Intended defect: the form is laid out in a `table` that holds no data. The table also carries a data table's structure: a `caption` ("Your question") and a header row of `th` cells ("Field", "Your answer"). Assistive technology announces a data table with headers that describe nothing, and reads each field's cell with a meaningless header.

Everything else is clean:
- Every field has a `label` tied to it with `for`.
- `autocomplete` tokens are set on name and email, and the right `input` types are used.
- The submit button is native and named, and the reading order (label, then field) matches the visual order.
- Focus is visible, and contrast is about 7.1:1 or better.
- Language, title, one `h1`, `main`.

## Expected findings

1. **[Definite]** A layout table carries data-table structure (`caption` and `th`).
   - Criterion: WCAG 2.2 SC 1.3.1 Info and Relationships (Level A), tier 1, from `knowledge/wcag/sc-1.3.1-info-and-relationships.md` ("A `table` used for layout that carries `th`, `caption`, or a summary. Definite. F46").
   - HTML entry: `knowledge/html/tables.md`. The HTML Standard (§4.9.1) says tables must not be used as layout aids; that part is advice cited from the HTML section, inside the same finding.
   - Where: `table.layout`, its `caption`, and its `th` cells.
   - Acceptable fix directions: drop the table and lay the form out with CSS grid or flexbox (`html/tables.md`, `html/forms.md`); at minimum, remove the `caption` and `th` and add `role="presentation"`. As a direction, not a patch.

## Also acceptable

- A note that the reading order is fine here (label then field), so SC 1.3.2 is met.
- A note, marked advice, that a `fieldset` and `legend` could group the fields if a group heading is wanted.
- Manual-review notes that a criterion appears met and needs a browser check.
- A note that axe may or may not flag the table, depending on its layout-table heuristics; the finding must come from reading.

## Must not

- Report the labels, the inputs, the button, `autocomplete`, or the reading order as failures.
- Report the HTML conformance problem as a second WCAG finding, separate from 1.3.1.
- Report contrast, focus style, headings, landmarks, or language as failures.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

Whether axe flags this depends on its table rules and how it classifies the table; nothing in the entries says it will. Observed 2026-10-23: axe-core 4.14.0 reported 0 violations, default and WCAG 2.2-tagged. A clean axe run does not clear the defect. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as definite under SC 1.3.1 (Level A), tier 1, and nothing from the Must not list appears.
