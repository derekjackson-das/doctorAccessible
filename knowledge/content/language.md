# Content: Language

- House standard: `docs/content-standards.md`, section 8.
- Sources:
  - W3C WAI, "Writing for Web Accessibility", updated 5 August 2022. https://www.w3.org/WAI/tips/writing/ Tier 2 (expanding acronyms on first use).
  - W3C, "Understanding Success Criterion 3.1.5: Reading Level", updated 28 June 2026. https://www.w3.org/WAI/WCAG22/Understanding/reading-level.html Tier 2 (measuring multilingual pages).
- WCAG: `wcag/sc-3.1.1-language-of-page.md` (Level A), `wcag/sc-3.1.2-language-of-parts.md` (Level AA). SC 3.1.4 Abbreviations is Level AAA, beyond our target, with no entry yet.
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

A page with no declared language fails SC 3.1.1, and a passage in another language that is not marked can fail SC 3.1.2; report them there at the confidence their entries give, with that entry's exceptions for proper names, technical terms, and words that have become part of the surrounding language. An abbreviation not expanded on first use misses the house standard and is likely, never definite. A project's `a11y-spec.md` may change the standard; the spec wins.

## What it is

Telling browsers and assistive technology which human language the text is in, page by page and passage by passage, and making sure abbreviations are understood.

## Why it matters

Screen readers and translation tools use the declared language to choose pronunciation and rules. Text in the wrong language setting can come out garbled. An unexpanded abbreviation stops a reader who does not know it.

## How to do it

- **Declare the page's language** on the `html` element (`wcag/sc-3.1.1-language-of-page.md`).
- **Mark passages in another language** with `lang` on the containing element, except where the 3.1.2 entry's exceptions apply (`wcag/sc-3.1.2-language-of-parts.md`).
- **Expand acronyms and abbreviations on first use,** for example "Web Content Accessibility Guidelines (WCAG)" (W3C writing tips; house standard).
- **Multilingual pages and reading level:** measure each language separately (`content/reading-level.md`).

## How to check it

- The `html` element has a `lang` value that matches the page's main language.
- Each passage in another language has its own `lang`.
- The first use of each abbreviation is expanded.
