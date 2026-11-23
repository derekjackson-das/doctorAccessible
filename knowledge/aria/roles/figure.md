# Role: figure

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "figure role", https://www.w3.org/TR/wai-aria-1.2/#figure. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `figure` and `figcaption`, https://www.w3.org/TR/html-aria/#el-figure
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.42, https://www.w3.org/TR/html-aam/#el-figure
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: figure role", last modified 20 November 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/figure_role
- Related entries: `html/images.md`, `aria/roles/img.md`, `aria/accessible-name.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.1.1-non-text-content.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="figure"` on a `figure` is redundant and never a finding. The role does not give an image a text alternative; that is still owed under 1.1.1.

## What it is

A piece of content set apart from the running text and referred to from it: an image, a diagram, a code sample, an example. WAI-ARIA 1.2: "A perceivable section of content that typically contains a graphical document, images, code snippets, or example text."

Unlike `img`, a figure's content stays exposed. A figure can hold an image, a table, a list, and a caption, and each keeps its own role (`aria/roles/img.md`).

## The native element

`figure`, with `figcaption` for the caption (HTML-AAM 3.5.42). ARIA in HTML marks `role="figure"` on it "NOT RECOMMENDED".

## When writing the role is justified

On a `div` when `figure` and `figcaption` cannot be used (`aria/using-aria.md`, rule 1). MDN gives the retrofit case: markup the team cannot change, with the role added by script.

## What the spec asks of authors

- "Authors SHOULD provide a reference to the figure from the main text, but the figure need not be displayed at the same location as the referencing element."
- "Authors MAY reference text serving as a caption using aria-describedby."
- "Authors MAY provide a label using aria-label or MAY reference text serving as a label using aria-labelledby."
- Naming: allowed, from the author; not required ("Accessible Name Required: False").
- MDN: `aria-labelledby` for a short visible caption, `aria-describedby` for a longer one, `aria-label` when there is no visible caption. With the native elements, the `figcaption` does this.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.
- It stands alone: it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `figure` (redundant, "NOT RECOMMENDED").
- **Allowed:** the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** `img`; `picture`; `section`, `aside`, and the other landmark elements; an `li` inside a list; `figcaption` (it allows `group`, `none`, and `presentation` only).

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

A `figure` with a `figcaption` allows no other role. A `figure` without one allows any role, and each replaces the figure. `role="img"` on a `figure` is the one to watch: it hides everything inside, so it suits only a figure that is a single picture with a name (`aria/roles/img.md`).

## How it fails in code

- An image inside a figure with no text alternative, on the theory that the caption covers it: `wcag/sc-1.1.1-non-text-content.md`, at that entry's confidence for the image. A caption says what the figure is; it is not always an alternative for the image.
- A `div role="figure"` whose caption is not tied to it with `aria-labelledby` or `aria-describedby`: advice. The caption is still exposed as text.
- `role="img"` on a figure whose content needs to be reached: see `aria/roles/img.md`.

## How to check

For each `role="figure"` and `figure`: every image inside has its own alternative, and the caption is tied to the figure. In the browser's accessibility tree, confirm the figure, its name or description, and that its contents are still there. Observed with axe-core 4.14.0 on 2026-11-23: no rule fired on a `role="figure"` with no name.
