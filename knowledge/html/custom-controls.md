# HTML: Custom controls, and the native element to try first

- Tier 1: HTML Living Standard, §4.10 Forms (`input` types, `select`, `datalist`) and §4.11 Interactive elements (§4.11.1 The details element, §4.11.4 The dialog element), accessed 2026-10-23. https://html.spec.whatwg.org/multipage/input.html , https://html.spec.whatwg.org/multipage/interactive-elements.html
- Tier 1: ARIA in HTML, W3C Recommendation 11 August 2026. https://www.w3.org/TR/html-aria/
- Tier 2: W3C, "Using ARIA", Discontinued Draft 24 February 2026, rule 1 (`aria/using-aria.md`); WAI Tutorials, Forms Tutorial (updated 27 March 2026). https://www.w3.org/WAI/tutorials/forms/
- Related: every `aria/patterns/` entry, `patterns/` (whether to build the control at all), `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

This entry is a map from a control people build by hand to the native element that may already do it. Choosing a custom control is advice, never a finding on its own (`aria/using-aria.md`). The failures come from what the custom control leaves out, under the `wcag/` entries named below.

## Native first

Using ARIA's first rule: if a native element has the meaning and behavior needed, use it. Its exceptions: the native feature is not implemented or not accessibly supported, it cannot be styled as the design needs, or HTML has no such feature.

| Built by hand | Try first | Notes | If ARIA is still needed |
|---|---|---|---|
| Clickable `div` | `button` | `html/buttons.md` | `aria/using-aria.md` |
| Clickable `div` that navigates | `a href` | `html/links.md` | |
| Custom checkbox or toggle switch | `input type="checkbox"` | Style the native input; ARIA in HTML lets `input type="checkbox"` take `role="switch"`, and forbids `aria-checked` on it | |
| Custom radio group | `input type="radio"` in a `fieldset` | `html/forms.md` | |
| Custom select | `select`, with `optgroup` | `patterns/autocomplete.md` | `aria/patterns/autocomplete.md` |
| Type-ahead suggestions | `input` with `datalist` | Roselli's caveats in `patterns/autocomplete.md` | `aria/patterns/autocomplete.md` |
| Show/hide section, accordion | `details` and `summary` | The HTML Standard: a disclosure widget; caveats in `patterns/accordion.md` | `aria/patterns/accordion.md` |
| Modal | `dialog` with `showModal()` | `html/dialogs.md` | `aria/patterns/modal-dialog.md` |
| Date picker | `input type="text"` with a stated format, or `type="date"` | `patterns/date-picker.md` | `aria/patterns/date-picker.md` |
| Slider | `input type="range"` | | |
| Progress or meter | `progress`, `meter` | | |
| Tabs, tooltip, carousel, feed | No native element | Consider whether to build it (`patterns/`) | `aria/patterns/tabs.md`, `tooltip.md`, `carousel.md`, `infinite-scroll.md` |

## What the native element gives by default

Role, name, state, keyboard behavior, and focus, maintained by the browser instead of by the team (`wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`).

## Where people go wrong

- Rebuilding a native control in `div`s for its look, then missing the role, the state, or the keys.
- Restyling a native control in a way that breaks it: removing the focus ring, hiding the input so it cannot be focused, or giving `summary` a role (`patterns/accordion.md`).
- ARIA added to a native element that already has it, such as `role="button"` on `button` (`aria/aria-in-html.md`). Not a finding.

## When ARIA is genuinely needed

When the table's last column names an entry: the control has no native equivalent, or the native one fails a need the spec records. Then the matching `aria/patterns/` entry, `aria/using-aria.md`, and `aria/accessible-name.md` apply.
