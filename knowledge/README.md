# Knowledge library

Markdown entries the agents and skills read on demand. One entry per success criterion or topic. This is the thing the team maintains.

## Rules for an entry

- Write it in your own words from the source. This repo is public. Quote only the normative text itself, which the W3C licence allows with attribution, and link everything else.
- Every entry carries: the standard and version, the level, the tier 1 source URL, the tier 2 source URL, and the date it was verified against the live page.
- Tiers: 1 normative (the Recommendation text), 2 informative from W3C (Understanding, Techniques, tutorials, APG), 3 practitioner (WebAIM, Deque rule descriptions, MDN, and the like). A tier 3 claim never stands alone for what a requirement is.
- Say which versions the criterion exists in. WCAG 2.0, 2.1, and 2.2 are all live in different regulations.
- Working drafts are awareness only.
- Name the file `sc-<number>-<slug>.md` for WCAG entries. Start from `wcag/_template.md`.
- Add the entry to `INDEX.md` in the same commit.

## Verifying

"Verified" means a person or an agent opened the live source on that date and confirmed the quoted text and the level. Re-verify when W3C publishes an updated Recommendation.
