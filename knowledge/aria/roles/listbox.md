# Role: listbox

- Category: widget (composite).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "listbox role", https://www.w3.org/TR/wai-aria-1.2/#listbox. ARIA in HTML, W3C Recommendation 11 August 2026, the rows for `select`, `ul`, `ol`, `menu`, and form-associated custom elements, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row for `select` rendered as a list box (3.5.115); a drop-down `select` maps to `combobox` (3.5.116), https://www.w3.org/TR/html-aam/
- Practice (tier 2): ARIA Authoring Practices Guide, "Listbox Pattern" (no date on the page), https://www.w3.org/WAI/ARIA/apg/patterns/listbox/. A pattern, not a requirement.
- Reference (tier 3): MDN Web Docs, "ARIA: listbox role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role
- Related entries: `aria/roles/option.md`, `aria/patterns/autocomplete.md`, `html/forms.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-21 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full by fetch.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`).

## What it is

A list of options the user selects one or more of. WAI-ARIA 1.2: "A widget that allows the user to select one or more items from a list of choices."

## The native element

`select` with `multiple` or a `size` greater than one (HTML-AAM 3.5.115). A drop-down `select` is a `combobox` instead. MDN also suggests radios (one choice) or checkboxes (several) as native alternatives.

## When writing the role is justified

When `select` cannot do the job, or inside a combobox (`aria/patterns/autocomplete.md`). APG warns: options are read as one flat string, so nothing inside an option (a heading, a link, a button) survives; a list of links or buttons is not a listbox, and a grid is the pattern for interactive content.

## What the spec asks of authors

- "To be keyboard accessible, authors SHOULD manage focus of option descendants for all instances of this role, as described in Managing Focus."

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: `group → option`, `option`.
- Required states and properties: none.
- Supported states and properties: `aria-errormessage`, `aria-expanded`, `aria-invalid`, `aria-multiselectable`, `aria-readonly`, `aria-required`.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-haspopup` as deprecated on this role.
- Naming: name from author; **required**.
- `aria-multiselectable="true"` for multiple selection.
- Selection is marked on the options with `aria-selected` or `aria-checked`, never both in one listbox (APG).

**The whole component.** It must own `option` elements, directly or in a named `group`; needs a name unless it is part of a combobox; and needs the keyboard below. Focus is on the listbox with `aria-activedescendant`, or roved across the options.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `select` rendered as a list box.
- **Allowed:** `ul`, `ol`, `menu`, form-associated custom elements, and the elements that allow any role, such as `div`, `span`, `p`, and `table`.
- **Not allowed:** `li`, headings, `nav` and the other landmark elements, `button`, `a`, text inputs (use `combobox` there).

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## Keyboard it promises

APG, Listbox Pattern. On focus: the selected option, or the first. Down and Up move; in single-select, selection may follow focus (optional, and APG warns it can hurt). Home and End (optional; strongly recommended over five options). Type-ahead recommended, especially over seven options. Multi-select: Space toggles; Shift+arrows extend; Shift+Space selects a range; Control+A selects all (all optional), or the alternative model with Control.

## What an explicit role takes away

- On a `ul` or `ol`, the list goes; the `li` elements must take `option`.
- On a `select`, nothing is gained: it is already a listbox or combobox.

## How it fails in code

- The role on a `div` or `span` with no `tabindex`, so the control cannot be reached by keyboard: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F42). Report once, as that entry says, not again under 4.1.2.
- The role and `tabindex="0"` but no key handler, so the listbox can be focused but not operated: `wcag/sc-2.1.1-keyboard.md`, definite per that entry (F54).
- No accessible name: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry for a control with no name.
- Options with no `aria-selected` (or `aria-checked`) for the selection: `wcag/sc-4.1.2-name-role-value.md`, definite per that entry.
- Links or buttons inside options: their roles are lost. `wcag/sc-4.1.2-name-role-value.md`, likely; use a list of links or a grid.
- The role used where the native element would do: advice, never a finding on its own (`aria/using-aria.md`, rule 1).

## How to check

For each `role="listbox"`: it owns options, has a name, the arrow keys move, selection is exposed, and nothing interactive sits inside an option. In the browser's accessibility tree, confirm the role, the name, and the state are exposed and change as the control is used. Then operate it with the keyboard alone, using the keys above. axe checks the required attributes (`aria-required-attr`, mapped to 4.1.2), required parents and children (`aria-required-parent`, `aria-required-children`, mapped to 1.3.1), and allowed roles (`aria-allowed-role`, best practice), per `knowledge/axe-rules.md`. It cannot tell whether the keys work.
