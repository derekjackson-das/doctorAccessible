# Role: presentation

- Category: document structure. Synonym: `none` (`aria/roles/none.md`).
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "presentation role" and "Presentational Roles Conflict Resolution", https://www.w3.org/TR/wai-aria-1.2/#presentation. ARIA in HTML, W3C Recommendation 11 August 2026, https://www.w3.org/TR/html-aria/ (the rows say which elements allow it).
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page; lists no HTML equivalent), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: presentation role", last modified 12 May 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role
- Related entries: `aria/roles/none.md`, `aria/roles/generic.md`, `aria/using-aria.md` (rule 4), `aria/aria-in-html.md`, `html/tables.md`, `html/images.md`
- WCAG: `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-1.1.1-non-text-content.md`, `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2 text checked against a downloaded copy.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. This role does real damage when it removes meaning, so most of its failures are definite under 1.3.1 (below).

## What it is

It removes an element's own role, so the element is exposed as if it were a plain container, while its content stays. WAI-ARIA 1.2: "An element whose implicit native role semantics will not be mapped to the accessibility API."

It is **not** `aria-hidden="true"`. The spec's own note says many people mistake the two, which is why `none` was added as a synonym. The text inside a `role="presentation"` element is still read; only the element's role goes.

## The native element

None. APG lists no HTML equivalent. The spec names the intended uses: a layout table, a spacer or clearing element, an element that is only a hook for CSS, or an `img` inside a container that already carries the role and the text alternative.

## What the spec asks of authors, and what browsers do

Quoted from WAI-ARIA 1.2, in the order they matter:

- **Children that complete the element lose their roles too.** "When an explicit or inherited role of presentation is applied to an element with the implicit semantic of a WAI-ARIA role that has required owned elements ... the user agent MUST apply an inherited role of presentation to any owned elements that do not have an explicit role defined." On a `table`: `thead`, `tbody`, `tfoot`, `tr`, `th`, `td`, and `caption` lose theirs. On a `ul` or `ol`: the `li` items. Nested tables and lists are not affected unless they carry the role themselves.
- **Focusable elements ignore it.** "If an element is focusable, or otherwise interactive, user agents MUST ignore the presentation role and expose the element with its implicit role." `role="presentation"` on a link, button, or anything with `tabindex` does nothing; `aria/using-aria.md` rule 4 says never to write it there.
- **Global ARIA attributes cancel it.** "If an element has global WAI-ARIA states or properties, user agents MUST ignore the presentation role and expose the element with its implicit role." `<h1 role="presentation" aria-describedby="x">` is still a heading.
- **On an `img`, it is the same as hiding the image:** "using role="presentation" or role="none" on an HTML img is equivalent to using aria-hidden="true"." "Authors SHOULD NOT provide meaningful alternative text (for example, use alt="" in HTML) when the presentation role is applied to an image."
- Naming: MDN says it must not have a name; do not use `aria-label` or `aria-labelledby`. A name is itself a global property, so it cancels the role.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none. Supported states and properties: none beyond the global ones, and any global one cancels the role (above).
- Prohibited states and properties: `aria-label`, `aria-labelledby`. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: prohibited ("Name From: prohibited").
- Its one context use: removing an element that sits between a composite widget and its parts. The spec's example is a `ul role="tree"` whose `li` elements get `role="presentation"` so the `a role="treeitem"` inside each is owned by the tree.

## Where it can and cannot be used

From ARIA in HTML, section 4, plus the WAI-ARIA 1.2 rules above:

- **Native element:** none. On an `img` with `alt=""` and no name it is redundant ("NOT RECOMMENDED"): that image is already presentational.
- **Allowed:** `article`, `aside`, `br`, `dl`, `embed`, `fieldset`, `figcaption`, `footer`, `form`, `h1` to `h6`, `header`, `hr`, `iframe`, `menu`, `nav`, `ol`, `search`, `section`, `ul`, `wbr`, an `li` whose parent no longer exposes a list role, and the elements that allow any role, such as `div`, `span`, `p`, `table`, `thead`, `tbody`, and `tfoot`.
- **Not allowed:** `main`; an `img` with alt text (it is not on that row's list); an `li` inside a real list; `button`; `a` with `href`; form fields (`input`, `select`, `textarea`); `details`, `summary`; `caption`, `legend`, `dd`, `dt`; `body`.
- **Ignored by browsers even where allowed:** on any focusable element, and on any element that carries a global `aria-*` attribute.

## What an explicit role takes away

Everything about the element's identity: a heading stops being a heading, a list stops being a list, a table stops being a table, along with the children named above. ARIA in HTML decides which elements allow it at all: `main` allows no role; `header`, `footer`, `nav`, `aside`, `form`, `section`, and `search` allow it.

## How it fails in code

- `role="presentation"` or `role="none"` on an element that carries meaning, such as a data table with headers, a list whose grouping matters, or a heading: `wcag/sc-1.3.1-info-and-relationships.md`, definite per that entry (F92).
- On an `img` that conveys information, with meaningful `alt`: not allowed by ARIA in HTML, and the image is hidden, so its information is not available. 1.1.1, likely; open `wcag/sc-1.1.1-non-text-content.md` for the confidence it gives.
- On a focusable element: ignored by browsers, so nothing is removed; advice (`aria/using-aria.md`, rule 4; axe `presentation-role-conflict`, best practice). Also check why it was added: often the author meant to hide something decorative that is still focusable.
- On a layout table that cannot yet be replaced: correct use; advice to replace the table with CSS (`html/tables.md`).

## How to check

Search for `role="presentation"` and `role="none"`. For each: is the element focusable or does it carry a global `aria-*` attribute (then the role is ignored)? Does the element or its children convey structure that the page relies on (then it is a 1.3.1 failure)? In the accessibility tree, confirm what is exposed. axe: `presentation-role-conflict` (best practice).
