# Eval 044: manual testing checklist for one component (a form)

Input: `request.md`. A developer asks for a checklist covering only the room request form on a page that also has a navigation bar and a newsletter form. The spec lists three modes: keyboard only, NVDA with Firefox, and 200% and 400% zoom. There is no pattern entry for forms, so the skill should open `knowledge/html/forms.md`. The form holds several likely problems on purpose. This eval tests scope and the `html/` route, not one defect.

Intended outcome: a checklist in the shape of `templates/at-test-checklist.md` for the room request form alone, grouped by the spec's three modes and then by the form's parts (fields, the radio group, submitting with errors, submitting successfully), with a Watch for section limited to the form's code.

## Expected

1. **Scope is the form.** Items cover the room request form only. The navigation and the newsletter form get no items. Mentioning that the tester reaches the form from the page, or that the rest of the page is out of scope, is fine.
2. **The spec's modes, and only those.** Sections for keyboard only, NVDA with Firefox, and zoom. No VoiceOver, forced colors, or reduced motion section; a one-line note that they are not on the list is fine.
3. **Checklist shape.** Tick boxes; each item says what to do and gives an "Expected" pass condition with a `wcag/` entry, or is marked manual review.
4. **Uses `html/forms.md`.** Says there is no pattern entry, and draws items from the forms entry: each field's label is read with it; the radio group's question ("Room size") is read with each option (`wcag/sc-1.3.1-info-and-relationships.md`); the required state is read (`wcag/sc-4.1.2-name-role-value.md` or `wcag/sc-3.3.2-labels-or-instructions.md`).
5. **Keyboard items:** Tab through the fields in visual order (`wcag/sc-2.4.3-focus-order.md`); arrow keys move within the radio group (from `testing/keyboard-only.md`); the date field can be filled by keyboard (`wcag/sc-2.1.1-keyboard.md`); Request room works with Enter and with Space; after a submit with errors, note where focus goes; focus visible on every field (`wcag/sc-2.4.7-focus-visible.md`).
6. **Error and success items:** submit empty, then with a bad email. Each error says what is wrong and is tied to its field, so it is read on returning to the field (`wcag/sc-3.3.1-error-identification.md`). The email error suggests a fix (`wcag/sc-3.3.3-error-suggestion.md`, optional). "Request sent" is announced while focus stays where it was (`wcag/sc-4.1.3-status-messages.md`).
7. **NVDA setup and items** from `testing/screen-reader-windows.md`: Speech Viewer; F to move by form field; note the browse and focus mode switches; the warning that a tester's unfamiliarity can look like a defect.
8. **Zoom items** at 200% and 400% on the form's labels, fields, and error text (`wcag/sc-1.4.4-resize-text.md`, `wcag/sc-1.4.10-reflow.md`).
9. **A Watch for section, separate from the items, limited to the form,** naming at least two of these with a place in the code and the item that confirms it:
   - the radio buttons have no `fieldset` and `legend`, so "Room size" is a paragraph with no tie to the options;
   - the errors are listed at the top and not tied to their fields (no `aria-describedby`, no `aria-invalid`);
   - focus is not moved on a submit with errors, and the error box is not a live region;
   - the email field has no `autocomplete` token (`wcag/sc-1.3.5-identify-input-purpose.md`).
10. **Items stay neutral, and never speak as a user.** No item predicts a failure or what NVDA will say.

## Also acceptable

- A note that `novalidate` turns off the browser's own error messages, so all errors come from the script.
- Testing the radio group with Space as well as arrow keys.
- A "What to record" section and a Gaps section.
- Asking where the checklist file should live, or offering a place outside the repo.

## Must not

- Write or change code, or offer fixed code.
- Include items for the navigation or the newsletter form.
- Include sections for modes not on the spec's list.
- State a criterion number, title, level, or keyboard command not found in the entries without marking it unverified.
- Put an expected failure in a checklist item, or predict what a screen reader will say.

## Pass condition

Items 1 to 6, 9, and 10 are present, items 7 and 8 are not contradicted, and nothing from the Must not list appears.
