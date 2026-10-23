# ARIA pattern: Accordion

- W3C patterns (tier 2): ARIA Authoring Practices Guide, "Accordion Pattern (Sections With Show/Hide Functionality)" and "Disclosure (Show/Hide) Pattern", no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/patterns/accordion/ and https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/ Patterns, not requirements: nothing in them is a conformance rule, and following them does not guarantee that assistive technology supports them.
- Normative (tier 1): WAI-ARIA 1.2, `button` and `region` roles and the `aria-expanded` state, W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/. A `region` requires a name.
- Practitioner testing (tier 3):
  - Adrian Roselli, "Disclosure Widgets", 20 May 2020, updated 28 January 2024. https://adrianroselli.com/2020/05/disclosure-widgets.html Native `details`/`summary` against a `button` with `aria-expanded`, in JAWS 2019 with Chrome 81, NVDA 2019 with Firefox 76, VoiceOver on macOS 10.15.2 with Safari, TalkBack on Android 10 with Chrome 81 and Firefox 68, and VoiceOver on iPadOS 13.4, retested on iPadOS 16.5 (9 August 2023) and 17.3 (28 January 2024).
  - Scott O'Hara, "The details and summary elements, again", 12 September 2022. https://www.scottohara.me/blog/2022/09/12/details-summary.html How `summary` is exposed across screen readers and browsers (versions not given), and what `role="button"` on it breaks.
  - Heydon Pickering, "Collapsible Sections", Inclusive Components, 26 October 2017. https://inclusive-components.design/collapsible-sections/ Build guidance; notes `aria-controls` support.
- Related entries: `patterns/accordion.md` (whether to use an accordion, the criteria, the manual tests), `aria/using-aria.md`, `aria/aria-in-html.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

The criteria in `patterns/accordion.md` decide whether code fails WCAG; report a failure once, under its criterion. Departing from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier. Leaving out `aria-controls`, or the optional `region` role, is never a finding on its own.

**Testing gap.** Roselli's desktop and Android tests are from 2020; only his iPadOS retests (2023 and 2024) are within three years, and they cover the native element. O'Hara's 2022 post gives no versions. Test the ARIA build with the spec's desktop screen readers.

## Native first

A `details` element with a `summary` is a disclosure with no script: it toggles by keyboard and exposes its state in most pairings. An accordion can be a series of them. What is lost, from the testing below: `summary` is announced inconsistently ("button", "summary", "disclosure triangle"), TalkBack with Firefox skipped it in 2020, and VoiceOver on iPadOS has gone back and forth on its state. See `patterns/accordion.md`.

## Roles, states, and properties

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|
| Each header | heading (`h2`, `h3`, ... at the right level) | | Author | Contains only the button (APG) |
| Button inside the heading | `button` (native) | `aria-expanded="true"` or `"false"` | Script, on every toggle | The state is the whole point |
| Button | | `aria-controls` pointing at the panel | Author | Optional in effect: Roselli calls support sparse; Pickering found it worked only in JAWS in 2017 |
| Button | | `aria-disabled="true"` if the open panel cannot be closed | Script | Only for accordions that keep one panel open |
| Each panel | `region`, optional | `aria-labelledby` pointing at its button | Author | The APG warns against it with more than about six panels open at once |

## Naming

Each button's name is its text, which is also the section heading. A `region` panel is named by its button through `aria-labelledby` (`aria/accessible-name.md`).

## Keyboard

From the APG pattern, in our words: Enter or Space on a header toggles its panel; Tab and Shift+Tab move through the page as normal, through every header and any controls in open panels. No arrow keys are required. A native `button` gives Enter and Space for free.

## What testing found

- **A `button` with `aria-expanded` was announced as a button with its collapsed or expanded state** in every pairing Roselli tested in 2020 but one. With TalkBack and Firefox on Android 10, the button was announced without its state, and the native `summary` was skipped entirely when moving by controls.
- **`role="button"` on a `summary` drops its state** in macOS Safari, and stops a heading nested inside it from being exposed as a heading (O'Hara, 2022). ARIA in HTML lists the same case as a side effect to avoid.
- **`aria-controls` adds little.** Roselli calls assistive technology support sparse; Pickering found it worked only in JAWS in 2017. Put the panel straight after its button in the source, so a reader meets it next.
- **Do not put `aria-expanded` on a link** that navigates; Roselli's 2021 update says it confuses screen reader users in particular.

## How it fails in code

- `aria-expanded` written in the markup but never updated by the script, so the panel opens while the state still says collapsed: a state that changes visually without being exposed, `wcag/sc-4.1.2-name-role-value.md`, definite.
- A clickable `div` header with no role and no keyboard handling: 4.1.2 and 2.1.1; see those entries for how to report once.
- The heading role put on the button itself (`<button role="heading">`), or the button outside the heading: the heading is lost or the button is overridden (`aria/aria-in-html.md`); report under 1.3.1 or 4.1.2 by its effect.
- `role="button"` added to a `summary`: advice against, with O'Hara's finding; a finding only if the state is then lost in a pairing the spec tests.
