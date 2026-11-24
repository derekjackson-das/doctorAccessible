# Role: dialog

- Category: window.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "dialog role", https://www.w3.org/TR/wai-aria-1.2/#dialog. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `dialog` and `section`, https://www.w3.org/TR/html-aria/#el-dialog
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.33 (`dialog`), https://www.w3.org/TR/html-aam/#el-dialog
- Practice (tier 2): the ARIA Authoring Practices Guide "Dialog (Modal) Pattern" is covered in `aria/patterns/modal-dialog.md`.
- Reference (tier 3): MDN Web Docs, "ARIA: dialog role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/dialog_role
- WAI-ARIA 1.3 (Working Draft 4 June 2026): awareness only. The draft changes the MUST on naming a dialog to a SHOULD.
- Related entries: `html/dialogs.md`, `aria/patterns/modal-dialog.md`, `patterns/modal-dialog.md`, `aria/roles/alertdialog.md`, `aria/accessible-name.md`
- WCAG: `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: how to build a dialog, the keys it promises, how it fails, and the manual tests are in `html/dialogs.md`, `aria/patterns/modal-dialog.md`, and `patterns/modal-dialog.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. A custom `role="dialog"` where the `dialog` element would do is advice, never a finding on its own. `role="dialog"` on a `dialog` element is redundant and never a finding.

## What it is

A window inside the page, set apart from the rest of it. WAI-ARIA 1.2: "A dialog is a descendant window of the primary window of a web application."

## The native element

`dialog` (HTML-AAM 3.5.33). ARIA in HTML allows `role="dialog"` on it but marks it "NOT RECOMMENDED"; the only other role it allows there is `alertdialog`. What the element provides when opened with `showModal()` is in `html/dialogs.md`.

## What the spec asks of authors

- "Authors MUST provide an accessible name for a dialog, which can be done with the aria-label or aria-labelledby attribute."
- "Authors SHOULD ensure that all dialogs (both modal and non-modal) have at least one focusable descendant element."
- "Authors SHOULD focus an element in the modal dialog when it is displayed, and authors SHOULD manage focus of modal dialogs."

**Sources differ on the name.** WAI-ARIA 1.2 says MUST and lists "Accessible Name Required: True". MDN says a name is strongly recommended but not a requirement of the role, and the 1.3 Working Draft says SHOULD. The Recommendation stands: treat the name as required. For reporting, `aria/patterns/modal-dialog.md` makes an unnamed dialog manual review, because the 4.1.2 entry has no case for it.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: `aria-modal`, inherited from `window`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; **required**.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `dialog` (redundant, "NOT RECOMMENDED").
- **Allowed:** `section`, and the elements that allow any role, such as `div`.
- **Not allowed:** `article`, `aside`, `main`, `form`, `fieldset`, `nav`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- `role="dialog"` on a `div` supplies the role and nothing else: no modality, no Escape to close, no inert page behind it. Script has to do all of it (`aria/patterns/modal-dialog.md`).
- On a `section` with an accessible name, the `region` landmark is replaced by `dialog`.

## Where the detail lives

- The native element: `html/dialogs.md`. A custom dialog, `aria-modal`, focus, keyboard, failures: `aria/patterns/modal-dialog.md`. Whether to use a modal at all, and the manual tests: `patterns/modal-dialog.md`.
- axe: `aria-dialog-name` is a best-practice rule, not a WCAG one (`knowledge/axe-rules.md`); it did not fire on an unnamed dialog in a run with the WCAG tags (axe-core 4.14.0, 2026-11-23). Check the name by reading the code.
