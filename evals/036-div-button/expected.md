# Eval 036: a div that acts as a button

Input: `input.html`. A book page with a "Reserve this book" control.

Intended defect: "Reserve this book" is a `div` with only an `onclick` handler. It has no role, no `tabindex`, and no key handling. A keyboard user cannot reach it, and assistive technology does not expose it as a button.

Everything else is clean:
- The result message goes into a `p` with `role="status"`, present from load, so it is announced without moving focus.
- Language, title, one `h1` and an `h2`, `header` and `main`, a named link.
- Text and border contrast are about 7.1:1 or better (#005a9c and #1a1a1a on white), and focus is visible on the link.

## Expected findings

1. **[Definite]** "Reserve this book" cannot be reached or activated by keyboard and is not exposed as a button.
   - Criterion: WCAG 2.2 SC 2.1.1 Keyboard (Level A), tier 1, from `knowledge/wcag/sc-2.1.1-keyboard.md` ("A `div` or `span` acting as a link or button with no `tabindex`, so it cannot be reached at all. Definite, and also a 4.1.2 defect"; F42). Reporting it under SC 4.1.2 Name, Role, Value (Level A), with 2.1.1 co-cited in the same finding, is equally acceptable. One finding, not two.
   - HTML entry: `knowledge/html/buttons.md`.
   - Where: `div.reserve`.
   - Acceptable fix directions: use a native `<button type="button">`, which brings focus, Enter and Space, and the button role. As a direction, not a patch.

## Also acceptable

- A note that `role="button"` with `tabindex="0"` and key handling would also work, but the native button is the first choice (`aria/using-aria.md`, rule 1).
- Manual-review notes that a criterion appears met and needs a browser check.
- A note that axe is not expected to catch this.

## Must not

- Report the defect twice, under 2.1.1 and again under 4.1.2.
- Report the status message, which is a live region already.
- Report contrast, the link, headings, landmarks, or language as failures.
- Report the `div`'s hover style or missing focus style as a separate finding; it cannot take focus at all, which is the finding.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

The 2.1.1 entry says axe "does not detect a clickable `div` with no key handler", so axe is not expected to report this defect. Observed 2026-10-23: axe-core 4.14.0 reported 0 violations, default and WCAG 2.2-tagged. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as definite under SC 2.1.1 or SC 4.1.2 (Level A), tier 1, with the other co-cited at most once, and nothing from the Must not list appears.
