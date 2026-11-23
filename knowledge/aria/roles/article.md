# Role: article

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "article role", https://www.w3.org/TR/wai-aria-1.2/#article. ARIA in HTML, W3C Recommendation 11 August 2026, row for `article`, https://www.w3.org/TR/html-aria/#el-article
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.8, https://www.w3.org/TR/html-aam/#el-article
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: article role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/article_role
- Related entries: `aria/patterns/infinite-scroll.md`, `aria/roles/document.md`, `aria/roles/application.md`, `aria/roles/region.md`, `html/landmarks.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="article"` on an `article` is redundant and never a finding. Almost nothing about this role is a WCAG failure by itself.

## What it is

A self-contained piece of content: a post, a news story, a comment. WAI-ARIA 1.2: "A section of a page that consists of a composition that forms an independent part of a document, page, or site." The spec is explicit that it "is not a navigational landmark".

## The native element

`article` (HTML-AAM 3.5.8). ARIA in HTML marks `role="article"` on it "NOT RECOMMENDED".

## When writing the role is justified

- On a `div` when `article` cannot be used (`aria/using-aria.md`, rule 1).
- As the items of a `feed`, which owns `article` elements (`aria/patterns/infinite-scroll.md`). An `article` element does this without the role.
- Inside an `application`, on a focusable element that holds ordinary content: WAI-ARIA 1.2 names `document` or `article` for that (`aria/roles/application.md`).

## What the spec asks of authors

- "When an article is in the context of a feed, the author MAY specify values for aria-posinset and aria-setsize."
- The spec's other statements are for assistive technology, not authors: when the user moves into an article, tools that intercept keys "SHOULD switch to document browsing mode".
- Nested articles are related to the article they sit in: a comment inside a post.
- Naming: allowed, from the author; not required.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: `aria-posinset`, `aria-setsize`, for articles in a feed. MDN: `aria-posinset` counts from 1.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.
- It stands alone, or is one item in a `feed`.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `article` (redundant, "NOT RECOMMENDED").
- **Allowed:** the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `section`, `main`, `aside`, `nav`, `header`, `footer`; an `li` inside a list; `button`; `a` with `href`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- ARIA in HTML allows `application`, `document`, `feed`, `main`, `none`, `presentation`, and `region` on an `article`. Each replaces the article role.
- A `header` or `footer` inside an `article`, or inside an element with `role="article"`, is not a `banner` or `contentinfo` landmark (ARIA in HTML, rows for `header` and `footer`; `html/landmarks.md`).

## How it fails in code

- The items of a `role="feed"` are not articles: `aria/patterns/infinite-scroll.md` gives the criterion and confidence.
- Every card, teaser, and widget on a page wrapped in `article`: advice. It is not a failure. MDN notes that many assistive technologies let users move between articles, so the role should mark something worth moving to.
- `role="article"` used as if it were a landmark, with `main` missing: the missing landmark is the issue, under `html/landmarks.md`.

## How to check

Search for `role="article"` and `article`. Could each one stand on its own? In a feed, are `aria-posinset` and `aria-setsize` set and kept current as items load? In the browser's accessibility tree, confirm the article role. Observed with axe-core 4.14.0 on 2026-11-23: no rule fired on a `role="article"` on a `div`.
