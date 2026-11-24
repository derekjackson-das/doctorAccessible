# Role: combobox

- Category: widget (composite).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "combobox role", https://www.w3.org/TR/wai-aria-1.2/#combobox. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `select`, `input`, and `button`, https://www.w3.org/TR/html-aria/#el-select
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows 3.5.116 (`select` rendered as a drop-down box) and 3.5.77 (`input` with a suggestions source), https://www.w3.org/TR/html-aam/#el-select-combobox
- Practice (tier 2): the ARIA Authoring Practices Guide "Combobox Pattern" is covered in `aria/patterns/autocomplete.md`.
- Reference (tier 3): MDN Web Docs, "ARIA: combobox role", last modified 16 July 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role
- WAI-ARIA 1.3 (Working Draft 4 June 2026): awareness only. The draft moves `aria-controls` from required to supported.
- Related entries: `aria/patterns/autocomplete.md`, `patterns/autocomplete.md`, `html/forms.md`, `aria/roles/listbox.md`, `aria/roles/option.md`, `aria/roles/textbox.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: how to build a combobox, the keys it promises, how it fails, and the manual tests are in `aria/patterns/autocomplete.md` and `patterns/autocomplete.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. A custom combobox where `select` or `datalist` would do is advice, never a finding on its own. `role="combobox"` on an element that already has the role is redundant and never a finding.

## What it is

A field with a popup that helps set its value. WAI-ARIA 1.2: "An input that controls another element, such as a listbox or grid, that can dynamically pop up to help the user set the value of the input."

## The native element

- A `select` shown as a drop-down box (HTML-AAM 3.5.116).
- An `input` of type text, search, tel, url, or email with a `list` attribute pointing at a `datalist` (HTML-AAM 3.5.77).

ARIA in HTML marks `role="combobox"` on both as "NOT RECOMMENDED". Their limits are in `patterns/autocomplete.md`.

## What the spec asks of authors

- "Authors MUST set aria-expanded to true on an element with role combobox when it is expanded and false when it is collapsed."
- "Authors MUST ensure the popup element associated with a combobox has a role of listbox, tree, grid, or dialog."
- "Authors MUST set aria-controls on a combobox element to a value that refers to the combobox popup element."
- "If the combobox popup element has a role other than listbox, authors MUST specify a value for aria-haspopup that corresponds to the role of its popup."
- Where the field autocompletes, authors MUST set `aria-autocomplete` to match the behavior.

**The older structures no longer conform.** WAI-ARIA 1.2: "a combobox following the ARIA 1.1 combobox specification will no longer conform with the ARIA specification." The 1.1 form was a non-focusable wrapper with the role, holding a text field and a popup; the 1.0 form used `aria-owns` where 1.2 uses `aria-controls`. In 1.2 the role goes on the field itself.

**Sources differ on `aria-controls`.** WAI-ARIA 1.2 requires it. MDN says the role requires only `aria-expanded`, and the 1.3 Working Draft makes `aria-controls` supported, not required. The Recommendation stands: set both, always (`aria/patterns/autocomplete.md`).

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none.
- Required states and properties: `aria-controls`, `aria-expanded`.
- Supported states and properties: `aria-activedescendant`, `aria-autocomplete`, `aria-errormessage`, `aria-haspopup` (default `listbox`), `aria-invalid`, `aria-readonly`, `aria-required`.
- Prohibited states and properties: none. No global attribute is marked deprecated on this role.
- Naming: name from author; **required**. On an `input`, a `label` element provides it.

**The whole component.** The field, its popup (`listbox`, `tree`, `grid`, or `dialog`), and the popup's items: `aria/patterns/autocomplete.md`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** a drop-down `select`, and a text-like `input` with `list` (redundant, "NOT RECOMMENDED").
- **Allowed:** `input type="text"` with no `list`; `button`; `input` of type `button`, `reset`, or `submit`; a form-associated custom element; and the elements that allow any role, such as `div`.
- **Not allowed:** `input type="search"` with no `list` (it takes `searchbox` only); a `select` with `multiple` or a `size` above 1 (it is a `listbox`); `a` with `href`; `ul`, `section`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- On an `input type="text"` the `textbox` role is replaced by `combobox`, which is the intended use; the element still takes text.
- On a `button` the button role is replaced; this is the select-only form (MDN).
- On a `div` nothing native is lost and nothing is gained: focus, the value, and every key are script's job.

## Where the detail lives

- Build, states, keyboard, `aria-activedescendant`, failures: `aria/patterns/autocomplete.md`. The native options and the manual tests: `patterns/autocomplete.md`.
- axe: `aria-required-attr` fires on a `combobox` with no `aria-expanded` and no `aria-controls` (mapped to 4.1.2; observed with axe-core 4.14.0 on 2026-11-23; `knowledge/axe-rules.md`). It cannot tell whether the popup is exposed or the keys work.
