# Pattern: Modal dialog

- Sources:
  - W3C, "Dialog (Modal) Pattern", ARIA Authoring Practices Guide, https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/. Tier 2. A pattern, not a requirement.
  - Adrian Roselli, "Dialog Focus in Screen Readers", 12 October 2020, updated 6 June 2025, https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html. Tier 3.
  - Adrian Roselli, "Where to Put Focus When Opening a Modal Dialog", 6 June 2025, updated 23 April 2026, https://adrianroselli.com/2025/06/where-to-put-focus-when-opening-a-modal-dialog.html. Tier 3.
  - Adrian Roselli, "Should a Dialog Close When Clicked Outside?", 12 August 2026, https://adrianroselli.com/2026/08/should-a-dialog-close-when-clicked-outside.html. Tier 3.
  - Scott O'Hara, "Use the dialog element (reasonably)", 26 January 2023, https://www.scottohara.me/blog/2023/01/26/use-the-dialog-element.html. Tier 3.
- Related entries: `ux/modals-and-interruptions.md`, `coga/objective-5-help-users-focus.md`, `coga/objective-4-avoid-mistakes.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.4.11-focus-not-obscured-minimum.md`, `wcag/sc-3.3.4-error-prevention-legal-financial-data.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the dialog is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer.

## The need it usually serves

Something must be decided or supplied before the person goes on: confirm a deletion, agree to terms, enter a missing value, read a warning. The dialog stops everything else so that one thing gets dealt with. Most dialogs in the wild are not that; they are messages that could have been on the page.

## The simpler thing that often serves, and what is lost

An inline message, a banner, or a separate page. `ux/modals-and-interruptions.md` carries the research: a modal costs the person their place, people dismiss popups on reflex, and timing is the usual failure. What is lost by not using a modal: the guarantee that the person saw it before continuing. For a destructive or irreversible action that guarantee is worth having; for anything else it is usually not. Roselli (2026) adds that when the task in the dialog might need information from the page behind it, such as a footer link or an on-screen error, a standalone page serves better than a modal.

## What doing it right requires

Native first: the HTML `dialog` element opened with its modal method gives inert content behind, a contained tab sequence, Escape to close, and initial focus handling for free. O'Hara (2023) marks the point at which the HTML specification settled how the element places initial focus and argues it is time to use it instead of custom dialogs, while allowing that a project's browser support needs may say otherwise. The 2.4.3 entry lists the W3C technique for this.

The APG pattern's expectations, in our words: content outside the dialog is inert; Tab and Shift+Tab cycle inside the dialog and never leave it; Escape closes it; when it opens, focus moves to something inside it; when it closes, focus returns to what opened it. The APG's own notes on initial focus say the right target depends on the content.

What the APG does not say: where exactly to put focus. Roselli (2025) argues that every blanket rule is wrong, including his own, and offers a method: for a short message, the dialog itself or its heading; where the person must choose, the least destructive option, which should be the close button. Nor does the APG settle whether clicking outside should close the dialog; Roselli (2026) says it depends, and that a dialog the person must complete should not close by accident, by Escape, or by an outside click, and probably should not be a modal at all if they might need the page behind it.

## What practitioners found when they tested it

- **Roselli, 2020, updated 2025.** Test matrix: JAWS 2020 and NVDA 2020.2 with Chrome 85 and Firefox 81 on Windows 10, VoiceOver on macOS Catalina with Safari and Chrome, TalkBack on Android 11, VoiceOver on iOS 14 with Safari, all at default settings, activating a button and recording what was spoken. Focusing an element inside the dialog exposed the dialog's role and name in NVDA with Firefox, JAWS with Chrome, and VoiceOver on macOS with Safari, with wording that differed by pair ("Frank modal dialog", "Frank dialog, selected", "Frank, web dialog"). TalkBack with Chrome announced the dialog on entry but read the heading and close button without the dialog context. He singles out iOS 14 as the problem case. His point: teams rarely know what a screen reader will say, and should test rather than assume.
- **O'Hara, 2023.** The native element's initial-focus behavior was undefined for years and that uncertainty drove custom dialogs; the specification change resolved it. Non-modal dialogs still had open questions.

## Criteria it touches

Getting out: `wcag/sc-2.1.2-no-keyboard-trap.md`. Focus in and back: `wcag/sc-2.4.3-focus-order.md`. Name and role of the dialog and its controls: `wcag/sc-4.1.2-name-role-value.md`. A dialog that opens on focus or on input: `wcag/sc-3.2.1-on-focus.md`, `wcag/sc-3.2.2-on-input.md`. Focus visible inside and not covered: `wcag/sc-2.4.7-focus-visible.md`, `wcag/sc-2.4.11-focus-not-obscured-minimum.md`. Reflow of the dialog at 320 CSS pixels: `wcag/sc-1.4.10-reflow.md`. A confirmation dialog as the "Confirmed" route: `wcag/sc-3.3.4-error-prevention-legal-financial-data.md`. Dismissal without moving focus if it appears on hover or focus: `wcag/sc-1.4.13-content-on-hover-or-focus.md`.

## Manual tests it demands

- Keyboard: open the dialog; record where focus lands. Tab past the last control; record that focus wraps inside. Press Escape; record that it closes and where focus returns.
- Screen reader, each pair in the spec: open the dialog; record what is announced, in Roselli's words, exactly. Try to read content behind the dialog with the virtual cursor; record whether it is reachable.
- Click or tap outside; record what happens, and whether that matches the dialog's purpose.
- 400% zoom and 320 CSS pixels: record whether the dialog fits, scrolls, and keeps its close control reachable.

## What consult should say

1. What happens if the person does not see this? If the answer is "nothing much", it is not a modal.
2. Will they need anything from the page behind it to finish? If yes, a page, not a modal.
3. If a modal stays: the native `dialog` element, focus to the least destructive choice, and a decision on outside-click recorded in the spec.

See `ux/modals-and-interruptions.md` for the research and the nonmodal alternatives.
