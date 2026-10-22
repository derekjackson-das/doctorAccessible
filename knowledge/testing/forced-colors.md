# Testing: Forced colors (Windows Contrast Themes)

- Sources:
  - Adrian Roselli, "WHCM and System Colors", 10 February 2021, updated 24 May 2026. https://adrianroselli.com/2021/02/whcm-and-system-colors.html Tier 3.
  - MDN Web Docs, "forced-colors", last modified 20 April 2026. https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors Tier 3.
- Related entries: `wcag/sc-1.4.11-non-text-contrast.md`, `wcag/sc-1.4.1-use-of-color.md`, `wcag/sc-1.1.1-non-text-content.md`, `wcag/sc-2.4.7-focus-visible.md`.
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

WCAG 2.x does not cover forced colors mode directly. Roselli records the working group's 2019 answer to that effect. A problem seen only in forced colors is manual review, not a WCAG failure, unless it also fails a criterion in another way. For example, a control with no visible boundary may fail `wcag/sc-1.4.11-non-text-contrast.md`, and a state shown only by color may fail `wcag/sc-1.4.1-use-of-color.md`. Report those under their criteria. Roselli treats testing custom widgets in this mode as part of a definition of done, and some people use it to lower contrast, not raise it.

## Setup

- **Windows:** Roselli gives the Windows 10 path (Settings, Ease of Access, High contrast) and notes that Windows 11 renamed the feature Contrast Themes, still under the accessibility settings. Choose a theme and apply it. Alt+Left Shift+Print Screen turns on the last theme used. Test at least one dark theme and one light theme.
- **Browsers:** Edge or Chrome on Windows. In Roselli's 2021 tests, Firefox 85 handled some cases differently, for example background images, so include Firefox if the spec lists it.
- **Without Windows:** Edge's developer tools can emulate forced colors on macOS (More Tools, then Rendering), as Roselli documented in 2022. The emulation offers only one color scheme, so treat it as a first pass, not the test.

## The steps

1. Load the page in forced colors. Note any text, icon, or control that disappears or becomes unreadable.
2. Check every control has a visible edge or text: buttons, inputs, checkboxes, toggles, tabs, custom widgets. A `div` given a button role does not get button colors. MDN notes that browsers choose colors by native element, not by ARIA role.
3. Check icons and SVGs. Line art in an image file may vanish against the background; inline SVG that uses `currentColor` follows the text color (Roselli).
4. Check every state: hover, focus, selected, checked, disabled, error, current page. Note any state shown only by a background color, box shadow, or gradient. MDN lists these among the things forced colors removes or overrides.
5. Tab through the page and note whether focus is always visible.
6. Check text over images: browsers draw a backplate behind text (MDN). Note any text still hard to read.

## What passing looks like

- All content and every control remain visible and identifiable.
- Every state is shown by something forced colors keeps: text, an outline, a border, an icon. Where one of these is missing, check the matching criterion (`wcag/sc-1.4.11-non-text-contrast.md`, `wcag/sc-1.4.1-use-of-color.md`, `wcag/sc-2.4.7-focus-visible.md`) and report it there; anything else is manual review.

## What to record

Windows version, theme name, browser and version (or "emulation" and which browser), and for each step what happened, with a screenshot of any failure, the result, and the tester.
