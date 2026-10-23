# ARIA pattern: Accordion

- W3C patterns (tier 2): ARIA Authoring Practices Guide, "Accordion Pattern (Sections With Show/Hide Functionality)" and "Disclosure (Show/Hide) Pattern", no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/patterns/accordion/ and https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/ Patterns, not requirements: nothing in them is a conformance rule, and following them does not guarantee that assistive technology supports them.
- Normative (tier 1):
  - WAI-ARIA 1.2, `button` and `region` roles and the `aria-expanded` state, W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/. A `region` requires a name.
  - ARIA in HTML, W3C Recommendation 11 August 2026, https://www.w3.org/TR/html-aria/. A `summary` that belongs to its `details` takes no role, and its exposed role varies by browser and assistive technology. `h1` to `h6` may not take `role=button`.
- Practitioner testing (tier 3): the sources and their full results are in `patterns/accordion.md`: Adrian Roselli, "Disclosure Widgets", 20 May 2020, updated 28 January 2024, https://adrianroselli.com/2020/05/disclosure-widgets.html; Scott O'Hara, "The details and summary elements, again", 12 September 2022; Heydon Pickering, "Collapsible Sections", 26 October 2017. This entry adds Roselli's results for the ARIA button.
- Related entries: `patterns/accordion.md` (whether to use an accordion, the native element, the criteria, the manual tests), `aria/using-aria.md`, `aria/aria-in-html.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

The criteria in `patterns/accordion.md` decide whether code fails WCAG; report a failure once, under its criterion. Departing from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier. Leaving out `aria-controls`, or the optional `region` role, is never a finding on its own.

**Testing gap.** No listed source tests the ARIA button pattern within three years: Roselli's tests of it are from 2020. His one retest inside the window, iPadOS 17.3 on 28 January 2024, covers the native element only, and O'Hara's 2022 post is outside it and gives no versions. Test the ARIA build with the spec's screen readers.

## Native first

`details` with `summary` gives a disclosure with no script, and an accordion can be a series of them. The testing in `patterns/accordion.md` shows what is lost: inconsistent role announcements, and states missing in some pairings.

## Roles, states, and properties

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|
| Each header | heading (`h2`, `h3`, ... at the right level) | | Author | Contains only the button (APG) |
| Button inside the heading | `button` (native) | `aria-expanded="true"` or `"false"` | Script, on every toggle | The state is the whole point |
| Button | | `aria-controls` pointing at the panel | Author | Roselli calls support sparse; Pickering wrote in 2017 that only JAWS used it |
| Button | | `aria-disabled="true"` if the open panel cannot be closed | Script | Only for accordions that keep one panel open |
| Each panel | `region`, optional | `aria-labelledby` pointing at its button | Author | The APG warns against it when more than about six panels can be expanded at the same time |

## Naming

Each button's name is its text, which is also the section heading. A `region` panel is named by its button through `aria-labelledby` (`aria/accessible-name.md`).

## Keyboard

From the APG pattern, in our words: Enter or Space on a header toggles its panel; Tab and Shift+Tab move through the page as normal, through every header and any controls in open panels. No arrow keys are required. A native `button` gives Enter and Space for free.

## What testing found

ARIA-specific results only; the native `summary` results are in `patterns/accordion.md`.

- **The `button` with `aria-expanded` came through with role and state in four of Roselli's six 2020 pairings.** The two exceptions: NVDA 2019 with Firefox 76 announced the name and state but no role, and TalkBack with Firefox 68 on Android 10 announced the name and role but no state.
- **Do not put `aria-expanded` on a link** that navigates; Roselli's 1 February 2021 update says it confuses screen reader users in particular.

## How it fails in code

- `aria-expanded` written in the markup but never updated by the script, so the panel opens while the state still says collapsed: a state that changes visually without being exposed, `wcag/sc-4.1.2-name-role-value.md`, definite.
- A clickable `div` header with no role and no keyboard handling: definite under `wcag/sc-2.1.1-keyboard.md` and 4.1.2; that entry says how to report it once.
- `role="button"` put on the heading itself, instead of a button inside it: ARIA in HTML does not allow it, and the heading is lost from heading navigation (`patterns/accordion.md`). Report under 1.3.1 at that entry's confidence.
- `role="button"` added to a `summary`: ARIA in HTML allows no role there, and O'Hara found it drops the state in macOS Safari. A finding only if the state is then lost in a pairing the spec tests.
