# Eval 041: a reusable field component with a hardcoded id

Input: `request.md`. A transcript eval for the `react-jsx` skill: a shared `EmailField` component that hardcodes `id="email"` and `htmlFor="email"`, rendered twice on the settings page (the account form and the footer newsletter form).

Intended defect: on the settings page two inputs share the id `email`, and both labels point at it. One of the two inputs, the newsletter field in the footer, ends up with visible label text that is not associated with it. The cause is React-specific in practice: a component that can appear twice hardcodes an id. Everything else is clean: `htmlFor` is used correctly, the input has a type and `autoComplete`, the buttons are real buttons with text.

## Expected findings

1. **[Definite]** A form control with visible label text that is not associated with it, on the settings page.
   - Criterion: WCAG 2.2 SC 1.3.1 Info and Relationships (Level A), tier 1, reported once and naming SC 4.1.2 Name, Role, Value (Level A) as shared, per the 1.3.1 entry. Either criterion as the heading is fine as long as it is one finding.
   - Where: `EmailField.jsx`, the hardcoded `id="email"` and `htmlFor="email"`, as rendered twice by `SettingsPage.jsx`.
   - React cause: a hardcoded id in a component that renders more than once; IDs must be unique (`knowledge/frameworks/react-jsx.md`, tier 3, react.dev "useId").
   - Fix direction: generate the id with `useId()` inside the component and use it for both `htmlFor` and `id`. Offered as a suggestion.

## Also acceptable

- Naming the duplicate id as an HTML conformance problem, as advice, alongside the finding.
- Grading it likely instead of definite, if the answer says it is reading JSX and not a rendered page.
- A note that the same applies to any `aria-describedby` or `aria-labelledby` the component might add later.
- Loading `html-patterns` and citing `knowledge/html/forms.md`.

## Must not

- Report `htmlFor` as wrong, or tell the developer to use `for`.
- Report the defect twice, once as WCAG and once as a "React" finding, or once under 1.3.1 and again under 4.1.2.
- Rest the finding on react.dev alone, or call react.dev an accessibility authority.
- Report `autoComplete="email"` or the buttons as defects.
- Rewrite the component without offering it as a suggestion.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Say what a screen reader user would hear or experience.

## Pass condition

Finding 1 is present at definite or likely, under SC 1.3.1 or 4.1.2 as one finding, names the hardcoded id in a component rendered twice as the cause and `useId` as the fix, and nothing from the Must not list appears.
