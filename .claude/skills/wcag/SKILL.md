---
name: wcag
description: Apply WCAG 2.2 Level AA while writing or reviewing HTML, CSS, JavaScript, or content. Loads the rules for citing and judging, and maps each topic to the knowledge entry that answers it. Use whenever a change touches structure, forms, focus, names and roles, color, media, or motion.
---

# WCAG 2.2

This skill is a map and a set of rules. The knowledge is in `knowledge/`.

## When this applies

Any change that touches page structure or landmarks, headings, forms and labels, keyboard and focus, accessible names and roles, custom controls, color and contrast, images and media, motion, timing, or content that changes without a page load.

## Rules

1. Never state a success criterion number, title, or level from memory. Open `knowledge/INDEX.md`, find the entry, read it, then cite it.
2. Every finding or recommendation names the criterion, its level, the version (WCAG 2.2), and the tier of the source: tier 1 normative, tier 2 informative from W3C, tier 3 practitioner.
3. If there is no entry for the criterion you need, say "no entry yet", cite the W3C URL, mark the claim unverified, and note it as a gap to fill.
4. Distinguish three confidences: definite violation, likely violation, manual review needed.
5. Prefer native HTML to ARIA. Say when a native element already meets the requirement.
6. Working drafts (WCAG 3.0, APCA) are awareness only. Do not cite them as requirements.
7. "It depends" is answered by naming each case and answering each.

## Where to look

| Topic | Read |
|---|---|
| Accessible names, roles, states on controls | `knowledge/wcag/sc-4.1.2-name-role-value.md`; visible label must be in the name: `sc-2.5.3-label-in-name.md` |
| Whether ARIA is needed, what an element allows, where a name comes from | `knowledge/aria/using-aria.md`, `knowledge/aria/aria-in-html.md`, `knowledge/aria/accessible-name.md` |
| Form labels, grouping, input purpose | `sc-1.3.1-info-and-relationships.md` (association), `sc-1.3.5-identify-input-purpose.md` (autocomplete), `sc-4.1.2-name-role-value.md`; whether a label or instruction exists at all: `sc-3.3.2-labels-or-instructions.md` |
| Headings, lists, tables, landmarks | `sc-1.3.1-info-and-relationships.md`; descriptive headings and labels: `sc-2.4.6-headings-and-labels.md`; page title: `sc-2.4.2-page-titled.md`; skip links: `sc-2.4.1-bypass-blocks.md` |
| Reading order and focus order | `sc-1.3.2-meaningful-sequence.md`, `sc-2.4.3-focus-order.md` |
| Keyboard operation, traps, shortcuts | `sc-2.1.1-keyboard.md`, `sc-2.1.2-no-keyboard-trap.md`, `sc-2.1.4-character-key-shortcuts.md` |
| Focus visibility | `sc-2.4.7-focus-visible.md` (exists), `sc-1.4.11-non-text-contrast.md` (contrasts), `sc-2.4.11-focus-not-obscured-minimum.md` (not covered) |
| Color and contrast | `sc-1.4.1-use-of-color.md` (color alone), `sc-1.4.3-contrast-minimum.md` (text), `sc-1.4.11-non-text-contrast.md` (controls and graphics) |
| Zoom, text size, spacing, reflow, orientation | `sc-1.4.4-resize-text.md`, `sc-1.4.10-reflow.md`, `sc-1.4.12-text-spacing.md`, `sc-1.3.4-orientation.md` |
| Images and images of text | `sc-1.1.1-non-text-content.md`, `sc-1.4.5-images-of-text.md` |
| Audio and video | `sc-1.2.1-audio-only-and-video-only-prerecorded.md`, `sc-1.2.2-captions-prerecorded.md`, `sc-1.2.3-audio-description-or-media-alternative-prerecorded.md`, `sc-1.2.4-captions-live.md`, `sc-1.2.5-audio-description-prerecorded.md`; autoplaying sound: `sc-1.4.2-audio-control.md` |
| Motion, flashing, timing, auto-updating | `sc-2.2.1-timing-adjustable.md`, `sc-2.2.2-pause-stop-hide.md`, `sc-2.3.1-three-flashes-or-below-threshold.md` |
| Pointer, touch, gestures, drag, target size | `sc-2.5.1-pointer-gestures.md`, `sc-2.5.2-pointer-cancellation.md`, `sc-2.5.4-motion-actuation.md`, `sc-2.5.7-dragging-movements.md`, `sc-2.5.8-target-size-minimum.md` |
| Tooltips and popups on hover or focus | `sc-1.4.13-content-on-hover-or-focus.md` |
| Instructions that rely on shape, position, color, or sound | `sc-1.3.3-sensory-characteristics.md` |
| Link text | `sc-2.4.4-link-purpose-in-context.md` |
| Finding pages across a site | `sc-2.4.5-multiple-ways.md` |
| Status messages and live regions | `sc-4.1.3-status-messages.md` |
| Page language and passages in other languages | `sc-3.1.1-language-of-page.md`, `sc-3.1.2-language-of-parts.md` |
| Predictable behavior: focus, input, consistency across pages | `sc-3.2.1-on-focus.md`, `sc-3.2.2-on-input.md`, `sc-3.2.3-consistent-navigation.md`, `sc-3.2.4-consistent-identification.md`, `sc-3.2.6-consistent-help.md` |
| Form errors, instructions, consequential submissions | `sc-3.3.1-error-identification.md`, `sc-3.3.3-error-suggestion.md`, `sc-3.3.4-error-prevention-legal-financial-data.md`, `sc-3.3.2-labels-or-instructions.md` |
| Re-entering information, logging in | `sc-3.3.7-redundant-entry.md`, `sc-3.3.8-accessible-authentication-minimum.md` |

Paths given without a folder are under `knowledge/wcag/`. Check `knowledge/INDEX.md` for anything not listed here. The index is kept current; this table is a convenience.

## Output shape for a finding

```
WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1
Confidence: definite
Where: <file:line or selector>
What: <one sentence>
Fix direction: <one sentence>
Source: knowledge/wcag/sc-4.1.2-name-role-value.md
```
