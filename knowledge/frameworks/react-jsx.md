# Framework layer: React and JSX

- Tier 3: React documentation, react.dev, React 19.3 (released 9 September 2026), accessed 2026-10-23. Pages used: "Common components" https://react.dev/reference/react-dom/components/common , "`<input>`" https://react.dev/reference/react-dom/components/input , "`<select>`" https://react.dev/reference/react-dom/components/select , "useId" https://react.dev/reference/react/useId , "Manipulating the DOM with Refs" https://react.dev/learn/manipulating-the-dom-with-refs , "Preserving and Resetting State" https://react.dev/learn/preserving-and-resetting-state . The pages carry no revision date.
- Related: `html/forms.md`, `html/custom-controls.md`, `aria/accessible-name.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-3.2.2-on-input.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

This entry says how React writes what `knowledge/html/` and `knowledge/aria/` already say to build. It is tier 3, an implementation reference like MDN: authoritative on how React behaves, never on what accessibility requires. What to build comes from `html/` and `aria/`; whether code fails comes from the `wcag/` entry, once, at that entry's confidence. React behaviour that causes a failure is named as the cause, not reported as a finding of its own.

## JSX is the same HTML, with some names changed

- **Most attributes take the DOM property name, not the HTML attribute name.** `htmlFor` for `for`, `className` for `class` (Common components). A `<label for=...>` in JSX is a mistake React warns about; the fix is `htmlFor`.
- **`aria-*` names are unchanged.** React passes ARIA attributes with exactly the HTML names, hyphen and all (Common components). What each element allows is still `aria/aria-in-html.md`.
- **`tabIndex` is camel-cased.** React's own reference says to avoid values other than `-1` and `0` (Common components), the same advice as `wcag/sc-2.4.3-focus-order.md`.
- **Labels work as in HTML.** React's `<input>` and `<select>` pages say to put the control inside a `<label>`, or to pair `<label htmlFor>` with the control's `id`, and call this essential for screen readers. The rules themselves are in `html/forms.md`.

## IDs: never hardcoded in a component that can appear twice

A component may render more than once on a page, and IDs must be unique, so React's docs call a hardcoded `id` bad practice and point to `useId` instead ("useId"). This matters for every relationship that rests on an ID: `htmlFor` and `id`, `aria-describedby`, `aria-labelledby`, `aria-controls`. With a hardcoded ID, the second copy of the component points its label or description at the first copy's control, so the second control is left with no associated label (the failure is in `wcag/sc-1.3.1-info-and-relationships.md` and `wcag/sc-4.1.2-name-role-value.md`, reported once).

- One `useId()` call can make a prefix for several related IDs in a component ("useId").
- `useId` is not for list keys; keys come from the data ("useId").

## Focus: refs, and DOM nodes React replaces

- **Moving focus** is done with a ref: `ref={inputRef}`, then `inputRef.current.focus()` (Manipulating the DOM with Refs). React calls focus management one of the proper uses of refs. Refs are set when React commits to the DOM, so they are read in event handlers or Effects, not during render.
- **Where focus should go** after a dialog opens or closes, or content appears, is `wcag/sc-2.4.3-focus-order.md` and the `aria/patterns/` entry, not React.
- **React destroys and rebuilds DOM nodes** when a different component type renders at the same position, or when a `key` changes (Preserving and Resetting State). A focused element that is destroyed takes focus with it.
- **A component defined inside another component** is a new component type on every render, so its whole subtree, inputs included, is rebuilt each time the parent re-renders (Preserving and Resetting State: "don't nest component definitions"). In a field whose `onChange` sets the parent's state, that is every keystroke: the input is replaced and focus is lost. The fix is to declare the component at the top level.
- **Removing the focused item**, such as a list row whose delete button was pressed, leaves focus nowhere unless the code moves it. Where it should go is a design decision (`wcag/sc-2.4.3-focus-order.md`).

## Events: `onChange` fires on every change

React's `onChange` on `<input>` and `<select>` behaves like the browser's `input` event: it fires on every keystroke, and for a `<select>` as soon as the user picks a different option ("`<input>`", "`<select>`"). A handler that navigates or submits in `onChange` is the change-of-context case in `wcag/sc-3.2.2-on-input.md`.

## Where people go wrong

- `for` instead of `htmlFor`, or a `class` attribute: a warning in development, a missing label in the page.
- A hardcoded `id` in a reusable field component.
- A component declared inside another one, so focus is lost on each keystroke.
- A `div` with `onClick` instead of a `button`. Nothing about JSX changes `html/buttons.md`.
- Reading a ref during render to move focus; it is `null` on the first render.
