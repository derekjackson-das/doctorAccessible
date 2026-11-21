# Role: option

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "option role", https://www.w3.org/TR/wai-aria-1.2/#option. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `option`, `button`, `a` with `href`, `img`, `input type=checkbox`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `option` (3.5.99), which sets `aria-selected` from the element's selectedness, https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Listbox Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/listbox/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: option role", last modified 21 August 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/option_role
- Related entries: `aria/roles/listbox.md`, `aria/patterns/autocomplete.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.5.3-label-in-name.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

One choice in a listbox. WAI-ARIA 1.2: "A selectable item in a listbox."

## The native element

`option` in a `select` or `datalist` (HTML-AAM).

## When writing the role is justified

Only inside a `listbox` (or a `group` inside one).

## What the spec asks of authors

- "Authors MUST ensure elements with role option are contained in, or owned by, an element with the role listbox or group within a listbox."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: `group`, `listbox`.
- Required owned elements: none.
- Required states and properties: `aria-selected`.
- Supported states and properties: `aria-checked`, `aria-posinset`, `aria-setsize`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-haspopup`, `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; **required**. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- `aria-selected` is required by WAI-ARIA 1.2. APG and MDN: set it on options that can be selected, `true` or `false`, and leave it off options that cannot be; and in one listbox use `aria-selected` or `aria-checked`, not both.

**The whole component.** It must be contained in or owned by a `listbox`, or a `group` in one. On its own it is not an option. See `aria/roles/listbox.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `option` in a list of options (no other role allowed there).
- **Allowed:** `button`, `a` with `href`, `img` with alt text, `input type=checkbox`, `input type=button`, `submit`, `reset`, `image`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `li` inside a real list, headings, landmark elements, text inputs, `select`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

The listbox's keys (`aria/roles/listbox.md`). An option is not a tab stop of its own.

## What an explicit role takes away

- On an `a` with `href` or a `button`, that role goes; the option is read as one string, and any action it had is no longer announced.
- Children are presentational.

## How it fails in code

- An option with no `listbox` around it: invalid; `wcag/sc-4.1.2-name-role-value.md`, likely.
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- An `aria-label` that drops the option's visible text: `wcag/sc-2.5.3-label-in-name.md`, per that entry (MDN).

## How to check

Every `option` is inside a `listbox` in the accessibility tree; selection exposed. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
