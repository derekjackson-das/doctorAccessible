# Run 2026-10-23: react-jsx skill on eval 041

- Method: `evals/run.sh` (fresh `claude -p` session loading the react-jsx skill; no Write or Edit; key, run files and RESULTS.md off limits), graded by `evals/check.py` (judge). Claude Code 2.1.309. SKILL.md with rule 8.
- Result: **pass.** Runs 1 and 2, before rule 8, failed on predicted screen-reader output; runs 3 and 4, with it, passed. This is run 3.

## Answer

I've read the skills and knowledge entries; here is the review.

# Review: `EmailField.jsx`

**Spec check:** `a11y-spec.md` covers Harvard staff managing their account on a work laptop, tested with NVDA with Firefox, VoiceOver with Safari on macOS, and keyboard only. It records no pattern decisions, so nothing in it rules this component in or out.

The component uses the native elements: a real `<label>`, a real `<input type="email">`, and `htmlFor` rather than `for`. One thing blocks the merge.

## Finding 1: the newsletter field on the settings page has no label

```
WCAG 2.2 SC 1.3.1 Info and Relationships (Level A), tier 1
  and WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1. One defect, reported once.
Confidence: definite
Where: EmailField.jsx, line 12 (htmlFor="email") and line 14 (id="email"),
       as used in SettingsPage.jsx at lines 28 and 34
What: On the settings page, both <label for="email"> elements point to the same ID.
      The browser connects that ID to the first matching input, which is the account
      field in <main>. That leaves the newsletter input in <footer> with no
      associated label.
React cause: The component hardcodes its id, and the excerpt renders it twice on one
      page. React's docs call a hardcoded id in a reusable component bad practice and
      point to useId (knowledge/frameworks/react-jsx.md, "IDs"; tier 3, react.dev,
      React 19.3).
Fix direction: Give each instance its own ID with useId, or nest the input inside
      the label so no ID is needed (knowledge/html/forms.md, "The native approach").
Source: knowledge/wcag/sc-1.3.1-info-and-relationships.md ("A form control with visible
      label text that is not associated with it. Definite. Shared with SC 4.1.2");
      knowledge/wcag/sc-4.1.2-name-role-value.md
```

**Why it's definite:** the excerpt you sent shows both instances on one page, so this isn't a guess about how the component might be used. On pages with only the footer, one instance renders and its label works. The defect appears wherever two instances share a page, and the settings page is one.

**A side effect, not a second finding:** on the settings page, clicking the text "Email for the newsletter" focuses the account email field.

**No finding for the duplicate ID itself.** axe flags `duplicate-id` under 4.1.1, which is obsolete in WCAG 2.2. `knowledge/axe-rules.md` records it as "no entry, not a finding." The failure is the missing label above.

### Suggested fix (a suggestion, not applied to your code)

Option A, `useId`. This is the better choice for a shared field, because it extends to a hint or error later:

```jsx
import { useId } from 'react';

export function EmailField({ label, value, onChange }) {
  const id = useId();
  return (
    <div className="field">
      <label htmlFor={id}>{label}</label>
      <input
        id={id}
        type="email"
        autoComplete="email"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
    </div>
  );
}
```

If you later add a format hint or an error message, build its ID from the same value (for example `` `${id}-hint` `` with `aria-describedby`). One `useId()` call can prefix several related IDs (react-jsx.md, "IDs").

Option B, the input inside the label. This needs no ID, but you'll need one anyway as soon as a description is attached:

```jsx
<label>
  {label}
  <input type="email" autoComplete="email" value={value}
         onChange={(e) => onChange(e.target.value)} />
</label>
```

## What already meets the requirement

- **SC 1.3.5 Identify Input Purpose (Level AA), tier 1** (`knowledge/wcag/sc-1.3.5-identify-input-purpose.md`). Both uses collect the user's own email, and `autoComplete="email"` is the matching token. This passes. Keep it in the shared component.
- **`onChange`** only updates state. It doesn't navigate or submit, so the change-of-context case in `wcag/sc-3.2.2-on-input.md` doesn't apply (react-jsx.md, "Events").
- **The component is declared at the top level**, not inside another component, so the focus loss on each keystroke described in react-jsx.md ("Focus") doesn't apply.

## Checks to run after the fix (run them on the settings page)

These steps say what to record. They don't predict the result.

1. **Accessibility inspector (Firefox):** select each email input and record its computed name. Each name should match its own visible label.
2. **Pointer:** click each label's text and record which field gets focus.
3. **Keyboard only:** Tab through both forms and record the order fields receive focus and whether focus is visible on each.
4. **NVDA with Firefox:** press F to move between form fields, then Tab to each. Record what is read for each email field: label, type, value (`knowledge/testing/screen-reader-windows.md`, step 5).
5. **VoiceOver with Safari, macOS:** open the rotor (VO+U), go to Form Controls, and record the name listed for each email field (`knowledge/testing/screen-reader-apple.md`).

Running `/at-test-protocol` turns these into the full numbered script for your tester.

## For the spec

The spec has no pattern decisions yet. With your agreement, I'd add one: "Shared form components generate IDs with `useId`; no hardcoded `id`, `htmlFor`, or `aria-*` ID references." I haven't changed any files.
