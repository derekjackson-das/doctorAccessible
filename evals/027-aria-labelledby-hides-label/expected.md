# Eval 027: `aria-labelledby` that replaces the visible label

Input: `input.html`. A two-field library card application.

Intended defect: the date-of-birth field has a correct `label for="dob"` reading "Date of birth". It also has `aria-labelledby="dob-hint"`, pointing at the format hint. In the name computation, `aria-labelledby` comes before the native `label` (AccName 1.1, step 2B before 2D, in `knowledge/aria/accessible-name.md`). So the field's accessible name is "Use the format DD/MM/YYYY", and the visible label "Date of birth" is not in it. The hint was meant for `aria-describedby`.

Everything else is clean: language set, title present, one `h1`, landmarks, the "Full name" field labelled with `label for`, autocomplete values on both fields, a named submit button, visible focus.

## Expected findings

1. **[Definite]** The date-of-birth field's accessible name does not contain its visible label.
   - Criterion: WCAG 2.2 SC 2.5.3 Label in Name (Level A), tier 1, from `knowledge/wcag/sc-2.5.3-label-in-name.md` ("a control with visible text and an `aria-label` that does not contain that text", definite, F96; the same holds for `aria-labelledby`).
   - ARIA entry: `knowledge/aria/accessible-name.md`, for why the `label` is ignored.
   - Where: `input#dob`.
   - Acceptable fix directions: change `aria-labelledby` to `aria-describedby="dob-hint"`, so the label names it and the hint describes it; or remove `aria-labelledby`, with the hint in the `label`; or list both ids, label first, in `aria-labelledby`. As a direction, not a patch.

## Also acceptable

- Cross-referencing SC 4.1.2 Name, Role, Value or SC 1.3.1 Info and Relationships, as related, not as second findings. The field does have a name, so 4.1.2's "no name" case does not apply.
- A note that the browser's accessibility tree would confirm the computed name.
- A note that axe is not expected to catch this (see Automated scan).

## Must not

- Report the "Full name" field, the submit button, the heading, landmarks, focus, or language.
- Report the defect twice, under 2.5.3 and again under 4.1.2 or 1.3.1.
- Say the field has no accessible name.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe flags form fields with no name; this field has one, from `aria-labelledby`. The 2.5.3 entry says axe's `label-content-name-mismatch` rule compares visible text with the name for elements named by their content, and is experimental in some versions. A text input is not named by its content, so axe is not expected to report this defect; the finding must come from reading. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as definite under SC 2.5.3 (Level A), tier 1, and nothing from the Must not list appears.
