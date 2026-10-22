# COGA Objective 6: Ensure processes do not rely on memory

- Source: W3C, Making Content Usable for People with Cognitive and Learning Disabilities, Working Group Note, 29 April 2021
- Tier: 2, informative from W3C. A Working Group Note is guidance, not a conformance requirement. Meeting it is not needed to conform to WCAG 2.2, and missing it is not a WCAG failure.
- Objective: https://www.w3.org/TR/coga-usable/#x4-7-objective-6-ensure-processes-do-not-rely-on-memory
- User stories: https://www.w3.org/TR/coga-usable/#x3-6-objective-6-ensure-processes-do-not-rely-on-memory
- User-need map: https://www.w3.org/TR/coga-usable/#a-6-objective-6-ensure-processes-do-not-rely-on-memory
- Verified against the live source: 2026-10-22 by Caesar Alam with Claude Code, direct fetch of the Note and of the WCAG 2.2 Recommendation for every criterion cited

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. When the same defect also fails a WCAG criterion, report it once, under that criterion and its entry, and name this entry as context. Two WCAG 2.2 criteria, 3.3.7 and 3.3.8, came out of this work and are requirements at our target; check them first.

## The objective in plain words

Do not make people remember, copy, or calculate to get through a process. Logging in, registering, and recovering an account should work without memorizing a password, transcribing a code, solving a puzzle, or reading a lot of text. Information a person gave earlier in a process should still be in front of them when they need it again. Phone menus should let a caller reach a person without remembering which number meant what.

## User needs it serves

- **Remembering from previous steps.** People with short-term and working memory impairments need processes that show them what they entered earlier rather than asking them to recall it.
- **Accessible authentication.** People who forget passwords or have impaired executive function need to sign in without remembering or transcribing passwords, codes, or usernames, without many steps, without puzzles or calculations, and without much text.
- **Voice menus.** People with memory or language processing impairments need to reach a human easily, hear the option before its number, have time to respond, and go back without starting over. Voice menus are outside a web page, but sites often send people to them.

## Patterns W3C lists

- [Provide a login that does not rely on memory or other cognitive skills](https://www.w3.org/TR/coga-usable/#x4-7-1-provide-a-login-that-does-not-rely-on-memory-or-other-cognitive-skills-pattern): no memorized strings, calculations, copying, puzzles, gestures, or retyping characters shown on screen, for login, registration, and reset.
- [Allow the user a simple, single step, login](https://www.w3.org/TR/coga-usable/#x4-7-2-allow-the-user-a-simple-single-step-login-pattern): at least one single-step option.
- [Provide a login alternative with less words](https://www.w3.org/TR/coga-usable/#x4-7-3-provide-a-login-alternative-with-less-words-pattern): at least one option that needs little reading or writing.
- [Let users avoid navigating voice menus](https://www.w3.org/TR/coga-usable/#x4-7-4-let-users-avoid-navigating-voice-menus-pattern): a reserved key or word that reaches a person at any time; few options; no promotions; patient timing.
- [Do not rely on users calculations or memorizing information](https://www.w3.org/TR/coga-usable/#x4-7-5-do-not-rely-on-users-calculations-or-memorizing-information-pattern): no remembering, copying, calculating, or fast response anywhere in a process.

## WCAG criteria that touch it

Numbers, titles, and levels checked against the WCAG 2.2 Recommendation of 12 December 2024. Level AAA rows are not our target; they show how far WCAG reaches.

| SC | Title | Level | Entry | Overlap |
|---|---|---|---|---|
| 3.3.8 | Accessible Authentication (Minimum) | AA | no entry yet | No cognitive function test at any authentication step unless an alternative, an assisting mechanism, object recognition, or personal content is offered |
| 3.3.7 | Redundant Entry | A | no entry yet | Information already given in the same process is filled in or selectable, with stated exceptions |
| 1.3.5 | Identify Input Purpose | AA | `wcag/sc-1.3.5-identify-input-purpose.md` | Fields about the user carry `autocomplete`, which password managers and autofill rely on |
| 2.2.1 | Timing Adjustable | A | `wcag/sc-2.2.1-timing-adjustable.md` | Time limits, including on one-time codes, can be adjusted or extended |
| 3.3.9 | Accessible Authentication (Enhanced) | AAA | no entry yet | As 3.3.8 without the object-recognition and personal-content exceptions |

## Where WCAG stops

3.3.8 is satisfied when a password field allows paste and password managers. That still leaves a person who does not use a password manager facing a password. WCAG does not require a single-step or low-text login option, does not cover registration questions that test memory outside authentication, allows object-recognition puzzles at AA, does not cover voice menus, and does not reach calculations or copying elsewhere in a process (such as copying a reference number from one page to another) unless 3.3.7 applies to the same process.

## How it is used

- **Verify** reports WCAG failures first: a password field that blocks paste, or a text CAPTCHA with no alternative, is definite under 3.3.8 once its entry exists. Under this entry: a process that shows a reference number on one page and asks for it on a later page outside the same process (likely); a login with no option beyond username and password, when a password manager works (manual review).
- **Consult** asks whether the audience in the spec can be expected to manage passwords, and whether an email link or passkey option is possible.
