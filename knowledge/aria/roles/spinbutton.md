# Role: spinbutton

- Category: widget (range).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "spinbutton role", https://www.w3.org/TR/wai-aria-1.2/#spinbutton. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for text `input` with no `list`, and form-associated custom elements, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `input type=number` (3.5.68), https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Spinbutton Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/spinbutton/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: spinbutton role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/spinbutton_role
- Related entries: `aria/roles/slider.md`, `aria/roles/textbox.md`, `html/forms.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A value, usually a number, that the user types or steps up and down. WAI-ARIA 1.2: "A form of range that expects the user to select from among discrete choices."

## The native element

`input type=number` (HTML-AAM). MDN notes the date and time input types use spin buttons inside them.

## When writing the role is justified

When `input type=number` cannot be used. The usual build is a text input with the role, plus increase and decrease buttons kept out of the tab order (APG; WAI-ARIA 1.2).

## What the spec asks of authors

- "Authors MAY create a spinbutton with children or owned elements, but MUST limit those elements to a textbox and/or two buttons."
- "Alternatively, authors MAY apply the spinbutton role to a text input and create sibling buttons to support the increment and decrement functions."
- "To be keyboard accessible, authors SHOULD manage focus of descendants for all instances of this role, as described in Managing Focus."
- "When a spinbutton receives focus, authors SHOULD ensure focus is placed on the textbox element if one is present, and on the spinbutton itself otherwise."
- "Authors SHOULD also ensure the up and down arrows on a keyboard perform the increment and decrement functions and that the increment and decrement button elements are NOT included in the primary navigation ring, e.g., the Tab ring in HTML."
- "Authors SHOULD set the aria-valuenow attribute when the spinbutton has a value."
- "Authors SHOULD set the aria-valuemin attribute when there is a minimum value, and the aria-valuemax attribute when there is a maximum value."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: none.
- Supported states and properties: `aria-errormessage`, `aria-invalid`, `aria-readonly`, `aria-required`, `aria-valuemax`, `aria-valuemin`, `aria-valuenow`, `aria-valuetext`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-haspopup` as deprecated on this role.
- Naming: name from author; **required**.
- WAI-ARIA 1.2 requires none of the value attributes; it says authors SHOULD set `aria-valuenow` when there is a value (below). MDN's page contradicts itself on the defaults for `aria-valuemin` and `aria-valuemax`; take WAI-ARIA 1.2.
- `aria-invalid="true"` when the value is out of range (APG).

**The whole component.** Its children, if any, are limited to a textbox and two buttons (WAI-ARIA 1.2 MUST). Focus stays on the text field; the buttons are not tab stops.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `input type=number`.
- **Allowed:** a text `input` with no `list` attribute, form-associated custom elements, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `input type=number` (already one; no other role allowed), `input type=range`, `button`, `li`, headings, landmark elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Spinbutton Pattern: Up increases, Down decreases; Home and End go to the minimum and maximum where they exist; Page Up and Page Down step further (optional). If the field can be typed in, the normal text-editing keys must still work: APG warns that script must not capture them.

## What an explicit role takes away

- On a text `input`, the textbox role becomes spinbutton; typing still works, and the arrow keys must now step the value.

## How it fails in code

- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- Up and Down do nothing: `wcag/sc-4.1.2-name-role-value.md`, likely; the role promises them.
- Script that blocks normal editing keys in the field: `wcag/sc-2.1.1-keyboard.md`, likely.
- The value changes but `aria-valuenow` or `aria-valuetext` does not: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry.
- The role used where the native element would do: advice, never a finding on its own (`aria/using-aria.md`, rule 1).

## How to check

Focus on the field; Up and Down change the value; typing works; the value is exposed. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
