# Eval 029: tabs with a roving tabindex and no arrow keys

Input: `input.html`. A "Course formats" page with three tabs: In person, Online, Hybrid.

Intended defect: the tabs use the APG's roving tabindex. The active tab has `tabindex="0"` and the others have `tabindex="-1"`, but the script handles only `click`. There is no arrow-key handler, so a keyboard user can reach only the active tab. The Online and Hybrid tabs, and their panels, cannot be reached or chosen without a mouse.

Everything else is clean: `tablist` with a name, `tab` roles inside it, `aria-selected` and `tabindex` updated on every change, `aria-controls`, each `tabpanel` named by its tab, panels hidden with `hidden`, visible focus, language, title, one `h1`, `main`. Contrast: #005a9c on white and white on #005a9c are both about 7.1:1. The selected tab is shown by fill, bold text, and an underline, not by color alone.

## Expected findings

1. **[Definite]** The inactive tabs cannot be reached or activated by keyboard.
   - Criterion: WCAG 2.2 SC 2.1.1 Keyboard (Level A), tier 1, from `knowledge/wcag/sc-2.1.1-keyboard.md` ("controls taken out of the tab order with `tabindex="-1"` and given no other keyboard route", definite).
   - ARIA entry: `knowledge/aria/patterns/tabs.md`, which lists "inactive tabs set to `tabindex="-1"` with no arrow-key handler" as definite under 2.1.1.
   - Where: the `tab` buttons `#tab-online` and `#tab-hybrid`; the script, which adds only `click` listeners.
   - Acceptable fix directions: add Left and Right Arrow handling that moves focus between tabs (and, optionally, Home and End), per the APG; or leave all tabs at `tabindex="0"`, so Tab reaches each. As a direction, not a patch.

## Also acceptable

- A practice note, marked as the APG pattern and not a requirement, on automatic versus manual activation.
- A manual-review note, from the tabs entry, that JAWS and NVDA virtual cursors may land on an inactive tab (O'Hara, 2018), with the testing gap named.
- A note that axe is not expected to catch this.

## Must not

- Report missing ARIA roles, names, or states; they are present and updated.
- Report missing Home and End keys as a failure; they are optional in the APG.
- Report the defect twice, under 2.1.1 and again under 4.1.2 or 2.4.3.
- Report contrast, use of color for the selected tab (it is also bold and underlined), focus style, headings, landmarks, or language.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe checks the roles and attributes, which are valid. It does not test key handling, so it is not expected to report this defect. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as definite under SC 2.1.1 (Level A), tier 1, and nothing from the Must not list appears.
