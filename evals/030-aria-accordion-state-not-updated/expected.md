# Eval 030: accordion whose `aria-expanded` never changes

Input: `input.html`. A "Library questions" page with two accordion sections.

Intended defect: each header is a native `button` inside an `h2`, with `aria-expanded="false"` and `aria-controls` pointing at its panel. The script toggles the panel's `hidden` attribute and a CSS class that turns the chevron, but never updates `aria-expanded`. A sighted user sees the section open. A screen reader still reports "collapsed".

Everything else is clean: native buttons in headings, so Enter and Space work; the chevron is drawn with borders, not text, so it adds nothing to the button's name; visible focus; language, title, one `h1`, `main`. Contrast: #005a9c on white is about 7.1:1.

## Expected findings

1. **[Definite]** The headers' expanded state is never exposed: `aria-expanded` stays "false" when a panel opens.
   - Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1, from `knowledge/wcag/sc-4.1.2-name-role-value.md` ("A custom ... expandable region that changes state visually without exposing that state ... Definite when the state is user-settable").
   - ARIA entry: `knowledge/aria/patterns/accordion.md`, which lists this case.
   - Where: both `h2 button[aria-expanded]`; the click handler in the script.
   - Acceptable fix directions: set `aria-expanded` to match `!panel.hidden` in the click handler, and drive the chevron from `[aria-expanded="true"]` so the two cannot drift; or use `details` and `summary`. As a direction, not a patch.

## Also acceptable

- A note, marked advice, that `aria-controls` adds little (from the accordion entry).
- A manual test: open a section with a screen reader and record the state announced.
- A note that axe is not expected to catch this.

## Must not

- Report the buttons as unreachable or inoperable by keyboard; they are native buttons.
- Report the headings, the `aria-controls`, or the missing optional `region` role.
- Report the chevron as part of the name; it has no text.
- Report the defect twice, under 4.1.2 and again under 1.3.1.
- Report contrast, focus style, landmarks, or language.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe sees a valid `aria-expanded` value on a button. It does not compare the state with what is shown, so it is not expected to report this defect. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as definite under SC 4.1.2 (Level A), tier 1, and nothing from the Must not list appears.
