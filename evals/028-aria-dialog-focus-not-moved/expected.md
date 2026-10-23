# Eval 028: modal dialog that never receives focus

Input: `input.html`. A shared-files page with a "Delete Budget-2026.xlsx" button that opens a confirmation dialog.

Intended defect: the dialog's ARIA is right. It has `role="dialog"`, `aria-modal="true"`, `aria-labelledby` pointing at its visible heading, and a short `aria-describedby`. The page behind is made `inert` while it is open. But `openDialog()` never moves focus into it. Focus is left on the trigger, which has just become inert, or is lost to the document; either way nothing in the dialog has focus, and nothing in it is announced on open. WAI-ARIA 1.2 says authors should focus an element in a modal dialog when it is displayed.

Everything else is clean: the dialog is hidden until opened (`.backdrop[hidden]` overrides the grid display), language set, title present, one `h1`, `main` landmark, named buttons, visible focus (#005a9c, about 7.1:1 on white), body text far above 4.5:1. Escape closes the dialog, and both buttons close it and return focus to the trigger.

## Expected findings

1. **[Likely]** Focus is not moved into the modal dialog when it opens.
   - Criterion: WCAG 2.2 SC 2.4.3 Focus Order (Level A), tier 1, from `knowledge/wcag/sc-2.4.3-focus-order.md` ("Focus not moved into a modal when it opens ... Definite once observed"). Read from the code, it is likely; definite needs a person to observe it.
   - ARIA entry: `knowledge/aria/patterns/modal-dialog.md`, which lists this case, with the WAI-ARIA 1.2 "should" on focusing modal dialogs.
   - Where: `openDialog()` in the script; the `div[role="dialog"]`.
   - Acceptable fix directions: move focus into the dialog on open, for example to the Cancel button (the least destructive action, per the APG) or to the heading given `tabindex="-1"`; or use a native `dialog` with `showModal()`, which places focus itself. As a direction, not a patch.

## Also acceptable

- A manual test: open the dialog by keyboard and with a screen reader, and record where focus is.
- A note, marked advice, that native `dialog` with `showModal()` would make `aria-modal` unnecessary.
- A note that axe is not expected to catch this.

## Must not

- Grade it definite without saying it was observed in a browser.
- Report the dialog's role, name, description, or `aria-modal` as wrong; they are correct.
- Report a keyboard trap (2.1.2); Escape and both buttons close it.
- Report focus return on close; it returns to the trigger.
- Report the trigger, the heading, landmarks, contrast, focus style, or language.
- Report the defect twice, under 2.4.3 and again under 2.1.1 or 4.1.2.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe checks markup and ARIA, not where focus goes after a click, so it is not expected to report this defect. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present under SC 2.4.3 (Level A), tier 1, at likely, or at definite with the observation stated, and nothing from the Must not list appears.
