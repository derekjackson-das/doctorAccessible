# Role: toolbar

- Category: structure (a group of controls).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "toolbar role", https://www.w3.org/TR/wai-aria-1.2/#toolbar. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `ul`, `ol`, and `menu`, https://www.w3.org/TR/html-aria/
- Practice (tier 2): ARIA Authoring Practices Guide, "Toolbar Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: toolbar role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/toolbar_role
- Related entries: `aria/roles/menubar.md`, `aria/roles/button.md`, `aria/roles/radiogroup.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A compact group of controls, such as the formatting buttons above an editor. WAI-ARIA 1.2: "A collection of commonly used function buttons or controls represented in compact visual form."

## The native element

None.

## When writing the role is justified

For a group of three or more controls (APG). With fewer, plain buttons in the tab order are simpler.

## What the spec asks of authors

- "Authors MUST supply a label on each toolbar when the application contains more than one toolbar."
- "Authors MAY manage focus of descendants for all instances of this role, as described in Managing Focus."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: none.
- Supported states and properties: `aria-orientation`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-haspopup`, `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.
- A name is required when there is more than one toolbar (WAI-ARIA 1.2 MUST); `aria-orientation` defaults to `horizontal`.

**The whole component.** It holds ordinary controls (buttons, toggle buttons, a radio group, a menu button, a spin button). The toolbar takes one tab stop and the arrows move between its controls, usually with roving `tabindex`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `ul`, `ol`, `menu`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `nav`, `header`, `footer` and the other landmark elements, `li`, headings, `button`, form fields.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Toolbar Pattern: Tab moves in, to the first enabled control (or the last one used), and out again; one tab stop. Left and Right move between controls, optionally wrapping (Up and Down in a vertical toolbar); Home and End (optional). Avoid controls that need the same arrows; if one must, put it last. A documented shortcut to reach the toolbar is recommended.

## What an explicit role takes away

- On a `ul` or `ol`, the list and its items lose their roles.

## How it fails in code

- Every control in the tab order and no arrow keys: not a failure (the controls still work), but the role promises a single stop. Advice; `wcag/sc-4.1.2-name-role-value.md` at most manual review.
- Arrows that do nothing and controls taken out of the tab order: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (roving tabindex with no arrow handler).
- Two toolbars with no names: breaks a WAI-ARIA MUST; advice unless a criterion breaks.

## How to check

One tab stop into the toolbar; arrows move between controls; each control works with its own keys. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
