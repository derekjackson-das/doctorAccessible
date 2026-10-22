# Testing: Keyboard only

- Sources:
  - WebAIM, "Keyboard Accessibility", last updated 14 May 2026. https://webaim.org/techniques/keyboard/ Tier 3.
  - GOV.UK Service Manual, Accessibility community, "Testing for accessibility", last updated 29 October 2024. https://www.gov.uk/service-manual/helping-people-to-use-your-service/testing-for-accessibility Tier 3.
- Related entries: `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-2.4.7-focus-visible.md`, `wcag/sc-2.4.11-focus-not-obscured-minimum.md`, `wcag/sc-2.4.1-bypass-blocks.md`, `wcag/sc-3.2.1-on-focus.md`; the manual tests in each `patterns/` entry.
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

A failed step is evidence for a finding under the criterion it checks, reported once under that criterion. A step with no criterion behind it is a manual-review note, not a WCAG failure.

## Setup

- A physical keyboard; put the mouse or trackpad out of reach. GOV.UK lists keyboard access first among the checks a team can run itself.
- On macOS Safari, turn on the setting "Press Tab to highlight each item on a webpage" (Safari settings, Advanced). WebAIM's VoiceOver article tells testers to enable it before testing.
- On a phone or tablet, repeat the steps with a Bluetooth keyboard if the spec's audience uses mobile; WebAIM advises it, since some people pair a keyboard with a phone.

## The steps

1. Load the page. Press Tab once. Note what receives focus first, and whether a skip link appears.
2. Keep pressing Tab through the whole page, then Shift+Tab back. At each stop: can you see where focus is, is it a thing you can act on, and does the order follow the visual layout?
3. Operate each control with its standard keys (WebAIM's table): Enter for links; Enter or Space for buttons; Space for checkboxes; arrow keys within radio groups and select menus; Escape to close dialogs; arrow keys within tab lists, sliders, and menus. For a scrolling region that takes focus, arrow keys scroll it and Space pages through it.
4. For each component that opens something (a menu, dialog, disclosure, popup), open it, use it, close it, and note where focus goes.
5. Try to leave every component with Tab, Shift+Tab, or Escape. Note any place focus cannot leave.
6. Watch for focus hidden behind sticky headers, banners, or chat widgets.
7. Watch for things that take focus but do nothing, and for things that act on focus alone, such as a menu that opens or a page that changes when tabbed onto.

## What passing looks like

- Every action a mouse user can take is possible from the keyboard (`wcag/sc-2.1.1-keyboard.md`).
- Focus can always be moved away by keyboard (`wcag/sc-2.1.2-no-keyboard-trap.md`).
- The focus order preserves meaning and operation (`wcag/sc-2.4.3-focus-order.md`).
- Focus is always visible (`wcag/sc-2.4.7-focus-visible.md`) and never entirely hidden by author content (`wcag/sc-2.4.11-focus-not-obscured-minimum.md`).
- A way exists to skip repeated blocks (`wcag/sc-2.4.1-bypass-blocks.md`).
- Nothing changes context just because it received focus (`wcag/sc-3.2.1-on-focus.md`).

## What to record

Browser and version, operating system, and for each step: the element, the key pressed, what happened, pass or fail, and the tester. For a failure, note the exact focus position before and after. Record keyboard-only results separately from screen reader results; a screen reader changes how keys behave.
