---
name: design
description: Visual design judgment above the WCAG minimum. Use when designing, building, or reviewing color and contrast, focus indicators, target sizes, motion and animation, layouts at zoom (reflow), or text spacing. Maps each topic to a knowledge entry that keeps the WCAG 2.2 AA Requirement apart from the good Practice above it. Practice-only findings are likely or manual review, never definite.
---

# Design

This skill is a map and a set of rules. The knowledge is in `knowledge/design/`, which rests on `knowledge/wcag/`. The rules for citing are in the `wcag` skill and apply here unchanged.

## When this applies

Any change or review that touches colors, focus styles, the size or spacing of controls, animation or transitions, layout at high zoom or narrow widths, or how text is spaced and sized. Also use it in consult, whenever a design choice is being made.

## Rules

1. **Requirement and Practice are separate.** Each design entry has a Requirement part (WCAG 2.2 Level AA, tier 1, from the `wcag/` entries) and a Practice part: Level AAA criteria (tier 1, but beyond our target), W3C informative material (tier 2), and named practitioners (tier 3). Never present a Practice point as a requirement.
2. **Requirement failures** are reported once, under the criterion, at the confidence the `wcag/` entry gives. The design entry is named as context.
3. **Practice-only findings are likely or manual review, never definite,** and never called a WCAG failure. This includes anything that rests only on a Level AAA criterion, which is beyond our target.
4. **Measure, do not guess.** Contrast ratios are computed from the actual colors with the WCAG formula, against the colors actually next to the element, in every state. A number from memory is not a measurement.
5. **Check the real context.** A value that passes on the page body can fail on a header, a card, or an image. Check every background an element can sit on.
6. Never state a criterion number, title, or level from memory. Open the entry. If there is none, say "no entry yet" and mark the claim unverified.
7. Working drafts, including WCAG 3 contrast and APCA, are awareness only.
8. Advise and describe; do not silently restyle the developer's code.

## Where to look

| Topic | Read |
|---|---|
| Text and non-text contrast, color alone | `knowledge/design/contrast.md` |
| Focus indicators: visible, contrasting, not hidden | `knowledge/design/focus-indicators.md` |
| Size and spacing of pointer targets | `knowledge/design/target-size.md` |
| Flashing, auto-playing motion, reduced motion | `knowledge/design/motion.md` |
| Layout at 400% zoom and narrow widths | `knowledge/design/reflow.md` |
| Line height, letter and word spacing, line length | `knowledge/design/text-spacing.md` |
| How a person tests any of these | `knowledge/testing/` (zoom, reduced motion, forced colors, keyboard) |
| The criteria themselves | `knowledge/INDEX.md`, then the `wcag/` entry |

## Output shape for a finding

```
Requirement finding:
WCAG 2.2 SC x.x.x Title (Level A or AA), tier 1
Confidence: definite | likely | manual review (from the wcag/ entry)
Where: <selector or file:line>
What: <one sentence, with the measured value if there is one>
Design entry: knowledge/design/<topic>.md
Fix direction: <one sentence>

Practice finding:
Practice, not a requirement: <the point>, <source and tier>
Confidence: likely | manual review
Where: <selector or file:line>
What: <one sentence>
Design entry: knowledge/design/<topic>.md
Fix direction: <one sentence>
```
