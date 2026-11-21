# Role: scrollbar

- Category: widget (range).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "scrollbar role", https://www.w3.org/TR/wai-aria-1.2/#scrollbar. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `img`, https://www.w3.org/TR/html-aria/
- Reference (tier 3): MDN Web Docs, "ARIA: scrollbar role", last modified 21 August 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/scrollbar_role
- Related entries: `aria/roles/slider.md`, `wcag/sc-2.1.1-keyboard.md` (scrollable regions)
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A custom scrollbar that controls which part of a scrolling area is visible. WAI-ARIA 1.2: "A graphical object that controls the scrolling of content within a viewing area, regardless of whether the content is fully displayed within the viewing area."

## The native element

None maps to it. The native answer is a scrolling element (CSS `overflow`) with the browser's own scrollbar (MDN).

## When writing the role is justified

Rarely. MDN says it is always best to use native scrollbars; a custom one has to script every keyboard and pointer action.

## What the spec asks of authors

- "Authors MUST set the aria-controls attribute on the scrollbar element to reference the scrollable area it controls."
- "Authors MAY set aria-valuemin and aria-valuemax to indicate the minimum and maximum thumb position."
- "Authors MUST set the aria-valuenow attribute to indicate the current thumb position."
- "If aria-valuenow is missing or has an unexpected value, browsers MAY implement the repair techniques specified in the section describing handling author errors in states and properties, which are equivalent to the repair techniques for <input[type="range"]> in [ HTML ]."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: `aria-controls`, `aria-valuenow`.
- Supported states and properties: `aria-disabled`, `aria-orientation`, `aria-valuemax`, `aria-valuemin`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-haspopup`, `aria-invalid` as deprecated on this role.
- Naming: name from author; not required. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- `aria-orientation` defaults to `vertical` (MDN).

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `img` with alt text, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** form fields, `button`, `a`, `li`, headings, landmark elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

MDN (no APG pattern): with focus in the area it controls, Up and Down scroll a line, Page Up and Page Down a screen; pointer clicks on the track and dragging the thumb must work too. The scrolling area itself must be keyboard reachable (`wcag/sc-2.1.1-keyboard.md`).

## What an explicit role takes away

- Children are presentational.

## How it fails in code

- `aria-controls` or `aria-valuenow` missing (both required): `wcag/sc-4.1.2-name-role-value.md`, likely.
- The scrolling content cannot be scrolled from the keyboard: `wcag/sc-2.1.1-keyboard.md`, per that entry.
- The role used where the native element would do: advice, never a finding on its own (`aria/using-aria.md`, rule 1).

## How to check

Prefer removing it for a native scrollbar. If kept: `aria-controls` points at the area, `aria-valuenow` follows the position, and the area scrolls by keyboard. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
