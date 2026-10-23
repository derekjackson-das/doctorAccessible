# ARIA pattern: Name

The ARIA side of one widget. Whether to build the widget at all, the simpler alternative, and the manual tests live in the matching `patterns/` entry; this entry does not repeat them. It covers only what is ARIA-specific: roles, states and properties, naming, keyboard, and what practitioners found when they tested the ARIA itself.

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Pattern name", URL. A pattern, not a requirement: nothing in it is a conformance rule, and following it does not guarantee that assistive technology supports it.
- Normative (tier 1): WAI-ARIA 1.2 role definitions used, and the ARIA in HTML rows for the elements used.
- Practitioner testing (tier 3), at least two from `knowledge/SOURCES.md`: author, "Title", date (and updated date if shown), URL; one line each on what was tested, with which screen reader and browser.
- Support data (tier 3), if used: a11ysupport.io tests updated within three years only, with the date.
- Related entries: `patterns/<name>.md`, `aria/using-aria.md`, `aria/accessible-name.md`, `wcag/...`
- Verified against the live sources: YYYY-MM-DD by <name>

## Status and reporting

The criteria in `patterns/<name>.md` decide whether code fails WCAG; report a failure once, under its criterion. Departing from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier. ARIA that a native element would make unnecessary is advice, never a finding on its own (`aria/using-aria.md`).

**Testing gap.** Include this when fewer than two listed sources report testing the ARIA with assistive technology, or when the tests are old enough that support has changed since. Say what is missing. Do not fill the gap with sources off the list.

## Native first

What native HTML does this job, wholly or partly, and what is lost by using it. Link the `patterns/` entry for the full argument.

## Roles, states, and properties

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|

"Set by" says whether the author writes it once or script updates it as the user acts.

## Naming

Where each part's accessible name comes from, in the order of `aria/accessible-name.md`.

## Keyboard

The keys the APG pattern expects, in our words, marked as a pattern. Then what practitioners found real users and screen readers do differently.

## What testing found

Each practitioner's result: what broke, with which screen reader and browser, and when. Newest first.

## How it fails in code

The ARIA mistakes seen most often for this widget, each tied to the criterion it breaks, or marked advice.
