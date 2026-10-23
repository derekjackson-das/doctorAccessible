# HTML: Images

- Tier 1: HTML Living Standard, §4.8.4.4 Requirements for providing text to act as an alternative for images, accessed 2026-10-23. https://html.spec.whatwg.org/multipage/images.html
- Tier 1: ARIA in HTML, W3C Recommendation 11 August 2026, rows for `img` with and without `alt`, and `svg`. https://www.w3.org/TR/html-aria/
- Tier 2: WAI Tutorials, Images Tutorial (updated 8 April 2026), "Functional Images" (updated 12 April 2017), "Decorative Images" (updated 27 July 2019). https://www.w3.org/WAI/tutorials/images/
- Related: `content/alt-text.md` (what the text should say), `aria/accessible-name.md`, `wcag/sc-1.1.1-non-text-content.md`, `wcag/sc-1.4.5-images-of-text.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

This entry says how to mark images up; `content/alt-text.md` says what the text should say. Whether code fails WCAG is decided by the `wcag/` entries named below; report a failure once, under its criterion, at that entry's confidence.

## The native approach

- **Every `img` has an `alt` attribute.** The HTML Standard's default is that it is present and not empty, and is an appropriate replacement for the image; the exceptions are listed in §4.8.4.4.
- **`alt=""` for a decorative image,** including one beside text that already says the same thing, or one inside a link whose text already names the destination (WAI tutorial; HTML Standard §4.8.4.4.8).
- **An image that is the only content of a link or button** takes alt text that says where the link goes or what the button does, not what the picture shows (HTML Standard §4.8.4.4.2; WAI tutorial: a logo linking home is "W3C home"; a magnifying-glass button is "search").
- **An inline `svg`** that carries meaning gets `role="img"` and a name; a decorative one gets `aria-hidden="true"`.
- **Real text, not pictures of text,** wherever the visual effect can be done with CSS (`wcag/sc-1.4.5-images-of-text.md`).

## What the native approach satisfies by default

An `img` with an `alt` has its text alternative exposed as its name, and `alt=""` makes assistive technology skip it, with no ARIA (`wcag/sc-1.1.1-non-text-content.md`; ARIA in HTML).

## Where people go wrong

- No `alt` at all, which the HTML Standard does not allow outside its listed exceptions (`wcag/sc-1.1.1-non-text-content.md`, eval 002).
- A decorative image given text such as "spacer" or "image".
- An icon-only link or button whose image has `alt=""`, leaving the control with no name (`wcag/sc-4.1.2-name-role-value.md`).
- Meaningful images put in CSS `background-image`, with no text equivalent.
- `role="presentation"` instead of `alt=""`; the WAI tutorial notes it is less widely supported.

## When ARIA is genuinely needed

- `role="img"` with `aria-label` or `aria-labelledby` for an inline `svg`, or for a group of elements that together form one image.
- `aria-hidden="true"` on a decorative `svg` or icon font.
- `aria-describedby` to point a complex chart at its longer description on the page.
