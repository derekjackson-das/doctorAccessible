# Eval 047: custom switches that never expose on or off

Input: `input.html`. A "Notification settings" page with two custom switches built from `div` elements.

Intended defect: each switch has `role="switch"`, `tabindex="0"`, a name from `aria-labelledby`, and click, Space, and Enter handlers, but no `aria-checked`. WAI-ARIA 1.2 lists `aria-checked` as required for `switch`. The script toggles only a CSS class, so the on or off state is shown visually and never exposed.

Everything else is clean:
- The switches are focusable and operable by keyboard (Space and Enter) and pointer, and each has a name.
- `header`, `main`, `footer`, one `h1`, `lang`, `title`, a real submit `button`.
- Text is #1a1a1a on white. The switch border is #1a1a1a (off) or #0b4f9c (on) on white, well over 3:1. Focus is visible.

## Expected findings

1. **[Definite]** The switches' state is not exposed.
   - Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1, from `knowledge/wcag/sc-4.1.2-name-role-value.md` ("A custom checkbox, toggle, tab, or expandable region that changes state visually without exposing that state ... Definite when the state is user-settable").
   - Role entry: `knowledge/aria/roles/switch.md`, where `aria-checked` is the required state.
   - Where: both `div[role="switch"]`; the toggle function that changes only the class.
   - Acceptable fix directions: set `aria-checked` to `true` or `false` on load and update it on every toggle; or use a native `input type=checkbox` (optionally with `role="switch"`) or a `button`. As a direction, not a patch.

Reporting both switches in one finding, or as one finding with two locations, is correct. Two separate findings for the same defect is not.

## Also acceptable

- A note, marked advice, that a native checkbox or a `button` with `aria-pressed` would avoid the script.
- A note that the visible labels sit beside the switches and are associated through `aria-labelledby`, which is fine.
- A note that the form's values are not submitted, because `div` elements are not form controls: manual review or advice, not a WCAG finding.
- Manual-review notes that a criterion appears met and needs a browser check.

## Must not

- Report missing keyboard access or a missing name; both are present.
- Report the defect more than once, or under 1.3.1 as well as 4.1.2.
- Call it a failure of 1.4.11 or 1.4.1; the state is not shown by color alone (the knob moves).
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Say what a screen reader user would hear or experience.
- Rewrite the page.

## Automated scan

axe-core has a rule for required ARIA attributes (`aria-required-attr`); whether it fired is recorded in `RESULTS.md`. The finding does not depend on it.

## Pass condition

Finding 1 is present as definite under SC 4.1.2 (Level A), tier 1, once, and nothing from the Must not list appears.
