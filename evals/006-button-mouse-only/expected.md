# Eval 006: custom button that works only with a mouse

Input: `input.html`. A course page with a "Show syllabus" control that reveals a hidden section.

Intended defect: the control is a `span` with `role="button"`, `tabindex="0"`, a correct name, and correct `aria-expanded` and `aria-controls` state, but its only event handler is `onclick`. A keyboard user can tab to it and sees focus, but Enter and Space do nothing, because a `span` does not fire click on those keys the way a native `button` does. Everything else is clean: language set, title present, one `h1`, landmarks, visible focus, contrast above the thresholds, name and role and state exposed.

## Expected findings

1. **[Definite]** Custom button cannot be activated by keyboard.
   - Criterion: WCAG 2.2 SC 2.1.1 Keyboard (Level A), tier 1
   - Source: `knowledge/wcag/sc-2.1.1-keyboard.md`
   - Where: the `span.toggle` with `role="button"` inside `main`
   - Acceptable fix directions: replace the `span` with a native `button` element (technique H91), which handles Enter and Space without script; or add a `keydown` handler for Enter and Space that calls the same function (technique G90). The entry names F54 as the matching failure.

## Also acceptable

- A note that the control's name, role, and state are correctly exposed, so SC 4.1.2 is met and the defect is operability alone. This is the point of the eval: the ARIA is right and the behavior is still broken.
- A manual-review note that the fix should be confirmed by tabbing to the control and pressing Enter and Space.

## Must not

- Report SC 4.1.2 as a failure; the control has a name, a role, and exposed state.
- Report focus visibility; the `:focus-visible` outline applies to the `span` because it has `tabindex="0"`.
- Report the hidden section, the heading, landmarks, language, or contrast.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is expected to report no violations. It has no default rule that detects a `role="button"` element with only a click handler; the defect is found by reading the script or by keyboard testing. A verifier that treats the clean scan as a pass has failed this eval.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
