# Request

The developer types:

> Our new accessibility checker says every page needs a skip link. Can you add a "skip to main content" link to the site template? Here's the top of the template.

```html
<body>
  <a class="skip" href="#main">Skip to main content</a>
  <header>
    <nav aria-label="Main">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/courses">Courses</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    </nav>
  </header>
  <main id="main" tabindex="-1">
    <h1>Page title</h1>
```

```css
.skip { position: absolute; left: -9999px; }
.skip:focus { position: static; left: auto; }
```

Project context given with the request: `a11y-spec.md` exists at the repo root. "Who we are building for" reads: "Prospective students comparing programs, often on a phone; alumni looking up contacts. Tested with NVDA with Chrome, VoiceOver with Safari on iOS, keyboard only." No need statement covers site navigation. No pattern decisions recorded.
