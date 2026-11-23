# Role: math

- Category: document structure.
- Normative (tier 1): W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023, "math role", https://www.w3.org/TR/wai-aria-1.2/#math. ARIA in HTML, W3C Recommendation 11 August 2026, rows for `math` and `img`, https://www.w3.org/TR/html-aria/#el-math
- Mapping (tier 2): W3C, "HTML Accessibility API Mappings 1.0", Working Draft 26 October 2026, row 3.5.90 (defers to MathML AAM), https://www.w3.org/TR/html-aam/#el-math
- Practice (tier 2): ARIA Authoring Practices Guide, "Structural Roles" (no date on the page), https://www.w3.org/WAI/ARIA/apg/practices/structural-roles/
- Reference (tier 3): MDN Web Docs, "ARIA: math role", last modified 6 June 2025, https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/math_role
- Related entries: `html/images.md`, `aria/roles/img.md`, `aria/accessible-name.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-1.1.1-non-text-content.md`
- Verified against the live sources: 2026-11-23 by Derek Jackson with Claude Code. WAI-ARIA 1.2, ARIA in HTML, and HTML-AAM text checked against downloaded copies; APG and MDN pages read in full from downloaded copies.

## Status and reporting

A role is not a criterion. Misuse is reported once, under the criterion it breaks, at that entry's confidence. Breaking a WAI-ARIA or ARIA in HTML rule with no barrier shown is advice (`aria/aria-in-html.md`). `role="math"` on a `math` element is redundant and never a finding. The role does not make an expression readable; the markup or the text alternative does.

## What it is

A mathematical expression. WAI-ARIA 1.2: "Content that represents a mathematical expression."

## The native element

The MathML `math` element. ARIA in HTML gives it the `math` role implicitly and allows no other role on it. HTML-AAM 3.5.90 leaves its mapping to the MathML mapping specification.

The sources disagree here. APG's "Structural Roles" table lists `math` with no HTML equivalent. ARIA in HTML (tier 1) names the `math` element. Take ARIA in HTML.

## When writing the role is justified

- On an `img` that is a picture of an expression, with a text alternative. ARIA in HTML allows `math` on an `img` that has a name, and WAI-ARIA 1.2's own example does this.
- On an element holding an expression written as text or produced by a rendering library, where MathML is not in the page.

WAI-ARIA 1.2 says to use native MathML wherever possible and to test thoroughly, and notes that an image with a text alternative does not give the navigation that MathML can.

## What the spec asks of authors

- "Authors SHOULD ensure that images of math are labeled by text that describes the mathematical expression as it might be spoken."
- "authors MAY use JavaScript to downgrade the content to a format the browser can display", where a browser does not support a native math format.
- Naming: allowed, from the author; not required.
- MDN: `aria-label` when the children are presentational or there is no visible label; `aria-labelledby` when a visible label exists.

## Attributes and context it needs

From the role's characteristics in WAI-ARIA 1.2:

- Required context role: none. Required owned elements: none. Required states and properties: none.
- Supported states and properties: none beyond the global ones.
- Prohibited states and properties: none. WAI-ARIA 1.2 marks the global `aria-disabled`, `aria-errormessage`, `aria-haspopup`, and `aria-invalid` as deprecated on this role.
- Naming: name from author; not required.
- Children presentational: false. Unlike `img`, what is inside stays exposed.
- It stands alone: it needs no other role around or inside it.

## Where it can and cannot be used

From ARIA in HTML, section 4:

- **Native element:** `math` (redundant, "NOT RECOMMENDED").
- **Allowed:** an `img` that has an accessible name, and the elements that allow any role, such as `div`, `span`, and `p`.
- **Not allowed:** an `img` with no `alt` and no name; `picture`; `legend`; `caption`; `button`; `a` with `href`; `h1` to `h6`.

Using the role where it is not allowed is a conformance error against ARIA in HTML: advice, unless it breaks a criterion (`aria/aria-in-html.md`).

## What an explicit role takes away

On an `img`, the `img` role is replaced by `math`; the `alt` text is still the name.

## How it fails in code

- An image of an expression with no `alt`: `wcag/sc-1.1.1-non-text-content.md`, definite per that entry (F65), with or without the role.
- An image of an expression whose `alt` is "equation" or "formula": `wcag/sc-1.1.1-non-text-content.md`, manual review per that entry; a person compares the text to the expression.
- An expression built from positioned `span` elements, superscripts, and symbols, with `role="math"` and no text alternative: what is exposed is the characters in source order. `wcag/sc-1.1.1-non-text-content.md`, manual review.

## How to check

For each expression: is it MathML, an image, or styled text? An image has `alt` that reads as the expression would be spoken. In the browser's accessibility tree, confirm what is exposed for it. Observed with axe-core 4.14.0 on 2026-11-23: no rule fired on a `role="math"` on a `div`. `image-alt` covers an `img` with no `alt` (`knowledge/axe-rules.md`).
