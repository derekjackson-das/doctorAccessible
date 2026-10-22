# COGA Objective 7: Provide help and support

- Source: W3C, Making Content Usable for People with Cognitive and Learning Disabilities, Working Group Note, 29 April 2021
- Tier: 2, informative from W3C. A Working Group Note is guidance, not a conformance requirement. Meeting it is not needed to conform to WCAG 2.2, and missing it is not a WCAG failure.
- Objective: https://www.w3.org/TR/coga-usable/#x4-8-objective-7-provide-help-and-support
- User stories: https://www.w3.org/TR/coga-usable/#x3-7-objective-7-provide-help-and-support
- User-need map: https://www.w3.org/TR/coga-usable/#a-7-objective-7-provide-help-and-support
- Verified against the live source: 2026-10-22 by Caesar Alam with Claude Code, direct fetch of the Note and of the WCAG 2.2 Recommendation for every criterion cited

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. When the same defect also fails a WCAG criterion, report it once, under that criterion and its entry, and name this entry as context.

## The objective in plain words

Make help easy to find from anywhere a person might get stuck, and make a human reachable in few steps through the channel the person prefers. Support understanding in more than one way: summaries, pictures, examples, and plain explanations of what each choice means and what it costs. Help with forms and unusual controls, with directions, and with remembering what comes next. Feedback channels matter too: if a person cannot report a problem, the site never learns it has one.

## User needs it serves

- **Help.** People who find sites hard need to ask for help and give feedback from any point, on the same timeline as others, through a channel they can use, and to reach a person easily.
- **Support.** People who struggle with text need in-page support they control: symbols, graphs and pictures beside text, read-aloud with highlighting, clear confirmation when something happens, and reminders they set up themselves. Help must look different from the main content.
- **Directions.** People whose disabilities affect navigation and sequencing need help with routes and directions.
- **Cognitive stress.** People affected by busy, confusing, or upsetting content need simple, consistent content, a way to avoid triggers, fewer chances for error, and confidence that they are safe.
- **Task management.** People with executive function impairments or difficulty with numbers need explanations of unusual controls, the pros and cons of each choice, and, before starting, the steps, time, materials, and limits involved.

## Patterns W3C lists

- [Provide human help](https://www.w3.org/TR/coga-usable/#x4-8-1-provide-human-help-pattern): easy to find on every page and step, through the user's preferred channel, in as few steps as possible.
- [Provide alternative content for complex information and tasks](https://www.w3.org/TR/coga-usable/#x4-8-2-provide-alternative-content-for-complex-information-and-tasks-pattern): summaries, step-by-step versions, charts, familiar symbols, and well-structured video alongside complex text.
- [Clearly state the results and disadvantages of actions, options, and selections](https://www.w3.org/TR/coga-usable/#x4-8-3-clearly-state-the-results-and-disadvantages-of-actions-options-and-selections-pattern): benefits, risks, and consequences of each option, including what differs from what the user asked for.
- [Provide help for forms and non-standard controls](https://www.w3.org/TR/coga-usable/#x4-8-4-provide-help-for-forms-and-non-standard-controls-pattern): explanations and examples for complex forms and unusual controls.
- [Make it easy to find help and give feedback](https://www.w3.org/TR/coga-usable/#x4-8-5-make-it-easy-to-find-help-and-give-feedback-pattern): simple feedback forms, reachable wherever a user may get stuck.
- [Provide help with directions](https://www.w3.org/TR/coga-usable/#x4-8-6-provide-help-with-directions-pattern): recognizable landmarks, stable routes, help reorienting, personalizable terms for distance and direction.
- [Provide reminders](https://www.w3.org/TR/coga-usable/#x4-8-7-provide-reminders-pattern): reminders only at the user's request, through standard interfaces where possible, in a form the user chooses.

## WCAG criteria that touch it

Numbers, titles, and levels checked against the WCAG 2.2 Recommendation of 12 December 2024. Level AAA rows are not our target; they show how far WCAG reaches.

| SC | Title | Level | Entry | Overlap |
|---|---|---|---|---|
| 3.2.6 | Consistent Help | A | `wcag/sc-3.2.6-consistent-help.md` | When help mechanisms repeat across pages, they stay in the same relative order; new in WCAG 2.2 |
| 3.3.2 | Labels or Instructions | A | `wcag/sc-3.3.2-labels-or-instructions.md` | Labels or instructions when input is required |
| 4.1.3 | Status Messages | AA | `wcag/sc-4.1.3-status-messages.md` | Confirmation messages reach assistive technology without focus |
| 1.1.1 | Non-text Content | A | `wcag/sc-1.1.1-non-text-content.md` | Supporting images and charts need text alternatives |
| 3.3.5 | Help | AAA | no entry yet | Context-sensitive help is available |

## Where WCAG stops

Consistent Help applies only if help exists; WCAG does not require a site to offer help, a human contact, or a feedback channel at all. It does not require alternative versions of complex content, plain statements of what a choice will cost or lose, help with non-standard controls beyond a label or instruction, or reminders. Context-sensitive help is AAA.

## How it is used

- **Consult** asks where a person in the spec would get stuck and how they would reach a human from there.
- **Verify** might report: a help link present on some pages and missing from a form step where errors are likely (manual review, this entry; 3.2.6 checked for order where help does repeat); a pricing option that hides what is excluded (likely, this entry); a contact path that requires an account (manual review).
- **ux** entries, when they exist, carry the evidence on support channels.
