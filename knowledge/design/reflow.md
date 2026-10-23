# Design: Reflow

- Requirement sources (tier 1): `wcag/sc-1.4.10-reflow.md`, `wcag/sc-1.4.4-resize-text.md`, `wcag/sc-2.4.11-focus-not-obscured-minimum.md`.
- Practice sources:
  - W3C, "Understanding Success Criterion 1.4.10: Reflow", updated 6 September 2026. https://www.w3.org/WAI/WCAG22/Understanding/reflow.html Tier 2.
  - WebAIM, "Responsive Design and Reflow", last updated 30 October 2024. https://webaim.org/techniques/reflow/ Tier 3.
  - Adrian Roselli, "Horizontal Scrolling Containers Are Not a Content Strategy", 1 August 2025, updated 3 September 2025. https://adrianroselli.com/2025/08/horizontal-scrolling-containers-are-not-a-content-strategy.html Tier 3.
  - Adrian Roselli, "1.4.10: Adversarial Conformance", 23 February 2025, updated 31 August 2026. https://adrianroselli.com/2025/02/1-4-10-adversarial-conformance.html Tier 3.
- Related entries: `testing/zoom.md`, `patterns/carousel.md`
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

A design that fails the Requirement is reported under its criterion, once, at the confidence its `wcag/` entry gives. A design that meets the Requirement but misses a Practice point is reported as likely or manual review, never definite, and never as a WCAG failure.

## Requirement (tier 1)

- At the width in `wcag/sc-1.4.10-reflow.md` (320 CSS pixels, a 1280-pixel window at 400% zoom), content works without loss and without scrolling in two directions. Content designed to scroll horizontally, such as vertical text, is checked at a height of 256 CSS pixels instead. Content that needs a two-dimensional layout, such as data tables, maps, and video, is excepted.
- Text can be enlarged to 200% without loss (`wcag/sc-1.4.4-resize-text.md`).
- Sticky or fixed content must not entirely hide the focused element at any size (`wcag/sc-2.4.11-focus-not-obscured-minimum.md`, new in WCAG 2.2; a project held to WCAG 2.1 is not bound by it, though meeting it costs nothing extra).

## Practice (tier 2 and 3, not required)

- **Test the way people zoom.** Set the window to 1280 pixels and zoom in steps to 400%, checking at each step that nothing is lost, nothing scrolls sideways, and dialogs, menus, accordions, and tooltips still work (WebAIM).
- **Unstick fixed content at small sizes.** The Understanding page's example of a fixed advertisement that covers focus at high zoom is fixed by making it static, or by giving people a way to dismiss it (W3C). In "Horizontal Scrolling Containers Are Not a Content Strategy", Roselli adds that a sticky header or footer makes scrolling and reading harder for people on phones in landscape.
- **Keep two-way scrolling to the smallest box that needs it.** The Understanding page says it is best to limit two-way scrolling to the sections that need it, rather than the whole page (W3C).
- **A horizontal scroller is not a fix for reflow.** Roselli argues that sideways-scrolling containers used to dodge reflow are a content problem to solve in the design, and that any scroller that remains needs a visible cue that it scrolls.
- **Break long words properly.** `word-break: break-all` can pass reflow while making text hard to read; Roselli recommends CSS hyphenation, soft hyphens, or `<wbr>` instead.

## How to check

Follow `testing/zoom.md` at 200% and at 400% or 320 CSS pixels. At 400%, tab through the page to catch focus hidden under sticky content, and open every dialog and menu.
