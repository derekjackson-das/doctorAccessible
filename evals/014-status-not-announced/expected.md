# Eval 014: result count that changes without a live region

Input: `input.html`. A course finder with a search field, a result count, and a filtered list.

Intended defect: as the user types, script filters the list and rewrites the text of `p#count` ("4 courses", "2 courses", "0 courses"). Focus stays in the search field. The count paragraph has no `role="status"`, no `aria-live`, and is not an `output` element, so a screen reader user typing in the field hears nothing about how many results remain. Everything else is clean: language set, title present, one `h1`, landmarks, the field has a visible associated label, `autocomplete="off"` is appropriate on a search field that is not about the user, visible focus, contrast above the thresholds. Note the search field is not covered by 1.3.5, as that entry says.

## Expected findings

1. **[Definite]** Status message is not programmatically determinable.
   - Criterion: WCAG 2.2 SC 4.1.3 Status Messages (Level AA), tier 1
   - Source: `knowledge/wcag/sc-4.1.3-status-messages.md`
   - Where: `p#count`, updated by the `input` listener in the script
   - Acceptable fix directions: add `role="status"` to the count element (technique ARIA22), or make it an `output` element, which carries that role natively; keep the element present from page load and change only its text. The entry names F103 as the matching failure.

## Also acceptable

- A manual-review note that whether every keystroke should produce an announcement is a design question, and that debouncing or announcing only when typing pauses may serve better.
- A note that the hidden list items are removed from the accessibility tree by the `hidden` attribute, which is correct.
- A cross-reference to SC 1.3.5 saying the search field is not covered, showing the entry was read.

## Must not

- Report SC 4.1.2, 1.3.1, or 3.3.2; the field is labeled and associated.
- Report `autocomplete="off"` under 1.3.5; a search term is not information about the user, per that entry.
- Report SC 3.2.2; filtering in place is not a change of context, per that entry.
- Report the heading, landmarks, focus style, language, or contrast.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is expected to report no violations. It has no rule for a missing live region. A verifier that treats the clean scan as a pass has failed this eval.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
