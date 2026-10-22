# COGA Objective 5: Help users focus

- Source: W3C, Making Content Usable for People with Cognitive and Learning Disabilities, Working Group Note, 29 April 2021
- Tier: 2, informative from W3C. A Working Group Note is guidance, not a conformance requirement. Meeting it is not needed to conform to WCAG 2.2, and missing it is not a WCAG failure.
- Objective: https://www.w3.org/TR/coga-usable/#x4-6-objective-5-help-users-focus
- User stories: https://www.w3.org/TR/coga-usable/#x3-5-objective-5-help-users-focus
- User-need map: https://www.w3.org/TR/coga-usable/#a-5-objective-5-help-users-focus
- Verified against the live source: 2026-10-22 by Caesar Alam with Claude Code, direct fetch of the Note and of the WCAG 2.2 Recommendation for every criterion cited

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. When the same defect also fails a WCAG criterion, report it once, under that criterion and its entry, and name this entry as context.

## The objective in plain words

Keep people on their task. Remove what pulls attention away, let people turn off what remains, and keep the path to a goal short. Before a long task, say how long it takes and what to have ready. When attention is lost anyway, headings, breadcrumbs, and progress indicators let a person pick up where they left off. "Focus" here means a person's attention, not keyboard focus.

## User needs it serves

- **Distractions.** People with attention impairments and impaired memory need tasks free of distraction, an easy way to switch off what distracts them, a clear start and end to each task, and a way to recover context after losing focus: where they are, what they just did, and what comes next.

## Patterns W3C lists

- [Limit interruptions](https://www.w3.org/TR/coga-usable/#x4-6-1-limit-interruptions-pattern): let users control pop-ups, reminders, and changing content, except emergencies; let them limit distracting content such as ads, social feeds, moving images, and sound.
- [Make short critical paths](https://www.w3.org/TR/coga-usable/#x4-6-2-make-short-critical-paths-pattern): only the necessary steps; optional steps separated and skippable.
- [Avoid too much content](https://www.w3.org/TR/coga-usable/#x4-6-3-avoid-too-much-content-pattern): few main choices per screen; extras moved to the footer or behind a clearly named "more"; a simplified version where possible.
- [Provide information so a user can complete and prepare for a task](https://www.w3.org/TR/coga-usable/#x4-6-4-provide-information-so-a-user-can-complete-and-prepare-for-a-task-pattern): time estimate, resources needed, and an overview before starting; clear signs of in progress and done.

## WCAG criteria that touch it

Numbers, titles, and levels checked against the WCAG 2.2 Recommendation of 12 December 2024. Level AAA rows are not our target; they show how far WCAG reaches.

| SC | Title | Level | Entry | Overlap |
|---|---|---|---|---|
| 2.2.2 | Pause, Stop, Hide | A | `wcag/sc-2.2.2-pause-stop-hide.md` | Moving, blinking, scrolling, and auto-updating content can be paused, stopped, or hidden |
| 1.4.2 | Audio Control | A | `wcag/sc-1.4.2-audio-control.md` | Audio that plays automatically can be paused or turned down |
| 2.3.1 | Three Flashes or Below Threshold | A | `wcag/sc-2.3.1-three-flashes-or-below-threshold.md` | Flashing limits, for seizure safety rather than attention |
| 3.2.1 | On Focus | A | `wcag/sc-3.2.1-on-focus.md` | Receiving keyboard focus does not change context |
| 2.4.11 | Focus Not Obscured (Minimum) | AA | `wcag/sc-2.4.11-focus-not-obscured-minimum.md` | Banners and chat widgets must not entirely hide the focused component; new in WCAG 2.2 |
| 2.2.4 | Interruptions | AAA | no entry yet | Interruptions can be postponed or suppressed, except emergencies |
| 2.4.8 | Location | AAA | no entry yet | Where the user is within a set of pages |
| 3.2.5 | Change on Request | AAA | no entry yet | Changes of context only on request, or can be turned off |

## Where WCAG stops

WCAG at A and AA lets users stop motion and sound once it starts. It does not limit pop-ups, chat prompts, cookie banners, or promotions that break into a task (suppressing interruptions is AAA), the number of choices on a screen, the length of a path to a goal, or the presence of side content. It does not ask that a task tells people what they need before they begin. A page with a newsletter modal, a chat bubble, and twelve calls to action can conform, as long as none of them entirely hides the component with keyboard focus.

## How it is used

- **Consult** challenges every element that is not part of the task the need statement names, and asks whether a modal, banner, or carousel is needed at all. "Build less" is often the answer here.
- **Verify** might report: a modal that opens unprompted over a form in progress (likely, this entry); a multi-step task with no statement of what to have ready (manual review); auto-advancing content that starts on its own, runs longer than five seconds alongside other content, and has no pause control (definite under 2.2.2, not under this entry).
- **patterns** entries for carousel, modal dialog, and infinite scroll, when they exist, link here.
