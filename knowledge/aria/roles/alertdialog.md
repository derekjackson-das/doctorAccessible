# Role: alertdialog

- Category: window.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "alertdialog role", https://www.w3.org/TR/wai-aria-1.2/#alertdialog. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `dialog` and `section`, https://www.w3.org/TR/html-aria/#el-dialog
- Mapping (tier 2): none. No element maps to this role in "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Alert and Message Dialogs Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/. A pattern, not a requirement. Read in full from a downloaded copy.
- Reference (tier 3): MDN Web Docs, "ARIA: alertdialog role", last modified 29 September 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/alertdialog_role
- WAI-ARIA 1.3 (Working Draft 4 June 2026): awareness only. The draft says authors SHOULD name an alert dialog and no longer lists the name as required.
- Related entries: `aria/roles/dialog.md`, `aria/roles/alert.md`, `aria/patterns/modal-dialog.md`, `html/dialogs.md`, `aria/live-regions.md`
- WCAG: `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: an alert dialog is built, operated, and tested as a modal dialog, and that is in `html/dialogs.md` and `aria/patterns/modal-dialog.md`, not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A dialog that carries an urgent message and needs a response. WAI-ARIA 1.2: "A type of dialog that contains an alert message, where initial focus goes to an element within the dialog." It is a subclass of both `alert` and `dialog`.

## The native element

None maps to it. ARIA in HTML allows `role="alertdialog"` on the `dialog` element, which keeps what the element provides (`html/dialogs.md`).

## When to choose it

When a message needs the user to act, such as confirming a deletion. A message with no controls is an `alert` or a `status` (`aria/live-regions.md`). WAI-ARIA 1.2, under `alert`: "If an author desires focus to move to a message when it is conveyed, the author SHOULD use alertdialog instead of alert."

## What the spec asks of authors

- "Content authors SHOULD make alert dialogs modal by ensuring that, while the alertdialog is shown, keyboard and mouse interactions only operate within the dialog."
- "When the alert dialog is displayed, authors SHOULD set focus to an active element within the alert dialog, such as a form control or confirmation button."
- "Authors SHOULD use aria-describedby on an alertdialog to reference the alert message element in the dialog."

**Sources differ on the name.** WAI-ARIA 1.2 lists "Accessible Name Required: True". MDN says a name is strongly recommended but not required by ARIA, and the 1.3 Working Draft says SHOULD. The Recommendation stands: treat the name as required, and report as for `dialog` (`aria/roles/dialog.md`).

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: `aria-modal`, inherited from `window`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; **required**.
- The APG pattern adds: `aria-modal="true"`, `aria-labelledby` or `aria-label` for the title, and `aria-describedby` pointing at the message.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `dialog`, `section`, and the elements that allow any role, such as `div`.
- **Not allowed:** `article`, `aside`, `main`, `form`, `fieldset`, `nav`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

On a `dialog` element the `dialog` role is replaced by `alertdialog`, its subclass. On a `div` the role supplies nothing but the role; modality, focus, and Escape are script's job (`aria/patterns/modal-dialog.md`).

## Where the detail lives

- Focus, keyboard, `aria-modal`, failures: `aria/patterns/modal-dialog.md`. The APG says the keyboard interaction is the modal dialog's.
- Choosing between `alert`, `status`, and `alertdialog`: `aria/live-regions.md`.
