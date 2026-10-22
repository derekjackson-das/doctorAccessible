# Testing: Zoom at 200% and 400%

- Sources:
  - W3C, "Understanding Success Criterion 1.4.10: Reflow", Understanding WCAG 2.2, accessed 2026-10-22. https://www.w3.org/WAI/WCAG22/Understanding/reflow.html Tier 2.
  - W3C, "Understanding Success Criterion 1.4.4: Resize Text", Understanding WCAG 2.2, accessed 2026-10-22. https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html Tier 2.
- Related entries: `wcag/sc-1.4.4-resize-text.md`, `wcag/sc-1.4.10-reflow.md`, `wcag/sc-2.4.11-focus-not-obscured-minimum.md`, `wcag/sc-1.4.12-text-spacing.md`.
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

A failed step is evidence for a finding under the criterion it checks, reported once under that criterion. Screen magnifiers, such as ZoomText or the operating system's own magnifier, are a separate test. This entry covers browser zoom only.

## Setup

A desktop browser with its window at 1280 CSS pixels wide, at 100% zoom to start. The Understanding page for Reflow explains why: at 400% zoom, a 1280-pixel window is equivalent to the 320 CSS pixel width the criterion uses. Use the browser's zoom (Ctrl or Command with Plus), not a text-only setting, unless testing text-only resizing on purpose.

## The steps

1. **200% zoom.** Read every piece of text, including labels, buttons, and form values. Note any text that is cut off, overlaps other text, or did not grow.
2. **400% zoom, or a 320 CSS pixel wide window.** Scroll the page top to bottom. Note any place where you must also scroll sideways to read a line of text, and whether that content is one of the Understanding page's exceptions, such as graphics and video, data tables, persistent toolbars, and layouts needed for meaning.
3. **At 400%, use every control** the component has: open menus, dialogs, and popups; fill fields; submit. Note anything that cannot be reached, opens off screen, or covers the thing it belongs to.
4. **At 400%, Tab through the page.** Note focus hidden behind sticky headers, footers, cookie banners, or chat buttons. The Reflow Understanding page names fixed content at high zoom as a common problem.
5. **Optional, text spacing:** apply the 1.4.12 spacing values with a bookmarklet or user stylesheet, and note any text cut off or overlapping.

## What passing looks like

- Text can be enlarged to 200% without loss of content or function (`wcag/sc-1.4.4-resize-text.md`).
- At 320 CSS pixels wide, content reflows to one column with no two-way scrolling, apart from the listed exceptions (`wcag/sc-1.4.10-reflow.md`).
- Focus is never fully hidden by author content at any zoom (`wcag/sc-2.4.11-focus-not-obscured-minimum.md`).
- Text spacing changes lose nothing (`wcag/sc-1.4.12-text-spacing.md`).

## What to record

Browser and version, window width, zoom level, and for each step what happened, with a screenshot of any failure, pass or fail, and the tester. Record which content was judged an exception, and why.
