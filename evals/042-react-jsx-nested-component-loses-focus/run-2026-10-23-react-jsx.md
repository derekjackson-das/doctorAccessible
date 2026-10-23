# Run 2026-10-23: react-jsx skill on eval 042

- Method: as for eval 041. Claude Code 2.1.309. SKILL.md with rule 8.
- Result: **pass.** Passed 3 of 3 (two runs before rule 8, one after). This is the run after.

## Answer

Done reading: the react-jsx skill, `html-patterns`, the React entry, and the 2.4.3, 2.1.1, 3.2.2 and forms entries. Here is the answer to the developer.

---

**The problem:** `SearchBox` is declared inside `Directory`. Every keystroke calls `setQuery`, which re-renders `Directory`, and that render creates a brand-new `SearchBox` function. React sees a different component type in the same position. It throws away the old `<div>` and `<input>` and builds new ones. The input that had focus no longer exists, so focus goes with it. The letter you typed stays because `query` lives in the parent, so the new input shows it. But focus is now outside the field.

Paste works because a paste is one change event. The field is rebuilt once, but by then the whole string is already in, so nobody notices the focus loss.

Source: `knowledge/frameworks/react-jsx.md`, "Focus", from react.dev "Preserving and Resetting State" ("don't nest component definitions"), React 19.3, tier 3.

### Finding

```
WCAG 2.2 SC 2.4.3 Focus Order (Level A), tier 1
Confidence: manual review
Where: Directory, SearchBox declared at line 13 of your snippet, rendered at line 34
What: after each character typed, the rendered page no longer has focus in the
      search input; the input element is removed and a new one put in its place.
React cause: a component declared inside another is a new component type on every
      render, so its subtree is rebuilt each time the parent re-renders; here that
      is every keystroke, since onChange sets the parent's state
      (knowledge/frameworks/react-jsx.md, tier 3, react.dev, React 19.3).
Fix direction: keep the native <label htmlFor> + <input type="search">; declare
      SearchBox at the top level of the module.
```

**Why manual review, when the code makes the cause certain.** The React side is certain from the code: `onChange` sets the parent's state, so the parent re-renders on every keystroke. But `knowledge/wcag/sc-2.4.3-focus-order.md` has no case yet for focus lost when a node is replaced. Its closest cases cover focus not moved into a dialog or not returned from one. `knowledge/aria/patterns/infinite-scroll.md` records the same gap and grades this kind of defect manual review under 2.4.3. So this rests on an entry that does not cover it yet, and it is marked unverified until the entry gets the case. Your users' reports fit the finding, but a tester still has to record it (see the steps below).

**Criteria I considered and did not report:**
- 2.1.1 Keyboard, F55 ("script that moves focus away from an element as soon as it receives it"): the closest case in that entry, but here focus is lost on input, not when the field receives focus.
- 3.2.2 On Input: its entry covers navigation, submission and new windows, not this.

That leaves one defect and one finding.

### Suggested fix (yours to apply)

Move the component out and pass the state in:

```jsx
function SearchBox({ query, onQueryChange }) {
  return (
    <div className="search">
      <label htmlFor="directory-search">Search staff by name</label>
      <input
        id="directory-search"
        type="search"
        value={query}
        onChange={(e) => onQueryChange(e.target.value)}
      />
    </div>
  );
}

export default function Directory({ people }) {
  const [query, setQuery] = useState('');
  // ...filter as before...
  // <SearchBox query={query} onQueryChange={setQuery} />
}
```

Putting the `<div className="search">…</div>` JSX straight into `Directory`'s return works just as well. What matters is that no component function is declared during render.

### What is already right

- A native `<input type="search">` with a visible `<label htmlFor>` pointing at its `id`. That is the labelling pattern in `knowledge/html/forms.md`, so no ARIA is needed.
- The hardcoded `id="directory-search"` is not a finding here. Your spec says the directory renders once per page. If it ever renders twice, or `SearchBox` gets reused, switch to `useId()` (`react-jsx.md`, "IDs").
- List keys come from `p.id`, from the data, which is correct.

### Manual tests owed (from the spec: keyboard only, NVDA with Firefox, VoiceOver with Safari on macOS)

Run these before and after the fix:

1. **Keyboard only, Firefox and Safari.** Tab to the search field and type `smith`. Record whether all five characters land in the field, and whether the focus indicator is still on the field after the last one. Then press Tab once and record where focus goes next. It should be the first result link.
2. **NVDA with Firefox.** Same steps. After each character, record where NVDA's focus is: the search field or somewhere else. Write down what NVDA reports, not what you think a user would make of it.
3. **VoiceOver with Safari.** Same steps and the same recording.

To get a full script, load `at-test-protocol`. Once the fix is in, I can dispatch the verifier for an independent check.

### For the spec

There are no pattern decisions recorded yet. You could add: "React components are declared at module top level, never inside another component." Say yes and I'll propose the wording. I haven't edited anything.
