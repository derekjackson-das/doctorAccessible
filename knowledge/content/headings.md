# Content: Headings

- House standard: `docs/content-standards.md`, section 4.
- Sources:
  - Digital.gov, "Design for understanding: Headings", no date shown on the page; page metadata gives publication in September 2025; accessed 2026-10-23. https://digital.gov/guides/plain-language/design/headings Tier 3.
  - W3C WAI Tutorials, "Headings" (Page Structure), updated 4 May 2017. https://www.w3.org/WAI/tutorials/page-structure/headings/ Tier 2.
  - W3C WAI, "Writing for Web Accessibility", updated 5 August 2022. https://www.w3.org/WAI/tips/writing/ Tier 2.
- WCAG: `wcag/sc-2.4.6-headings-and-labels.md` (headings describe topic or purpose), `wcag/sc-1.3.1-info-and-relationships.md` (headings marked up as headings), `wcag/sc-2.4.2-page-titled.md` (the page title).
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

A heading that does not describe its section can fail SC 2.4.6. Report it there at the confidence the 2.4.6 entry gives; whether a heading "describes" is often a judgment call. From the text alone the reviewer reports likely; the 2.4.6 entry makes it definite once a person confirms it. A heading that meets 2.4.6 but is weak, such as a bare topic word where a question or statement would serve better, misses the house standard and is likely or manual review, never definite. A project's `a11y-spec.md` may change the standard; the spec wins.

## What it is

The short labels over each section that let a reader see the page's outline and jump to what they need.

## Why it matters

People skim headings to decide whether a page has what they came for, and screen reader users move by heading. A heading that says only "Overview" or "More" tells neither group anything.

**A conflict between sources.** Digital.gov warns that topic headings such as "General", "Application", and "Scope" can be too vague to help, but it still allows topic headings, and its own guide uses "Overview" as one. The house standard is stricter: "Overview", "Introduction", and "More" are not headings. Following principle 13, the stricter reading applies.

## How to do it

- **Say what the section holds.** Digital.gov ranks question headings first when the reader's questions are known ("How do I apply?"), statement headings next, and plain topic headings last.
- **Concise but descriptive.** Not so long they overwhelm the text, and not so short they say nothing (Digital.gov's "Be concise, but descriptive" examples). "Deadlines for spring term", not "Dates".
- **One main heading** that says what the page is, then nested levels in order. No skipped levels going down, for example an `h2` followed directly by an `h4` (house standard). The W3C tutorial says to avoid skipping where possible, and notes that closing a subsection can jump back up more than one level; the house rule is the stricter one.
- **Draft the headings first.** Digital.gov suggests writing the headings before the text, to find the page's structure.

## How to check it

- Read the headings alone, in order: can someone tell what the page covers and where to go?
- Check each heading against the text under it: does it describe that text?
- Check the levels in the markup, with no skipped ranks and one main heading (`wcag/sc-1.3.1-info-and-relationships.md`).
