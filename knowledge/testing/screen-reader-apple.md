# Testing: Screen reader on Apple devices (VoiceOver, macOS and iOS)

- Sources:
  - WebAIM, "Using VoiceOver to Evaluate Web Accessibility", last updated 17 June 2026. https://webaim.org/articles/voiceover/ Tier 3. Mainly the macOS version.
  - WebAIM, "VoiceOver on Mobile", last updated 5 August 2020. https://webaim.org/articles/voiceover/mobile Tier 3.
  - WebAIM, "Testing with Screen Readers: Questions and Answers", last updated 20 May 2019. https://webaim.org/articles/screenreader_testing/ Tier 3.
- Related entries: `testing/screen-reader-windows.md`, `testing/keyboard-only.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-4.1.3-status-messages.md`, `wcag/sc-2.5.1-pointer-gestures.md`.
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

A failed step is evidence for a finding under the criterion it checks, reported once under that criterion. Record what was heard, and have a practiced user confirm before calling anything a failure; WebAIM warns that unfamiliarity looks like a defect. This test does not replace testing with people who use VoiceOver every day (principle 7). WebAIM's mobile guide dates from 2020 and Apple moves settings between releases; check against the current Apple user guide. Android's TalkBack is not covered here. If the spec lists it, there is no entry yet; follow the same steps with TalkBack's own gestures and mark the result unverified against this entry.

## Setup

- **macOS:** turn VoiceOver on (Command+F5, or a triple-press of Touch ID). The VO keys are Control+Option. Test in Safari, which WebAIM says works best with VoiceOver, and turn on Safari's option to let Tab reach every item on a page.
- **iOS and iPadOS:** turn it on in Settings, Accessibility, VoiceOver, and set the Accessibility Shortcut so a triple-click turns it off and on. In the rotor settings, enable at least Headings, Links, Form Controls, Tables, Landmarks, and Speaking Rate. Test in mobile Safari.

## The steps, macOS

1. Read the page (VO+A). Note anything read out of order, twice, or not at all.
2. Open the rotor (VO+U) and move through its lists: headings, links, landmarks, form controls, tables. Check that each list makes sense on its own.
3. Tab through controls and activate them with VO+Space. Note what is read for each: name, role, state.
4. In tables, note whether the caption is read, then move cell to cell with VO+arrow keys. Note whether headers are read. WebAIM notes VoiceOver struggles with spanned headers and an empty top-left cell; record exactly what is read.
5. Trigger every update the component makes. For status messages (a confirmation, an error count, a result count), note whether it is announced while focus stays where it was. For changes that move focus, such as a dialog opening, note what is announced on arrival.
6. Optionally, turn on Screen Curtain (VO+Shift+F11) to test without looking.

## The steps, iOS

1. Swipe up with two fingers to read the whole page from the top. WebAIM's gesture table gives two-finger swipe up as "from the top" and two-finger swipe down as "from the selected item"; its quick evaluation list says swipe down. The table is the more specific; if in doubt, select the first item first. Note the order.
2. Swipe right through every item. Note anything skipped or unreachable.
3. Set the rotor to Headings, then Links, then Form Controls, then Landmarks, and swipe down through each.
4. Tables: set the rotor to Tables to reach each table, then swipe through its cells. Note whether the caption is read, and whether row and column headers are read with each cell.
5. Activate each control by selecting it and double-tapping anywhere. Note the result and the announcement.
6. Repeat key tasks with a Bluetooth keyboard if the spec's audience may use one.
7. With VoiceOver off, since it replaces the standard gestures, note any action that needs a path-based or multi-finger gesture with no single-pointer alternative.

## What passing looks like

- Every control is read with a name, a role, and its state (`wcag/sc-4.1.2-name-role-value.md`).
- Structure appears in the rotor as it appears on screen (`wcag/sc-1.3.1-info-and-relationships.md`).
- Status messages are announced without moving focus (`wcag/sc-4.1.3-status-messages.md`).
- Path-based or multi-finger actions can also be done with a single pointer and no path (`wcag/sc-2.5.1-pointer-gestures.md`).

## What to record

Device, OS version, browser, and VoiceOver; for each step, what was done, what was spoken, pass or fail, and the tester. Note whether the tester is a daily VoiceOver user.
