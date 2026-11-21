# Role: radio

- Category: widget.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "radio role", https://www.w3.org/TR/wai-aria-1.2/#radio. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `input type=radio`, `button`, `a` with `href`, `img`, and the `input` button types, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `input type=radio` (3.5.70), which sets `aria-checked`, `aria-setsize`, and `aria-posinset`, https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Radio Group Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/radio/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: radio role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radio_role
- Related entries: `aria/roles/radiogroup.md`, `html/forms.md`, `aria/roles/menuitemradio.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="radio"` on `input type=radio` is redundant, never a finding.

## What it is

One of a set of choices where only one can be chosen. WAI-ARIA 1.2: "A checkable input in a group of elements with the same role, only one of which can be checked at a time."

## The native element

`input type=radio` with a `label`, grouped by a shared `name` and usually by `fieldset` and `legend` (HTML-AAM; MDN). The browser handles the arrow keys and the single choice.

## When writing the role is justified

When native radios cannot be used. Never one radio alone: a radio only makes sense in its group.

## What the spec asks of authors

- "Authors SHOULD ensure that elements with role radio are explicitly grouped in order to indicate which ones affect the same value."
- "If it is not possible to make the radio buttons DOM children of the radiogroup, authors SHOULD use the aria-owns attribute on the radiogroup element to indicate the relationship to its children."
- ARIA in HTML: authors MUST NOT use `aria-checked` on `input type=radio`.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: none.
- Required states and properties: `aria-checked`.
- Supported states and properties: `aria-posinset`, `aria-setsize`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-errormessage`, `aria-haspopup`, `aria-invalid` as deprecated on this role.
- Naming: name from contents or author; **required**. Children are presentational: anything inside is read as plain text, so headings, lists, or controls inside it lose their roles.
- `aria-checked` takes `true` or `false`; `mixed` is not valid for a radio (MDN).

**The whole component.** A radio needs its group: a `radiogroup` (or a native radio group) that contains or owns it and has a name; exactly one radio checked at a time; and the arrow-key behavior below. A `role="radio"` outside a group is a broken component. See `aria/roles/radiogroup.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `input type=radio` (redundant, "NOT RECOMMENDED").
- **Allowed:** `button`, `a` with `href`, `img` with alt text, `input type=button`, `submit`, `reset`, `image`, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `input type=checkbox`, text inputs, `select`, `li`, headings, `label`, landmark elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Radio Group Pattern. Tab moves into the group, to the checked radio or, if none, the first; one tab stop for the whole group. Space checks the focused radio. Right and Down move to the next radio and check it, wrapping; Left and Up move to the previous one and check it, wrapping. Inside a toolbar the arrows move focus without checking, and Space (or Enter, optional) checks.

## What an explicit role takes away

- On a `button` or link, that role goes.
- Children are presentational.

## How it fails in code

- The role on a `div` or `span` with no `tabindex`, so the control cannot be reached by keyboard: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F42). Report once, as that entry says, not again under 4.1.2.
- Every radio in the tab order with no arrow-key handling, or the arrow keys missing: manual review under `wcag/sc-2.1.1-keyboard.md`; the group can still be operated with Tab and Space, but not as a radio group is expected to work.
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- Radios with no group around them, or a group with no name: `wcag/sc-1.3.1-info-and-relationships.md` or `wcag/sc-4.1.2-name-role-value.md`, at those entries' confidence.
- The state changes visually but the state attribute is missing or never updated: `wcag/sc-4.1.2-name-role-value.md`, definite when the user can set the state, per that entry.
- The role used where the native element would do: advice, never a finding on its own (`aria/using-aria.md`, rule 1).

## How to check

Find each set of `role="radio"`. Is there a named `radiogroup` around them? Is only one checked? Do the arrow keys move and check? In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
