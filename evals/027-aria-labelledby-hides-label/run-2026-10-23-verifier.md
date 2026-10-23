# Run 2026-10-23: verifier on eval 027

- Verifier: `.claude/agents/verifier.md`, with the knowledge library at commit f1d257c.
- Method: a general-purpose agent told to read `verifier.md` and follow it, then verify `input.html`. It was told not to open `expected.md`, any run file, or `RESULTS.md`, and not to write or install anything. A prompt test, not a fresh-session load.
- axe: not run (Node.js not installed).
- Result: **pass.**

## Graded against `expected.md`

- Finding 1, SC 2.5.3 Label in Name (Level A), tier 1, definite, on `input#dob`, with the computed name "Use the format DD/MM/YYYY" and the reason (AccName 1.1 step 2B before the `label`), citing `aria/accessible-name.md`: present.
- Fix direction: `aria-describedby` for the hint, the native `label` for the name. Acceptable.
- Not reported twice; the field is not said to have no name; the `aria-labelledby` is not called an ARIA in HTML violation: yes.
- Must not: nothing from the list. The name field, the button, the heading, landmarks, focus, and language were checked and passed.
- Also acceptable, used: the accessibility tree as the confirming check; a note that axe's `label-content-name-mismatch` may not fire for an input.

## The report, as given

## Checked
`evals/027-aria-labelledby-hides-label/input.html` (32 lines: a library card form with a name field, a date-of-birth field with a format hint, and a submit button). I read all of it by hand. axe was not run (see Automated scan). The repo has no `a11y-spec.md`, neither at the root nor in `docs/`, so the check is against WCAG 2.2 AA alone, plus the house defaults in `docs/content-standards.md`.

## Findings
### [Definite] The date-of-birth field's name comes only from the format hint, so the visible label "Date of birth" is left out
- Where: input.html line 26, `input#dob` with `aria-labelledby="dob-hint"`. The label is on line 21 (`label[for="dob"]`) and the hint is on line 25 (`span#dob-hint`).
- What: `aria-labelledby` comes before the associated `label` when the accessible name is worked out. The name this code exposes is therefore "Use the format DD/MM/YYYY", and it does not contain the visible label text "Date of birth".
- Criterion: WCAG 2.2 SC 2.5.3 Label in Name (Level A), W3C Rec 12 Dec 2024, tier 1. The entry lists this exact pattern ("aria-labelledby points only at other text, such as a format hint") as definite, failure F96. The name-order reasoning comes from Accessible Name and Description Computation 1.1, section 4.3, step 2B, tier 1, as summarized in the ARIA entry.
- Source: knowledge/wcag/sc-2.5.3-label-in-name.md; knowledge/aria/accessible-name.md
- Fix direction: Take `aria-labelledby` off so the native `label` gives the name, and connect the hint as a description with `aria-describedby` instead of putting it in the name.

No other defects found. Things checked and passed:
- `html lang="en"` is set.
- The `title` is descriptive.
- There is one `h1`, and `header` and `main` landmarks are present.
- The name field has an associated label.
- `autocomplete` tokens are `name` and `bday`. Both fit their fields, though I did not check them against the W3C input purposes list in this run (knowledge/wcag/sc-1.3.5-identify-input-purpose.md).
- The button is a native `button` with text.
- A focus outline is declared with `:focus-visible`.
- Contrast, computed by hand from the declared colors with the WCAG relative-luminance formula:
  - Body text #1a1a1a on #fff is far above the 4.5:1 threshold.
  - Hint text #4a4a4a on #fff is about 8.9:1, above 4.5:1 (knowledge/wcag/sc-1.4.3-contrast-minimum.md).
  - The focus outline #005a9c against #fff is about 7.1:1, above the 3:1 threshold (knowledge/wcag/sc-1.4.11-non-text-contrast.md).
- The input borders are browser defaults that the author did not change, so the 1.4.11 exemption applies.

## Content
- Reading level: not measured. No readability tool was run, and the page has only a few words of body text, too few for a meaningful Flesch-Kincaid score.
- Heading: "Apply for a library card" describes the page and is the only `h1`. It meets docs/content-standards.md section 4.
- Instructions: the format hint comes before its field, as section 7 asks. Whether "Use the format DD/MM/YYYY" is clear to the intended readers is manual review. "DD/MM/YYYY" is a format pattern rather than an abbreviation, but whether it needs explaining is a judgment call (section 8).
- Links, alt text, error messages: none on the page.

## Spec deviations
None. The project has no `a11y-spec.md`, so there are no deviations to report.

## Manual checks remaining
- In the browser's accessibility tree, look at `#dob`. Record the computed name and description and where each comes from. Repeat after any fix.
- Screen reader test (NVDA with Firefox or Chrome, and VoiceOver with Safari; see knowledge/testing/screen-reader-windows.md and screen-reader-apple.md): Tab to each field and the button. Record exactly what is spoken for the name, role, and any description.
- Speech recognition test (for example Dragon or Voice Control): say "click Date of birth". Record whether focus moves to the field.
- Keyboard only: Tab through the form. Record the focus order and whether the focus outline can be seen on every control.
- Zoom to 200% and 400% and apply text-spacing overrides. Record any clipped or overlapping text.
- Forced colors (Windows Contrast Themes): record whether the fields, the button, and the focus outline stay visible.
- Server-side errors after submit cannot be judged from this file.

## Automated scan
Not run. axe cannot run on this machine because Node.js is not installed, so `npx --yes @axe-core/cli --tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa` was not available. When it is run, look at the `label-content-name-mismatch` rule in particular. That rule mainly checks elements named from their content, so for this input it may not fire, or may only land in incomplete. A clean result would not clear the finding above.
