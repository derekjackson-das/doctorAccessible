## Checked

- File: `/Users/derekjackson/Documents/CCode/doctorAccessible/evals/046-aria-presentation-on-data-table/input.html` (71 lines, one static page with inline CSS and no JavaScript).
- Method: read in full, scanned with `tools/axe.py` (axe-core 4.14.0, WCAG 2.2 tags), and measured with `tools/readability.py`.
- Spec: there is no `a11y-spec.md` beside the file, at the repo root, or in `docs/`, so this was checked against WCAG 2.2 AA alone.
- `expected.md`, `evals/RESULTS.md`, and run files were not opened.

## Findings

### [Definite] Data table carries `role="presentation"`, which removes its table, header, and caption semantics
- Where: `input.html` line 34, `<table role="presentation">` (selector `main > table`), covering lines 34 to 64.
- What: The table holds real data (libraries by day, with `th scope="col"`, `th scope="row"`, and a `caption`), but the presentation role strips the table's role and, by inheritance, the roles of its rows, header cells, data cells, and caption. The header-to-cell relationships shown visually are therefore not programmatically determinable.
- Criterion: WCAG 2.2 SC 1.3.1 Info and Relationships (Level A), W3C Recommendation 12 December 2024, tier 1. The entry lists this pattern as definite (failure F92, tier 2).
- Source: `knowledge/wcag/sc-1.3.1-info-and-relationships.md`.
- Supporting sources:
  - `knowledge/aria/roles/presentation.md` gives the inheritance rule from WAI-ARIA 1.2 (W3C Recommendation 6 June 2023, tier 1).
  - `knowledge/html/tables.md` reserves the role for layout tables that cannot yet be replaced.
- Why the role is not ignored: the table is not focusable and carries no global `aria-*` attribute, so neither of the entry's conditions for a browser ignoring the role applies.
- Fix direction: remove `role="presentation"` from the table; the native markup underneath is already correct.

### [Likely]
None.

### [Manual review]
None beyond the checks listed under "Manual checks remaining".

### Checked and not a finding
- **Text contrast, SC 1.4.3 Contrast (Minimum) (Level AA), `knowledge/wcag/sc-1.4.3-contrast-minimum.md`.** All text clears the entry's 4.5:1 threshold. The ratios below were computed from the declared CSS colors with the Recommendation's formula:

  | Text | Colors | Ratio |
  |---|---|---|
  | Body text | `#1a1a1a` on `#fff` | 17.4:1 |
  | Links | `#0b4f9c` on `#fff` | 8.04:1 |
  | Header cells | `#1a1a1a` on `#f2f2f2` | 15.55:1 |

- **Target size, SC 2.5.8 Target Size (Minimum) (Level AA), `knowledge/wcag/sc-2.5.8-target-size-minimum.md`.** The navigation links sit in a flex row with a `1rem` gap, and axe reported no target-size violation with the `wcag22aa` tag passed. Rendered sizes were not measured by hand.
- **Reflow, SC 1.4.10 Reflow (Level AA), `knowledge/wcag/sc-1.4.10-reflow.md`.** Nothing in the CSS sets a fixed or minimum width. The entry permits a data table to scroll in two dimensions, but the page has to be observed at the test width (see manual checks).
- **Page basics.** `lang="en"`, a descriptive `<title>`, `header`/`nav`/`main`/`footer` landmarks, a named `nav`, one `h1`, and an explicit `a:focus-visible` outline are all present. No criterion is cited because none of these is a defect.

## Content

- **Reading level:** `readability.py 1.0 (2026-10-23)` gives Flesch-Kincaid Grade Level 3.4 against the house target of 8 (at or below).
  - It measured `<main>` and left out `h1` x1, `nav` x1, `style` x1.
  - Counts: 52 words, 20 sentences, 79 syllables (estimated by rule).
  - The tool notes the text is under 100 words, so the score means little. It is a signal, not a pass.
- **Headings:** one `h1`, "Opening hours this week", describes the page; there are no skipped levels. Meets standard 4 of `docs/content-standards.md`.
- **Link text:** "Campus Libraries", "Hours", "Locations", "Contact", "Holiday opening hours", and "Accessibility statement" each say where they go, and none is duplicated. Meets standard 5.
- **Alt text:** no images, so not applicable.
- **Error messages:** no forms, so not applicable.
- **Language:** `lang="en"` is declared, with no foreign-language passages and no unexpanded abbreviations. Meets standard 8.
- **Caption text:** "Opening hours by library and day" describes the table, but under the current markup it is not exposed as a caption (see the finding).
- **[Manual review] Time format:** times use the 24-hour clock ("8:00 to 22:00"). Whether that suits this audience is a plain-language judgment for a person, and there is no spec to settle it.

## Spec deviations

None reportable: there is no `a11y-spec.md`.

## Manual checks remaining

- **Accessibility tree, before the fix.** Open the page in a browser's accessibility inspector, select the table at line 34, and record the role exposed for the table, a `th`, a `td`, and the caption.
- **Screen reader, after the fix.** Using the project's assistive technology, move through the table with table navigation commands and try to locate it from a tables list. Record whether the caption, column headers, and row headers are reported for each data cell.
- **Keyboard only.** Tab through all six links. Record the order and whether the focus outline is visible on each, including the current-page link.
- **Zoom.** At 1280 pixels wide and 400 percent zoom (320 CSS pixels), record whether anything outside the table needs horizontal scrolling and whether the navigation row stays fully reachable. Repeat at 200 percent.
- **Text spacing overrides.** Apply them and record any clipped or overlapping text in table cells.
- **Forced colors (Windows Contrast Themes).** Record whether table borders, the header cell distinction, and the focus outline remain visible.
- **`aria-current="page"` on "Hours".** Record what the tester's screen reader reports for it. The current page also has no visual marker beyond default link styling; whether that is adequate is a design judgment, not a finding.
- **Cross-page consistency.** Navigation and help across pages cannot be judged from one page.

## Automated scan

```
axe-core 4.14.0 via @axe-core/cli (axe), tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa
page: file:///Users/derekjackson/Documents/CCode/doctorAccessible/evals/046-aria-presentation-on-data-table/input.html
raw JSON: /var/folders/th/2_b8_m913qv7cv3ydxpt5tdm0000gq/T/doctor-a11y-axe/046-aria-presentation-on-data-table-20261121-001008.json

violations: 0

incomplete: 0

passes: 19 rules   inapplicable: 45 rules

raw (violations and incomplete):
{
  "violations": [],
  "incomplete": []
}
```

- **Violations:** none, so no axe result supports the finding above; it comes from reading the code.
- **Incomplete:** none.
- **Why the clean run is not a pass:** axe did not flag the one definite defect. The only axe rule in `knowledge/axe-rules.md` that names the presentation role, `presentation-role-conflict`, is mapped there as a best practice rather than a WCAG finding. Per `knowledge/aria/roles/presentation.md`, it concerns the role being ignored on focusable elements, which is not this case.
