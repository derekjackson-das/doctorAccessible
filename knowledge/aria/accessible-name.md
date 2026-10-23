# ARIA: How an accessible name is computed

- Sources:
  - W3C, "Accessible Name and Description Computation 1.1", W3C Recommendation 18 December 2018. https://www.w3.org/TR/accname-1.1/ Tier 1. The 1.2 draft is a Working Draft, awareness only.
  - W3C, "HTML Accessibility API Mappings 1.0", W3C Working Draft 21 October 2026. https://www.w3.org/TR/html-aam/ Tier 2: which HTML feature supplies the name for each element (section 4.1), for example `label` for an `input`, `alt` for an `img`.
  - W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023. https://www.w3.org/TR/wai-aria-1.2/ Tier 1: which roles take their name from content.
  - W3C, "ARIA in HTML", W3C Recommendation 11 August 2026. https://www.w3.org/TR/html-aria/ Tier 1: elements where naming by `aria-label` is prohibited.
- Related: `aria/using-aria.md`, `aria/aria-in-html.md`
- WCAG: `wcag/sc-4.1.2-name-role-value.md` (a name exists), `wcag/sc-2.5.3-label-in-name.md` (the name contains the visible label), `wcag/sc-1.1.1-non-text-content.md` (images), `wcag/sc-1.3.1-info-and-relationships.md` (labels associated)
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

This entry explains how a name is worked out; it is not a criterion. A control with no name, or with a name that drops its visible label, fails the criterion named above; report it there, once, at the confidence its entry gives. Working out the name by reading the code is a prediction. The browser's accessibility tree, viewed in developer tools, shows the name actually computed.

## What it is

The accessible name is the short text a screen reader announces for an element, and what speech recognition users say to activate it: "Search", "Close", "Date of birth". The description is extra text announced after it, usually from `aria-describedby`; HTML-AAM section 4.2 adds fallbacks for some elements, ending with `title` when it was not used as the name. The computation is the ordered set of steps a browser uses to find the name.

## The order, in plain words

The browser stops at the first step that gives a result (AccName 1.1, section 4.3, step 2):

1. **Hidden content gives nothing,** unless it is directly referenced by `aria-labelledby`, `aria-describedby`, or a native label. Hidden text pointed to that way still counts (step 2A).
2. **`aria-labelledby`:** the text of the referenced elements, in the order the ids are listed, joined with spaces. This beats everything below, including a `label` element (step 2B).
3. **`aria-label`,** if it is not empty (step 2C).
4. **The host language's own naming** (step 2D). For HTML, HTML-AAM section 4.1 sets the order for each element inside this step, for example:
   - text inputs and `textarea`: the associated `label` (several labels joined in page order; a control wrapped in its label leaves its own value out), then `title`, then `placeholder`;
   - `input type="submit"`, `"reset"`, `"button"`: the `label`, then the `value`, then the browser's default ("Submit"), then `title`;
   - `button`: the `label`, then its content, then `title`;
   - `img`: `alt`, even when empty; `title` only if there is no `alt` at all. An `img` with `alt=""` has no name and is treated as presentational;
   - `table`: its `caption`; `fieldset`: its `legend`.
   `role="presentation"` or `role="none"` switches this step off.
5. **For a control inside another control's label,** its current value, so a text field inside a checkbox's label adds what was typed (step 2E).
6. **The content:** for roles whose name comes from content in WAI-ARIA 1.2, such as buttons, links, and headings, the text inside, including CSS `::before` and `::after` text (step 2F). Table cells are a conflict: WAI-ARIA lets a cell take its name from content, but HTML-AAM section 4.1.12 gives `td` and `th` only `aria-label`, `aria-labelledby`, and `title`. Following principle 13, do not count on a cell's text as its name.
7. **The tooltip attribute,** the generic last resort, only if nothing else gave a name (step 2I). In HTML, `title` usually comes in earlier, at the end of the element's own order in step 4.

The order is the point. A later step never fills in once an earlier one gave a name. An `aria-labelledby` pointing at a hint replaces the visible `label`. An `aria-label` on a button replaces the button's text.

**Prohibited does not mean ignored.** ARIA in HTML forbids `aria-label` on a plain `span`, but the AccName 1.1 algorithm does not skip it, so `<button><span aria-label="x">Save</span></button>` can come out as "x". Browsers and screen readers vary. Treat it as manual review and check the accessibility tree.

## Why it matters

A name that is missing leaves a screen reader user with "button" or "edit text" and nothing else. A name that differs from the visible label breaks speech recognition commands (`wcag/sc-2.5.3-label-in-name.md`).

## How to do it

- Prefer the native label and visible text. A `button` with text, an `input` with a `label`, an `img` with `alt`: no ARIA needed.
- Use `aria-labelledby` to name a control from visible text that is already on the page, such as a dialog from its heading, or a "Delete" button from its row's file name. Include the control's own visible text in the list.
- Use `aria-label` only where there is no visible text, such as an icon-only button. Where there is visible text, the name must contain it.
- Put hints and formats in `aria-describedby`, not in the name.
- Do not use `aria-label` or `aria-labelledby` on an element whose role cannot be named, such as a plain `div` or `span` (`aria/aria-in-html.md`).
- Do not rely on `title` or `placeholder` for the name. They come last in the order, and the placeholder disappears once the user types (`content/error-messages.md`).

## How to check it

- For each control, walk the order above and write down the name it yields. Then compare it with the visible label.
- Confirm in the browser's accessibility tree, which shows the computed name and where it came from.
- axe flags controls, images, and links with no name. Whether a name is the right one, or contains the visible text, is mostly manual.
