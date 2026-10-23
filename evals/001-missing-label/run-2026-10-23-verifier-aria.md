# Run 2026-10-23: verifier on eval 001, after the ARIA foundation entries

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit f1d257c (adds `knowledge/aria/` and a row in the wcag skill map).
- Method: a general-purpose agent told to read `verifier.md` and follow it, then verify `input.html`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- Why: a regression run. This eval is about an accessible name, so the new `aria/accessible-name.md` could change the answer.
- axe: not run (Node.js not installed).
- Result: **pass.** One definite finding under SC 4.1.2 (Level A), with 1.3.1 co-cited in the same finding; the shared word "Search" as manual review; nothing from the must-not list.

## The report, as given

## Checked
`evals/001-missing-label/input.html`, all 28 lines, read by hand. I did not run axe because Node.js is not installed on this machine and `npx` is unavailable. The repo has no `a11y-spec.md`, either at the root or in `docs/`, so I checked against WCAG 2.2 AA only. Entries opened: `knowledge/INDEX.md`, `.claude/skills/wcag/SKILL.md`, wcag entries for SC 4.1.2, 1.3.1, 3.3.2, 2.4.6, 2.4.7, 1.4.11, 1.4.3, 2.5.8, 3.1.1 and 2.4.2, `aria/accessible-name.md`, `testing/screen-reader-windows.md`, `content/reading-level.md` and `docs/content-standards.md`.

## Findings
### [Definite] Search text field has no accessible name; visible "Search" text is not associated with it
- Where: `evals/001-missing-label/input.html` lines 21–22, `<span>Search</span>` followed by `<input type="text" id="q" name="q">`
- What: Nothing names the input: no `label` points at `id="q"` or wraps it, and it has no `aria-label`, `aria-labelledby`, `title` or `placeholder`. The visible "Search" text in the adjacent `span` is not programmatically connected, so the HTML naming order yields no name.
- Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1. The same defect also fails WCAG 2.2 SC 1.3.1 Info and Relationships (Level A), tier 1, as a visible label that is not associated (F111). The 1.3.1 entry says to report this once and name both criteria.
- Source: knowledge/wcag/sc-4.1.2-name-role-value.md; knowledge/wcag/sc-1.3.1-info-and-relationships.md; name computation from knowledge/aria/accessible-name.md
- Fix direction: Use a native `label` element associated with the input, H44 in both entries (for example, turn the existing visible text into a `label for="q"`), so the visible word "Search" becomes the accessible name.

No other defects found. Notes on things checked that pass:
- SC 3.3.2 Labels or Instructions (Level A) is met. Visible label text exists, and the entry says an unassociated visible label is "Not this criterion; the label exists." (knowledge/wcag/sc-3.3.2-labels-or-instructions.md)
- SC 2.4.6 Headings and Labels (Level AA). "Site search" (h1) and "Search" describe their purpose. (knowledge/wcag/sc-2.4.6-headings-and-labels.md)
- SC 2.4.7 Focus Visible (Level AA). The author supplies a `:focus-visible` outline and does not remove the default. (knowledge/wcag/sc-2.4.7-focus-visible.md)
- SC 1.4.11 Non-text Contrast (Level AA). I computed 7.14:1 for the focus outline color #005a9c against the white body background #fff, from the colors declared on lines 8 and 11, using the relative-luminance contrast formula. The entry's threshold is 3:1. The outline is offset 2px, so the adjacent color is the page background. (knowledge/wcag/sc-1.4.11-non-text-contrast.md)
- SC 1.4.3 Contrast (Minimum) (Level AA). I computed 17.40:1 for body text #1a1a1a on #fff, from line 8. The entry's threshold for normal text is 4.5:1. Text and background colors are both set. (knowledge/wcag/sc-1.4.3-contrast-minimum.md)
- SC 3.1.1 Language of Page (Level A). `lang="en"` is on `html`. (knowledge/wcag/sc-3.1.1-language-of-page.md)
- SC 2.4.2 Page Titled (Level A). The title "Site search" is present and describes the page. (knowledge/wcag/sc-2.4.2-page-titled.md)

## Content
- Reading level: not measured. There is no readability tool on this machine, and the main content is three words ("Site search", "Search", "Search"), too short for a meaningful Flesch-Kincaid score.
- Headings: one `h1`, "Site search", which says what the page is; no skipped levels. This meets content standards section 4.
- Link text and alt text: the page has no links and no images.
- Error messages and instructions: the page has none. A free-text search field needs no format instruction.
- Language: declared (section 8).
- Manual review: the visible label and the button both say "Search". That matches technique G167 (an adjacent button labels a search field's purpose), cited in the 3.3.2 entry. Whether a person reads the duplicated word as clear is a human judgment.

## Spec deviations
There is no `a11y-spec.md` at the repo root or in `docs/`. Nothing to compare against.

## Manual checks remaining
- Accessibility tree: in browser developer tools, inspect `#q` and record the computed name and where it comes from. Before the fix, record whether the name is empty. After the fix, record that it contains "Search" (SC 2.5.3 Label in Name, knowledge/wcag/sc-2.5.3-label-in-name.md).
- NVDA with Chrome or Firefox (knowledge/testing/screen-reader-windows.md, step 5): press Tab to reach the text field and record the Speech Viewer text (name, role, value). Press F to move through form fields and record the same. Press B to reach the button and record what is read. Note the NVDA, browser and Windows versions, and whether the tester uses a screen reader daily.
- Speech recognition: try activating the field by saying its visible label ("click Search") and record which element, if any, gets focus.
- Keyboard only: press Tab through the page and record the focus order (field, then button), whether the focus outline is visible on each, and whether Enter in the field submits the form.
- Target size (knowledge/wcag/sc-2.5.8-target-size-minimum.md): from the CSS, the input and button have 0.5rem padding around inherited body text, which is likely above 24 by 24 CSS pixels. That is an estimate, not a measurement. Measure the rendered boxes in developer tools and record them.
- Zoom and reflow: at 200% and 400% zoom (knowledge/testing/zoom.md), record whether the flex row wraps or clips at narrow widths.
- Forced colors (knowledge/testing/forced-colors.md): record whether the input boundary and the focus outline stay visible.

## Automated scan
Not run. Node.js is not installed on this machine, so `npx --yes @axe-core/cli --tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa` could not be run. There are no violations, incomplete, passes or inapplicable results to report.
