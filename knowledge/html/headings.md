# HTML: Headings

- Tier 1: HTML Living Standard, §4.3.11 Headings and outlines, accessed 2026-10-23. https://html.spec.whatwg.org/multipage/sections.html
- Tier 1: ARIA in HTML, W3C Recommendation 11 August 2026, row for `h1` to `h6` (implicit `heading` with `aria-level` from the tag). https://www.w3.org/TR/html-aria/
- Tier 2: WAI Tutorials, "Headings" (updated 4 May 2017), Page Structure Tutorial. https://www.w3.org/WAI/tutorials/page-structure/headings/
- Related: `content/headings.md` (what a heading should say), `html/landmarks.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.4.6-headings-and-labels.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

This entry says how to mark headings up; `content/headings.md` says what they should say. Whether code fails WCAG is decided by the `wcag/` entries named below; report a failure once, under its criterion, at that entry's confidence. A skipped level breaks the HTML Standard, but no `wcag/` entry makes it a WCAG failure (the 2.4.6 entry calls it a best practice), so it is advice, not a finding.

## The native approach

- **`h1` to `h6` for every heading,** at the level that matches the outline.
- **A level-1 heading.** The HTML Standard recommends ("should") that a document with headings has at least one at level 1.
- **No skipping going down.** The HTML Standard makes it a conformance rule: each heading after another must be at most one level deeper, the same level, or any level higher. An `h1` followed by an `h3` is non-conforming. Going back up more than one level, when a subsection closes, is allowed (HTML Standard; WAI tutorial).
- **Headings for structure, not size.** Style with CSS; do not pick a level for how it looks.

## What the native approach satisfies by default

The heading role and level are exposed with no ARIA, and screen reader users can move by heading or by level (`wcag/sc-1.3.1-info-and-relationships.md`).

## Where people go wrong

- Bold or large text standing in for a heading: no heading exposed (`wcag/sc-1.3.1-info-and-relationships.md`, when the visual design implies a heading).
- A heading element used only to make text big, where no section follows.
- Skipped levels: non-conforming HTML, and against the `content/headings.md` house rule. Advice, not a WCAG finding.
- `role="button"` put on a heading for an accordion, which removes the heading (`aria/patterns/accordion.md`): put a `button` inside the heading instead.

## When ARIA is genuinely needed

Almost never. `role="heading"` with `aria-level` only where a real heading element cannot be used, such as text inside a component you do not control (`aria/using-aria.md`, rule 1).
