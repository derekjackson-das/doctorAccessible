# Pattern: Name

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Pattern name", URL. A pattern, not a requirement: nothing in it is a conformance rule, and following it does not guarantee that assistive technology supports it.
- W3C tutorial (tier 2), if one exists: WAI Tutorials, "Title", URL.
- Practitioner testing (tier 3), at least two from `knowledge/SOURCES.md`: author, "Title", date (and updated date if shown), URL; one line each on what was tested and with what.
- Related entries: `ux/...` (whether people want the pattern at all), `aria/patterns/<name>.md` for the roles, states, naming, and keyboard, where the pattern uses ARIA, `wcag/...`, `coga/...`
- Verified against the live sources: YYYY-MM-DD by <name>

## Status and reporting

The criteria listed below decide whether code fails WCAG; report a failure once, under its criterion. Everything else here is advice. Using this pattern, or not using the simpler alternative, is never a finding on its own. A departure from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier.

**Testing gap.** Include this when fewer than two sources on the list report testing the pattern with assistive technology, or when the tests are old enough that browsers or screen readers have changed since. Say what is missing (which assistive technology, which years) and which listed sources could not be read. Do not fill the gap with sources off the list.

## The need

What people are usually trying to do when a team reaches for this pattern. One short paragraph.

## The simpler alternative and its cost

The plainer thing that often meets the same need, usually native HTML or static content, and what is honestly lost by choosing it. This is the section that matters most.

## What doing it right requires

The parts a correct build cannot skip, summarized from the Authoring Practices and corrected by what practitioners found broken in real assistive technology. Native HTML first. Link to the Authoring Practices page for detail; do not restate it. Where an `aria/patterns/` entry exists, the ARIA detail (roles, states, naming, keyboard) lives there; test results stay here and are not repeated there.

## Criteria it touches

| SC | Title | Level | Entry | Why it comes up |
|---|---|---|---|---|

## Manual tests

What a person has to try, with which assistive technology, before the pattern counts as working. Written as checks for a tester, never as what a user "would experience".
