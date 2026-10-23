# Eval 031: combobox whose highlighted option is never exposed

Input: `input.html`. A "Find a department" form with a type-ahead field.

Intended defect: the field is an `input` with `role="combobox"`, named by its `label`, with `aria-autocomplete="list"`, `aria-controls`, and `aria-expanded` kept in step with the popup. Up and Down Arrow move a highlight through the suggestions, and Enter accepts one. But the highlight is only a CSS class. The script never sets `aria-activedescendant` on the field, or `aria-selected` on the option. DOM focus stays in the field, so a screen reader is never told which suggestion is active.

Everything else is clean: label, keyboard support (arrows, Enter, Escape), the listbox and options roles, `aria-expanded`, visible focus on the field, the highlight shown by fill, bold, and an inner outline (not color alone), contrast (#1a1a1a on white; white on #005a9c, about 7.1:1), language, title, one `h1`, `main`.

## Expected findings

1. **[Definite]** The highlighted suggestion is not exposed to assistive technology: no `aria-activedescendant` on the field, no `aria-selected` on the option.
   - Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1, from `knowledge/wcag/sc-4.1.2-name-role-value.md` (a custom control that "changes state visually without exposing that state (... `aria-selected` ...)", definite when user-settable).
   - ARIA entry: `knowledge/aria/patterns/autocomplete.md`, which lists this case.
   - Where: `highlight()` in the script; `input#dept` and the `[role="option"]` elements.
   - Acceptable fix directions: in `highlight()`, set `aria-activedescendant` on the input to the active option's id (and clear it when there is none), and set `aria-selected="true"` on that option; or use `datalist`. As a direction, not a patch.

## Also acceptable

- A manual-review note, from the entry, that mobile screen readers ignore `aria-activedescendant`, so the result must be tested there.
- A note, marked advice, that a native `datalist` or `select` may serve.
- A note that axe is not expected to catch this.

## Must not

- Report the field's name, role, or `aria-expanded`; they are correct.
- Report keyboard operation; arrows, Enter, and Escape work.
- Report a missing count of results under 4.1.3; the page shows no status message.
- Report the highlight as color alone; it is also bold and outlined.
- Report `autocomplete="off"` under 1.3.5; a department is not information about the user.
- Report the defect twice, under 4.1.2 and again under 1.3.1 or 2.1.1.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe checks that the roles and attributes present are valid, and they are. It does not check that `aria-activedescendant` follows the visible highlight, so it is not expected to report this defect. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as definite under SC 4.1.2 (Level A), tier 1, and nothing from the Must not list appears.
