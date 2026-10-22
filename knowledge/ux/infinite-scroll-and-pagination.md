# UX heuristic: Infinite scroll and pagination

- Sources:
  - Hoa Loranger, "Infinite Scrolling Is Not for Every Website", Nielsen Norman Group, 2 February 2014. https://www.nngroup.com/articles/infinite-scrolling/
  - Tim Neusesser, "Infinite Scrolling: When to Use It, When to Avoid It", Nielsen Norman Group, 4 September 2022. https://www.nngroup.com/articles/infinite-scrolling-tips/
- Tier: 3, usability research. Nielsen Norman Group is on `knowledge/SOURCES.md` for UX claims only. Neusesser also comments on screen readers and ARIA; those remarks are not cited here. Accessibility claims below come from the linked `wcag/` and `coga/` entries.
- Related entries: `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.3-focus-order.md`, `coga/objective-2-find-what-they-need.md`, `coga/objective-4-avoid-mistakes.md`, `coga/objective-5-help-users-focus.md`
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the same list is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer.

## What the research found

- **It suits browsing, not finding.** Endless loading works for a flat stream of similar items that people browse with no particular goal, such as social feeds or news. It works poorly when people look for something specific, compare items, or only need the top few results (both articles).
- **People lose their place.** With pages, people remember that an item was on page 3; on one long page they cannot (both articles). When the Back button returns them to the top of the list, they have to scroll through everything again (Neusesser).
- **It hides the end.** The footer, with contact details and policies, can become unreachable. When new items load out of sight, people may think they have reached the end when they have not (Neusesser). On desktop the scroll bar misstates how much is left (Loranger).
- **Too many choices can stall people.** Pages give a beginning, an end, and a sense of progress; an endless list can leave people looking without acting (Loranger).
- **Middle options:** a Load More button keeps the footer reachable, signals that there is more, and loads less for people on slow or metered connections, at the cost of one click (Neusesser). Pagination built into a scrolling list was too new for NN/g to have test data in 2022 (Neusesser).

## When the pattern serves people

When the content is a stream of items of equal weight, people browse rather than search, and nothing important sits in the footer.

## When it does not

- Search results, product listings people compare, and anything people need to find again (both articles).
- Sites whose footer holds help, contact, or policy links.
- Audiences on slow connections or limited data (Neusesser).

## The accessibility side

- Loading more must work from the keyboard, and the footer's links must stay reachable by keyboard; check `wcag/sc-2.1.1-keyboard.md`.
- New items must enter the focus order where they make sense (`wcag/sc-2.4.3-focus-order.md`). WCAG does not require a way to skip past a long list on one page; Bypass Blocks covers blocks repeated across pages. A skip link is still worth offering.
- WCAG does not require the page to announce that more items loaded. If it shows a message such as "20 more results loaded", WCAG 2.2 SC 4.1.3 Status Messages (Level AA), W3C Rec 12 Dec 2024, tier 1, requires that assistive technology can present it without moving focus. No entry yet.
- `coga/objective-2-find-what-they-need.md` (find and refind), `coga/objective-4-avoid-mistakes.md` (let users go back without losing their place), and `coga/objective-5-help-users-focus.md` (avoid too much content) cover the cognitive side.

## What consult should say

1. Is the person in the need statement looking for something specific, comparing, or coming back later? Then use pagination, or a Load More button with a count of items shown and the total.
2. Is anything important in the footer? Then classic infinite scroll is ruled out.
3. If infinite scroll stays, the Back button returns people to the same item, and loading shows that it is happening.
