# UX heuristic: Modals and interruptions

- Sources:
  - Therese Fessenden, "Modal & Nonmodal Dialogs: When (& When Not) to Use Them", Nielsen Norman Group, 23 April 2017. https://www.nngroup.com/articles/modal-nonmodal-dialog/
  - Anna Kaley, "Popups: 10 Problematic Trends and Alternatives", Nielsen Norman Group, 30 June 2019. https://www.nngroup.com/articles/popups/
- Tier: 3, usability research. Nielsen Norman Group is on `knowledge/SOURCES.md` for UX claims only. Accessibility claims below come from the linked `wcag/` and `coga/` entries.
- Related entries: `wcag/sc-2.1.2-no-keyboard-trap.md`, `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.4.11-focus-not-obscured-minimum.md`, `coga/objective-5-help-users-focus.md`, `coga/objective-4-avoid-mistakes.md`
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the same dialog is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer.

## What the research found

- **A modal stops the task.** A modal dialog disables the page behind it until the person deals with it. That costs the time to read and dismiss it, and the time to recover what they were doing; people can lose track of the original task altogether. It can also cover the very content the dialog asks about (Fessenden).
- **People dismiss popups on reflex.** Overuse has taught people to close overlays without reading them, so a modal is a poor place for a message that matters (Kaley). Using the modal format for trivial things also weakens it for the warnings that need it (Fessenden).
- **Timing is the most common failure.** NN/g lists popups shown before the page has loaded, right after login, before the person has done anything, during a critical task, and several in a row. In its studies, participants reacted with frustration and distrust, and one abandoned the task (Kaley).
- **The two articles differ on warnings.** Fessenden supports modals for warnings that prevent lost work or irreversible actions. Kaley says critical information is better placed on the page, because people close popups without reading them. Following principle 13, this entry takes the stricter reading: put the warning on the page where possible, and use a modal only when the action is about to destroy work and the person must decide before it happens.
- **Nonmodal options exist for most cases:** a banner, an inline message, a link in the footer, a small panel that does not block the page (both articles).

## When the pattern serves people

NN/g supports a modal when the stakes justify the interruption (Fessenden):
- to prevent or warn about an error that would lose work or cannot be undone;
- to ask for information the system needs to continue something the person started;
- to break a complex task into short steps, though a multi-step task may deserve its own page;
- to ask a short question that saves the person effort later.

A legally required prompt, such as cookie consent or age verification, is the one case where a dialog before the content is acceptable (Kaley).

## When it does not

- Newsletter, feedback, app-download, and promotion prompts that are not part of the person's task (both articles).
- Anything during checkout or another high-stakes process (Fessenden).
- Decisions that need information the modal hides (Fessenden).
- Form errors: show them on the page next to the field, where the person can see them while fixing it (Fessenden).
- Cookie notices: a nonmodal banner does the job with less disruption (Kaley).
- Warnings before an external link: a short note at the link is enough (Kaley).

## The accessibility side

- A modal may hold focus while it is open, but a keyboard user must be able to close or leave it, for example with Escape or a close button (`wcag/sc-2.1.2-no-keyboard-trap.md`). Focus must move in an order that preserves meaning (`wcag/sc-2.4.3-focus-order.md`). The dialog and its controls need names and roles (`wcag/sc-4.1.2-name-role-value.md`).
- A nonmodal panel or banner must not entirely hide the component that has keyboard focus (`wcag/sc-2.4.11-focus-not-obscured-minimum.md`).
- `coga/objective-5-help-users-focus.md` covers unrequested interruptions; suppressing them is Level AAA in WCAG, so for most of these cases WCAG does not help and this entry does.
- How to build an accessible dialog belongs in the `patterns` and `aria` entries (roadmap 3.2 and 3.8).

## What consult should say

1. Is it a warning about lost work or an action that cannot be undone, or information the system needs to continue something the person started? Then a modal may be right; keep it to one short question, and prefer an on-page warning where that works.
2. Otherwise, did the person ask for this? If not, it is not a modal. Offer an inline message or a banner.
3. Does it appear before the person has done anything, during a task, or on top of another overlay? Move it or drop it.
4. Could it be a page instead? Multi-step or decision-heavy content usually should be.
