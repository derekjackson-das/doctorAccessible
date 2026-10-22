# Pattern: Infinite scroll

- Sources:
  - W3C, "Feed Pattern", ARIA Authoring Practices Guide, https://www.w3.org/WAI/ARIA/apg/patterns/feed/. Tier 2. A pattern, not a requirement.
  - Adrian Roselli, "So You Think You've Built a Good Infinite Scroll", 31 May 2014, updated 5 April 2024, https://adrianroselli.com/2014/05/so-you-think-you-built-good-infinite.html. Tier 3.
- Related entries: `ux/infinite-scroll-and-pagination.md`, `coga/objective-2-find-what-they-need.md`, `coga/objective-5-help-users-focus.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.1-bypass-blocks.md`, `wcag/sc-4.1.3-status-messages.md`, `wcag/sc-2.2.2-pause-stop-hide.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the feed is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer.

## The need it usually serves

A long list, and the team wants the person to keep going without pressing anything: a feed, search results, a product grid. The person wants to find something in the list and, often, to get past it to the rest of the page. Infinite scroll serves the first want only while the person is browsing idly; it works against the second entirely.

## The simpler thing that often serves, and what is lost

Pagination, or a "load more" button that the person presses. `ux/infinite-scroll-and-pagination.md` carries the research on when each serves. Roselli's checklist (2014, kept current to 2024) is the engineering test: can the person press Back and return to the same place; is there paging when the script fails; does the page have a footer anyone can reach; can a keyboard user reach everything after the feed; can a URL point at a place in the list; can the person jump ahead; can the person turn infinite scroll off with one visible control. His blunt observation: content that loads below the last focusable element, or a footer that keeps retreating, might as well not exist for keyboard and screen reader users. What is lost by choosing pagination: the uninterrupted flow. What is gained: a footer, a Back button that works, shareable positions, and a stopping point.

## What doing it right requires

There is no native HTML infinite scroll. The APG feed pattern's expectations, in our words: the feed is a structure, not a widget, so screen readers stay in reading mode inside it; each item is an article with a label and a position in the set; the page tells assistive technology how many items there are and that more are loading; Page Down and Page Up move between items and Control plus Home or End jump out of the feed; because none of this is a desktop convention, the keys must be documented where a person will find them. The pattern is a contract between the page and the assistive technology about when to load more as the reading cursor nears the end.

What the APG does not say: how to meet Roselli's list. A conforming feed can still swallow the footer, break Back, and offer no way off the treadmill.

## What practitioners found when they tested it

- **Roselli, 2014 to 2024.** The failures he lists are structural rather than screen-reader-specific: unreachable footers, lost scroll position on return, no paging fallback when the script breaks, no addressable URL for a position, no way to disable the behavior. He notes that engagement metrics such as bounce rate flatter infinite scroll for reasons that have nothing to do with the person's success. The checklist has had a decade of feedback from other practitioners and he reports it is still rarely met.

## Criteria it touches

Everything after the feed must stay reachable: `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.1-bypass-blocks.md`, `wcag/sc-2.4.3-focus-order.md`. Loading announcements: `wcag/sc-4.1.3-status-messages.md`. Content that auto-updates beside other content: `wcag/sc-2.2.2-pause-stop-hide.md`. Structure of items: `wcag/sc-1.3.1-info-and-relationships.md`. Documented keys if custom ones exist: `wcag/sc-3.3.2-labels-or-instructions.md`. A "load more" control's name and size: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.5.8-target-size-minimum.md`. Timed behavior: `wcag/sc-2.2.1-timing-adjustable.md`.

## Manual tests it demands

- Keyboard only: Tab from the top; record whether the footer is ever reached and how many items load along the way.
- Screen reader, each pair in the spec: read to the end of the loaded items; record whether loading is announced, whether the count is announced, and whether the reading cursor can leave the feed.
- Follow an item, press Back; record where the page lands.
- Disable JavaScript; record whether the list is reachable at all.
- Share the URL from deep in the list; record where it opens.
- Look for the control that turns infinite scroll off; record whether it exists and where.

## What consult should say

1. Does the person need to reach anything below the list? If yes, pagination or "load more", and a footer.
2. Will they come back to a place in the list? If yes, the position needs a URL.
3. If infinite scroll stays: Roselli's checklist in the spec as acceptance criteria, and the feed pattern's announcements.

See `ux/infinite-scroll-and-pagination.md` for the research.
