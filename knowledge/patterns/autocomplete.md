# Pattern: Autocomplete (combobox)

- Sources:
  - W3C, "Combobox Pattern", ARIA Authoring Practices Guide, https://www.w3.org/WAI/ARIA/apg/patterns/combobox/. Tier 2. A pattern, not a requirement.
  - Adrian Roselli, "Under-Engineered Comboboxen?", 29 June 2023, updated 19 August 2026, https://adrianroselli.com/2023/06/under-engineered-comboboxen.html. Tier 3.
  - Sarah Higley, "<select> your poison", 3 January 2020, https://sarahmhigley.com/writing/select-your-poison/, pointing to her two-part series on custom selects and comboboxes published at 24 Accessibility. Tier 3.
- Related entries: `coga/objective-6-do-not-rely-on-memory.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.5-identify-input-purpose.md`, `wcag/sc-3.3.7-redundant-entry.md`, `wcag/sc-4.1.3-status-messages.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the control is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer.

## The need it usually serves

A list too long to scan, such as forty departments or every country, and the person knows roughly what they want and would rather type a few letters than scroll. That is a real need. The pattern is overused when the list is short enough for a native `select`, and when a plain text field with validation would do.

## The simpler thing that often serves, and what is lost

A native `select`, grouped with `optgroup` if the list has a natural shape, or a text field with a `datalist` for suggestions. A native `select` with forty options is keyboard-operable, announced correctly, type-ahead searchable in most browsers, and reflows for free. What is lost by not building a custom combobox: filtering as you type with a styled list, and control over the look of the open list. What is gained: everything the 4.1.2 entry says native controls give by default, and nothing to test across every assistive technology pair. `coga/objective-6-do-not-rely-on-memory.md` favors recognition over recall either way, which is an argument for showing options, not for building them by hand.

## What doing it right requires

Native first: `datalist` is the HTML combobox. Roselli (2023, updated 2026) tested it and reports that it generally works with screen readers, with the caveats listed below; styling applies to the text field but not to the list itself. If the native control will not do, Higley's series (2020) is the tested reference for three shapes: a select-only combobox that replaces `select`, an editable combobox, and an editable multi-select combobox, each with the trade-offs explained.

The APG pattern's expectations, in our words: the combobox is a text field or a read-only field in the tab sequence; its popup, which may be a listbox, grid, tree, or dialog, is not in the tab sequence; Down Arrow moves into the popup, onto the first option or the one after an automatically selected suggestion; Escape closes the popup; the field reports whether the popup is open and which option is active. Many optional behaviors exist, and the one that shapes everything is whether the person can type.

What the APG does not say: how any of this performs in real assistive technology, which is where Roselli's and Higley's testing comes in.

## What practitioners found when they tested it

- **Roselli, 2023, updated 2026.** `datalist`: JAWS with Chrome announced the field as a combo, said a list was expanded, read each option's visible text with a count, but did not announce the chosen value on return to the field. NVDA with Firefox announced the field as a combo box with autocomplete and did announce the value on return. Narrator with Edge announced a combo edit with suggestions, with position and count in scan mode. VoiceOver on macOS with Safari announced a list box popup and read only the option's value when it differed from its visible text, so he advises keeping value and text identical or omitting one. Firefox on Android did not support `datalist` at the time despite the support tables saying it did, so TalkBack could do nothing with it. He found the Windows build of Firefox the only browser to show option text while hiding the value, matching `select`.
- **Higley, 2020.** A year of testing custom selects and comboboxes led to three recommended implementations and an account of why the problem is hard; the full reasoning and the alternatives considered are in the series, with test code published for each variation.

## Criteria it touches

Name, role, expanded state, active option: `wcag/sc-4.1.2-name-role-value.md`. Keyboard operation and no trap in the popup: `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`. Visible label and the name containing it: `wcag/sc-3.3.2-labels-or-instructions.md`, `wcag/sc-2.5.3-label-in-name.md`. Autocomplete tokens where the field is about the person: `wcag/sc-1.3.5-identify-input-purpose.md`. Suggestion counts announced: `wcag/sc-4.1.3-status-messages.md`. Choosing an option must not change context: `wcag/sc-3.2.2-on-input.md`. Popup at 320 CSS pixels and under text spacing: `wcag/sc-1.4.10-reflow.md`, `wcag/sc-1.4.12-text-spacing.md`. Option targets: `wcag/sc-2.5.8-target-size-minimum.md`. Errors on a value not in the list: `wcag/sc-3.3.1-error-identification.md`, `wcag/sc-3.3.3-error-suggestion.md`.

## Manual tests it demands

- Keyboard: type two letters; press Down Arrow; record where focus goes. Arrow through; press Escape; record that the popup closes and focus stays in the field. Press Tab from an open popup; record what happens.
- Screen reader, each pair in the spec: record what is announced on focusing the field, on the popup opening, on each option, and on return to the field after choosing. Compare against Roselli's results.
- Mobile: record whether the native control or the custom popup works with the platform screen reader at all.
- 400% zoom: record whether the popup fits and scrolls.
- Enter a value not in the list; record the error.

## What consult should say

1. How long is the list, really? Under a few dozen, a native `select`. Grouped, `optgroup`.
2. Must the person be able to type? If yes, `datalist` first, with Roselli's caveats checked on the project's platforms.
3. If a custom combobox stays: Higley's tested shapes as the starting point, and every pair in the spec tested before launch.
