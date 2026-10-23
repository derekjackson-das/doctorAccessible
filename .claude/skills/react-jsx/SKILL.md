---
name: react-jsx
description: The React layer over html-patterns. Use when writing or reviewing React components or JSX: labels and htmlFor, IDs and useId, aria-* in JSX, refs and focus, components that lose focus on re-render, and onChange handlers. Says how React writes the native patterns; what to build still comes from knowledge/html/ and knowledge/aria/, and what fails from knowledge/wcag/.
---

# React and JSX

This skill is a layer, not a replacement (principle 11). Load `html-patterns` too: it decides what to build. This skill only says how React writes it and where React causes defects of its own. The facts are in `knowledge/frameworks/react-jsx.md`, tier 3, from react.dev. The rules for citing are in the `wcag` skill and apply here unchanged.

## When this applies

Any `.jsx` or `.tsx` file, or React code pasted into the conversation. Also when a page built with React fails a check and the cause may be React, such as focus lost after typing or a label that reaches the wrong field.

## Rules

1. **Native first, in JSX too.** A `<button>`, a `<label>`, a `<select>` in JSX are the native elements. Open `knowledge/html/` for what to build before anything React-specific.
2. **react.dev is tier 3.** It is the reference for how React behaves, never for what accessibility requires. A finding rests on its `wcag/` entry; React is named as the cause.
3. **One finding per defect.** A hardcoded ID that leaves a field unlabeled is one finding under the label criterion, with the React cause and the React fix. It is not a second "React" finding.
4. **Read the component as it renders.** Ask how many times it appears on the page, which IDs it hardcodes, what re-renders on each keystroke, and which DOM nodes React will replace. The entry lists each case.
5. **Confidence from the code.** Reading JSX, you see what will render, not what did. When a defect depends on how the component is used (rendered twice, re-rendered on input), say what usage the code shows and grade at the `wcag/` entry's confidence, or one step lower if that usage is not shown.
6. Never state a criterion number, title, or level, or a React behaviour, from memory. Open the entry. If the entry does not cover it, say "no entry yet" and mark it unverified.
7. Advise and describe; do not silently rewrite the developer's component. A suggested fix is offered as a suggestion.
8. **Never say what a screen reader will announce or what a user gets** (principle 7). Say what the rendered page exposes, such as "the newsletter input has no associated label", and give the test step and what to record.

## Where to look

| Question | Read |
|---|---|
| `htmlFor`, `className`, `aria-*`, `tabIndex` in JSX | `knowledge/frameworks/react-jsx.md`, "JSX is the same HTML" |
| How to label a field, group controls | `knowledge/html/forms.md` |
| IDs in a reusable component; `useId` | `knowledge/frameworks/react-jsx.md`, "IDs" |
| Moving focus; focus lost when React replaces a node | `knowledge/frameworks/react-jsx.md`, "Focus"; where it should go: `knowledge/wcag/sc-2.4.3-focus-order.md` |
| `onChange` that navigates or submits | `knowledge/frameworks/react-jsx.md`, "Events"; `knowledge/wcag/sc-3.2.2-on-input.md` |
| The ARIA for a widget with no native element | `knowledge/aria/patterns/`, through the `html-patterns` skill |
| The criteria themselves | `knowledge/INDEX.md`, then the `wcag/` entry |

## Output shape for a finding

```
WCAG 2.2 SC x.x.x Title (Level A or AA), tier 1
Confidence: definite | likely | manual review (from the wcag/ entry)
Where: <component, file:line>
What: <one sentence: what the rendered page exposes>
React cause: <the React behaviour, from knowledge/frameworks/react-jsx.md (tier 3, react.dev)>
Fix direction: <the native element from html/, written the React way>
```
