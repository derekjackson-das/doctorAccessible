## Checked

- File: `/Users/derekjackson/Documents/CCode/doctorAccessible/evals/048-aria-img-no-name/input.html` (46 lines, static HTML and CSS, no script).
- How: read in full, scanned with `tools/axe.py` (axe-core 4.14.0), and measured with `tools/readability.py`.
- Spec: no `a11y-spec.md` beside the file, at the repo root, or in `docs/`. Checked against WCAG 2.2 AA alone.
- Per the constraints, `expected.md`, `evals/RESULTS.md`, and run files were not opened. No files were changed.

## Findings

### [Definite] Star ratings use `role="img"` with no accessible name
- Where: lines 28 and 35, `<span class="stars" role="img">★★★★☆</span>` and `<span class="stars" role="img">★★☆☆☆</span>` (axe targets `article:nth-child(3) > p:nth-child(2) > span` and `article:nth-child(4) > p:nth-child(2) > span`).
- What: each rating is exposed as an image with no `aria-label`, `aria-labelledby`, or `title`, and the rating appears nowhere else in the review as text.
- Why the star characters do not rescue it: per `knowledge/aria/roles/img.md`, the role takes its name from the author only, and its descendants are presentational (WAI-ARIA 1.2, W3C Rec 6 June 2023, tier 1).
- Criterion: WCAG 2.2 SC 1.1.1 Non-text Content (Level A), W3C Rec 12 Dec 2024, tier 1.
- Source: `knowledge/wcag/sc-1.1.1-non-text-content.md` ("An `svg` or an element with `role="img"` that has no accessible name. Definite."), supported by `knowledge/aria/roles/img.md`.
- Fix direction: give each rating a text alternative that states the value (for example "4 out of 5 stars"), either as a name on the `role="img"` element or as real text with the glyphs hidden from assistive technology.
- Scope: one defect, two instances. It is not repeated under SC 4.1.2, because the rating is not a user interface component (`knowledge/wcag/sc-4.1.2-name-role-value.md`).

### [Likely]
None.

### [Manual review]
None beyond the checks listed under "Manual checks remaining".

### Checked and passing from code
Contrast ratios below were computed from the declared CSS colors with the WCAG relative luminance formula.

| Check | What the code shows | Entry |
|---|---|---|
| Page language | `lang="en"` on `html`; "Priya" and "Tomás" are proper names, which the entry exempts | `sc-3.1.1-language-of-page.md`, `sc-3.1.2-language-of-parts.md` |
| Page title | "Study room reviews – Campus Libraries", page name first | `sc-2.4.2-page-titled.md` |
| Structure | One `h1`, two `h2`, no skipped levels; `header`, `main`, `footer` and `article` present | `sc-1.3.1-info-and-relationships.md` |
| Bypass | Landmarks present, no skip link; the entry counts this as a pass | `sc-2.4.1-bypass-blocks.md` |
| Body text contrast | `#1a1a1a` on `#fff` is 17.4:1, against the 4.5:1 threshold | `sc-1.4.3-contrast-minimum.md` |
| Link text contrast | `#0b4f9c` on `#fff` is 8.04:1, against the 4.5:1 threshold | `sc-1.4.3-contrast-minimum.md` |
| Star glyph contrast | `#1a1a1a` on `#fff` is 17.4:1, above the 4.5:1 text threshold and the 3:1 graphics threshold, whichever applies | `sc-1.4.3-contrast-minimum.md`, `sc-1.4.11-non-text-contrast.md` |
| Focus indicator | `a:focus-visible` draws a 3px `#0b4f9c` outline; 8.04:1 on white, against the 3:1 threshold | `sc-2.4.7-focus-visible.md`, `sc-1.4.11-non-text-contrast.md` |
| Use of color | Links keep the default underline and none sit in body text; filled and empty stars differ by shape | `sc-1.4.1-use-of-color.md` |
| Link purpose | "Campus Libraries", "Book a study room", "Accessibility statement" each stand alone | `sc-2.4.4-link-purpose-in-context.md` |
| Target size | Each link sits alone in its own paragraph, separated by at least 1rem of padding or margin. A 24px circle on each would not meet another, so the spacing exception applies if any is under 24px high. | `sc-2.5.8-target-size-minimum.md` |

The `#767676` borders (4.54:1 on white) are decorative separators, not needed to identify a component, so no threshold applies.

## Content

- Reading level: `readability.py 1.0 (2026-10-23)`, measured over `<main>`, leaving out h1 x1, h2 x2, style x1.
  - 57 words, 7 sentences, 76 syllables (estimated by rule).
  - Flesch-Kincaid Grade Level 3.3 against the house default target of 8 (no spec target): at or below.
  - The tool notes that under 100 words the score means little. It is a signal, not a pass.
- Headings: "Study room reviews", "Room 204, Science Library", "Room 3B, Law Library" describe their sections. One `h1`, no skipped levels. Meets `docs/content-standards.md` section 4.
- Link text: all three links say where they go. Meets section 5.
- Alt text: there are no `img` elements. The two star ratings are images by role and have no text alternative, which is the finding above (section 6, reported under SC 1.1.1).
- Error messages: none on the page; not applicable.
- Language: declared, with no foreign-language passages or unexpanded abbreviations. Meets section 8.
- Plain language and organization: short, active sentences with a one-line summary under the `h1`. Manual review only in the sense that a person should still read it.

## Spec deviations

None reportable: there is no `a11y-spec.md` for this input.

## Manual checks remaining

- **Screen reader, before the fix:** with the project's screen readers (none are listed, as there is no spec), move through each review. Record what is exposed at the star rating in each article and whether the rating value is available anywhere.
- **Screen reader, after the fix:** `knowledge/aria/roles/img.md` (MDN, tier 3) notes that some browser and screen reader pairs read a label on character-based `role="img"` content twice. Test each pair and record what is read.
- **Equivalence of the eventual name:** a person confirms the text alternative states the same rating the glyphs show (4 of 5, 2 of 5). axe cannot judge this.
- **Keyboard:** Tab through the three links. Record that the focus outline is visible on each and that the order is header, main, footer.
- **Zoom and reflow:** check at 200% and at 400% (320 CSS px wide). Record any clipping or horizontal scrolling; `.review` uses `max-width: 40rem` and nothing in the CSS suggests a problem.
- **Text spacing:** apply the text-spacing overrides and record whether the stars (which have `letter-spacing: .1em`) or any text clip.
- **Forced colors (Windows Contrast Themes):** record that the star glyphs, borders, and focus outline remain visible.
- **Cross-page criteria:** this is a single page, so consistent navigation, consistent identification, consistent help, and multiple ways cannot be judged here.

## Automated scan

- axe-core 4.14.0 via `@axe-core/cli`, tags `wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa`.
- Page: `file:///Users/derekjackson/Documents/CCode/doctorAccessible/evals/048-aria-img-no-name/input.html`
- Raw JSON (outside the repo): `/var/folders/th/2_b8_m913qv7cv3ydxpt5tdm0000gq/T/doctor-a11y-axe/048-aria-img-no-name-20261123-143854.json`
- Passes: 13 rules. Inapplicable: 50 rules.

Violations: 1
- `role-img-alt` (serious; wcag2a, wcag111): "[role="img"] and [role="image"] elements must have alternative text"
  - `article:nth-child(3) > p:nth-child(2) > span`
  - `article:nth-child(4) > p:nth-child(2) > span`
  - Failure summary for both: aria-label attribute does not exist or is empty; aria-labelledby attribute does not exist, references elements that do not exist or references elements that are empty; element has no title attribute.

Incomplete: 1
- `color-contrast` (serious; wcag2aa, wcag143): "Elements must meet minimum color contrast ratio thresholds"
  - Same two spans. Reason: "Element content contains only non-text characters".

Raw block as printed (violations and incomplete):
```
{
  "violations": [
    { "id": "role-img-alt", "impact": "serious", "tags": ["wcag2a", "wcag111"],
      "help": "[role=\"img\"] and [role=\"image\"] elements must have alternative text",
      "helpUrl": "https://dequeuniversity.com/rules/axe/4.14/role-img-alt?application=webdriverjs",
      "nodes": [
        { "target": ["article:nth-child(3) > p:nth-child(2) > span"],
          "failureSummary": "Fix any of the following:\n  aria-label attribute does not exist or is empty\n  aria-labelledby attribute does not exist, references elements that do not exist or references elements that are empty\n  Element has no title attribute" },
        { "target": ["article:nth-child(4) > p:nth-child(2) > span"],
          "failureSummary": "(same)" } ] } ],
  "incomplete": [
    { "id": "color-contrast", "impact": "serious", "tags": ["wcag2aa", "wcag143"],
      "help": "Elements must meet minimum color contrast ratio thresholds",
      "helpUrl": "https://dequeuniversity.com/rules/axe/4.14/color-contrast?application=webdriverjs",
      "nodes": [
        { "target": ["article:nth-child(3) > p:nth-child(2) > span"],
          "failureSummary": "Fix any of the following:\n  Element content contains only non-text characters" },
        { "target": ["article:nth-child(4) > p:nth-child(2) > span"],
          "failureSummary": "(same)" } ] } ]
}
```
The second node's failure summary is abbreviated here as "(same)"; the full text is in the raw JSON.

Mapping to findings:
- `role-img-alt` maps to SC 1.1.1 in `knowledge/axe-rules.md` and supports the Definite finding above.
- `color-contrast` (incomplete) is a lead, not a finding. axe could not judge glyph-only content; the computed 17.4:1 clears every threshold in the 1.4.3 and 1.4.11 entries.
