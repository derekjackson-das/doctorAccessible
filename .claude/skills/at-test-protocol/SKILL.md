---
name: at-test-protocol
description: The human testing mode. Use when a component, page, or feature needs manual testing with assistive technology, when a need statement or the spec lists manual tests owed, or when someone asks how to test something with a keyboard, screen reader, zoom, reduced motion, or forced colors. Writes a numbered test script a person follows, built from the project spec's assistive technology list and the procedures in knowledge/testing/. It never tests, and never says what a user would experience.
---

# AT test protocol

This skill is a procedure and a map. The steps live in `knowledge/testing/`; the checks behind them live in `knowledge/wcag/` and `knowledge/patterns/`. The rules for citing are in the `wcag` skill and apply here unchanged.

## When this applies

A component or page is built, or about to be, and a person will test it. Also when the spec's "Open manual tests" or a need statement's "Manual tests owed" needs turning into steps someone can follow.

## Principle 7, first

Doctor Accessible writes the script; a person runs it. The script says what to do, what to look or listen for, and what to record. It never says what a user "would experience", "would hear", or "would feel", and it never predicts a result. Write "note what is announced", not "the screen reader will say". The same goes for what will not be announced ("the color is not spoken") and for what a group of users "gets": the script says what to check, and a developer note says what the code exposes. Expected results are stated as conditions to check, tied to a criterion: "the control's name and state are read" (`wcag/sc-4.1.2-name-role-value.md`).

## Before anything else

Read the project's `a11y-spec.md`: repo root first, then `docs/`. Its "Who we are building for" section lists the assistive technology and browser pairs the team tests with. Write the script for exactly those. If there is no spec or no list, say so, propose a list from `templates/a11y-spec.md`'s examples matched to the audience, mark it "to confirm", and suggest the `planning` skill.

## Building the script

1. **Identify the component** and its parts: controls, states, things that open or update, and any motion.
2. **Open the pattern entry** in `knowledge/patterns/` if one matches, and take its manual tests. If none matches, say "no pattern entry" and build from the testing entries alone.
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

## Rules

1. Never state a criterion number, title, level, or keyboard command from memory. Open the entry. If there is no entry, say so and mark the step unverified. That holds for a criterion named only in passing, such as a Level AAA one: write "no entry yet" and "unverified" beside it, or leave it out.
2. One script per component, grouped by mode, in the order the spec lists the modes.
3. Keep it to what a tester will actually do. A script nobody finishes is a test that did not happen.
4. Do not fix code and do not write code. If a step is likely to fail from what the code shows, say so in a note for the developer, separate from the script.
5. Where the testing entry warns that a tester's unfamiliarity can look like a defect, keep that warning in the script.
6. Test every control the same way. If the entry says to try a control with Enter and with Space, write that step for each control, not only the first.

## Output shape

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

Close by pointing to the spec's "Open manual tests" section: propose adding the script with an owner and a date, and write it there only when the developer agrees.

## Where to look

| Question | Read |
|---|---|
| Which AT the project tests with | the project's `a11y-spec.md`; else `templates/a11y-spec.md` and the `planning` skill |
| Steps per mode | `knowledge/testing/`, listed in `knowledge/INDEX.md` |
| Manual tests a pattern demands | `knowledge/patterns/<pattern>.md` |
| What a step checks | `knowledge/wcag/`, through `knowledge/INDEX.md` |
| Why the script never speaks as a user | `docs/principles.md`, principle 7 |
