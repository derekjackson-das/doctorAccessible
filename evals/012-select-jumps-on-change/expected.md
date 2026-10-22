# Eval 012: select that navigates as soon as a value is chosen

Input: `input.html`. A department directory with one labeled select list.

Intended defect: the `select` has a `change` handler that navigates to a new page the moment an option is chosen. A keyboard user arrowing down through the options to hear them triggers the first one and is taken away. There is no "Go" button and the instruction above the control does not warn that choosing an option will leave the page. Everything else is clean: language set, title present, one `h1`, landmarks, the select has a visible associated `label`, a placeholder option, visible focus, contrast above the thresholds.

## Expected findings

1. **[Definite]** Changing the select causes a change of context without warning.
   - Criterion: WCAG 2.2 SC 3.2.2 On Input (Level A), tier 1
   - Source: `knowledge/wcag/sc-3.2.2-on-input.md`
   - Where: the `select#dept` and its `onchange` attribute
   - Acceptable fix directions: remove the `change` handler and add a submit button that performs the navigation (technique G80); or, if automatic navigation must stay, say so in the instruction before the control (technique G13). The entry lists this as the classic jump menu.

## Also acceptable

- A note that "Choose a department to open its contact page" describes the purpose but does not warn that selection itself navigates, so it does not satisfy G13. A verifier that judges the sentence a sufficient warning and downgrades to Likely has misread it, but should not be failed for raising the question.
- A cross-reference to SC 2.1.1 Keyboard, since the keyboard user is the one harmed, marked as not a separate finding.
- A cross-reference to SC 3.2.1 On Focus, marked as not applicable because focus alone does nothing.

## Must not

- Report SC 4.1.2, 1.3.1, or 3.3.2; the select has a visible, associated label.
- Report the heading, landmarks, focus style, language, or contrast.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is expected to report no violations. It has no rule for change-of-context behavior. A verifier that treats the clean scan as a pass has failed this eval.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
