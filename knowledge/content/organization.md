# Content: Organization

- House standard: `docs/content-standards.md`, section 3.
- Sources:
  - Digital.gov, "Principles of plain language", "Design for understanding", and "Clear and short", no date shown on the page; page metadata gives publication in September 2025; accessed 2026-10-23. https://digital.gov/guides/plain-language/principles , https://digital.gov/guides/plain-language/design , https://digital.gov/guides/plain-language/writing/clear-short Tier 3.
  - W3C WAI, "Writing for Web Accessibility", updated 5 August 2022. https://www.w3.org/WAI/tips/writing/ Tier 2.
  - `coga/objective-2-find-what-they-need.md`, `coga/objective-3-clear-content.md` (tier 2).
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md` (structure shown visually must be in the markup), `wcag/sc-1.3.2-meaningful-sequence.md` (reading order).
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

A text that fails a WCAG criterion is reported under that criterion, once, at the confidence its `wcag/` entry gives. A text that meets WCAG but misses the house standard or the sources' guidance is reported as likely or manual review, never definite, and never as a WCAG failure. A project's `a11y-spec.md` may change the standard; the spec wins.

## What it is

The order and grouping of what is on the page: what comes first, how it is chunked, and how a reader can see the shape before reading the detail.

## Why it matters

Digital.gov notes that a crowded, wordy page puts readers off before they start. Readers with attention or memory difficulties need the important thing first and clear chunks to return to (`coga/objective-2-find-what-they-need.md`). The same layout helps a screen reader user moving by headings and lists.

## How to do it

- **Key information at the top.** Structure pages logically with the most important information first, and summarize long documents up front (Digital.gov).
- **A topic sentence for each paragraph,** and one topic per paragraph (Digital.gov).
- **Short sections** that a descriptive heading can summarize; long sections are hard to name (Digital.gov).
- **Lists for scanning** (Digital.gov; W3C), **tables for complex relationships** (Digital.gov).
- **Emphasis sparingly.** Bold or italics for what matters most; Digital.gov warns that all-capital text is harder to read and comes across as shouting.
- **Order follows the reader's task,** not the order the writer thought of it (house standard).

## How to check it

- Read only the first sentence of each section: does it carry the point?
- Read only the headings: do they outline the page (`content/headings.md`)?
- Check that lists, tables, and headings are real markup, not visual styling (`wcag/sc-1.3.1-info-and-relationships.md`).
