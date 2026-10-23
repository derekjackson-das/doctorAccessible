# ARIA pattern: Modal dialog

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Dialog (Modal) Pattern", no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/ A pattern, not a requirement: nothing in it is a conformance rule, and following it does not guarantee that assistive technology supports it.
- Normative (tier 1):
  - WAI-ARIA 1.2, `dialog` role, W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/#dialog. Name from author; an accessible name is required; authors should give every dialog at least one focusable descendant and should focus an element in a modal dialog when it is displayed.
  - ARIA in HTML, `dialog` element row, W3C Recommendation 11 August 2026, https://www.w3.org/TR/html-aria/. Implicit `role=dialog`; `alertdialog` may be set (`dialog` itself is allowed but not recommended).
- Practitioner testing (tier 3): the sources and their full results are in `patterns/modal-dialog.md`. This entry adds only what bears on the ARIA:
  - Adrian Roselli, "Dialog Focus in Screen Readers", 12 October 2020, updates to 6 June 2025. https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html Announcements for focus on a custom `role="dialog"` container, its heading, or its close button: JAWS 2020 and NVDA 2020.2 with Chrome 85 and Firefox 81, VoiceOver on macOS 10.15.6 and iOS 14, TalkBack on Android 11. His 18 December 2024 update covers `aria-modal` with the native element.
  - Scott O'Hara, "Having an open dialog (archival post)", 5 March 2019, updated 26 January 2023. https://www.scottohara.me/blog/2019/03/05/open-dialog.html Includes `aria-modal` with VoiceOver on iOS 15.0.2, from his early 2022 retest.
- Related entries: `patterns/modal-dialog.md` (whether to use a modal, the native element, the criteria, the manual tests), `aria/using-aria.md`, `aria/accessible-name.md`, `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

The criteria in `patterns/modal-dialog.md` decide whether code fails WCAG; report a failure once, under its criterion. Departing from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier. A custom `role="dialog"` where the native element would do is advice, never a finding on its own (`aria/using-aria.md`).

**Testing gap.** The listed screen reader tests of custom ARIA dialogs are from 2020 (Roselli) and 2019 to early 2022 (O'Hara), none within three years. No listed source reports a current test of `aria-modal` with VoiceOver on iOS or with TalkBack. Test with the spec's assistive technology before relying on any result here.

## Native first

`dialog` opened with `showModal()` supplies the role, the modality, and closing on Escape. In January 2023 the HTML standard also defined where it puts initial focus (O'Hara, 2023); no listed source has tested that in browsers. The case for the native element, and what it costs, is in `patterns/modal-dialog.md`.

## Roles, states, and properties

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|
| Dialog container | `dialog` (the `dialog` element gives it) | `aria-labelledby` pointing at the visible title, or `aria-label` | Author | A name is required for the role |
| Dialog container | | `aria-modal="true"` | Author, custom dialogs only | Not needed with `showModal()` (Roselli, 18 December 2024 update) |
| Dialog container | | `aria-describedby`, optional | Author | Only for short, plain messages (APG) |
| Page outside the dialog | | inert (the `inert` attribute, or `showModal()`) | Script | Legacy builds used `aria-hidden="true"` on the rest of the page; the dialog must not be inside it (APG) |
| Close control | `button` | a name, such as "Close" | Author | The APG strongly recommends a visible close button in the tab sequence |

**`aria-modal` is a promise the page must keep.** The APG warns that it can stop some assistive technology from perceiving anything outside the dialog. So set it only when script really prevents interaction outside the dialog and the styling obscures it.

## Naming

The dialog takes its name from `aria-labelledby` pointing at its heading, so the visible title and the name match (`aria/accessible-name.md`). `aria-label` only when there is no visible title. A description from `aria-describedby` is announced with the name when the dialog opens; the APG advises leaving it off when the content has structure, such as lists or several paragraphs, because it is read as one unbroken string.

## Keyboard

From the APG pattern, in our words:

- On open, focus moves inside the dialog. Usually to the first focusable element, but to a static element at the top, given `tabindex="-1"`, when the content is long or structured, and to the least destructive button when the action is hard to undo. WAI-ARIA 1.2 says the same for modal dialogs, as a "should".
- Tab and Shift+Tab cycle inside the dialog.
- Escape closes it.
- On close, focus returns to the control that opened it, unless that control is gone or the workflow makes another place more logical.

## What testing found

ARIA-specific results only; the rest are in `patterns/modal-dialog.md`.

- **VoiceOver on iOS could leave an `aria-modal` dialog** by ordinary swiping and reach the page behind it, on iOS 15.0.2 (O'Hara, early 2022).
- **Focus on the close button lost the dialog's name on TalkBack.** In Roselli's 2020 tests, the desktop pairings announced the dialog's name whichever of the container, heading, or close button had focus. TalkBack with Chrome on Android 11 announced only "Close, button" when the close button was focused.
- **`aria-modal` is redundant with `showModal()`,** which makes the dialog modal itself (Roselli, 18 December 2024 update).

## How it fails in code

- `role="dialog"` with `aria-modal="true"`, but script never moves focus into it on open, so focus is left on the trigger or lost: `wcag/sc-2.4.3-focus-order.md`, likely from code, definite once observed.
- No way to close by keyboard, with focus held inside: `wcag/sc-2.1.2-no-keyboard-trap.md`, definite.
- The dialog inside an element with `aria-hidden="true"`: its controls are focusable but hidden from assistive technology (`aria/using-aria.md`, rule 4). Report under the criterion its effect breaks, usually 4.1.2, at that entry's confidence.
- `aria-modal="true"` on a dialog that leaves the rest of the page usable: advice, citing the APG warning and O'Hara's iOS result, unless a criterion entry ties the result to a barrier.
- No name on the dialog: WAI-ARIA requires one, but the 4.1.2 entry has no case for an unnamed dialog, so this is manual review, citing the role definition.
