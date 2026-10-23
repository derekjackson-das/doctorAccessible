# Pattern: Tabs

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Tabs Pattern", accessed 2026-10-22 (the page shows no date). https://www.w3.org/WAI/ARIA/apg/patterns/tabs/ A pattern, not a requirement.
- W3C tutorial: none.
- Practitioner sources (tier 3, on `knowledge/SOURCES.md`):
  - Scott O'Hara, "Trouble Tabbing To Tabs and Cheeky Checking Checkboxes", 2 November 2018, updated 5 February 2019. https://www.scottohara.me/blog/2018/11/02/tabbing-into-tabs.html Tested several tab widgets and a reduced test case with NVDA 2018.3.2, JAWS 18 and 2018, and VoiceOver with Safari and Chrome on macOS High Sierra.
  - Léonie Watson, "Using tabbed interfaces with a screen reader", 29 May 2012. https://tink.uk/using-tabbed-interfaces-with-a-screen-reader/ How NVDA and JAWS users operate tabs; demonstrated with NVDA 2012.2 beta and Firefox 12.
  - Heydon Pickering, "Tabbed Interfaces", Inclusive Components, 5 October 2017. https://inclusive-components.design/tabbed-interfaces/ Build guidance and the case for a table of contents instead; no named assistive technology test.
- Related entries: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `patterns/accordion.md`; `aria/patterns/tabs.md` (the roles, states, naming, keyboard, and the ARIA test results).
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

The criteria listed below decide whether code fails WCAG; report a failure once, under its criterion. Everything else here is advice. Using this pattern, or not using the simpler alternative, is never a finding on its own. A departure from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier.

**Testing gap.** The two tested sources date from 2012 and 2018. Nothing on the list reports a current test of tabs with desktop or mobile screen readers, voice control, or magnification. Treat the screen reader behavior below as history to check, not as current fact. a11ysupport.io, also on the list, renders its results with script and could not be read for this entry.

## The need

Switching between a few related sections in the same space, such as product details, specifications, and reviews, without scrolling between them.

## The simpler alternative and its cost

- **Sections with headings and a table of contents.** Pickering describes a basic tab interface as a table of contents of same-page links pointing to sections. With all sections on the page, everything can be read in order, searched, and printed, and links work without script. The cost: a longer page, and the visual effect of one panel at a time is lost. Pickering warns against styling such a list of links to look like tabs, because tabs promise keyboard behavior that links do not have.
- **Separate pages.** When each "tab" is really a different view, use ordinary links to separate pages or views, not tab semantics (Pickering). The cost: a page load or route change between views.
- **An accordion at every screen width** (`patterns/accordion.md`), which Pickering recommends when there are many tabs or an unknown number. Each heading sits with its content, and a single column fits any screen. The cost: only one section shows at a time without the side-by-side switching tabs give, and an accordion carries its own support problems. Pickering advises against switching tabs into an accordion only on narrow screens: the two are built and operated differently, and the hybrid is not worth its complexity.

## What doing it right requires

From the Authoring Practices, unless noted:
- **Roles, names, and states** are in `aria/patterns/tabs.md`.
- **One tab stop for the list.** Only the active tab is in the tab order; Left and Right Arrow move between tabs; Tab moves on into the panel. Home and End are optional. Pickering explains the reason: otherwise keyboard users step through every tab to reach the panel's content.
- **Activate on focus only when it is instant.** Automatic activation is recommended only when panels show with no noticeable delay; otherwise tabs activate on Enter or Space.
- **Down Arrow: the sources differ.** The Authoring Practices say a horizontal tab list should not respond to Down or Up Arrow, so those keys keep scrolling the page. Pickering's tabs use Down Arrow to move focus into the panel, so screen reader users do not land on the next tab. Following the Authoring Practices is the safer default; if Down Arrow is used, test that page scrolling still works.
- **Screen readers have to switch modes.** Watson explained in 2012 that NVDA and JAWS pass arrow keys to the page only once they switch to applications mode, which happens when the person tabs onto a tab. Users who do not know this may not find the arrow keys.
- **Entering the list from reading mode went wrong in 2018.** O'Hara found that in NVDA and JAWS, pressing Tab from the virtual cursor into a tab list focused the first tab, or the last one going backwards, rather than the active tab. VoiceOver on macOS behaved correctly. He filed bugs and offered a workaround script, which fixed NVDA but left JAWS focusing the right tab silently. Whether the bugs are fixed is not recorded on the list; check it in testing.

## Criteria it touches

| SC | Title | Level | Entry | Why it comes up |
|---|---|---|---|---|
| 4.1.2 | Name, Role, Value | A | `wcag/sc-4.1.2-name-role-value.md` | Tab, tab list, and panel roles; selected state |
| 1.3.1 | Info and Relationships | A | `wcag/sc-1.3.1-info-and-relationships.md` | The link between each tab and its panel |
| 2.1.1 | Keyboard | A | `wcag/sc-2.1.1-keyboard.md` | Every tab reachable and operable by keyboard |
| 2.4.3 | Focus Order | A | `wcag/sc-2.4.3-focus-order.md` | Tab moving from the list into the active panel, and back |
| 2.4.7 | Focus Visible | AA | `wcag/sc-2.4.7-focus-visible.md` | Focus on tabs and on a focusable panel |
| 1.4.1 | Use of Color | A | `wcag/sc-1.4.1-use-of-color.md` | A selected tab shown by color alone |
| 1.4.11 | Non-text Contrast | AA | `wcag/sc-1.4.11-non-text-contrast.md` | The indicator that shows which tab is selected |
| 1.4.10 | Reflow | AA | `wcag/sc-1.4.10-reflow.md` | A row of tabs at narrow widths and high zoom |

## Manual tests

With the assistive technology named in the project's `a11y-spec.md`:
- Keyboard only: Tab lands on the selected tab; arrow keys move between tabs; Tab then moves into the panel; Shift+Tab returns to the selected tab.
- Screen reader: each tab's role, name, position, and selected state are announced; the panel is announced with its name. Also press Tab from reading mode into the list and record which tab gets focus. Landing on the first or last tab instead of the selected one is the 2018 screen reader bug O'Hara reported, not a coding error or a WCAG failure; note it and consider his workaround.
- Mobile screen readers: tabs can be found and activated by swiping, and the selected state is announced.
- Voice control: each tab can be activated by its visible name.
- Zoom to 400%: the tab list wraps or scrolls without hiding tabs, and the selected indicator stays visible.
