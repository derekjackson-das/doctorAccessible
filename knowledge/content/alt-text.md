# Content: Alternative text for images

- House standard: `docs/content-standards.md`, section 6.
- Sources:
  - W3C WAI Tutorials, "An alt Decision Tree", updated 13 May 2024. https://www.w3.org/WAI/tutorials/images/decision-tree/ Tier 2.
  - W3C WAI Tutorials, "Informative Images", updated 17 June 2019. https://www.w3.org/WAI/tutorials/images/informative/ Tier 2.
  - WebAIM, "Alternative Text", last updated 19 October 2021. https://webaim.org/techniques/alttext/ Tier 3.
- WCAG: `wcag/sc-1.1.1-non-text-content.md` (Level A), `wcag/sc-1.4.5-images-of-text.md` (Level AA).
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

A missing text alternative, or one that does not serve the image's purpose, fails SC 1.1.1; report it there at the confidence the 1.1.1 entry gives. Alt text that serves the purpose but misses the house standard, such as one starting "image of", one that repeats nearby text, or one far longer than needed, is likely or manual review, never definite. A project's `a11y-spec.md` may change the standard; the spec wins.

## What it is

The text in an image's `alt` attribute, read in place of the image by screen readers and shown when images do not load.

## Why it matters

Alt text is what a reader who cannot see the image gets instead. It has to carry the image's purpose in this context. WebAIM's point is that the same image can mean different things on different pages, and only the author knows which.

## How to do it

Follow the W3C decision tree:
- **Text in the image:** if the same text is nearby, or the text is only decoration, use an empty `alt`. If it is an icon with a function, give the function. Otherwise put the image's text in the `alt`.
- **Image in a link or button:** say where the link goes or what the button does.
- **Image that adds meaning:** a brief description that conveys that meaning in context.
- **Decorative image:** `alt=""`, so it is skipped (W3C; WebAIM).

Then write it well (WebAIM):
- **Succinct:** usually a few words, rarely more than a short sentence or two.
- **Not redundant** with text next to the image.
- **No "image of", "picture of", or "graphic of".** Screen readers already announce that it is an image. Say it is a photograph or a drawing only when that matters.
- **Context is everything:** describe what the image is for on this page, not everything in it.

A chart or diagram gets a short `alt`, with its data or meaning in the text around it (house standard).

## How to check it

- Every `img` has an `alt` attribute, empty or not (WebAIM).
- Read each `alt` without the image. Does it do the image's job here, and stop?
- Look for "image of", "picture of", "graphic of", file names, and text that repeats the caption.
- For images of text, check that the `alt` carries the text, and whether real text could be used instead (`wcag/sc-1.4.5-images-of-text.md`).
