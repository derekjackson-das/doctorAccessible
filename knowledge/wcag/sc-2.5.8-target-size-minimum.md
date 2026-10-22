# SC 2.5.8 Target Size (Minimum)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 2 Operable / 2.5 Input Modalities
- Tier 1 source: https://www.w3.org/TR/WCAG22/#target-size-minimum
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Also in: WCAG 2.2 only. New in 2.2; not in 2.0 or 2.1.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> The size of the target for pointer inputs is at least 24 by 24 CSS pixels, except when:
>
> **Spacing.** Undersized targets (those less than 24 by 24 CSS pixels) are positioned so that if a 24 CSS pixel diameter circle is centered on the bounding box of each, the circles do not intersect another target or the circle for another undersized target;
>
> **Equivalent.** The function can be achieved through a different control on the same page that meets this criterion;
>
> **Inline.** The target is in a sentence or its size is otherwise constrained by the line-height of non-target text;
>
> **User Agent Control.** The size of the target is determined by the user agent and is not modified by the author;
>
> **Essential.** A particular presentation of the target is essential or is legally required for the information being conveyed.
>
> Note 1: Targets that allow for values to be selected spatially based on position within the target are considered one target for the purpose of the success criterion. Examples include sliders, color pickers displaying a gradient of colors, or editable areas where you position the cursor.
>
> Note 2: For inline targets the line-height should be interpreted as perpendicular to the flow of text. For example, in a language displayed vertically, the line-height would be horizontal.

## What it requires, in our words

Buttons, links, and other things you click or tap need to be at least 24 by 24 CSS pixels, or, if smaller, spaced so that a 24-pixel circle around each one does not touch a neighbor. Small, crowded targets are hard for people with tremors, low vision, or large fingers, and a miss can trigger the wrong action. Links inside a sentence are exempt because their height follows the text. Unstyled native controls such as a default checkbox are exempt. If the same action is available elsewhere on the page through a target that passes, the small one is allowed. This is a floor; the Level AAA version asks for 44 pixels.

## How it fails in code

- Icon buttons, pagination links, or toolbar controls smaller than 24 by 24 CSS pixels packed next to each other with little or no gap. Definite when sizes and spacing are known from the CSS.
- A row of small social-media icon links at 20 pixels with 2 pixels between them. Definite.
- Small close buttons on dialogs, tags, or chips. Definite when measured under 24 pixels and adjacent to other targets.
- A small target that stands alone with 24 pixels of clear space around it. Passes by the spacing exception.
- Links in running text. Pass by the inline exception.
- A small "remove" icon beside each item when a full-size "Remove" button exists elsewhere for the same item. Passes by the equivalent exception; manual review to confirm.

## How to meet it

- Technique C42, "Using min-height and min-width on target container to ensure sufficient target spacing": `min-width: 24px; min-height: 24px` on the clickable element, or padding that brings its box to that size.
- Space small targets so the 24-pixel circles do not overlap.
- The `design` entry for target size, when it exists, carries the practice above the floor.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.5.5 Target Size (Enhanced) is Level AAA at 44 by 44 and not a requirement here.
- SC 2.5.7 Dragging Movements (entry in this package). Alternatives to drag need adequately sized controls.
- SC 1.4.4 Resize Text (`wcag/sc-1.4.4-resize-text.md`). Targets sized in em grow with text; those in px do not.

## Automated coverage (tier 3)

axe-core tags `target-size` to this criterion. It measures rendered targets and spacing and reports those under 24 pixels without adequate space; it may return "needs review" where overlap cannot be resolved. Exceptions for equivalent controls and essential presentation are manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
