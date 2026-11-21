# Role: slider

- Category: widget (range).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "slider role", https://www.w3.org/TR/wai-aria-1.2/#slider. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `input type=range`, `button`, `img`, form-associated custom elements, and the `input` button types, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `input type=range` (3.5.71), https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Slider Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/slider/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: slider role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/slider_role
- Related entries: `aria/roles/spinbutton.md`, `html/forms.md`, `html/custom-controls.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.5.7-dragging-movements.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A control for picking a value from a range by moving a thumb. WAI-ARIA 1.2: "An input where the user selects a value from within a given range."

## The native element

`input type=range` (HTML-AAM). Use its `min`, `max`, and `step`, not the ARIA value attributes (MDN).

## When writing the role is justified

When `input type=range` cannot be used, such as a two-thumb range. MDN calls thumbs whose limits depend on each other an anti-pattern.

## What the spec asks of authors

- "Authors MAY set the aria-valuemin and aria-valuemax attributes."
- "Authors MUST set the aria-valuenow attribute."
- "If aria-valuenow is missing or has an unexpected value, browsers MAY implement the repair techniques specified in the section describing handling author errors in states and properties, which are equivalent to the repair techniques for <input[type="range"]> in [ HTML ]."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: `aria-valuenow`.
- Supported states and properties: `aria-errormessage`, `aria-haspopup`, `aria-invalid`, `aria-orientation`, `aria-readonly`, `aria-valuemax`, `aria-valuemin`.
- Prohibited states and properties: none.
- Naming: name from author; **required**. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- `aria-valuemin` defaults to 0 and `aria-valuemax` to 100 if not set (MDN).
- `aria-valuetext` when the number alone is not meaningful, such as a day name (APG).
- `aria-orientation` defaults to `horizontal`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `input type=range` (no other role allowed on it).
- **Allowed:** `button`, `img` with alt text, form-associated custom elements, `input type=button`, `submit`, `reset`, `image`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `input type=range` (already a slider; no role allowed), other form fields, `li`, headings, landmark elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Slider Pattern: Right and Up increase by one step; Left and Down decrease by one step; Home sets the minimum and End the maximum; Page Up and Page Down change by a larger step (optional). Focus sits on the thumb. APG warns that touch screen readers must synthesize these keys from gestures and support is incomplete: test on touch devices.

## What an explicit role takes away

- On a `button`, the button role goes; Enter and Space no longer mean anything for it.
- Children are presentational.

## How it fails in code

- The role on a `div` or `span` with no `tabindex`, so the control cannot be reached by keyboard: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F42). Report once, as that entry says, not again under 4.1.2.
- The role and `tabindex="0"` but no key handler, so the control can be focused but not operated: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F54).
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- `aria-valuenow` missing or not updated as the thumb moves: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry.
- Operable only by dragging: see `wcag/sc-2.5.7-dragging-movements.md`; arrow keys alone do not meet that criterion for pointer users.
- The role used where the native element would do: advice, never a finding on its own (`aria/using-aria.md`, rule 1).

## How to check

Each `role="slider"`: focusable, arrows and Home and End change the value, `aria-valuenow` follows, it has a name. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
