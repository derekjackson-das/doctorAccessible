I couldn't write the checklist to a file because you asked for no file changes. It's below in full instead.

---

# Saved reports: assistive technology test checklist

Draft, 2026-11-18. For the developer who built the page, to work through. It covers the whole Saved reports page: the report list, the "More actions" menu, the Rename dialog and the "Report deleted" message with Undo.

## How to use this checklist

- Work through one section at a time. Tick the box when the expected outcome holds. When it does not, write what actually happened under the item.
- Each "Expected" line is the condition that counts as a pass, not a prediction. Write down what you actually saw or heard.
- The WCAG entry in brackets is what a failure is evidence for. Report each defect once, under that entry. Items marked *manual review* have no criterion behind them; they are advice, not failures.
- Screen reader sections: if you do not use a screen reader every day, record what you heard and have a practiced user confirm before you call anything a fail. Unfamiliarity looks like a defect (WebAIM, tier 3, via `testing/screen-reader-apple.md`).
- This checklist does not replace testing with people who use assistive technology every day.
- "Watch for: code review" at the end lists likely problems found by reading the code. Use it to know where to look, not to decide the result in advance.

**Test setup.** The project has no spec, so these are a proposal based on what you said: macOS, Chrome and Safari. Confirm or change them.

| Mode | Setup |
|---|---|
| Keyboard only, Chrome and Safari on macOS | Physical keyboard, trackpad and mouse out of reach. In Safari, turn on "Press Tab to highlight each item on a webpage" (Settings, Advanced). (`testing/keyboard-only.md`) |
| VoiceOver with Safari on macOS | Command+F5 turns VoiceOver on. The VO keys are Control+Option. Use Safari with the Tab setting above. (`testing/screen-reader-apple.md`) |
| Zoom at 200% and 400%, Chrome on macOS | Window 1280 CSS pixels wide, start at 100%, use Command with Plus to zoom. (`testing/zoom.md`) |

Two modes are left out:
- **Reduced motion:** the page has no CSS transitions, animations or scripted movement, so there is nothing to suppress.
- **Forced colors:** it is a Windows feature, and on macOS you only get Edge's emulation, which is a first pass, not the test (`testing/forced-colors.md`). Add it if the audience includes people using Windows Contrast Themes.

**Starting state:** reload the page before each section so all three reports are present. Delete and Rename change the list.

---

## 1. Keyboard only (Chrome, then Safari)

### Moving around the page
- [ ] **1.1 Load the page and press Tab once.** Note what gets focus first.
  Expected: focus lands on a control you can see, at the start of the page content. [`wcag/sc-2.4.3-focus-order.md`]
- [ ] **1.2 Tab through the whole page, then Shift+Tab back.** At each stop, note where focus is.
  Expected: the order is the three "More actions" buttons from top to bottom, and focus is visible at every stop. [`wcag/sc-2.4.3-focus-order.md`, `wcag/sc-2.4.7-focus-visible.md`]

### The "More actions" menu
- [ ] **1.3 On "More actions" for "Course completion by term", press Enter.** Note where focus lands and where the menu appears.
  Expected: the menu opens next to that button, and focus is on "Rename" with a visible indicator. [`wcag/sc-2.4.3-focus-order.md`, `wcag/sc-2.4.7-focus-visible.md`]
- [ ] **1.4 With the menu open, press Tab, then Tab again.** Note each place focus goes.
  Expected: Tab moves from Rename to Delete. After Delete, focus goes to something that makes sense next to the menu, and never to something hidden or invisible. [`wcag/sc-2.4.3-focus-order.md`]
- [ ] **1.5 Reopen the menu and press Shift+Tab from "Rename".**
  Expected: focus goes back to the "More actions" button that opened it, not to a different report's button. [`wcag/sc-2.4.3-focus-order.md`]
- [ ] **1.6 Reopen the menu and press Escape.** Note where focus is afterwards: press Tab once and see what gets focus.
  Expected: the menu closes and focus returns to the "More actions" button that opened it. [`wcag/sc-2.4.3-focus-order.md`]
- [ ] **1.7 Reopen the menu, then Tab away from it without choosing anything.** Note whether the menu stays on screen, and whether it covers the focused control.
  Expected: the focused control is never fully covered by the menu. [`wcag/sc-2.4.11-focus-not-obscured-minimum.md`]
- [ ] **1.8 Repeat 1.3 and 1.6 for the first and last report.**
  Expected: the same results for each.

### The Rename dialog
- [ ] **1.9 Open the menu for "Monthly sign-ups" and press Enter on Rename.** Note where focus lands.
  Expected: focus moves inside the dialog, onto a control you can see. [`wcag/sc-2.4.3-focus-order.md`]
- [ ] **1.10 Tab and Shift+Tab around the dialog several times.**
  Expected: focus moves only between the "Report name" field, Cancel and Save, or out to the browser's own controls. It never reaches the report list behind the dialog. [`wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-2.4.3-focus-order.md`; reaching browser controls is acceptable per `patterns/modal-dialog.md`]
- [ ] **1.11 Press Escape.**
  Expected: the dialog closes and focus returns to the "More actions" button for "Monthly sign-ups". [`wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-2.4.3-focus-order.md`]
- [ ] **1.12 Reopen Rename, Tab to Cancel and press Enter.**
  Expected: the dialog closes, the name is unchanged, and focus returns to the "More actions" button for that report. [`wcag/sc-2.4.3-focus-order.md`]
- [ ] **1.13 Reopen Rename, type a new name in the field and press Enter.**
  Expected: the dialog closes, the new name shows in the list, and focus returns to the "More actions" button for that report. [`wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.3-focus-order.md`]
- [ ] **1.14 Reopen Rename, clear the field and choose Save.** Note what happens. *Manual review:* nothing tells you an empty name is not allowed. Decide whether an empty name should be blocked.

### Delete and Undo
- [ ] **1.15 Open the menu for "Support tickets, last 30 days" and press Enter on Delete.** Note where focus is: press Tab once and see what gets focus.
  Expected: focus is on a sensible visible control, such as the Undo button or the nearest remaining report's "More actions" button, not lost to the top of the page. [`wcag/sc-2.4.3-focus-order.md`]
- [ ] **1.16 Delete a report again, then reach the Undo button by keyboard alone.** Time how long it takes, and note whether the message disappears first.
  Expected: Undo can be reached and pressed by keyboard. [`wcag/sc-2.1.1-keyboard.md`] Also note whether the 5-second limit can be turned off, extended, or lengthened. [`wcag/sc-2.2.1-timing-adjustable.md`; whether a disappearing Undo counts as a time limit is a judgment, so record it as *manual review* unless a reviewer agrees it applies]
- [ ] **1.17 Press Enter on Undo.** Note where the report reappears and where focus is.
  Expected: the report comes back in its original place, and focus is on a sensible visible control, not lost. [`wcag/sc-2.4.3-focus-order.md`]

### Every control, Enter and Space
Press Enter on each, then Space on each. Reload the page between Delete and Undo as needed.

- [ ] More actions, Monthly sign-ups
- [ ] More actions, Course completion by term
- [ ] More actions, Support tickets, last 30 days
- [ ] Rename
- [ ] Delete
- [ ] Cancel (in the dialog)
- [ ] Save (in the dialog)
- [ ] Undo

Expected for all: the control does the same thing it does when clicked. [`wcag/sc-2.1.1-keyboard.md`]

## 2. VoiceOver with Safari on macOS

### Reading the page
- [ ] **2.1 Read the whole page (VO+A).** Note anything read out of order, read twice, or skipped.
  Expected: the heading "Saved reports", then the three reports, each followed by its button. The hidden menu, dialog and message are not read. [`wcag/sc-1.3.1-info-and-relationships.md`]
- [ ] **2.2 Open the rotor (VO+U) and go through the Headings, Landmarks and Form Controls lists.** Note what each one contains.
  Expected: one heading, "Saved reports"; a main landmark; and the three "More actions" buttons. Each list makes sense on its own. [`wcag/sc-1.3.1-info-and-relationships.md`]
- [ ] **2.3 Tab to each "More actions" button.** Note the name, role and state you hear, and whether anything says which report it belongs to.
  Expected: each one is read with the name "More actions", the role "button", and that it opens a menu. [`wcag/sc-4.1.2-name-role-value.md`] *Manual review:* three buttons with the same name may be hard to tell apart in the rotor's list. [`wcag/sc-2.4.6-headings-and-labels.md` has no case for repeated names]

### The menu
- [ ] **2.4 Activate "More actions" for "Course completion by term" (VO+Space).** Note what is announced, and whether you hear that the menu is open.
  Expected: focus moves to "Rename", read as a button, and the menu's open state is exposed in some way. [`wcag/sc-4.1.2-name-role-value.md`]
- [ ] **2.5 Move through the menu with VO and the arrow keys, then with Tab.** Note what role the items are read with. The button says it opens a menu, so note whether the items behave like a menu.
  Expected: the items are read with roles that match what they do. [`wcag/sc-4.1.2-name-role-value.md`]
- [ ] **2.6 Press Escape.** Note what is announced and where VoiceOver's cursor is.
  Expected: the cursor is back on the button that opened the menu. [`wcag/sc-2.4.3-focus-order.md`]

### The Rename dialog
- [ ] **2.7 Open Rename for any report.** Note what is announced when the dialog opens.
  Expected: the dialog's role and its name, "Rename report", are announced. [`wcag/sc-4.1.2-name-role-value.md`; a dialog with no name is *manual review* per `aria/patterns/modal-dialog.md`]
- [ ] **2.8 On the field, note what is read.**
  Expected: "Report name", the text field role, and the current value. [`wcag/sc-4.1.2-name-role-value.md`]
- [ ] **2.9 With the dialog open, use VO and the arrow keys to read forward and back past both ends of the dialog.**
  Expected: the cursor stays inside the dialog and never reaches the report list. [`wcag/sc-1.3.1-info-and-relationships.md`; the requirement comes from `patterns/modal-dialog.md`]
- [ ] **2.10 Close with Escape, then with Cancel, then with Save.** After each, note what is announced and where the cursor is.
  Expected: the cursor is on the "More actions" button for that report each time. [`wcag/sc-2.4.3-focus-order.md`]

### Status messages
Keep focus where it is and note whether the message is announced. [`wcag/sc-4.1.3-status-messages.md`]

- [ ] **2.11 Choose Delete for any report.** Expected: "Report deleted" is announced.
- [ ] **2.12 After deleting, try to reach Undo with VoiceOver before the message disappears.** Note whether you managed it, and how. [`wcag/sc-2.1.1-keyboard.md`; time limit *manual review* as in 1.16]

### Every control
- [ ] **2.13 Activate each control with VO+Space:** the three "More actions" buttons, Rename, Delete, Cancel, Save and Undo. Note what is read for each.
  Expected: each is read with its name and role, and does what it does when clicked. [`wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`]

- [ ] **Optional:** repeat 2.4 to 2.11 with Screen Curtain on (VO+Shift+F11).

## 3. Zoom at 200% and 400% (Chrome)

- [ ] **3.1 At 200%, read every piece of text:** the heading, the report names, the buttons, the menu items, the dialog, and the "Report deleted" message.
  Expected: nothing is cut off, overlapping, or failing to grow. [`wcag/sc-1.4.4-resize-text.md`]
- [ ] **3.2 At 400%, scroll top to bottom.**
  Expected: you never have to scroll sideways to read a line. [`wcag/sc-1.4.10-reflow.md`]
- [ ] **3.3 At 400%, scroll down to the last report and open its menu.** Note where the menu appears relative to its button.
  Expected: the menu appears next to the button that opened it, fully on screen. [`wcag/sc-1.4.10-reflow.md`]
- [ ] **3.4 At 400%, open the Rename dialog.**
  Expected: the heading, field, Cancel and Save can all be reached and used. [`wcag/sc-1.4.10-reflow.md`]
- [ ] **3.5 At 400%, delete a report.** Note how much of the screen the message covers, and whether you can reach Undo.
  Expected: the message and Undo can be read and reached. [`wcag/sc-1.4.10-reflow.md`]
- [ ] **3.6 At 400%, with the message showing, Tab through the page.**
  Expected: no focused control is fully hidden behind the message. [`wcag/sc-2.4.11-focus-not-obscured-minimum.md`]
- [ ] **3.7 Optional:** apply the text-spacing values with a bookmarklet and note any clipped text. [`wcag/sc-1.4.12-text-spacing.md`]

---

## What to record

For every item that does not pass:

- Browser and version, macOS version, and VoiceOver (VoiceOver items) or the zoom level and window width (zoom items).
- The item number, the control, the key pressed, and what happened.
- Where focus was before and after.
- For VoiceOver items, what was spoken, word for word if you can.
- A screenshot of any visual failure, and for zoom, which content you judged an exception and why.
- Pass or fail, the tester's name, and whether the tester uses VoiceOver every day.
- Keep keyboard-only results separate from VoiceOver results.

## Watch for: code review

Found by reading the page source pasted in the request, 2026-11-18. These are likely problems, not test results. The checklist items listed with each one confirm or rule it out. If an item passes, the risk didn't materialize; record that.

| # | What the code suggests | Where in the code | Confirm with |
|---|---|---|---|
| 1 | The menu sits at the end of the page, after `main`, so Tab and Shift+Tab out of it may go somewhere far from the button that opened it | `<div id="menu">` placed after `</main>` | 1.4, 1.5 |
| 2 | Escape hides the menu but nothing moves focus back, so focus may be left on a hidden button | `keydown` handler: `menu.hidden = true` only | 1.6, 2.6 |
| 3 | Nothing closes the menu when focus leaves it, so it may stay open over the list | No blur or focusout handler on `#menu` | 1.7 |
| 4 | The button says it opens a menu (`aria-haspopup="menu"`), but the popup is plain buttons with no menu role and no arrow-key handling, and the button has no `aria-expanded` to say whether it is open | `.more` buttons; `#menu` markup | 2.3, 2.4, 2.5 |
| 5 | Rename and Delete are hidden as they are pressed, so after the dialog closes, after Delete, or after Undo, focus has no visible place to return to | `menu.hidden = true` before `showModal()` and before `current.remove()`; Undo sets `toast.hidden = true` while focused | 1.11 to 1.13, 1.15, 1.17, 2.10 |
| 6 | The dialog's heading is not tied to it with `aria-labelledby`, so it may have no name | `<dialog id="rename-dialog">` | 2.7 |
| 7 | The "Report deleted" message has no live-region role, so it may not be announced | `<div id="toast">`, shown with `toast.hidden = false` | 2.11 |
| 8 | Undo disappears after 5 seconds and comes after everything else in the page, so reaching it in time by keyboard or VoiceOver may be hard | `setTimeout(..., 5000)`; `#toast` at end of body | 1.16, 2.12 |
| 9 | The menu is placed using window coordinates with no scroll offset, so on a scrolled page it may appear away from its button | `menu.style.top = r.bottom + "px"` with `position: absolute` | 3.3 |
| 10 | The message is fixed to the bottom-left corner, so at high zoom it may cover content or focused controls | `.toast { position: fixed; bottom: 24px; left: 24px }` | 3.5, 3.6 |
| 11 | Save accepts an empty name | Submit handler copies the value as-is | 1.14 |

## Gaps

- **No `a11y-spec.md`.** The modes above are a proposal and need confirming. Use the `planning` skill to create the spec, including whether iOS VoiceOver, NVDA, or forced colors belong on the list.
- **No pattern entry for an action menu (menu button) or for a toast or snackbar** in `knowledge/patterns/` or `knowledge/aria/patterns/`. Those items are built from the testing entries and the criteria alone.
- **The native dialog's initial focus is untested.** `patterns/modal-dialog.md` notes that no listed source has tested where `showModal()` puts initial focus since the 2023 HTML change, so 1.9 and 2.7 are first-hand evidence.
- **Not covered:**
  - color contrast and target size of the "⋯" buttons (axe checks these)
  - voice control
  - screen magnifiers
  - mobile
  - whether deleting with no confirmation, or the 5-second undo, is the right design (a `consult` question, not a test)

---

To save this as a file, I'd draft it in the scratchpad first and show you the path. Tell me where it should live, for example next to the page's own files, and I'll write it there once you say go. When the spec exists, I'd add this checklist to its "Open manual tests" section with an owner and a date, again only with your agreement.
