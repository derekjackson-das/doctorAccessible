---
name: at-test-protocol
description: The human testing mode. Use when a component, page, or feature needs manual testing with assistive technology, when a need statement or the spec lists manual tests owed, or when someone asks how to test something with a keyboard, screen reader, zoom, reduced motion, or forced colors, or asks for a manual testing checklist with expected outcomes. Writes a numbered test script, or a checklist for one component or a whole page with a pass condition per item, built from the project spec's assistive technology list and the procedures in knowledge/testing/. It never tests, and never says what a user would experience.
---

# AT test protocol

This skill is a procedure and a map. The steps live in `knowledge/testing/`; the checks behind them live in `knowledge/wcag/` and `knowledge/patterns/`. The rules for citing are in the `wcag` skill and apply here unchanged.

## When this applies

A component or page is built, or about to be, and a person will test it. Also when the spec's "Open manual tests" or a need statement's "Manual tests owed" needs turning into steps someone can follow.

Two output shapes. A **script** (below) for one component. A **checklist** (`templates/at-test-checklist.md`) for one component or a whole page, for a developer to work through and tick off: use it when asked for one, or when several components are involved.

Scope comes from the request. If it names one component, such as "the rename dialog" or "the sign-up form", cover that component only; the page around it is only where the tester opens it.

## Principle 7, first

Doctor Accessible writes the script; a person runs it. The script says what to do, what to look or listen for, and what to record. It never says what a user "would experience", "would hear", or "would feel", and it never predicts a result. Write "note what is announced", not "the screen reader will say". The same goes for what will not be announced ("the color is not spoken") and for what a group of users "gets": the script says what to check, and a developer note says what the code exposes. Expected results are stated as conditions to check, tied to a criterion: "the control's name and state are read" (`wcag/sc-4.1.2-name-role-value.md`).

## Before anything else

Read the project's `a11y-spec.md`: repo root first, then `docs/`. Its "Who we are building for" section lists the assistive technology and browser pairs the team tests with. Write the script for exactly those. If there is no spec or no list, say so, propose a list from `templates/a11y-spec.md`'s examples matched to the audience, mark it "to confirm", and suggest the `planning` skill.

For a page, read what it is built from: the HTML, the scripts, and the styles, from the files or from the running page. A checklist is only as concrete as this reading.

## Building the script

1. **Identify the component** and its parts: controls, states, things that open or update, and any motion. For a page, list every component on it first and treat each in turn.
2. **Open the pattern entry** in `knowledge/patterns/` if one matches, and take its manual tests. If none matches, say "no pattern entry". For a native element, such as a form, table, or dialog, open its `knowledge/html/` entry and take what it says should be exposed: labels, groups, errors tied to their fields. Otherwise build from the testing entries alone.
3. **For each mode on the spec's list, open its testing entry** and take the setup and the steps that apply to this component. Do not paste the whole entry; select.
   - Keyboard only: `knowledge/testing/keyboard-only.md`
   - NVDA on Windows (and as the model for JAWS): `knowledge/testing/screen-reader-windows.md`
   - VoiceOver on macOS or iOS: `knowledge/testing/screen-reader-apple.md`
   - 200% and 400% zoom: `knowledge/testing/zoom.md`
   - Reduced motion: `knowledge/testing/reduced-motion.md`
   - Forced colors: `knowledge/testing/forced-colors.md`
   - Anything else on the list, such as TalkBack, JAWS-specific commands, voice control, or a screen magnifier: "no entry yet". Write generic steps, mark them unverified, and note the gap.
4. **Make each step concrete for this component.** Not "check focus order", but "Tab from the button that opens the dialog; note where focus lands".
5. **Attach the condition and the criterion** each step checks, from the entries. A step with no criterion behind it is marked manual review.
6. **Say what to record**, from the testing entry: tool and browser versions, what was done, what happened, pass or fail, and the tester.

## Building the checklist

Same steps, same rules, in the template's shape. Each item is a tick box, what to do, and "Expected:" with the pass condition and its entry. Group by mode in the spec's order, then by part of the page, or for one component by its parts: trigger, open state, fields, errors, close. List every control by name under "Enter and Space", and every status message under one item each. Leave out a mode with nothing to test, and say why in one line.

Then the **Watch for** section: likely problems from reading the code in scope, each with where it is in the code and the checklist item that confirms or rules it out. It points the tester at where to look. It is not a result, so the checklist items above it stay neutral: an item never says it will fail.

## Rules

1. Never state a criterion number, title, level, or keyboard command from memory. Open the entry. If there is no entry, say so and mark the step unverified. That holds for a criterion named only in passing, such as a Level AAA one: write "no entry yet" and "unverified" beside it, or leave it out.
2. One script per component, grouped by mode, in the order the spec lists the modes. A checklist covers what was asked for, one component or the whole page, in the same order.
3. Keep it to what a tester will actually do. A script nobody finishes is a test that did not happen.
4. Do not fix code and do not write code. If a step is likely to fail from what the code shows, say so in a note for the developer, separate from the script, or in the checklist's Watch for section.
5. Where the testing entry warns that a tester's unfamiliarity can look like a defect, keep that warning in the script.
6. Test every control the same way. If the entry says to try a control with Enter and with Space, write that step for each control, not only the first.
7. A checklist is a file. Draft it in the scratchpad, show the developer the path, and ask where it should live. Offer places outside any repo, such as beside the page's own files; write it there only when they say so.

## Output shape (script)

```
## Test script: <component> (<date>)
Spec AT list used: <pairs>, or "no spec; proposed list, to confirm"
Pattern entry: <patterns/x.md, or "no pattern entry">

### <Mode 1, e.g. Keyboard only, Chrome on Windows>
Setup: <from the testing entry>
1. <do this>. Check: <condition> (<wcag entry>).
2. ...

### <Mode 2> ...

### What to record
<fields, from the testing entries>

### Gaps
<modes on the list with no testing entry; steps marked unverified>
```

The checklist's shape is `templates/at-test-checklist.md`.

Close by pointing to the spec's "Open manual tests" section: propose adding the script or checklist with an owner and a date, and write it there only when the developer agrees.

## Where to look

| Question | Read |
|---|---|
| Which AT the project tests with | the project's `a11y-spec.md`; else `templates/a11y-spec.md` and the `planning` skill |
| Steps per mode | `knowledge/testing/`, listed in `knowledge/INDEX.md` |
| Manual tests a pattern demands | `knowledge/patterns/<pattern>.md` |
| What a native element should expose, when no pattern matches | `knowledge/html/<element>.md` |
| What a step checks | `knowledge/wcag/`, through `knowledge/INDEX.md` |
| The checklist's shape | `templates/at-test-checklist.md` |
| Why the script never speaks as a user | `docs/principles.md`, principle 7 |
