# HTML: Dialogs

- Tier 1: HTML Living Standard, §4.11.4 The dialog element, accessed 2026-10-23. https://html.spec.whatwg.org/multipage/interactive-elements.html
- Tier 1: ARIA in HTML, W3C Recommendation 11 August 2026, row for `dialog` (implicit `dialog`; `alertdialog` may be set). https://www.w3.org/TR/html-aria/
- Tier 2: no WAI tutorial covers dialogs. The ARIA Authoring Practices "Dialog (Modal) Pattern" is summarized in `aria/patterns/modal-dialog.md`.
- Related: `patterns/modal-dialog.md` (whether to use one at all), `aria/patterns/modal-dialog.md`, `ux/modals-and-interruptions.md`, `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

This entry says how to build it. Whether code fails WCAG is decided by the `wcag/` entries named below; report a failure once, under its criterion, at that entry's confidence. A custom `role="dialog"` where `dialog` would do is advice, never a finding on its own.

## The native approach

- **`dialog` opened with `showModal()`** for a modal: the browser makes the rest of the page inert and closes it on Escape (`aria/patterns/modal-dialog.md`).
- **Initial focus with `autofocus`.** The HTML Standard says the dialog focusing steps pick a reasonable first element, but authors should put `autofocus` on the element the person is expected to use first, or on the `dialog` itself if there is none. For a destructive choice, that is the least destructive button (`aria/patterns/modal-dialog.md`).
- **A visible close button** inside the dialog.
- **A name from its heading,** with `aria-labelledby` pointing at the visible title.
- **Return focus** to the control that opened it when it closes (`wcag/sc-2.4.3-focus-order.md`).
- **Dialogs only for dialogs.** The HTML Standard says it is not conforming to use `dialog` for other controls: context menus, tooltips, and popup listboxes are not dialogs.
- **Keep it short.** The HTML Standard notes users do not expect scrollable dialogs; long content belongs on a page (`patterns/modal-dialog.md`).

## What the native approach satisfies by default

With `showModal()`: the dialog role, modality without `aria-modal` (Roselli, in `aria/patterns/modal-dialog.md`), Escape to close, and the page behind made inert, so neither Tab nor a screen reader's cursor reaches it.

## Where people go wrong

- A `div` styled as a modal with no focus moved into it (`wcag/sc-2.4.3-focus-order.md`, eval 028).
- Focus held inside with no keyboard way out (`wcag/sc-2.1.2-no-keyboard-trap.md`).
- `aria-modal="true"` on something that leaves the page usable (`aria/patterns/modal-dialog.md`).
- `dialog` used for a tooltip or a menu, which the HTML Standard calls non-conforming.

## When ARIA is genuinely needed

- `aria-labelledby` for the name, and `aria-describedby` for a short message.
- A custom `role="dialog"` only where the native element cannot be used; then everything in `aria/patterns/modal-dialog.md` applies.
