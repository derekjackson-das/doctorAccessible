# ARIA pattern: Tabs

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Tabs Pattern", no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/patterns/tabs/ A pattern, not a requirement: nothing in it is a conformance rule, and following it does not guarantee that assistive technology supports it.
- Normative (tier 1): WAI-ARIA 1.2, `tablist`, `tab`, and `tabpanel` roles, W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/#tablist. A `tab` must be inside a `tablist` and takes its name from its content; a `tabpanel` requires a name; `aria-selected` defaults to false.
- Practitioner testing (tier 3):
  - Scott O'Hara, "Trouble Tabbing To Tabs and Cheeky Checking Checkboxes", 2 November 2018, updated 5 February 2019. https://www.scottohara.me/blog/2018/11/02/tabbing-into-tabs.html Several tab widgets and a reduced test case with NVDA 2018.3.2, JAWS 18 and 2018, and VoiceOver with Safari and Chrome on macOS High Sierra.
  - Léonie Watson, "Using tabbed interfaces with a screen reader", 29 May 2012. https://tink.uk/using-tabbed-interfaces-with-a-screen-reader/ How NVDA and JAWS users operate tabs; NVDA 2012.2 beta with Firefox 12.
  - Adrian Roselli, "CSS-only Widgets Are Inaccessible", 25 March 2023, tabs section added 19 June 2024. https://adrianroselli.com/2023/03/css-only-widgets-are-inaccessible.html A review, not a screen reader test: radio-button "tabs" without the tab roles.
  - Heydon Pickering, "Tabbed Interfaces", Inclusive Components, 5 October 2017. https://inclusive-components.design/tabbed-interfaces/ Build guidance; no named test.
- Related entries: `patterns/tabs.md` (whether to use tabs, the criteria, the manual tests), `patterns/accordion.md`, `aria/using-aria.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

The criteria in `patterns/tabs.md` decide whether code fails WCAG; report a failure once, under its criterion. Departing from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier. Choosing automatic or manual activation, or leaving out the optional Home and End keys, is never a finding on its own.

**Testing gap.** The newest listed screen reader test of tab widgets is O'Hara's, from 2018 with a 2019 update, on NVDA 2018.3.2, JAWS 18 and 2018, and VoiceOver on macOS High Sierra. No listed source reports testing tabs with mobile screen readers, or with any screen reader in the last three years. a11ysupport.io could not be read for this entry (the site refused the request). Test with the spec's assistive technology.

## Native first

HTML has no tab element. The usual native alternatives are headings with a table of contents of in-page links, or a set of `details` disclosures (`patterns/tabs.md`, `patterns/accordion.md`). If the design must be tabs, the ARIA roles are what make it a tab widget for a screen reader. Roselli's 2024 note is that "tabs" built from radio buttons and CSS, without the tab roles, are not exposed as tabs at all, and he would likely fail them under 4.1.2.

## Roles, states, and properties

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|
| Container of the tabs | `tablist` | `aria-labelledby` to a visible label, or `aria-label`; `aria-orientation="vertical"` if vertical | Author | Horizontal is the default |
| Each tab, usually a `button` | `tab` | `aria-selected="true"` on the active tab, `"false"` on the others | Script, on every change | Must be inside the `tablist` |
| Each tab | | `aria-controls` pointing at its panel | Author | |
| Each tab | | `tabindex="0"` on the active tab, `"-1"` on the others | Script | The roving tabindex; the APG has Tab land on the active tab |
| Each panel | `tabpanel` | `aria-labelledby` pointing at its tab | Author | A name is required; `tabindex="0"` if the panel has nothing focusable at the start |

## Naming

Each tab's name comes from its text. Each panel is named by its tab through `aria-labelledby`, and the tab list by its visible label or `aria-label` (`aria/accessible-name.md`).

## Keyboard

From the APG pattern, in our words:

- Tab moves into the tab list, onto the active tab, and Tab again leaves it, usually to the panel.
- Left and Right Arrow move between tabs, wrapping at the ends; Up and Down for a vertical list.
- Home and End, optional, go to the first and last tab.
- Enter or Space activates the focused tab, when tabs do not activate on focus. The APG recommends activation on focus only when the panel appears without noticeable delay.

The roving tabindex depends on the arrow keys. With `tabindex="-1"` on the inactive tabs and no arrow-key handler, the inactive tabs cannot be reached by keyboard at all.

## What testing found

- **Screen reader virtual cursors bypass the roving tabindex.** In O'Hara's 2018 tests, a JAWS or NVDA user who reached the tab list with the virtual cursor and then pressed Tab landed on the first tab, which had `tabindex="-1"`, instead of the active one. Coming back up from the panel, they landed on the last tab. VoiceOver on macOS did not show this. He filed bugs with both, and wrote a script workaround that fixed NVDA's announcement but left JAWS silent.
- **Windows screen readers must switch modes** for the arrow keys to reach the widget. Watson's 2012 description: NVDA and JAWS have to enter applications mode, passing keys to the browser, and moving onto a tab with the Tab key is what triggers it. The roles also make them announce each tab as a tab.

## How it fails in code

- Inactive tabs set to `tabindex="-1"` with no arrow-key handler, so only a mouse can reach them: `wcag/sc-2.1.1-keyboard.md`, definite.
- `aria-selected` not updated when the active tab changes: a state that changes visually without being exposed, `wcag/sc-4.1.2-name-role-value.md`, definite.
- Tab-like controls with no `tab` and `tablist` roles, styled to look like tabs: 4.1.2 (Roselli, 2024). Report once.
