# Eval 017: consult on a workshop registration form

Input: `request.md`. A developer asks for a registration form and proposes a multi-step wizard and a custom dropdown for forty departments.

Intended outcome: a full consult. The need is real and the form should be built, but the smallest thing that meets it is a single plain HTML form, not a wizard, and the department picker should start from a native control. The answer gives the developer the criteria, the options with trade-offs, the manual tests, and a need statement ready for the spec.

## Expected

1. **Who and what** comes from the spec: staff and graduate students registering for workshops from a work laptop or a phone, trying to sign up in one sitting. Named AT: JAWS with Chrome, VoiceOver on macOS, keyboard only, 200% and 400% zoom.
2. **Smallest thing** says a single-page form with five fields meets the need, and that a one-question-per-screen wizard adds steps, state, and re-entry risk without serving the person better. "Build less" or equivalent appears for the wizard. For the department picker, the answer names a native `select` with forty options as the baseline that works everywhere, and treats a type-ahead combobox as an option with a cost, not the default.
3. **Patterns** opens `knowledge/patterns/` for the wizard and the autocomplete, finds no entries, says "no entry yet", and reasons from the WCAG entries instead, saying that is the basis.
4. **Criteria** are pulled from `knowledge/INDEX.md` and cited with level and tier from the entries. At minimum: SC 3.3.2 Labels or Instructions, SC 1.3.1 Info and Relationships (the session checkboxes as a grouped set with a legend), SC 1.3.5 Identify Input Purpose (name and email tokens), SC 3.3.1 Error Identification, SC 3.3.3 Error Suggestion, SC 4.1.2 Name, Role, Value. Acceptable additions: SC 3.3.7 Redundant Entry (a reason against the wizard), SC 2.4.6 Headings and Labels, SC 1.4.1 Use of Color (required marks), SC 2.5.8 Target Size (checkboxes on a phone), SC 3.3.4 if the registration is treated as a commitment, SC 4.1.3 Status Messages (confirmation after submit).
5. **Options** cover at least: single page versus wizard; native `select` versus combobox for departments; checkboxes for the sessions versus a multi-select. Each with what it costs and what it gives up.
6. **Manual tests owed** name the spec's AT and say what to do: JAWS and VoiceOver through every field hearing label, required state, and group question; keyboard only end to end including error recovery; 400% zoom on the checkbox group; a submission with errors to hear how they are announced.
7. **Need statement** in the template's format, dated, with "We will build: a single-page HTML form with five labeled fields", "Instead of: a multi-step wizard and a custom department dropdown", and a short "Why this is right".
8. **Content** is consulted: field labels that say what to enter, "dietary needs" explained with an example, session labels that include date and time, error messages that name the field and the fix, reading level at or below grade 8, against `docs/content-standards.md`.

## Also acceptable

- A proposed pattern decision row recording "native select for long lists unless testing shows otherwise".
- Noting that "look nice" is a design question the spec's design system section should answer, and asking whether one exists.
- Asking what happens after submission, since a confirmation page or message is part of the feature.

## Must not

- Write the form's HTML.
- Accept the wizard without weighing it against the single page.
- Recommend a custom combobox as the default without naming the native alternative first.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Assert usability research about wizards or dropdowns from memory without marking it unverified and noting there is no `ux` entry.
- Write into `a11y-spec.md` without the developer's agreement.

## Pass condition

Items 1 through 7 are present, the single-page form is preferred over the wizard with reasons, the native select is named before any custom control, and nothing from the Must not list appears.
