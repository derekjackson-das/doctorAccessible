# SC 1.4.10 Reflow

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 1 Perceivable / 1.4 Distinguishable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#reflow
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/reflow.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for:
>
> - Vertical scrolling content at a width equivalent to 320 CSS pixels;
> - Horizontal scrolling content at a height equivalent to 256 CSS pixels.
>
> Except for parts of the content which require two-dimensional layout for usage or meaning.
>
> Note 1: 320 CSS pixels is equivalent to a starting viewport width of 1280 CSS pixels wide at 400% zoom. For web content which is designed to scroll horizontally (e.g., with vertical text), 256 CSS pixels is equivalent to a starting viewport height of 1024 CSS pixels at 400% zoom.
>
> Note 2: Examples of content which requires two-dimensional layout are images required for understanding (such as maps and diagrams), video, games, presentations, data tables (not individual cells), and interfaces where it is necessary to keep toolbars in view while manipulating content. It is acceptable to provide two-dimensional scrolling for such parts of the content.

## What it requires, in our words

When someone zooms a desktop browser to 400 percent, the page is effectively 320 CSS pixels wide, the width of a small phone. At that width the content must flow into a single column that scrolls only up and down. Nothing may be lost, and the reader must not have to scroll sideways to finish a line of text. People with low vision use high zoom instead of a screen magnifier precisely because reflow keeps lines readable; a page that forces horizontal scrolling at every line is unusable to them. Data tables, maps, diagrams, and video may scroll in two dimensions because their meaning depends on the layout. A responsive design that already works on phones usually passes.

## How it fails in code

- Content that requires horizontal scrolling to read at 320 CSS pixels wide: fixed-width layouts, `min-width` on the page or main column above 320px, side-by-side columns that do not stack. Definite once observed at the test width.
- Content that disappears at small widths, such as a navigation or a data column hidden by a media query with no other way to reach it. Definite. F102.
- Long unbroken strings (URLs, codes) that overflow their container and force a horizontal scrollbar. Definite once observed.
- Sticky headers or footers that cover most of the viewport at high zoom. Likely; confirm how much is left.
- A data table that scrolls horizontally inside its own container. Not a failure; Note 2 permits it.

## How to meet it

- Technique C32, "Using media queries and grid CSS to reflow columns", and Technique C31, "Using CSS Flexbox to reflow content".
- Technique C33, "Allowing for Reflow with Long URLs and Strings of Text", with CSS word-breaking.
- Technique C38, "Using CSS width, max-width and flexbox to fit labels and inputs".
- Technique G206, "Providing options within the content to switch to a layout that does not require the user to scroll horizontally".
- Techniques G224 and G225 for indented text and horizontally scrolling panels.
- Advisory: Technique C34 to un-fix sticky headers at small widths, Technique C37 for images with `max-width: 100%`.
- Test: set the browser window to 1280 pixels wide and zoom to 400 percent, or use responsive mode at 320 pixels.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.4.4 Resize Text (entry in this package). The 200 percent requirement; reflow goes further.
- SC 1.3.4 Orientation (entry in this package). Both are about adapting to the viewport.
- SC 1.3.2 Meaningful Sequence (entry in this package). At one column, source order is the visible order.
- SC 1.4.12 Text Spacing (entry in this package). Often tested in the same pass.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Reflow is observed by rendering at the test width, which is manual or needs a browser-driven test outside axe. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
