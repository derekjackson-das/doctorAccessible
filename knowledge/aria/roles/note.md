# Role: note

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "note role", https://www.w3.org/TR/wai-aria-1.2/#note. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `aside` and `section`, https://www.w3.org/TR/html-aria/#el-aside
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page; lists no HTML equivalent), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: note role", last modified 12 May 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/note_role
- Related entries: `aria/roles/complementary.md`, `aria/roles/region.md`, `aria/roles/group.md`, `aria/aria-in-html.md`
- WCAG: none directly. A note is ordinary content; nothing about the role is a criterion.
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2 and ARIA in HTML text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). Using this role, or not using it, is never a WCAG finding. The one thing to check is what it replaced.

## What it is

An aside to the main content: a tip, a caveat, a parenthetical box. WAI-ARIA 1.2: "A section whose content is parenthetic or ancillary to the main content of the resource."

## The native element

None. APG lists no HTML equivalent. `aside` is close in meaning but maps to the `complementary` landmark (`aria/roles/complementary.md`).

## When writing the role is justified

When a callout should be marked as an aside without becoming a landmark. MDN: use it when no native element or other role fits; a quotation is a `blockquote`, and a caption belongs in a `figure`.

## What the spec asks of authors

WAI-ARIA 1.2 places no SHOULD or MUST on authors for this role.

- Naming: allowed, from the author; not required. MDN: `aria-labelledby` when the note has a visible title, otherwise `aria-label`, and either is optional.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.
- It stands alone: it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** none.
- **Allowed:** `aside`, `section`, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `main`, `nav`, `header`, `footer`, `article`, `form`; an `li` inside a list; `button`; `a` with `href`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- On an `aside`, the `complementary` landmark goes. That is the use ARIA in HTML allows it for: an `aside` that is a small callout, not a part of the page worth a landmark.
- On a `section` with a name, the `region` landmark goes.

## How it fails in code

- `role="note"` on an `aside` that is the page's sidebar: the landmark is removed. Advice (`html/landmarks.md`).
- A note that is an error, a warning the user must act on, or a status update: the role does not announce anything. See `aria/live-regions.md` for what does, and `wcag/sc-4.1.3-status-messages.md` for when it is required.

## How to check

Search for `role="note"`. Is the content an aside, and was a landmark replaced on purpose? In the browser's accessibility tree, confirm the role. Observed with axe-core 4.14.0 on 2026-11-23: no rule fired on a `role="note"` on a `div`.
