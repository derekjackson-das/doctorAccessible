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

### Library news on the home page (2026-10-01)

- **For:** staff and students glancing at the home page on a phone.
- **Trying to:** see what is new at the library this week.
- **We will build:** a short list of this week's news items, each a heading and one sentence with a link.
- **Instead of:** a news carousel.
- **Why this is right:** a list shows every item at once and needs no controls.
- **Manual tests owed:** VoiceOver on iOS reads the list in order.

## Pattern decisions

| Date | Pattern | Decision | Why |
|---|---|---|---|
| 2026-10-01 | Home page news | A list, not a carousel | See the need statement |

## Banned patterns

- **Carousels and slideshows, rotating or not.** Decided 2026-09-30 in consult: in our user testing, readers missed most slides. Use a short list of linked items instead.

## Open manual tests

None owed.

## Change log

| Date | Change | By |
|---|---|---|
| 2026-10-01 | Spec created in consult | Library web team |
