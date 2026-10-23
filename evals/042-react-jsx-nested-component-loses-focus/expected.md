# Eval 042: a component declared inside another loses focus on each keystroke

Input: `request.md`. A transcript eval for the `react-jsx` skill: a `SearchBox` component declared inside `Directory`. Each keystroke sets `query` in `Directory`, which re-renders and creates a new `SearchBox` component type, so React replaces the input and focus is lost after one character.

Intended defect: focus is lost from the search field after every character typed. The cause is React-specific: a nested component definition is a different component type on every render, so React rebuilds its DOM subtree (`knowledge/frameworks/react-jsx.md`, tier 3, react.dev "Preserving and Resetting State"). Everything else is clean: the label is associated with `htmlFor`, the id is used once in a component rendered once, the results are a real list of real links.

## Expected findings

1. **[Likely]** Focus leaves the search field after each character typed, because the input is replaced on every render.
   - Criterion: the answer names the criterion it judges this under, from an opened entry, and grades it likely or manual review, not definite: no `wcag/` entry lists this case as a failure. Acceptable: SC 3.2.2 On Input (Level A), with the change-of-context reading taken from the entries; SC 2.4.3 Focus Order (Level A); SC 2.1.1 Keyboard (Level A). Or no criterion, with the defect named as a functional bug that a keyboard user cannot get past, and the criterion question marked for a person.
   - Where: `SearchBox` declared inside `Directory`.
   - React cause: a component defined inside another is a new type each render, so its subtree, the input included, is rebuilt (`knowledge/frameworks/react-jsx.md`).
   - Fix direction: declare `SearchBox` at the top level and pass `query` and `setQuery` as props, or inline the markup in `Directory`. Offered as a suggestion.

## Also acceptable

- A note that the updating list of results may need a status message (SC 4.1.3), marked manual review.
- A manual test: type a name with the keyboard only and with NVDA, and record whether focus stays in the field.
- Explaining why pasting works (one change, one re-render).

## Must not

- Grade the focus loss definite.
- Blame `htmlFor`, the `id`, or `type="search"`.
- Suggest `autoFocus`, a `useEffect` that refocuses the input, or a ref-based refocus as the fix in place of moving the component to the top level.
- Report the defect more than once.
- Rest a WCAG finding on react.dev alone.
- Say what a screen reader user would hear or experience.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.

## Pass condition

Finding 1 is present at likely or manual review, names the nested component definition as the cause and declaring it at the top level as the fix, and nothing from the Must not list appears.
