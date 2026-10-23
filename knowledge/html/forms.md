# HTML: Forms

- Tier 1: HTML Living Standard, §4.10 Forms (§4.10.4 The label element, §4.10.15 The fieldset element, §4.10.16 The legend element, §4.10.7 The select element), accessed 2026-10-23. https://html.spec.whatwg.org/multipage/forms.html
- Tier 1: ARIA in HTML, W3C Recommendation 11 August 2026, rows for `input`, `select`, `textarea`, `label`, `fieldset`. https://www.w3.org/TR/html-aria/
- Tier 2: WAI Tutorials, "Labeling Controls" (updated 13 May 2024) and "Grouping Controls" (updated 27 March 2026), Forms Tutorial. https://www.w3.org/WAI/tutorials/forms/labels/ , https://www.w3.org/WAI/tutorials/forms/grouping/
- Related: `aria/accessible-name.md`, `content/error-messages.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-3.3.2-labels-or-instructions.md`, `wcag/sc-1.3.5-identify-input-purpose.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

This entry says how to build it. Whether code fails WCAG is decided by the `wcag/` entries named below; report a failure once, under its criterion, at that entry's confidence. Not using the native element is never a finding on its own.

## The native approach

- **Every control gets a `label`.** Explicitly, with `for` matching the control's `id`, or implicitly, with the control inside the `label`. Clicking the label then focuses or activates the control, a larger target for everyone (WAI tutorial).
- **A visually hidden label** where the purpose is obvious from the page, such as a search field next to a "Search" button: keep the `label` in the code and hide it with a visually-hidden class, not `display: none` (WAI tutorial).
- **Group related controls with `fieldset` and `legend`.** Radio buttons always; checkbox sets; repeated groups such as shipping and billing addresses. Keep the legend short, since some screen readers repeat it with every field (WAI tutorial).
- **Group long option lists with `optgroup`** inside `select` (WAI tutorial).
- **Use the right `input` type** (`email`, `tel`, `number`, `date`), which brings the right keyboard on phones, and `autocomplete` tokens for fields about the user (`wcag/sc-1.3.5-identify-input-purpose.md`).
- **Buttons label themselves** by their content; an `input type="submit"` by its `value` (WAI tutorial). See `html/buttons.md`.

## What the native approach satisfies by default

A labeled native control has a role, a name, and its state (checked, selected, value) exposed with no ARIA (`wcag/sc-4.1.2-name-role-value.md`). The label is programmatically associated (`wcag/sc-1.3.1-info-and-relationships.md`). Native controls are keyboard operable (`wcag/sc-2.1.1-keyboard.md`).

## Where people go wrong

- Text beside a field with no association: no name (`wcag/sc-4.1.2-name-role-value.md`, eval 001).
- `placeholder` as the only label: it disappears on input. `wcag/sc-4.1.2-name-role-value.md` grades it likely and cross-refers to `wcag/sc-3.3.2-labels-or-instructions.md` (`content/error-messages.md`, `aria/accessible-name.md`).
- `title` as the label: the WAI tutorial calls it less reliable and not recommended. Advice, not a finding.
- Radio buttons with no `fieldset`, so the question they answer is not exposed (`wcag/sc-1.3.1-info-and-relationships.md`).
- A layout `table` holding the form, which the HTML Standard calls non-conforming; with `th` or `caption` it is a 1.3.1 failure (`html/tables.md`).
- `aria-labelledby` pointing at a hint instead of the label: the hint replaces the label (`aria/accessible-name.md`, eval 027).

## When ARIA is genuinely needed

- `aria-describedby` for a format hint or an error message tied to its field.
- `aria-invalid` on a field in error, and `aria-required` only when `required` cannot be used (ARIA in HTML says not to set both).
- `role="group"` with `aria-labelledby` when a `fieldset` cannot be styled as needed (WAI tutorial).
- Custom selects and comboboxes: `aria/patterns/autocomplete.md`.
