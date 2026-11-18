# <Page, app, or component name>: assistive technology test checklist

<!--
The shape the at-test-protocol skill fills for a page checklist. Replace every <...>.
Keep the "How to use" bullets. Drop a mode section the spec does not list, or that has
nothing to test, and say why in one line under "Test setup".
-->

Draft, <YYYY-MM-DD>. For <who will run it>, testing <the page, or the component and the page it sits on, with its path or URL>.

## How to use this checklist

- Work through one section at a time. Tick the box when the expected outcome holds. When it does not, write what actually happened under the item.
- Each "Expected" line is the condition that counts as a pass, not a prediction. Write down what you actually saw or heard.
- The WCAG entry in brackets is what a failure is evidence for. Report each defect once, under that entry. Items marked *manual review* have no criterion behind them; they are advice, not failures.
- Screen reader sections: if you do not use a screen reader every day, record what you heard and have a practiced user confirm before you call anything a fail. Unfamiliarity looks like a defect (WebAIM, tier 3).
- This checklist does not replace testing with people who use assistive technology every day.
- "Watch for: code review" at the end lists likely problems found by reading the code. Use it to know where to look, not to decide the result in advance.

**Test setup.** <"From the spec's assistive technology list." or "The project has no spec, so these are a proposal. Confirm or change them.">

| Mode | Setup |
|---|---|
| <mode, with browser and platform> | <setup, from its knowledge/testing/ entry> |

<Any state to start from, such as sample data or a reset.>

---

## 1. <Mode, in the spec's order>

### <Part of the page, such as "Moving around the page"; or, for one component, one of its parts, such as "Opening it", "The fields", "Errors", "Closing it">
- [ ] **<What to do, naming the control.>**
  Expected: <the pass condition>. [`wcag/<entry>.md`]

### Every control, Enter and Space
Press Enter on each, then Space on each. <Any control not to confirm, and why.>

- [ ] <Control name>
- [ ] <Control name>

Expected for all: <condition>. [`wcag/sc-2.1.1-keyboard.md`]

### Status messages
<Screen reader sections.> For each, keep focus where it is and note whether the message is announced. [`wcag/sc-4.1.3-status-messages.md`]

- [ ] <What triggers it.> Expected: "<message text>" is announced.

## 2. <Next mode> ...

<For a second screen reader, repeat the first one's items with a table of its commands, from its testing entry, plus anything specific to it.>

---

## What to record

For every item that does not pass:

- <fields from the testing entries: versions, settings, what was done, what happened, focus before and after, screenshot, tester, daily user or not>

## Watch for: code review

Found by reading <files> on <YYYY-MM-DD>. They are likely problems, not test results. The checklist items listed with each one confirm or rule it out. If an item passes, the risk didn't materialize; record that.

| # | What the code suggests | Where in the code | Confirm with |
|---|---|---|---|
| 1 | <the likely problem, in plain words> | <file and function or line> | <section number and item name> |

## Gaps

- <No spec, if so.>
- <Components with no pattern entry.>
- <Modes with no testing entry, steps marked unverified.>
- <What this checklist does not cover.>
