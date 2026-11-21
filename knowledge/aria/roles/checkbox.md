# Role: checkbox

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "checkbox role", https://www.w3.org/TR/wai-aria-1.2/#checkbox. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `input type=checkbox`, `button`, `a` with `href`, `img`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `input type=checkbox` (3.5.59), which sets `aria-checked` from the element's state, including `mixed` for indeterminate, https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Checkbox Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: checkbox role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/checkbox_role
- Related entries: `html/forms.md`, `aria/roles/switch.md`, `aria/roles/menuitemcheckbox.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="checkbox"` on `input type=checkbox` is redundant, never a finding.

## What it is

A control that is checked, unchecked, or partly checked. WAI-ARIA 1.2: "A checkable input that has three possible values: true, false, or mixed."

## The native element

`input type=checkbox` with a `label` (HTML-AAM). It exposes the state, including the indeterminate state, with no script.

## When writing the role is justified

When a native checkbox cannot be used or styled. MDN calls using the native element the first rule of ARIA.

## What the spec asks of authors

- WAI-ARIA 1.2 places no author requirement on this role beyond its characteristics, below.
- ARIA in HTML: authors MUST NOT use `aria-checked` on `input type=checkbox`; the native `checked` state wins.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: `aria-checked`.
- Supported states and properties: `aria-errormessage`, `aria-expanded`, `aria-invalid`, `aria-readonly`, `aria-required`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-haspopup` as deprecated on this role.
- Naming: name from contents or author; **required**. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- `aria-checked` takes `true`, `false`, or `mixed`. APG uses `mixed` for a parent checkbox over a group that is partly checked.

**The whole component.** On its own a checkbox is complete. A set of related checkboxes is grouped with `fieldset` and `legend`, or `role="group"` with a name (APG).

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `input type=checkbox` (redundant, "NOT RECOMMENDED").
- **Allowed:** `button`, `a` with `href`, `img` with alt text, `input type=button`, `submit`, `reset`, `image`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `input type=radio`, text inputs, `select`, `li`, headings, `label`, landmark elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Checkbox Pattern: Space toggles it. That is the only key; Enter is not listed. Clicking its label should toggle it too (MDN).

## What an explicit role takes away

- On a `button`, the button role goes; the element must now expose `aria-checked` instead of `aria-pressed`.
- Children are presentational.

## How it fails in code

- The role on a `div` or `span` with no `tabindex`, so the control cannot be reached by keyboard: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F42). Report once, as that entry says, not again under 4.1.2.
- The role and `tabindex="0"` but no key handler, so the control can be focused but not operated: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F54).
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- No `aria-checked`, or `aria-checked` not updated when the box is toggled: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry.
- A group of checkboxes with a visible group label that is not associated: `wcag/sc-1.3.1-info-and-relationships.md`, at that entry's confidence.
- The role used where the native element would do: advice, never a finding on its own (`aria/using-aria.md`, rule 1).

## How to check

For each `role="checkbox"`: focusable, Space toggles, `aria-checked` changes, it has a name, and clicking the label toggles it. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
