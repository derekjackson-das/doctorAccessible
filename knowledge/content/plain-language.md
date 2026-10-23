# Content: Plain language

- House standard: `docs/content-standards.md`, section 1.
- Sources:
  - W3C WAI, "Writing for Web Accessibility", updated 5 August 2022. https://www.w3.org/WAI/tips/writing/ Tier 2.
  - Digital.gov, Plain Language Guide Series: "Principles of plain language", "Writing for understanding", "Clear and short", and "Test for understanding", no date shown on the page; page metadata gives publication in September 2025; accessed 2026-10-23. https://digital.gov/guides/plain-language/principles , https://digital.gov/guides/plain-language/writing , https://digital.gov/guides/plain-language/writing/clear-short , and "Test for understanding", https://digital.gov/guides/plain-language/test Tier 3 (the Federal Plain Language Guidelines row in `knowledge/SOURCES.md`).
  - `coga/objective-3-clear-content.md` (W3C Making Content Usable, tier 2).
- WCAG: no Level A or AA criterion sets plain language. SC 3.1.3 Unusual Words, 3.1.4 Abbreviations, and 3.1.5 Reading Level are Level AAA, beyond our target, with no entry yet.
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

A text that fails a WCAG criterion is reported under that criterion, once, at the confidence its `wcag/` entry gives. A text that meets WCAG but misses the house standard or the sources' guidance is reported as likely or manual review, never definite, and never as a WCAG failure. A project's `a11y-spec.md` may change the standard; the spec wins.

## What it is

Writing that the intended reader can understand on the first read, find what they need in, and act on. Digital.gov's first rule is to write for the audience; plain language is not "dumbing down", and the right words depend on who is reading.

## Why it matters

Most of what a reader meets on a page is text, and WCAG at A and AA says almost nothing about whether that text can be understood (`coga/objective-3-clear-content.md`). Readers with cognitive or learning disabilities, readers in a second language, and anyone reading in a hurry or under stress are the ones a dense text loses first.

## How to do it

- **Short sentences, one idea each.** Long sentences full of clauses and exceptions lose the main point; split them (Digital.gov; W3C).
- **Active voice.** It says who does what: "You must do it", not "It must be done" (Digital.gov).
- **Present tense where accuracy allows** (Digital.gov).
- **Verbs, not hidden verbs.** "We analyze data", not "We conduct an analysis of the data" (Digital.gov).
- **Common words.** Avoid unnecessarily complex words and phrases; expand an acronym the first time it appears; consider a glossary (W3C).
- **Short paragraphs on one topic,** each opening with a sentence that carries its point. Digital.gov cites writing experts' advice of no more than about 150 words, spread over three to eight sentences.
- **Lists** for parallel items (W3C; Digital.gov).
- **Explain what is implied.** Idioms, metaphors, and jokes need explaining or replacing (`coga/objective-3-clear-content.md`).

## How to check it

- Measure the reading level (`content/reading-level.md`) as a signal, not a verdict.
- Read it aloud, or ask someone outside the team to say back what it means. Digital.gov describes paraphrase testing for short pages and usability testing for longer ones and for forms.
- Look for passive sentences: a form of "to be" plus a past participle, as Digital.gov describes.
