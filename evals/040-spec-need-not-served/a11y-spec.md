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

### Opening hours (2026-10-01)

- **For:** staff and students on a phone, deciding whether to walk over now.
- **Trying to:** "Is Widener open right now, and until when?"
- **We will build:** today's opening and closing time, as text, as the first thing in the main content.
- **Instead of:** a weekly timetable as the only way to find today.
- **Why this is right:** the question is about today; a week's table makes people find the day first.
- **Manual tests owed:** on a phone with VoiceOver, today's hours are the first thing read in the main content.

## Pattern decisions

None yet.

## Banned patterns

None.

## Open manual tests

None owed.

## Change log

| Date | Change | By |
|---|---|---|
| 2026-10-01 | Spec created in consult | Library web team |
