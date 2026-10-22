# Eval 011: silent save message

Input: `input.html`. An email preferences form.

Intended defect: pressing "Save preferences" writes "Your preferences are saved." into `p#save-msg`. Focus stays on the button and the context does not change, so the text is a status message. The paragraph has no `role="status"`, `role="alert"`, `role="log"`, and no `aria-live`, so it cannot be programmatically determined as a status message. Everything else is clean: language set, title present, one heading, landmarks, checkboxes labeled and grouped in a fieldset with a legend, a named button, visible focus.

axe is expected to report nothing for this defect: `knowledge/wcag/sc-4.1.3-status-messages.md` records that axe-core 4.14.0 has no rule tagged for this criterion. A clean axe run is not a pass.

## Expected findings

1. **[Definite]** The save confirmation is a status message with no role or live-region property.
   - Criterion: WCAG 2.2 SC 4.1.3 Status Messages (Level AA), tier 1
   - Source: `knowledge/wcag/sc-4.1.3-status-messages.md`
   - Where: `p#save-msg`, written by the click handler on `button#save`
   - Acceptable fix directions: `role="status"` (technique ARIA22) on the paragraph from page load, an `output` element in its place, or `aria-live="polite"`. The container must carry the role before the message is inserted.

## Also acceptable

- Naming failure F103 from the entry.
- A manual-review item asking a human with assistive technology to confirm the message is presented without focus moving, written as a test step and what to record, not as what a user would hear.
- A note that `role="alert"` or `aria-live="assertive"` would be heavier than this routine message needs, citing the entry.

## Must not

- Recommend moving focus to the message as the primary fix.
- Report the checkboxes, fieldset, legend, button name, heading, landmarks, focus style, colors, or language.
- Report SC 4.1.2 for the message. The button's name, role, and state are correct.
- State a criterion number, title, level, or threshold that is not in the opened entries without marking it unverified.
- Describe what a screen reader would announce.
- Rewrite the code.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
