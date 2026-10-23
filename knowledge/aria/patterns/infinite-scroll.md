# ARIA pattern: Infinite scroll (feed)

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Feed Pattern", no date shown, accessed 2026-10-23. https://www.w3.org/WAI/ARIA/apg/patterns/feed/ A pattern, not a requirement: nothing in it is a conformance rule, and following it does not guarantee that assistive technology supports it.
- Normative (tier 1): WAI-ARIA 1.2, `feed` and `article` roles and `aria-busy`, `aria-posinset`, `aria-setsize`, W3C Recommendation 6 June 2023, https://www.w3.org/TR/wai-aria-1.2/#feed. ARIA in HTML, W3C Recommendation 11 August 2026, https://www.w3.org/TR/html-aria/ : the `article` element has the implicit `article` role.
- Practitioner testing (tier 3): Roselli's "So You Think You've Built a Good Infinite Scroll" (2014, updated 2024), with his 2018 keyboard check of the APG feed example, is in `patterns/infinite-scroll.md`. This entry adds none.
- Related entries: `patterns/infinite-scroll.md` (whether to use it, the checklist, the criteria, the manual tests), `ux/infinite-scroll-and-pagination.md`, `aria/using-aria.md`, `aria/accessible-name.md`, `wcag/sc-4.1.3-status-messages.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.3-focus-order.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

The criteria in `patterns/infinite-scroll.md` decide whether code fails WCAG; report a failure once, under its criterion. Departing from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier. Leaving out the `feed` role, `aria-posinset`, or `aria-setsize` is never a finding on its own; the APG's keys are suggestions.

**Testing gap.** Nothing on the list tests the `feed` role with a screen reader (`patterns/infinite-scroll.md`). Every point about how it behaves comes from the APG. Test with the spec's assistive technology.

## Native first

A paged list with real links, or a "Load more" button, keeps the footer reachable and gives a place to return to. See `patterns/infinite-scroll.md` and `ux/infinite-scroll-and-pagination.md`. A plain list of `article` elements needs no ARIA at all; the `feed` role is an addition for screen readers that support it.

## Roles, states, and properties

From the APG feed pattern, in our words:

| Element | Role | States and properties | Set by | Notes |
|---|---|---|---|---|
| The list of items | `feed` | `aria-labelledby` pointing at a visible heading, or `aria-label` | Author | Everything inside it is in an article |
| The list | | `aria-busy="true"` while items are added or removed, when the update takes more than one DOM operation, then `"false"` | Script | The APG calls resetting it to false extremely important, or the new items may not be exposed |
| Each item | `article` (the element gives it) | `aria-labelledby` pointing at its title; `aria-describedby` pointing at its main text, strongly recommended | Author | |
| Each item | | `aria-posinset` (its position) and `aria-setsize` (the total loaded, the total in the feed, or -1 if unknown) | Script | Updated as items load |

Ours, not the APG: a visible "loading" or "more loaded" message needs to be a live region (`role="status"`, `aria-live`, or `output`), or to receive focus, under `wcag/sc-4.1.3-status-messages.md`. The `feed` role does not announce anything itself.

## Naming

The feed is named by its heading; each article by its own title (`aria/accessible-name.md`).

## Keyboard

The APG says the feed has no established keyboard convention, and stresses easily discoverable documentation of whatever keys the page supports. It suggests Page Down and Page Up to move between articles, and Control+End and Control+Home to leave the feed forward and back. In 2018 Roselli found that the APG's own example put a control after the feed that keyboard users could not reach. In his 2019 pull request he noted that nothing told the person about Control+End. Both are in `patterns/infinite-scroll.md`.

## What testing found

Nothing on the list tests the ARIA of a feed. See `patterns/infinite-scroll.md` for Roselli's keyboard findings.

## How it fails in code

- A visible "loading" or "N more loaded" message inserted with no live-region role, and focus not moved to it: `wcag/sc-4.1.3-status-messages.md`, definite (F103).
- Content after the feed, such as the footer, that keyboard users can never reach: `wcag/sc-2.1.1-keyboard.md`, at that entry's confidence.
- Focus lost when items are removed or replaced: manual review under `wcag/sc-2.4.3-focus-order.md`, which has no case for it yet.
- `aria-busy="true"` never reset to false: advice, from the APG; a finding only through the criterion its effect breaks, and confirm with a screen reader.
- Page Down and the other suggested keys not supported: not a finding; document whatever keys are supported.
