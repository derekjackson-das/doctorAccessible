# UX heuristic: Carousels

- Sources:
  - Jakob Nielsen, "Auto-Forwarding Carousels and Accordions Annoy Users and Reduce Visibility", Nielsen Norman Group, 19 January 2013. https://www.nngroup.com/articles/auto-forwarding/
  - Kara Pernice, "Carousel Usability: Designing an Effective UI for Websites with Content Overload", Nielsen Norman Group, 14 September 2013, last reviewed 7 August 2026. https://www.nngroup.com/articles/designing-effective-carousels/
- Tier: 3, usability research. Nielsen Norman Group is on `knowledge/SOURCES.md` for UX claims only. Accessibility claims below come from the linked `wcag/` and `coga/` entries.
- Related entries: `wcag/sc-2.2.2-pause-stop-hide.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.5.8-target-size-minimum.md`, `coga/objective-2-find-what-they-need.md`, `coga/objective-5-help-users-focus.md`
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the same carousel is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer.

## What the research found

- **People miss what is in a carousel.** On screens large and small, people often scroll straight past the carousel, and anything beyond the first frame is seen least (Pernice). The benefits the article names are that several teams get to share the top of the home page, and that more content sits near the top, where it has some chance of being seen.
- **Movement makes it worse.** In an NN/g usability session, a participant looked for a sale that was the largest item on the home page and gave up, because the panel holding it rotated away every few seconds; that offer was on screen only a fifth of the time (Nielsen). Nielsen notes that people who read slowly, and people reading in a second language, may not finish a panel before it changes.
- **Moving content looks like advertising.** Because it moves, people assume it may be an ad and pass over it (Nielsen). Pernice adds that animated items resembling ads tend to be ignored.
- **One frame can mislead.** The team sees the set; a visitor may see one frame and judge the organization by it (Pernice).
- **A single static hero image may serve better in some cases,** partly because choosing one image forces a stronger choice (Pernice).

## When the pattern serves people

Rarely, and only when the content in it is optional. If a carousel is used, NN/g's guidance is: five frames or fewer, clear images and text, controls inside the carousel that show how many frames there are and which is current, controls large enough to hit, and no auto-advance unless the timing has been tested. Its rule of thumb for timing is about three words per second, and it advises against auto-advance on mobile (Pernice).

## When it does not

- When anything in it is important. Important content placed in a carousel should also be somewhere people will see it (Pernice).
- When it advances on its own and the audience includes slow readers or second-language readers (Nielsen). For people with motor or attention impairments, see the accessibility side below.
- When it exists to settle which department gets the top of the page, which is a governance problem, not a user need.

## The accessibility side

- An auto-advancing carousel that starts on its own, runs more than five seconds, and sits beside other content needs a way to pause, stop, or hide it. See `wcag/sc-2.2.2-pause-stop-hide.md`.
- Its controls need names and roles (`wcag/sc-4.1.2-name-role-value.md`) and a minimum target size (`wcag/sc-2.5.8-target-size-minimum.md`).
- `coga/objective-5-help-users-focus.md` (limit interruptions, user control over moving content) and `coga/objective-2-find-what-they-need.md` (key information visible without extra steps) cover the cognitive side.
- Practitioner tests of carousels with assistive technology belong in the `patterns` carousel entry (roadmap 3.2), not here.

## What consult should say

1. What is the one thing the person in the need statement must see on this page? Put it in plain text near the top, not in a frame.
2. Why is there more than one item? If the answer is that several teams want the space, say so and offer a static hero plus a short list of links.
3. If a carousel stays, it does not move on its own, and the rest of the page does not depend on anyone seeing frame two.

"Build less" is the usual answer: a static hero, or a list.
