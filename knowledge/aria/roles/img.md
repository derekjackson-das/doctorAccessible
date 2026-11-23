# Role: img

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "img role" and "Presentational Children" (5.2.9), https://www.w3.org/TR/wai-aria-1.2/#img. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `img`, `svg`, `embed`, `iframe`, `object`, and `figure`, https://www.w3.org/TR/html-aria/#el-img
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, rows 3.5.56 and 3.5.57, https://www.w3.org/TR/html-aam/#el-img
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: img role", last modified 14 October 2026, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/img_role
- WAI-ARIA 1.3 (Working Draft 4 June 2026): adds `image` as a synonym of `img`. Awareness only; see "Where it can and cannot be used".
- Related entries: `html/images.md`, `aria/accessible-name.md`, `aria/roles/presentation.md`, `aria/roles/figure.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.1.1-non-text-content.md`, `wcag/sc-4.1.2-name-role-value.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="img"` on an `img` element is redundant and never a finding.

## What it is

One image, whatever it is built from: a single element or several that together read as one graphic. WAI-ARIA 1.2: "A container for a collection of elements that form an image."

Two things follow from the role, and both are easy to miss. It needs a name. And everything inside it stops being exposed.

## The native element

`img`. ARIA in HTML gives it the `img` role when it has a non-empty `alt` or another name, and also when it has no `alt` and no name. With `alt=""` and no other name it is `none` or `presentation` instead (HTML-AAM 3.5.56 and 3.5.57). Writing `role="img"` on an `img` is "NOT RECOMMENDED".

## When writing the role is justified

- An inline `svg` that carries meaning (`html/images.md`).
- Several elements that form one image: characters used as a picture, an icon font glyph, a chart drawn from `div` elements. MDN gives emoji and ASCII art as examples, and notes that some browser and screen reader pairs read such a label twice, so it needs testing.

## What the spec asks of authors

- "In order for elements with a role of img to be perceivable, authors MUST provide a label using the aria-label or aria-labelledby attribute."
- Naming: required ("Accessible Name Required: True"), from the author only. Text inside the element does not name it.
- Presentational children (WAI-ARIA 1.2, 5.2.9): "The DOM descendants are presentational. User agents SHOULD NOT expose descendants of this element through the platform accessibility API."
- MDN: use `aria-labelledby` when a short visible label exists, `aria-describedby` for a longer description, and `aria-label` otherwise.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; **required**.
- Children presentational: true.
- It stands alone: it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `img` with a name, or with no `alt` at all (redundant, "NOT RECOMMENDED").
- **Allowed:** `embed`, `iframe`, `object`, and the elements that allow any role, such as `svg`, `div`, `span`, `i`, `canvas`, `p`, and a `figure` with no `figcaption`. `div`, `span`, `i`, and `p` are "Naming Prohibited" as plain elements; with this role they may be named, because the role allows a name.
- **Not allowed:** `picture`; a `figure` that has a `figcaption`; `button`; `a` with `href`; `h1` to `h6`; an `li` inside a list; `video` and `audio`.

ARIA in HTML writes the role as "img or image". `image` is not a role in WAI-ARIA 1.2; it comes from the 1.3 draft. Write `img`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

- **Everything inside it.** Headings, lists, links, and text inside a `role="img"` element are not exposed. Only the name is. This is the difference from `figure`, whose content stays (`aria/roles/figure.md`).
- On an `img`, ARIA in HTML allows other roles only when the image has a name: `button`, `link`, `checkbox`, `math`, and the rest of that row. Each replaces the image role. With no name, only `none` or `presentation` is allowed (`aria/roles/presentation.md`).

## How it fails in code

- `role="img"` with no accessible name, on an `svg` or any other element: `wcag/sc-1.1.1-non-text-content.md`, definite per that entry.
- A name that is present but not equivalent, such as "chart" on a chart: `wcag/sc-1.1.1-non-text-content.md`, manual review per that entry.
- Text or structure inside the element that the page relies on, such as a caption or a data table inside a `role="img"` chart, with a name that does not carry it: the content is not exposed. `wcag/sc-1.1.1-non-text-content.md`, likely; a person compares the name to what is inside.
- A link or button inside the element: its role and name are not exposed. `wcag/sc-4.1.2-name-role-value.md`, likely. Move it outside.
- A decorative graphic given `role="img"` and a name: advice. Leave the role off and hide the graphic instead (`html/images.md`).

## How to check

Search for `role="img"`. Each has `aria-label` or `aria-labelledby`, the name says what the image conveys, and nothing inside it needs to be reached on its own. In the browser's accessibility tree, confirm one image node with the name and no children. axe: `role-img-alt` fires on a `role="img"` with no name, and `svg-img-alt` covers `svg`; both are mapped to 1.1.1 (`knowledge/axe-rules.md`; `role-img-alt` observed with axe-core 4.14.0 on 2026-11-23). axe cannot tell whether the name is equivalent.
