# ARIA pattern: Autocomplete (combobox)

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Combobox Pattern", no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/patterns/combobox/ A pattern, not a requirement: nothing in it is a conformance rule, and following it does not guarantee that assistive technology supports it.
- Normative (tier 1): WAI-ARIA 1.2, `combobox`, `listbox`, and `option` roles and the `aria-activedescendant`, `aria-expanded`, `aria-controls`, `aria-autocomplete`, and `aria-selected` attributes, W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/#combobox. `aria-controls` and `aria-expanded` are required on a combobox.
  - ARIA in HTML, W3C Recommendation 11 August 2026, https://www.w3.org/TR/html-aria/. An `input type="text"` may take `role="combobox"`; a `ul` may take `listbox`; an `li` whose parent is no longer a list may take any role, such as `option`.
- Practitioner testing (tier 3): the native `datalist` results (Roselli, 2023, updated 2026) are in `patterns/autocomplete.md`. This entry adds:
  - Sarah Higley, "Aria-activedescendant is not focus", 16 October 2024. https://sarahmhigley.com/writing/activedescendant/ How NVDA, Narrator, JAWS, VoiceOver with Safari on macOS, and the mobile screen readers handle `aria-activedescendant`. She gives no method, versions, or test dates.
- Related entries: `patterns/autocomplete.md` (whether to build one, the native options, the criteria, the manual tests), `aria/using-aria.md`, `aria/accessible-name.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

The criteria in `patterns/autocomplete.md` decide whether code fails WCAG; report a failure once, under its criterion. Departing from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier. A custom combobox where `select` or `datalist` would do is advice, never a finding on its own (`aria/using-aria.md`).

**Testing gap.** Higley's 2024 post is within three years but describes behavior without versions or a test date. No listed source reports a dated, versioned test of an ARIA combobox with screen readers. Her tested combobox series is published on 24a11y.com, which is not on `knowledge/SOURCES.md`; it is not used here. Test with the spec's assistive technology.

## Native first

`select` for a fixed list, or an `input` with `datalist` for suggestions. Both, and their limits, are in `patterns/autocomplete.md`.

## Roles, states, and properties

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|
| The text field | `combobox` | named by its `label` | Author | DOM focus stays here the whole time |
| The text field | | `aria-expanded="true"` while the popup shows, `"false"` otherwise | Script | Defaults to false |
| The text field | | `aria-controls` pointing at the popup | Author | Required by WAI-ARIA 1.2; the APG says it is needed only while the popup shows. Following principle 13, set it always. ARIA 1.0 used `aria-owns`; the APG strongly recommends `aria-controls` |
| The text field | | `aria-activedescendant` pointing at the highlighted option, empty when none | Script, on every arrow key | How a screen reader learns which option is active |
| The text field | | `aria-autocomplete="list"`, `"both"`, or `"none"` | Author | Says how suggestions relate to what is typed |
| The popup | `listbox` (or `grid`, `tree`, `dialog`, with `aria-haspopup` to match) | | Author | `listbox` is the default |
| Each suggestion | `option` | `aria-selected="true"` on the highlighted option | Script | Selection follows the highlight in a combobox (APG) |

## Naming

The field is named by its `label` element, the native way (`aria/accessible-name.md`). Each option's name is its text. Keep any visible text and stored value the same, or one of them out of the option, as `patterns/autocomplete.md` explains from Roselli's `datalist` tests.

## Keyboard

From the APG pattern, in our words: the field is in the tab order and the popup is not. Down Arrow moves into the suggestions, and Up and Down move between them; Enter accepts the highlighted one; Escape closes the popup, and may clear the field. Typing stays in the field throughout. "Moving into the popup" means moving the highlight and `aria-activedescendant`, not DOM focus.

## What practitioners report (no versions or dates)

From Higley's 2024 post. She describes behavior without saying when or with which versions she saw it:

- **`aria-activedescendant` is not a second focus.** Keyboard events still go to the field; only a screen reader's virtual cursor treats the active option as focused.
- **Windows screen readers differ on mode switching.** NVDA and Narrator do not move the active descendant when their cursor moves, so switching between browse and forms mode can land somewhere unexpected; JAWS handles it.
- **Point it only at options.** If `aria-activedescendant` points at a button, NVDA switches to browse mode and the user can no longer type. Actions in the popup should also be marked up as options.
- **Mobile screen readers ignore it.** VoiceOver on iOS and TalkBack users swipe through the options without the active descendant changing. VoiceOver with Safari on macOS is unreliable with it.

## How it fails in code

- The highlighted option shown only by styling, with no `aria-activedescendant` and no `aria-selected`: the active option is a state that changes visually without being exposed, `wcag/sc-4.1.2-name-role-value.md`, definite.
- `aria-expanded` never set to true while the popup shows: the same 4.1.2 case, definite.
- Arrow keys that do nothing, so suggestions can only be clicked: `wcag/sc-2.1.1-keyboard.md`, definite.
- DOM focus moved into the list, so typing stops: advice against, from the APG; a finding only through the criterion its effect breaks.
- `aria-activedescendant` pointing at something that is not an option: advice against, from Higley; test it in NVDA.
- `role="combobox"` on a site-wide search field: Higley generally recommends against it, since a combobox suggests a choice from a list rather than free text, and a screen reader user looking for an edit field may miss it. Advice, not a finding.
