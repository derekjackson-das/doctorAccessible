# Role: feed

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "feed role", https://www.w3.org/TR/wai-aria-1.2/#feed. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `article`, `aside`, and `section`, https://www.w3.org/TR/html-aria/
- Mapping (tier 2): none. No element maps to this role in "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, https://www.w3.org/TR/html-aam/
- Practice (tier 2): the ARIA Authoring Practices Guide "Feed Pattern" is covered in `aria/patterns/infinite-scroll.md`.
- Reference (tier 3): MDN Web Docs, "ARIA: feed role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/feed_role
- Related entries: `aria/patterns/infinite-scroll.md`, `patterns/infinite-scroll.md`, `aria/roles/article.md`, `aria/roles/list.md`, `aria/live-regions.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-4.1.3-status-messages.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; the MDN page read in full from a downloaded copy.

## Status and reporting

A role is not a criterion. This is a short entry: how to build a feed, its keys, how it fails, and the manual tests are in `aria/patterns/infinite-scroll.md` and `patterns/infinite-scroll.md`, and are not repeated here. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Leaving the role off a list of articles is never a finding.

## What it is

A list of articles that grows or shrinks at its ends as the reader moves through it. WAI-ARIA 1.2: "A scrollable list of articles where scrolling may cause articles to be added to or removed from either end of the list." It is a subclass of `list`, and it announces nothing itself; a loading message still needs a live region (`aria/live-regions.md`).

## The native element

None. A plain list of `article` elements needs no ARIA (`aria/patterns/infinite-scroll.md`).

## What the spec asks of authors

- "When articles are added or removed from either or both ends of a feed, authors SHOULD set aria-busy to true on the feed element before the changes are made and set it to false after the changes are complete."
- "Authors SHOULD avoid inserting or removing articles in the middle of a feed."
- "Authors SHOULD make each article in a feed focusable and ensure that the application scrolls an article into view when user agent focus is set on the article or one of its descendant elements."
- "Authors SHOULD provide keyboard commands for moving focus among articles in a feed".
- Authors SHOULD try to load more articles before focus reaches either end, or MAY end the feed with an article holding a control that loads more.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none.
- Required owned elements: `article`.
- Required states and properties: none. Supported states and properties: none beyond the global ones; `aria-busy` is global.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required ("Accessible Name Required: False").
- On each `article`: `aria-posinset` and `aria-setsize`, with `aria-setsize="-1"` when the total is unknown (`aria/roles/article.md`).

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `article`, `aside`, `section`, and the elements that allow any role, such as `div`.
- **Not allowed:** `ul`, `ol`, `main`, `nav`. A feed is a kind of list, but the role is not allowed on the list elements.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- On an `article` the article role is replaced; the feed's items then need to be `article` elements inside it.
- On an `aside` the complementary landmark is replaced. On a `section` with an accessible name, the `region` landmark is.

## Where the detail lives

- Build, `aria-busy`, keyboard, failures: `aria/patterns/infinite-scroll.md`. Whether to use infinite scroll at all, and the manual tests: `patterns/infinite-scroll.md`.
- axe: `aria-required-children` fires on a `feed` with no `article` inside (mapped to 1.3.1; observed with axe-core 4.14.0 on 2026-11-23; `knowledge/axe-rules.md`).
