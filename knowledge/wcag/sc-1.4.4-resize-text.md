# SC 1.4.4 Resize Text

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 1 Perceivable / 1.4 Distinguishable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#resize-text
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Except for captions and images of text, text can be resized without assistive technology up to 200 percent without loss of content or functionality.

## What it requires, in our words

A person must be able to make the text twice as big using only the browser, and the page must still work: nothing cut off, nothing overlapping, no control that disappears. Browser zoom is the usual way and the Understanding page accepts it as meeting the criterion as long as the page does not block it. Text-only zoom, where the browser enlarges text but not layout, is the harder test and the one that exposes fixed-height boxes. Captions and images of text are exempt here; images of text have their own criterion.

## How it fails in code

- A viewport meta tag with `user-scalable=no` or a `maximum-scale` below 2, which blocks zoom on mobile. Definite.
- Text or controls that are clipped, truncated, overlapped, or hidden when text is enlarged to 200 percent. Definite once observed. F69.
- Form controls whose text does not grow with the rest of the page, because their size is fixed in pixels. Definite once observed. F80.
- Font sizes set in viewport units (`vw`, `vh`) with no fallback, so text does not respond to zoom. Definite. F94.
- Fixed-height containers with `overflow: hidden` around text. Likely from code; confirm by zooming.

## How to meet it

- Technique G142, "Using a technology that has commonly-available user agents that support zoom": do not block browser zoom.
- Technique C28, "Specifying the size of text containers using em units", so boxes grow with the text.
- Techniques C12, C13, and C14: percent, named, or em units for font sizes.
- Technique G146, "Using liquid layout", and Technique G179, "Ensuring that there is no loss of content or functionality when the text resizes and text containers do not change their width".
- Technique G178, "Providing controls on the web page that allow users to incrementally change the size of all text", when the browser's own zoom cannot be relied on.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.4.10 Reflow (entry in this package). The 400 percent, single-column requirement that supersedes most of this one in practice.
- SC 1.4.12 Text Spacing (entry in this package). Another "change the text, nothing breaks" requirement.
- SC 1.4.5 Images of Text (entry in this package). Exempt here, required there.

## Automated coverage (tier 3)

axe-core tags `meta-viewport` to this criterion. It flags viewport settings that disable zoom. Whether content survives being enlarged is a rendering test that remains manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
