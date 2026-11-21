# Eval 045: a toast with an Undo button in an injected alert

Input: `request.md`. A transcript eval for the `html-patterns` skill, testing `knowledge/aria/live-regions.md`. A delete action shows a toast built as a new `role="alert"` element holding the message and an Undo button. The toast is removed after 4 seconds.

This eval holds several related defects on purpose, because they come from one design decision: a timed toast used as a live region with a control in it. The entry separates them, and a correct answer does too.

Everything else is clean: the Delete buttons are real buttons with text, and the list and heading are fine.

## Expected points

1. **The region is created and filled in the same moment.** The `role="alert"` element is added to the page already holding its text, so the message may not be announced. The direction is to put an empty live region in the page at load and write the text into it. Criterion: WCAG 2.2 SC 4.1.3 Status Messages (Level AA), likely, from `knowledge/wcag/sc-4.1.3-status-messages.md` and `knowledge/aria/live-regions.md`.
2. **`alert` is the wrong level.** "Message deleted" is routine news, not an imperative interruption. The direction is `role="status"` (polite). The answer cites WAI-ARIA 1.2's rule that authors should not use assertive unless the interruption is imperative (tier 1), through the entry. Practice, likely at most. It is not reported as a definite failure.
3. **The Undo button cannot live in a live region.** A live region announces text only, so the button is not announced as a button. The toast may be gone before a keyboard or screen reader user reaches it, since it is appended at the end of `body` and removed after 4 seconds. The direction is: keep Undo available outside the toast, or keep the message until it is dismissed, or use a dialog the user moves into. Criteria: SC 2.1.1 Keyboard (Level A) or SC 2.4.3 Focus Order (Level A), likely or manual review.
4. **The 4-second timer.** The message and its Undo disappear on a clock the user cannot stop or extend. Criterion: SC 2.2.1 Timing Adjustable (Level A), likely or manual review. It is not definite, because the 2.2.1 entry has no toast case.

## Also acceptable

- Recommending a persistent message area instead of a toast, or not using a toast at all (Roselli 2020, through the entry).
- Mentioning that the region should be cleared shortly after the message, and named if there are several.
- Noting the testing gap: support claims in the entry have no recent versions.
- Pointing to `knowledge/html/dialogs.md` for the dialog option.
- Naming the manual tests from the entry, for the spec's screen readers.

## Must not

- Approve the design as it is.
- Recommend `role="alert"` or `aria-live="assertive"` for this message.
- Recommend moving focus into a `status` or `alert` element.
- Call any of the four points definite.
- Report the same defect twice under different criteria. Points 3 and 4 are separate defects.
- Cite Soueidan, O'Hara, or Roselli as the requirement, rather than as practice behind a criterion or the WAI-ARIA text.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Say what a screen reader user would hear or experience.
- Rewrite the code without offering it as a suggestion.

## Pass condition

Points 1 to 4 are all present, each at likely or manual review and tied to the criterion or source named above, and nothing from the Must not list appears.
