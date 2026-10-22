# Pattern: Tabs

- Sources:
  - W3C, "Tabs Pattern", ARIA Authoring Practices Guide, https://www.w3.org/WAI/ARIA/apg/patterns/tabs/. Tier 2. A pattern, not a requirement.
  - Scott O'Hara, "Trouble Tabbing To Tabs and Cheeky Checking Checkboxes", 2 November 2018, updated 5 February 2019, https://www.scottohara.me/blog/2018/11/02/tabbing-into-tabs.html. Tier 3.
  - Heydon Pickering, "Tabbed Interfaces", Inclusive Components, 5 October 2017, https://inclusive-components.design/tabbed-interfaces/. Tier 3.
- Related entries: `coga/objective-2-find-what-they-need.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-3.2.3-consistent-navigation.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the tab set is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer.

## The need it usually serves

Several views of related content share one space, and the person switches between them without leaving the page: a product's description, specifications, and reviews; a profile's posts and photos. The pattern earns its place when the person genuinely moves back and forth; it is misused when the "tabs" are really separate pages or a table of contents.

## The simpler thing that often serves, and what is lost

Headings and sections on one page, with a table of contents of same-page links at the top. Pickering (2017) builds exactly that and shows it already gives the person control over what they see; he argues from material honesty that a table of contents should not be dressed as tabs, because people who see tabs expect behavior a list of links does not have, and that a tabbed look should never be used for site-wide navigation, since selecting a tab should not load a new page. What is lost by choosing sections and a table of contents: the compact layout and the sense of switching in place. What is gained: no keyboard conventions to learn, every section reachable by heading navigation, find-in-page and print intact.

## What doing it right requires

There is no native HTML tab set. The APG pattern's expectations, in our words: the tabs sit in a tab list; Tab into the list lands on the active tab; Left and Right Arrow move between tabs, wrapping at the ends, and may or may not activate the newly focused tab; Tab out of the list goes to the panel or the first focusable thing inside it; each panel is labeled by its tab. Pickering notes that the ARIA roles exist chiefly to tell screen reader users which keyboard behavior to expect, and he adds a Down Arrow from the tab to its panel, with the panel focusable by script only, so screen reader users are not stranded on the tab list.

What the APG does not say: whether arrow keys should activate tabs automatically or only move focus, which depends on how expensive it is to show a panel, and whether the tabs are the right model at all.

## What practitioners found when they tested it

- **O'Hara, 2018.** With NVDA 2018.3.2 and JAWS 18 and 2018 at default settings, a user reading a page with the virtual cursor who then pressed Tab from just before the tab list could land on a tab with a negative tabindex, which should not be focusable, instead of the active tab. The bug did not appear when Tab had already visited another focusable element first, and did not appear in VoiceOver. He filed bugs with both screen reader vendors. The lesson: correct markup can still misbehave, and tab sets must be tested with the virtual cursor, not only with Tab.
- **Pickering, 2017.** Screen reader users entering a panel from its tab hear the panel's name because the panel is labeled by the tab; without the Down Arrow addition they could focus interactive content inside the panel without knowing where they were. He warns that making a non-interactive element focusable in the normal tab order fails the focus-order criterion, which is why the panel takes a negative tabindex.

## Criteria it touches

Roles, names, and selected state: `wcag/sc-4.1.2-name-role-value.md`. Keyboard operation of the list: `wcag/sc-2.1.1-keyboard.md`. Focus movement into the panel and the trap risk: `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`. Panel content as real structure: `wcag/sc-1.3.1-info-and-relationships.md`. Selected tab shown by more than color: `wcag/sc-1.4.1-use-of-color.md`, `wcag/sc-1.4.11-non-text-contrast.md`. Tab labels: `wcag/sc-2.4.6-headings-and-labels.md`. Tabs used as site navigation: `wcag/sc-3.2.3-consistent-navigation.md` and the On Input criterion if selecting one navigates, `wcag/sc-3.2.2-on-input.md`. Hidden panels at 320 CSS pixels: `wcag/sc-1.4.10-reflow.md`.

## Manual tests it demands

- Keyboard: Tab to the list; record which tab gets focus. Arrow left and right; record wrapping and whether panels change. Tab again; record where focus goes.
- Screen reader, each pair in the spec: read the page with the virtual cursor to just before the tabs, then press Tab; record which tab receives focus (O'Hara's bug). Record what is announced on a tab and on entering its panel.
- Pointer and touch: record that each tab is a target of at least 24 CSS pixels and that the selected tab is told apart by more than color.
- 400% zoom: record whether the tab list wraps or scrolls and whether hidden panels stay hidden.

## What consult should say

1. Does the person switch back and forth, or read once? Read once means headings, not tabs.
2. Are these really pages? Then they are navigation, and tabs are the wrong costume.
3. If tabs stay: the APG keyboard model, panels labeled by tabs, a way down into the panel, and a test with the virtual cursor.
