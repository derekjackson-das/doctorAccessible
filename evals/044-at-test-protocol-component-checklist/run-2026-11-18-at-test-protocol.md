Read the skill, the request, the checklist template, and the entries it points at (forms, date picker, the three testing modes, the WCAG criteria). Here is the answer to the developer.

---

The skill's rule 7 says a checklist is a file: draft it in the scratchpad, show you the path, and ask where it should live. You asked me not to create files here, so it's inline below. Tell me where it should go, somewhere outside any repo such as beside the page's own files, and I'll write it there on your go.

---

# Room request form: assistive technology test checklist

Draft, 2026-11-18. For the developer, testing the room request form (`#room-form`) and its confirmation message (`#sent`) on the "Book a study room" page. The rest of the page (main nav, footer newsletter form) is out of scope. It only matters as the place the form sits.

## How to use this checklist

- Work through one section at a time. Tick the box when the expected outcome holds. When it doesn't, write what actually happened under the item.
- Each "Expected" line is the condition that counts as a pass. It is not a prediction. Write down what you actually saw or heard.
- The WCAG entry in brackets is what a failure is evidence for. Report each defect once, under that entry. Items marked *manual review* have no criterion behind them. They are advice, not failures.
- Screen reader sections: if you don't use a screen reader every day, record what you heard and have a practiced user confirm before you call anything a fail. Unfamiliarity looks like a defect (WebAIM, "Testing with Screen Readers: Q&A", 20 May 2019, tier 3).
- This checklist does not replace testing with people who use assistive technology every day.
- "Watch for: code review" at the end lists likely problems found by reading the code. Use it to know where to look, not to decide the result in advance.

**Test setup.** From the spec's assistive technology list: keyboard only, NVDA with Firefox, 200% and 400% zoom.

| Mode | Setup |
|---|---|
| Keyboard only, Firefox on Windows | A physical keyboard, with the mouse or trackpad out of reach (`testing/keyboard-only.md`, GOV.UK 29 Oct 2024 and WebAIM 14 May 2026, tier 3). |
| NVDA with Firefox on Windows | Desktop keyboard layout, Caps Lock as the NVDA key, a clear voice at a comfortable rate, highlighting on, and Tools then Speech Viewer open so you can copy the transcript. Don't change the punctuation level or the document-formatting settings (`testing/screen-reader-windows.md`, WebAIM 28 Sep 2020, tier 3; check commands against the current NVDA user guide). |
| Zoom, Firefox | Window at 1280 CSS pixels wide, starting at 100%. Use browser zoom (Ctrl+Plus), not text-only zoom (`testing/zoom.md`, Understanding WCAG 2.2 for 1.4.10 and 1.4.4, tier 2). |

Start each run from a fresh page load with the form empty. Have a test name, an email, and a date ready. You'll submit the form three ways: completely empty, partly filled with a bad email, and fully valid.

---

## 1. Keyboard only

### Reaching the form
- [ ] **Load the page, then press Tab until focus reaches "Your name". Count the stops on the way.**
  Expected: you can see focus at every stop, and focus reaches the form after the three nav links, in visual order. [`wcag/sc-2.4.3-focus-order.md`, `wcag/sc-2.4.7-focus-visible.md`]
- [ ] **Tab through the form: Your name, Email, Date, Room size, Request room. Then Shift+Tab back to Your name.**
  Expected: the order matches the visual order both ways, focus is always visible, and nothing changes just because a field received focus. [`wcag/sc-2.4.3-focus-order.md`, `wcag/sc-2.4.7-focus-visible.md`, `wcag/sc-3.2.1-on-focus.md`]

### The fields
- [ ] **Type a name in "Your name" and an email in "Email".**
  Expected: the text appears in the field you are on. [`wcag/sc-2.1.1-keyboard.md`]
- [ ] **In "Date", type a date in the format the field shows. Then try a different common format. Then try a nonsense value.** Write down what the field accepts each time. Firefox's native date input has its own keys.
  Expected: you can enter a valid date from the keyboard alone, without opening a calendar. [`wcag/sc-2.1.1-keyboard.md`]
- [ ] **If the date field offers a calendar, open it from the keyboard, pick a day, and close it.**
  Expected: every part of the calendar can be reached and operated, and focus can leave it with Tab, Shift+Tab, or Escape. [`wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`]
- [ ] **Tab into Room size, then use the arrow keys to move through "Up to 2 people", "Up to 6 people", and "Up to 12 people".**
  Expected: Tab enters the group once, the arrow keys move between the options and select them, and Tab leaves the group for "Request room". [`wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`]

### Every control, Enter and Space
Press Enter on each, then Space on each. In the three text fields, Space types a space and Enter submits the form, so for those, just check that Enter submits.

- [ ] Up to 2 people (radio)
- [ ] Up to 6 people (radio)
- [ ] Up to 12 people (radio)
- [ ] Request room (button)
- [ ] Your name, Email, Date: Enter submits the form

Expected for all: Space selects a radio, Enter or Space activates the button, and every action a mouse can take is possible from the keyboard. [`wcag/sc-2.1.1-keyboard.md`]

### Errors
- [ ] **With the form empty, press Request room. Note where focus is afterwards.**
  Expected: the error messages appear in text, and each one names the field it is about. [`wcag/sc-3.3.1-error-identification.md`] Separately, write down where focus ended up and whether you could tell, without hunting, that something went wrong. *Manual review* for the focus position alone.
- [ ] **Fill in a name, type `abc` as the email, and press Request room.**
  Expected: the email error says what a valid entry looks like. [`wcag/sc-3.3.3-error-suggestion.md`]
- [ ] **From the button, Shift+Tab back to the first field that has an error and correct it.**
  Expected: you can reach each field in error from the keyboard. [`wcag/sc-2.1.1-keyboard.md`]

### Sending
- [ ] **Fill every field validly and press Request room.**
  Expected: the confirmation text appears, the error area is empty, and focus is still visible somewhere you can name. Write down where. [`wcag/sc-2.4.7-focus-visible.md`]

## 2. NVDA with Firefox

### The fields
- [ ] **Press F to move from field to field through the form, then Tab through it as well. For each field, note what is read.**
  Expected: each field is read with its name ("Your name", "Email", "Date"), its type, and its current value. [`wcag/sc-4.1.2-name-role-value.md`]
- [ ] **On each of the three text fields, note whether a required state is read.**
  Expected: each one is read as required. [`wcag/sc-4.1.2-name-role-value.md`] Also check whether the page shows in text that the fields are required. [`wcag/sc-3.3.2-labels-or-instructions.md`]
- [ ] **On the Date field, note what is read for each part of it, and what is read once a date is entered.**
  Expected: the field's name and its value are read. [`wcag/sc-4.1.2-name-role-value.md`]
- [ ] **Tab into Room size. Note whether "Room size" is read when you enter the group, then arrow through the options.**
  Expected: the group's question ("Room size") is read with the options, and each option is read with its label, its role, its checked state, and its position. [`wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-4.1.2-name-role-value.md`]
- [ ] **Listen for NVDA's beep as it switches between browse mode and focus mode while you move through the fields.** Record when it happens.
  Expected: you can type into the fields and arrow through the radios without switching modes by hand. *Manual review.*
- [ ] **On Request room, note what is read.**
  Expected: it is read as a button named "Request room". [`wcag/sc-4.1.2-name-role-value.md`]

### Reading the form
- [ ] **Move to the "Book a study room" heading (press H), then press NVDA+Down Arrow to read from there to the end of the form.**
  Expected: everything visible in the form is read, in order, nothing twice. [`wcag/sc-1.3.1-info-and-relationships.md`]

### Errors
- [ ] **After an empty submit, Tab back to "Your name". Note whether its error is read with the field.**
  Expected: the error is identified on the field it belongs to. [`wcag/sc-3.3.1-error-identification.md`, `wcag/sc-1.3.1-info-and-relationships.md`]
- [ ] **Repeat that on Email, Date, and the Room size group.**
  Expected: same as above, for each one. [`wcag/sc-3.3.1-error-identification.md`]

### Status messages
For each one, keep focus on Request room after pressing it, and note whether the message is announced. Copy the Speech Viewer text. [`wcag/sc-4.1.3-status-messages.md`]

- [ ] Empty submit. Expected: "Enter your name." is announced.
- [ ] Empty submit. Expected: "Enter an email address like name@example.edu." is announced.
- [ ] Empty submit. Expected: "Choose a date." is announced.
- [ ] Empty submit. Expected: "Choose a room size." is announced.
- [ ] Valid submit. Expected: "Request sent. We'll email you within one working day." is announced.
- [ ] Submit again after the confirmation has appeared once. Expected: the new message is announced again. Write down what you heard.

## 3. Zoom at 200% and 400%

### 200%
- [ ] **At 200%, read every label, the "Room size" text, every option, the button, the values you typed, and the error list after an empty submit.**
  Expected: no text is cut off, overlapping, or the same size as before. [`wcag/sc-1.4.4-resize-text.md`]

### 400% (1280 px window)
- [ ] **Scroll from the heading to the confirmation area.**
  Expected: the form fits in one column and no line of text needs sideways scrolling to read. [`wcag/sc-1.4.10-reflow.md`]
- [ ] **At 400%, fill every field, open the date field's calendar if it has one, and submit once empty and once valid.**
  Expected: every control can be reached and used, the date field's calendar opens on screen, and both the error list and the confirmation can be seen without sideways scrolling. [`wcag/sc-1.4.10-reflow.md`]
- [ ] **At 400%, Tab through the form.**
  Expected: the focused field is never fully hidden. [`wcag/sc-2.4.11-focus-not-obscured-minimum.md`]
- [ ] **After a valid submit at 400%, note whether the confirmation is in view or has to be scrolled to.**
  *Manual review.*

---

## What to record

For every item that does not pass:

- Browser and version, Windows version, and NVDA version for section 2.
- The window width and zoom level for section 3.
- The element, the key you pressed, and what happened. For keyboard failures, where focus was before and after.
- For NVDA, the Speech Viewer text, and whether the tester uses a screen reader every day. Note any setting changed from the setup above.
- For zoom failures, a screenshot. Note any content you judged to be an exception, and why.
- Pass or fail, and the tester.
- Keep the keyboard-only results separate from the NVDA results, because a screen reader changes how keys behave.

## Watch for: code review

Found by reading the HTML and inline script in the request on 2026-11-18. These are likely problems, not test results. The checklist items listed with each one confirm or rule it out. If an item passes, the risk didn't materialize. Record that.

| # | What the code suggests | Where in the code | Confirm with |
|---|---|---|---|
| 1 | The error box isn't a live region, and focus doesn't move to it. The errors may appear silently. | `<div id="form-errors" class="errors">` has no `role` or `aria-live`; the submit handler writes `innerHTML` and returns | 2, Status messages, the four error items |
| 2 | The errors aren't tied to their fields: no `aria-describedby`, no `aria-invalid`. A screen reader user on the field may hear no error. | The handler builds one `<ul>` at the top of the form | 2, Errors, both items |
| 3 | "Room size" is a `<p>`, not a `legend`, and the radios have no `fieldset`. The group's question may not be read with the options. | `<p>Room size</p>` and the three radio labels | 2, The fields, "Tab into Room size" |
| 4 | Required is in the code (`required`) but not shown in text on the page. | The three `<label>` elements | 2, The fields, the required item |
| 5 | After a submit, focus stays on the button while the errors appear above the fields. Keyboard users may not notice them. | Submit handler; no `focus()` call | 1, Errors, the empty-submit item |
| 6 | The confirmation region exists on page load, which is the sound way to do it. Writing the same text twice may not be announced the second time. | `#sent` with `role="status"`; `textContent` set to the same string | 2, Status messages, the last item |
| 7 | `form.reset()` clears every field after a valid send. Check that the confirmation is the only thing that explains what happened. | Last line of the handler | 1, Sending; 3, the last 400% item |

## Gaps

- **No pattern entry for the form as a whole.** The steps come from `html/forms.md` and the testing entries. For the Date field, `patterns/date-picker.md` applies to the native control. It flags a voice-control problem with `input type="date"` (Roselli, updated 18 Mar 2026, tier 3). Voice control isn't on the spec's list, so it isn't tested here. Raise it if your audience includes voice-control users.
- **Every mode on the spec's list has a testing entry.** No steps are unverified.
- **Outside this checklist:** the nav, the footer newsletter form, and any server-side handling. The checklist also doesn't cover `autocomplete` on Your name and Email. That's a code check, not an assistive technology test. `wcag/sc-1.3.5-identify-input-purpose.md` treats a missing token on a field about the user as definite, and axe doesn't flag it. Run the verifier for that.

---

**Note for the developer, separate from the checklist.** Items 1 to 3 in Watch for are what the code shows. The checklist is still neutral about them, because that's the tester's call to make. I'm not fixing them here. When you want a verdict, the verifier agent gives you one independently of this conversation.

**Next step.** The spec's "Open manual tests" section is where this checklist should be logged, with an owner and a date. Give me both and I'll add the entry once you approve it. Also tell me where the checklist file should live.
