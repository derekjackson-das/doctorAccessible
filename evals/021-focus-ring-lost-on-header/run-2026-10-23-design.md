# Design run, 2026-10-23, eval 021

Method: a general-purpose agent read `.claude/skills/design/SKILL.md` at commit 66bdcaa and followed it to review `input.html` on a developer's request. `expected.md`, run files, and `RESULTS.md` were off limits, and it wrote no files. This is a prompt test of the skill text, not a fresh-session load. axe was not run: Node.js is not installed on this machine. The 1.4.11 and 2.4.7 entries say axe has no rule for this defect.

Result against `expected.md`: **pass**.

- **The finding:** one requirement finding, definite, WCAG 2.2 SC 1.4.11 Non-text Contrast (Level AA), tier 1, from the entry.
  - Where: the `:focus-visible` rule applied to the header links.
  - Measured: the ring is 1.30:1 against `#00478a`, computed from the declared colors.
  - Fix direction: a header-specific ring color or a two-color indicator (C40). The design entry is named.
- **2.4.7:** cross-referenced pending a manual check, not filed as a second finding.
- **Passes:** the body focus ring passes at 7.14:1. Text contrast, use of color, and the rest of the page are reported only as passes.
- **Practice points:** both are marked as practice, at likely or manual review:
  - a single global focus color as the root cause;
  - header links under 44px (SC 2.5.5, AAA).

Nothing from the Must not list. Observation: the target-size practice point is not in the key, and is correctly framed as practice at manual review.
