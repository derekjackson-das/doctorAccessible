# Eval 001: missing label

Input: `input.html`. A site search form.

Intended defect: the text input has no accessible name. The word "Search" sits beside it in a `span` with no association to the control. Everything else is clean: language set, title present, one heading, landmarks, a named submit button, visible focus.

## Expected findings

1. **[Definite]** Text input has no accessible name.
   - Criterion: WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1
   - Source: `knowledge/wcag/sc-4.1.2-name-role-value.md`
   - Where: `input#q`
   - Acceptable fix directions: a `label` element with `for="q"`, wrapping the input in a `label`, or `aria-labelledby` pointing at the span given an id.

## Also acceptable

- A cross-reference to SC 1.3.1 or SC 3.3.2, marked "no entry yet", as a related criterion rather than a second finding.
- A manual-review note that the submit button and the input share the word "Search", which a human may want to differentiate.

## Must not

- Report the submit button. It has a name.
- Report the heading, landmarks, focus style, or language.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
