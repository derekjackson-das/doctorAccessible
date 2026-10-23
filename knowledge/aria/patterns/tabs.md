# ARIA pattern: Tabs

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Tabs Pattern", no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/patterns/tabs/ A pattern, not a requirement: nothing in it is a conformance rule, and following it does not guarantee that assistive technology supports it.
- Normative (tier 1):
  - WAI-ARIA 1.2, `tablist`, `tab`, and `tabpanel` roles, W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/#tablist. A `tab` must be inside a `tablist` and takes its name from its content; a `tabpanel` requires a name; `aria-selected` defaults to false.
  - ARIA in HTML, W3C Recommendation 11 August 2026, https://www.w3.org/TR/html-aria/. A `button` may take `role=tab`; so may `h1` to `h6`, though the Using ARIA example puts the heading inside the tab instead (`aria/using-aria.md`, rule 2).
- Practitioner testing (tier 3): the sources and their full results are in `patterns/tabs.md`: Scott O'Hara (2 November 2018, updated 5 February 2019), Léonie Watson (29 May 2012), Heydon Pickering (5 October 2017). This entry adds:
  - Adrian Roselli, "CSS-only Widgets Are Inaccessible", 25 March 2023, tabs section added 19 June 2024. https://adrianroselli.com/2023/03/css-only-widgets-are-inaccessible.html A review, not a screen reader test: radio-button "tabs" without the tab roles.
- Related entries: `patterns/tabs.md` (whether to use tabs, the criteria, the manual tests, the screen reader results), `patterns/accordion.md`, `aria/using-aria.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

The criteria in `patterns/tabs.md` decide whether code fails WCAG; report a failure once, under its criterion. Departing from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier. Choosing automatic or manual activation, or leaving out the optional Home and End keys, is never a finding on its own.

**Testing gap.** The newest listed screen reader test of an ARIA tab widget is O'Hara's, from 2018 with a 2019 update, on NVDA 2018.3.2, JAWS 18 and 2018, and VoiceOver on macOS High Sierra. No listed source reports testing tabs with mobile screen readers, or with any screen reader in the last three years. a11ysupport.io renders its results with script and could not be read for this entry. Test with the spec's assistive technology.

## Native first

HTML has no tab element. The plainer alternatives, headings with in-page links or a set of disclosures, are in `patterns/tabs.md`. If the design must be tabs, the ARIA roles are what make it a tab widget for a screen reader. Roselli's 2024 note: "tabs" built from radio buttons and CSS, without the tab roles, are not exposed as tabs, and he would likely fail them under 4.1.2.

## Roles, states, and properties

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|
| Container of the tabs | `tablist` | `aria-labelledby` to a visible label, or `aria-label`; `aria-orientation="vertical"` if vertical | Author | Horizontal is the default |
| Each tab, usually a `button` | `tab` | `aria-selected="true"` on the active tab, `"false"` on the others | Script, on every change | Must be inside the `tablist` |
| Each tab | | `aria-controls` pointing at its panel | Author | |
| Each tab | | `tabindex="0"` on the active tab, `"-1"` on the others | Script | The roving tabindex; Tab lands on the active tab |
| Each panel | `tabpanel` | `aria-labelledby` pointing at its tab | Author | A name is required; `tabindex="0"` if nothing at the start of the panel is focusable |

The selected tab also needs a visible cue that is not color alone (`wcag/sc-1.4.1-use-of-color.md`).

## Naming

Each tab's name comes from its text. Each panel is named by its tab through `aria-labelledby`, and the tab list by its visible label or `aria-label` (`aria/accessible-name.md`).

## Keyboard

From the APG pattern, in our words:

- Tab moves into the tab list, onto the active tab, and Tab again leaves it, usually to the panel.
- Left and Right Arrow move between tabs, wrapping at the ends; Up and Down for a vertical list.
- Home and End, optional, go to the first and last tab.
- Enter or Space activates the focused tab, when tabs do not activate on focus. The APG recommends activation on focus when the panel appears without noticeable delay.

The roving tabindex depends on the arrow keys. With `tabindex="-1"` on the inactive tabs and no arrow-key handler, the inactive tabs cannot be reached by keyboard alone. (A screen reader's virtual cursor can still reach them, as O'Hara found in 2018, so a screen reader test can hide the defect.)

## What testing found

The screen reader results for ARIA tabs are in `patterns/tabs.md`: in 2018, JAWS and NVDA entered the tab list on the wrong tab from the virtual cursor (O'Hara), and in 2012 NVDA and JAWS had to switch to applications mode for the arrow keys to work (Watson). Nothing newer is on the list.

## How it fails in code

- Inactive tabs set to `tabindex="-1"` with no arrow-key handler, so they cannot be reached by keyboard: `wcag/sc-2.1.1-keyboard.md`, definite.
- `aria-selected` not updated when the active tab changes: a state that changes visually without being exposed, `wcag/sc-4.1.2-name-role-value.md`, definite.
- The selected tab shown only by background color: `wcag/sc-1.4.1-use-of-color.md`, likely.
- Radio buttons styled as tabs, with no `tab` and `tablist` roles: likely under 4.1.2, on Roselli's 2024 review; the 4.1.2 entry has no such case. In-page links styled as tabs are a different, plainer pattern (`patterns/tabs.md`) and not this finding.
