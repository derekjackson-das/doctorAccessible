# Request

The developer types:

> Can you review this React component before I merge it? It's our shared email field. The newsletter signup in the footer uses it, and so does the account form on the settings page, which also has the footer.

```jsx
// EmailField.jsx
export function EmailField({ label, value, onChange }) {
  return (
    <div className="field">
      <label htmlFor="email">{label}</label>
      <input
        id="email"
        type="email"
        autoComplete="email"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
    </div>
  );
}

// SettingsPage.jsx (excerpt)
<main>
  <h1>Account settings</h1>
  <form onSubmit={saveSettings}>
    <EmailField label="Account email" value={email} onChange={setEmail} />
    <button type="submit">Save</button>
  </form>
</main>
<footer>
  <form onSubmit={subscribe}>
    <EmailField label="Email for the newsletter" value={newsEmail} onChange={setNewsEmail} />
    <button type="submit">Subscribe</button>
  </form>
</footer>
```

Project context given with the request: `a11y-spec.md` exists at the repo root. The project is a React 19 app. "Who we are building for" reads: "Harvard staff managing their account, on a work laptop. Tested with NVDA with Firefox, VoiceOver with Safari on macOS, keyboard only." No pattern decisions recorded.
