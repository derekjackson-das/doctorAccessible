# ARIA pattern: Modal dialog

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Dialog (Modal) Pattern", no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/ A pattern, not a requirement: nothing in it is a conformance rule, and following it does not guarantee that assistive technology supports it.
- Normative (tier 1): WAI-ARIA 1.2, `dialog` role (name from author; an accessible name is required), W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/#dialog. ARIA in HTML, `dialog` element row (implicit `role=dialog`; `alertdialog` the only other role allowed), W3C Recommendation 11 August 2026, https://www.w3.org/TR/html-aria/
- Practitioner testing (tier 3):
  - Adrian Roselli, "Dialog Focus in Screen Readers", 12 October 2020, updates to 6 June 2025. https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html What each screen reader announced when focus went to a custom `role="dialog"` container, its heading, or its close button: JAWS 2020 and NVDA 2020.2 with Chrome 85 and Firefox 81, VoiceOver on macOS 10.15.6 and iOS 14, TalkBack on Android 11. The 18 December 2024 update covers `aria-modal` with the native element.
  - Scott O'Hara, "Having an open dialog (archival post)", 5 March 2019, updated 26 January 2023. https://www.scottohara.me/blog/2019/03/05/open-dialog.html Native `<dialog>` and its polyfill with JAWS, NVDA, VoiceOver on macOS and iOS, and TalkBack, retested 2021 and early 2022, including `aria-modal` on iOS 15.
  - Scott O'Hara, "Use the dialog element (reasonably)", 26 January 2023. https://www.scottohara.me/blog/2023/01/26/use-the-dialog-element.html His current recommendation; not a test report.
- Related entries: `patterns/modal-dialog.md` (whether to use a modal, the criteria, the manual tests), `aria/using-aria.md`, `aria/accessible-name.md`, `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

The criteria in `patterns/modal-dialog.md` decide whether code fails WCAG; report a failure once, under its criterion. Departing from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier. A custom `role="dialog"` where the native element would do is advice, never a finding on its own (`aria/using-aria.md`).

**Testing gap.** The listed screen reader tests of custom ARIA dialogs are from 2020 (Roselli) and 2019 to early 2022 (O'Hara). Neither is within three years for desktop screen readers. No listed source reports a current test of `aria-modal` with VoiceOver on iOS, or with TalkBack. Test with the spec's assistive technology before relying on any announcement described here.

## Native first

The `dialog` element opened with `showModal()` gives the dialog role, makes the rest of the page inert, closes on Escape, and, since the HTML change of January 2023 that both O'Hara and Roselli report, puts initial focus on the first element in the tab order, or on the dialog itself if it has `autofocus` or nothing inside can take focus. O'Hara's 2023 view is that the native element is now generally the better choice, with `role="dialog"` kept for cases that need it. What is lost: some control over initial focus, and older browsers. See `patterns/modal-dialog.md`.

## Roles, states, and properties

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|
| Dialog container | `dialog` (native `dialog` gives it) | `aria-labelledby` pointing at the visible title, or `aria-label` | Author | A name is required for the role |
| Dialog container | | `aria-modal="true"` | Author, custom dialogs only | Not needed with `showModal()` (Roselli, 18 December 2024 update) |
| Dialog container | | `aria-describedby`, optional | Author | Only for short, plain messages (APG) |
| Page outside the dialog | | inert (the `inert` attribute, or `showModal()`) | Script | Legacy builds used `aria-hidden="true"` on the rest of the page; the dialog must not be inside it (APG) |
| Close control | `button` | a name, such as "Close" | Author | APG strongly recommends a visible close button in the tab sequence |

## Naming

The dialog takes its name from `aria-labelledby` pointing at its heading, so the visible title and the name match (`aria/accessible-name.md`). `aria-label` only when there is no visible title. A description from `aria-describedby` is read with the name when the dialog opens. The APG and Roselli both advise leaving it off when the content has structure, such as lists or several paragraphs, because it is read as one unbroken string.

## Keyboard

From the APG pattern, in our words:

- On open, focus moves inside the dialog. Usually to the first focusable element, but to a static element at the top, given `tabindex="-1"`, when the content is long or structured, and to the least destructive button when the action is hard to undo.
- Tab and Shift+Tab cycle inside the dialog.
- Escape closes it.
- On close, focus returns to the control that opened it, unless that control is gone or the workflow makes another place more logical.

## What testing found

- **`aria-modal` is a promise the page must keep.** The APG warns that marking a dialog modal hides the rest of the page from some assistive technology. So it should be set only when the page really prevents interaction outside the dialog and visually obscures it.
- **iOS VoiceOver could leave an `aria-modal` dialog** by ordinary swiping, reaching the page behind it, on iOS 15.0.2 (O'Hara, retest of early 2022).
- **Where focus lands changes what is announced.** In Roselli's 2020 tests, every desktop pairing announced the dialog's name whichever of the three targets was focused, but how much else was read varied widely. NVDA with Firefox read the whole content. TalkBack with Chrome announced only "Close, button" when the close button was focused, with no dialog name. His conclusion: test with your users; no single target is right.
- **`aria-modal` is redundant with `showModal()`,** which provides modality itself (Roselli, 18 December 2024 update).

## How it fails in code

- `role="dialog"` with `aria-modal="true"`, but script never moves focus into it on open. Focus stays on the trigger behind it: `wcag/sc-2.4.3-focus-order.md`, likely from code and definite once observed.
- No way to close by keyboard, with focus held inside: `wcag/sc-2.1.2-no-keyboard-trap.md`, definite.
- The dialog inside an element with `aria-hidden="true"`: its contents are hidden while focusable (`aria/using-aria.md`, rule 4), so the controls inside lose their role and name for a screen reader. Report under the criterion its effect breaks, usually 4.1.2.
- `aria-modal="true"` on a dialog that does not make the rest of the page inert: advice, with the APG and O'Hara findings, unless a criterion entry ties the result to a barrier.
- No name on the dialog: required by WAI-ARIA. The 4.1.2 entry has no case for an unnamed dialog, so this is manual review, citing the role definition.
