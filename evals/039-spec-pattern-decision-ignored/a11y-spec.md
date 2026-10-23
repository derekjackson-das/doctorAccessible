# Accessibility spec: Harvard Library visitor pages

## Conformance target

WCAG 2.2 Level AA (Harvard policy names 2.1 AA; 2.2 AA satisfies it).

## Who we are building for

Harvard staff and graduate students looking up library services, often on a phone between classes. Tested with VoiceOver on iOS, NVDA with Chrome, keyboard only, 400% zoom.

## Design system and components

None; plain HTML and CSS.

## Content standards

The house defaults in Doctor Accessible's `docs/content-standards.md` apply. Reading level target: grade 8.

## Need statements

### Borrowing questions (2026-10-01)

- **For:** students with a quick question about borrowing.
- **Trying to:** find the one answer they need without reading the whole page.
- **We will build:** questions that open to show their answer.
- **Instead of:** one long page of text.
- **Why this is right:** people scan the questions and open one.
- **Manual tests owed:** each question opens with Enter and Space and with VoiceOver on iOS.

## Pattern decisions

| Date | Pattern | Decision | Why |
|---|---|---|---|
| 2026-10-01 | Show/hide sections (questions, policies) | Native `details` and `summary`, not a scripted accordion | Works without script, and the team does not maintain widget code |

## Banned patterns

None.

## Open manual tests

None owed.

## Change log

| Date | Change | By |
|---|---|---|
| 2026-10-01 | Spec created in consult | Library web team |
