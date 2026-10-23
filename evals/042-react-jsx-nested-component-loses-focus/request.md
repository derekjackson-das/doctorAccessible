# Request

The developer types:

> Users say the search box on our staff directory "only lets you type one letter" and then they have to click back into it. It works fine if you paste. Here's the component. What's wrong?

```jsx
import { useState } from 'react';

export default function Directory({ people }) {
  const [query, setQuery] = useState('');

  function SearchBox() {
    return (
      <div className="search">
        <label htmlFor="directory-search">Search staff by name</label>
        <input
          id="directory-search"
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
      </div>
    );
  }

  const matches = people.filter((p) =>
    p.name.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <main>
      <h1>Staff directory</h1>
      <SearchBox />
      <ul>
        {matches.map((p) => (
          <li key={p.id}>
            <a href={`/people/${p.id}`}>{p.name}</a>
          </li>
        ))}
      </ul>
    </main>
  );
}
```

Project context given with the request: `a11y-spec.md` exists at the repo root. The project is a React 19 app. "Who we are building for" reads: "Harvard staff looking up a colleague, on a work laptop. Tested with NVDA with Firefox, VoiceOver with Safari on macOS, keyboard only." The directory component is rendered once per page. No pattern decisions recorded.
