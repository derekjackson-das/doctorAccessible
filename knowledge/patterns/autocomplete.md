# Pattern: Autocomplete (combobox)

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Combobox Pattern", accessed 2026-10-22 (the page shows no date). https://www.w3.org/WAI/ARIA/apg/patterns/combobox/ A pattern, not a requirement.
- W3C tutorial: none.
- Practitioner testing (tier 3, on `knowledge/SOURCES.md`):
  - Adrian Roselli, "Under-Engineered Comboboxen?", 29 June 2023, updated 19 August 2026. https://adrianroselli.com/2023/06/under-engineered-comboboxen.html Tested the native `datalist` element with JAWS and Chrome, NVDA and Firefox, Narrator and Edge, VoiceOver and Safari on macOS, and TalkBack with Firefox on Android.
  - Sarah Higley, "<select> your poison", 3 January 2020. https://sarahmhigley.com/writing/select-your-poison/ Points to her two-part series on custom selects and comboboxes, with tested code for each variation and three recommended implementations.
- Related entries: `ux/...` (no entry yet for this pattern), `aria/patterns/autocomplete.md` (the roles, states, naming, keyboard, and the ARIA test results), `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.5-identify-input-purpose.md`, `wcag/sc-4.1.3-status-messages.md`, `coga/objective-6-do-not-rely-on-memory.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

The criteria listed below decide whether code fails WCAG; report a failure once, under its criterion. Everything else here is advice. Using this pattern, or not using the simpler alternative, is never a finding on its own. A departure from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier.

## The need

A list too long to scan, such as forty departments or every country, and the person knows roughly what they want and would rather type a few letters than scroll. That is a real need. The pattern is overused when the list is short enough for a native `select`, and when a plain text field with validation would do. `coga/objective-6-do-not-rely-on-memory.md` favors recognition over recall either way, which is an argument for showing options, not for building them by hand.

## The simpler alternative and its cost

A native `select`, grouped with `optgroup` if the list has a natural shape, or a text field with a `datalist` for suggestions. A native `select` with forty options is keyboard-operable, announced correctly, type-ahead searchable in most browsers, and reflows for free. What is lost: filtering as you type with a styled list, and control over the look of the open list. What is gained: everything `wcag/sc-4.1.2-name-role-value.md` says native controls give by default, and nothing to test across every assistive technology pair.

## What doing it right requires

Native first: `datalist` is the HTML combobox. Roselli (2023, updated 2026) found it generally works with screen readers, with these caveats from his tests: JAWS with Chrome announced the field as a combo, said a list was expanded, read each option's visible text with a count, but did not announce the chosen value on return to the field; NVDA with Firefox announced the value on return; Narrator with Edge gave position and count in scan mode; VoiceOver on macOS with Safari read only an option's value when it differed from its visible text, so keep value and text identical or omit one; Firefox on Android did not support `datalist` at the time despite the support tables saying it did, so TalkBack could do nothing with it. Styling applies to the text field but not to the list.

If the native control will not do, Higley's 2020 post points to her two-part series on custom selects and comboboxes, covering a select-only combobox, an editable combobox, and an editable multi-select combobox. The series is published on 24a11y.com (2019), which is not on `knowledge/SOURCES.md` and is more than three years old, so its results are not used here. The ARIA for the pattern is in `aria/patterns/autocomplete.md`.

The Authoring Practices' roles, states, and keys are in `aria/patterns/autocomplete.md`. Whether the person can type is the choice that shapes everything. The guide does not say how any of this performs in real assistive technology; that is what the sources above supply.

## Criteria it touches

| SC | Title | Level | Entry | Why it comes up |
|---|---|---|---|---|
| 4.1.2 | Name, Role, Value | A | `wcag/sc-4.1.2-name-role-value.md` | Name, role, expanded state, and active option on a custom combobox |
| 2.1.1 | Keyboard | A | `wcag/sc-2.1.1-keyboard.md` | Arrow keys into and through the popup |
| 2.1.2 | No Keyboard Trap | A | `wcag/sc-2.1.2-no-keyboard-trap.md` | Leaving an open popup |
| 3.3.2 | Labels or Instructions | A | `wcag/sc-3.3.2-labels-or-instructions.md` | A visible label for the field |
| 2.5.3 | Label in Name | A | `wcag/sc-2.5.3-label-in-name.md` | If an `aria-label` replaces the visible text |
| 1.3.5 | Identify Input Purpose | AA | `wcag/sc-1.3.5-identify-input-purpose.md` | Autocomplete tokens when the field is about the person |
| 4.1.3 | Status Messages | AA | `wcag/sc-4.1.3-status-messages.md` | Announcing how many suggestions match |
| 3.2.2 | On Input | A | `wcag/sc-3.2.2-on-input.md` | Choosing an option must not change context |
| 1.4.10 | Reflow | AA | `wcag/sc-1.4.10-reflow.md` | The popup at 320 CSS pixels |
| 2.5.8 | Target Size (Minimum) | AA | `wcag/sc-2.5.8-target-size-minimum.md` | Option targets in a custom list |
| 3.3.1 | Error Identification | A | `wcag/sc-3.3.1-error-identification.md` | A value not in the list |
| 3.3.3 | Error Suggestion | AA | `wcag/sc-3.3.3-error-suggestion.md` | Suggesting the nearest match |

## Manual tests

- Keyboard: type two letters; press Down Arrow; record where focus goes. Arrow through; press Escape; record that the popup closes and focus stays in the field. Press Tab from an open popup; record what happens.
- Screen reader, each pair in the spec: record what is announced on focusing the field, on the popup opening, on each option, and on return to the field after choosing. Compare against Roselli's results above.
- Mobile: record whether the native control or the custom popup works with the platform screen reader at all; Firefox on Android is the known gap.
- 400% zoom: record whether the popup fits and scrolls.
- Enter a value not in the list; record the error text.
