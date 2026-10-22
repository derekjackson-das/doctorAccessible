# Testing: Screen reader on Windows (NVDA)

- Sources:
  - WebAIM, "Using NVDA to Evaluate Web Accessibility", last updated 28 September 2020. https://webaim.org/articles/nvda/ Tier 3.
  - WebAIM, "Testing with Screen Readers: Questions and Answers", last updated 20 May 2019. https://webaim.org/articles/screenreader_testing/ Tier 3.
  - GOV.UK Service Manual, Accessibility community, "Testing for accessibility", last updated 29 October 2024. https://www.gov.uk/service-manual/helping-people-to-use-your-service/testing-for-accessibility Tier 3.
- Related entries: `testing/screen-reader-apple.md`, `testing/keyboard-only.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-4.1.3-status-messages.md`, `wcag/sc-1.1.1-non-text-content.md`.
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

A failed step is evidence for a finding under the criterion it checks, reported once under that criterion. WebAIM warns that a tester who does not yet know a screen reader can mistake their own confusion for a defect. Record what was heard, and have a practiced user confirm before calling anything a failure. This test does not replace testing with people who use screen readers every day (GOV.UK; principle 7). WebAIM's NVDA guide dates from 2020; check commands against the current NVDA user guide.

## Setup

NVDA is free and Windows only. WebAIM's recommended settings, set once:
- the desktop keyboard layout;
- Caps Lock as the NVDA key;
- a clear voice at a comfortable rate;
- highlighting turned on, so you can see what is being read;
- Tools, then Speech Viewer, to see a transcript you can copy into the record.

Do not change punctuation level or document-formatting settings; they change what is read. Use the browser the spec pairs with NVDA, usually Chrome or Firefox.

## The steps

1. **Read the page top to bottom:** Ctrl+Home to go to the top, then NVDA+Down Arrow, which reads from the current position. Note anything read out of order, read twice, or not read at all.
2. **Navigate by structure** using single-key shortcuts: H and 1 to 6 for headings, D for landmarks, K for links, B for buttons, F for form fields, T for tables, L for lists, G for graphics. Note whether the structure matches what is visible.
3. **Open the Elements List** (NVDA+F7). Check that the links and headings make sense out of context.
4. **Images:** note what is read for each image and each icon button.
5. **Forms:** Tab to each field and note what is read: label, type, required state, current value, and any error. For grouped checkboxes or radio buttons, note whether the group's question is read. Note when NVDA switches between browse mode and focus mode; it beeps.
6. **Tables:** jump to the table with T and note whether its caption is read. Move cell by cell with Ctrl+Alt+arrow keys. Note whether row and column headers are read with each cell.
7. **Dynamic content:** trigger every update the component makes. For status messages (a confirmation, an error count, a result count), note whether it is announced while focus stays where it was. For changes that move focus, such as a dialog opening, note what is announced on arrival and where the reading position ends up.
8. **Custom widgets:** operate them with the keys the pattern documents. Note whether NVDA needs to be in focus mode, and whether it gets there by itself.

## What passing looks like

- Every control is read with a name, a role, and its state (`wcag/sc-4.1.2-name-role-value.md`).
- Headings, lists, tables, form groups, and landmarks are exposed as structure (`wcag/sc-1.3.1-info-and-relationships.md`).
- Images have text alternatives that serve their purpose (`wcag/sc-1.1.1-non-text-content.md`).
- Status messages are announced without moving focus (`wcag/sc-4.1.3-status-messages.md`).

## What to record

NVDA version, browser and version, Windows version, and for each step: what was done, the Speech Viewer text, pass or fail, and the tester. Note any setting changed from WebAIM's list. Say whether the tester is a daily screen reader user.
