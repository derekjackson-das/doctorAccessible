# Pattern: Infinite scroll

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Feed Pattern", accessed 2026-10-22 (the page shows no date). https://www.w3.org/WAI/ARIA/apg/patterns/feed/ A pattern, not a requirement.
- W3C tutorial: none.
- Practitioner sources (tier 3, on `knowledge/SOURCES.md`):
  - Adrian Roselli, "So You Think You've Built a Good Infinite Scroll", 31 May 2014, updated 5 April 2024. https://adrianroselli.com/2014/05/so-you-think-you-built-good-infinite.html An eleven-point checklist, with his keyboard check of the Authoring Practices feed example (2018). No screen reader test results.
- Related entries: `ux/infinite-scroll-and-pagination.md` (whether people want it at all), `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-4.1.3-status-messages.md`, `coga/objective-2-find-what-they-need.md`; `aria/` once that domain exists.
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

The criteria listed below decide whether code fails WCAG; report a failure once, under its criterion. Everything else here is advice. Using this pattern, or not using the simpler alternative, is never a finding on its own. A departure from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier.

**Testing gap.** The issue asks for at least two practitioners who tested the pattern with assistive technology. The sources list has one relevant article, and it reports a keyboard check, not a screen reader test. Nothing readable on the list tests the `feed` role with a screen reader, voice control, or magnification; a11ysupport.io renders its results with script and could not be read for this entry. Every claim below about how the feed role behaves comes from the Authoring Practices and needs confirming in the manual tests.

## The need

Browsing a long stream of similar items, such as posts or news, without stopping to page. `ux/infinite-scroll-and-pagination.md` covers when that need is real and when people are actually trying to find or compare something.

## The simpler alternative and its cost

- **Pagination.** Numbered pages with real links. Every page has an address, the back button works, the footer is reachable, and nothing depends on script. The cost: a click and a page load between screens, which interrupts browsing.
- **A "Load more" button with a count.** Content loads only when the person asks, the footer stays reachable, and a line such as "Showing 40 of 212" says where they are. The cost: a click per batch, and the team still has to manage focus and position when new items arrive.

Roselli's view, from his checklist, is that automatic infinite scroll should at least offer a visible, one-click way to switch to paging.

## What doing it right requires

From the Authoring Practices feed pattern, unless noted:
- **Structure:** the list has the `feed` role and a name; each item is an `article` with a name and, ideally, a description; each article states its position and the set size (or -1 when unknown); the feed is marked busy while items are added or removed.
- **Keyboard:** there is no established convention, so the page must document its keys. The suggested ones are Page Down and Page Up between articles, and Control+End and Control+Home to leave the feed forward or backward.
- **A way past the feed.** In 2018 Roselli found that the Authoring Practices' own feed example put a control after the feed that a keyboard user could never reach. He raised an issue, then filed a pull request in 2019, noting that the example's Control+End shortcut moves past the feed but nothing tells the person so. Whether the example has since been fixed is not recorded on the list. Anything after an endless list is at risk, including the footer.
- **Roselli's checklist**, in brief: the back button returns to the same place; paging still works when script fails; the footer can be reached or is not shown; keyboard users can reach everything else on the page; a URL can point to a place in the list; people can jump ahead several screens; memory use stays reasonable; there is a visible control to turn infinite scroll off; and the feature came from research or user requests, and was tested with real users.

## Criteria it touches

| SC | Title | Level | Entry | Why it comes up |
|---|---|---|---|---|
| 2.1.1 | Keyboard | A | `wcag/sc-2.1.1-keyboard.md` | Loading more, and reaching content after the feed, by keyboard |
| 2.4.3 | Focus Order | A | `wcag/sc-2.4.3-focus-order.md` | Where new items enter the focus order; focus lost when items are removed |
| 2.4.7 | Focus Visible | AA | `wcag/sc-2.4.7-focus-visible.md` | Focus on articles as the person moves through them |
| 4.1.2 | Name, Role, Value | A | `wcag/sc-4.1.2-name-role-value.md` | Names and roles on the feed, its articles, and any load control |
| 4.1.3 | Status Messages | AA | `wcag/sc-4.1.3-status-messages.md` | If a "loading" or "more loaded" message is shown, it is exposed without moving focus |
| 1.4.10 | Reflow | AA | `wcag/sc-1.4.10-reflow.md` | The list and its controls at narrow widths and high zoom |

## Manual tests

With the assistive technology named in the project's `a11y-spec.md`:
- Keyboard only: reach the footer and every control after the list; follow an item and press Back, and confirm the list returns to the same item.
- Screen reader in reading mode: more items load as the person reads; the documented keys move between articles and out of the feed; any loading message is announced.
- Script disabled or failing: the list still pages.
- Zoom to 400%: the list reflows and the turn-off or load-more control stays reachable.
- Check the switch to paging, if offered, is visible and works in one action.
