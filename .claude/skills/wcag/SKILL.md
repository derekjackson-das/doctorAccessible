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
| Accessible names, roles, states on controls | `knowledge/wcag/sc-4.1.2-name-role-value.md` |
| Form labels and instructions | no entry yet; see 4.1.2 for names, gap for SC 3.3.2 |
| Structure and relationships | no entry yet; gap for SC 1.3.1 |
| Keyboard, focus order, focus visible | no entry yet |
| Color and contrast | no entry yet |
| Images and media alternatives | no entry yet |

Check `knowledge/INDEX.md` for anything not listed here. The index is kept current; this table is a convenience.

## Output shape for a finding

```
WCAG 2.2 SC 4.1.2 Name, Role, Value (Level A), tier 1
Confidence: definite
Where: <file:line or selector>
What: <one sentence>
Fix direction: <one sentence>
Source: knowledge/wcag/sc-4.1.2-name-role-value.md
```
