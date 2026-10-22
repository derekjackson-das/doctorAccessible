# Pattern: Modal dialog

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Dialog (Modal) Pattern", accessed 2026-10-22 (the page shows no date). https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/ A pattern, not a requirement.
- W3C tutorial: none.
- Practitioner sources (tier 3, on `knowledge/SOURCES.md`):
  - Adrian Roselli, "Dialog Focus in Screen Readers", 12 October 2020, updated 6 June 2025. https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html Tested where initial focus lands in a custom dialog (built with the inert polyfill, not the native element), with JAWS 2020 and NVDA 2020.2 on Windows, VoiceOver on macOS and iOS 14, and TalkBack on Android 11. His 2023 update checked native `<dialog>` focus in Windows browsers only.
  - Scott O'Hara, "Having an open dialog (archival post)", 5 March 2019, updated 26 January 2023. https://www.scottohara.me/blog/2019/03/05/open-dialog.html Tested the native `<dialog>` element and its polyfill with JAWS, NVDA, VoiceOver on macOS and iOS, and TalkBack, in 2019, with retests in 2021 and early 2022. He marks it archival and points to his 2023 post.
  - Scott O'Hara, "Use the dialog element (reasonably)", 26 January 2023. https://www.scottohara.me/blog/2023/01/26/use-the-dialog-element.html His current recommendation; not a test report.
- Related entries: `ux/modals-and-interruptions.md` (when a modal is justified at all), `wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-4.1.2-name-role-value.md`, `coga/objective-5-help-users-focus.md`; `aria/` once that domain exists.
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

The criteria listed below decide whether code fails WCAG; report a failure once, under its criterion. Everything else here is advice. Using this pattern, or not using the simpler alternative, is never a finding on its own. A departure from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier.

**Testing gap.** The screen reader results on the list date from 2019 to early 2022. None tests the native `<dialog>` element opened with `showModal()` after the 2023 change to how it places initial focus, and none covers voice control or magnification. a11ysupport.io, also on the list, renders its results with script and could not be read for this entry; check it for tests updated within the last three years.

## The need

Stopping someone before an action that destroys work or cannot be undone, or asking for something the system needs to finish a task the person started. Often it is used instead for promotions, sign-ups, and content that could be a page; `ux/modals-and-interruptions.md` covers when a modal is justified.

## The simpler alternative and its cost

- **Put it on the page.** An inline confirmation, a message next to the control, or a disclosure that expands in place. The cost: the page layout has to make room, and a warning on the page is easier to scroll past than one that blocks everything.
- **Make it a page.** Long forms, terms, and multi-step tasks belong on their own page with their own address. O'Hara questions putting a whole page inside a modal at all. The cost: the person leaves the current view, and the team has to preserve state on return.
- **Undo instead of confirm.** Let the action happen and offer to reverse it. The cost: real back-end work to make actions reversible.

## What doing it right requires

- **Use the native `<dialog>` element opened with `showModal()`.** O'Hara's 2023 position is that browsers now take care of most of what custom ARIA dialogs required, so custom dialogs should give way to the native element unless a project has a specific reason. Roselli notes that `showModal()` makes the dialog modal for assistive technology without adding `aria-modal`. A custom `role="dialog"` remains possible, following the Authoring Practices.
- **A name**, from a visible title referenced with `aria-labelledby` (Authoring Practices).
- **Choose where focus starts.** Roselli's 2020 tests of a custom dialog showed announcements varied widely by screen reader and browser depending on whether focus went to the dialog, its heading, or a button. There is no single right answer. For a destructive choice, focus the least destructive control (Authoring Practices; Roselli). For long or structured content, focus a static element at the top, such as the title (Authoring Practices), or use `autofocus` on it with the native element (O'Hara). Avoid starting on a text field (Roselli). In 2023 the HTML standard changed the native element to focus the dialog itself as a fallback, rather than the page (O'Hara, 2023).
- **The page behind is inert**: the person cannot reach it by keyboard or with a screen reader's virtual cursor while the dialog is open (Authoring Practices). The sources differ on one detail. The Authoring Practices have Tab wrap around inside the dialog. O'Hara considers it correct that a native modal dialog lets Tab move on to the browser's own controls, as long as it never reaches the page behind. Either meets the need; do not build a trap that also blocks the browser's controls just to match the Authoring Practices.
- **Escape closes it, and a visible close button** is in its tab order (Authoring Practices).
- **Focus returns** to the control that opened it on close, unless that control is gone (Authoring Practices). In O'Hara's 2019 tests the native element did not do this on its own; current behavior is not recorded on the list, so check it.
- **Avoid the old polyfill.** O'Hara's early-2022 retests found the `<dialog>` polyfill let the JAWS virtual cursor escape in Firefox. Every major browser has shipped the native element since 2022.
- **Give it at least a close button.** In early 2022, before the 2023 focus change, O'Hara found that a native dialog with nothing focusable left JAWS silent and screen reader focus on the trigger. That may no longer hold, but the Authoring Practices recommend a visible close button anyway.

## Criteria it touches

| SC | Title | Level | Entry | Why it comes up |
|---|---|---|---|---|
| 2.1.1 | Keyboard | A | `wcag/sc-2.1.1-keyboard.md` | Opening, using, and closing by keyboard |
| 2.1.2 | No Keyboard Trap | A | `wcag/sc-2.1.2-no-keyboard-trap.md` | A modal may hold focus while open, but the person must be able to close it by keyboard |
| 2.4.3 | Focus Order | A | `wcag/sc-2.4.3-focus-order.md` | Focus moving into the dialog on open and back to the trigger on close |
| 2.4.7 | Focus Visible | AA | `wcag/sc-2.4.7-focus-visible.md` | Initial focus that lands somewhere invisible |
| 4.1.2 | Name, Role, Value | A | `wcag/sc-4.1.2-name-role-value.md` | Dialog role and name; names for the close control |
| 2.5.8 | Target Size (Minimum) | AA | `wcag/sc-2.5.8-target-size-minimum.md` | A small close icon in a corner |
| 1.4.10 | Reflow | AA | `wcag/sc-1.4.10-reflow.md` | Dialog content and close button usable at narrow widths and high zoom |

## Manual tests

With the assistive technology named in the project's `a11y-spec.md`:
- Keyboard only: open it; check where focus lands; Tab and Shift+Tab never reach the page behind (reaching the browser's own controls is acceptable); Escape closes it; focus returns to the trigger.
- Screen reader: the dialog's role and name are announced on open; all its content can be read, including any text before the first control; the page behind cannot be reached with the virtual cursor or, on mobile, by swiping.
- Voice control: the close button can be activated by its visible name.
- Zoom to 400% and a narrow window: all content and the close button can be reached.
- If it opens without the person asking, record that as a consult question (`ux/modals-and-interruptions.md`), not a test result.
