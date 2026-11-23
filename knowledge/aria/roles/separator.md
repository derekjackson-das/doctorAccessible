# Role: separator

- Category: structure when not focusable; widget when focusable.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "separator role", https://www.w3.org/TR/wai-aria-1.2/#separator. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `hr`, `button`, `img`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `hr` (3.5.52), https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Window Splitter Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/windowsplitter/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: separator role", last modified 21 August 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/separator_role
- Related entries: `aria/roles/menu.md` (separators between menu items), `aria/roles/slider.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). APG's Window Splitter Pattern is marked as still under review, with no working example yet; treat its keys as provisional.

## What it is

A divider between sections or groups of menu items. When focusable, it is a splitter the user moves to resize two panes. WAI-ARIA 1.2: "A divider that separates and distinguishes sections of content or groups of menuitems."

## The native element

`hr` (HTML-AAM), for the static kind. None for the focusable kind.

## When writing the role is justified

Static: when `hr` cannot be used; a decorative divider needs no role at all. Focusable: for a pane splitter, with the value attributes and keys below.

## What the spec asks of authors

- "Authors MAY make a separator focusable to create a widget that both provides a visible boundary between two sections of content and enables the user to change the relative size of the sections by changing the position of the separator."
- "If the separator is focusable, authors MUST set the value of aria-valuenow to a number reflecting the current position of the separator and update that value when it changes."
- "Authors SHOULD also provide the value of aria-valuemin if it is not 0 and the value of aria-valuemax if it is not 100."
- "In applications where there is more than one focusable separator, authors SHOULD provide an accessible name for each one."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: `aria-valuenow` (if focusable).
- Supported states and properties: `aria-disabled` (if focusable), `aria-orientation`, `aria-valuemax` (if focusable), `aria-valuemin` (if focusable), `aria-valuetext` (if focusable).
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-haspopup`, `aria-invalid` as deprecated on this role.
- Naming: name from author; not required. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- Static: no name needed; the value attributes do not apply.
- Focusable: `aria-valuenow` required; `aria-valuemin` (0) and `aria-valuemax` (100) when different; a name for each if there is more than one; APG adds `aria-controls` pointing at the primary pane.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `hr` (redundant, "NOT RECOMMENDED").
- **Allowed:** `button`, `img` with alt text, `input type=button`, `submit`, `reset`, `image`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** form fields, `a`, `li`, headings, landmark elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

Focusable only. APG, Window Splitter Pattern (provisional): arrows move the splitter; Enter collapses the primary pane or restores it; Home and End move to the smallest and largest sizes (optional); F6 cycles panes (optional).

## What an explicit role takes away

- On a `button`, the button role goes.
- Children are presentational.

## How it fails in code

- A focusable separator with no `aria-valuenow`: `wcag/sc-4.1.2-name-role-value.md`, likely.
- A splitter that can only be dragged: `wcag/sc-2.1.1-keyboard.md`, per that entry.
- A decorative divider given `role="separator"` where none was needed: advice.

## How to check

Static separators: an `hr` or nothing. Splitters: focusable, value exposed, arrow keys work. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
