# Verifier run, 2026-10-22, eval 005

Blind run through the registered `verifier` agent (`verifier.md` at commit 6a54d17), same conditions as the other runs.

Result against `expected.md`: **pass**. One Definite finding, SC 1.4.3 Contrast (Minimum) (Level AA), tier 1, sourced to the entry, at `.note`, with the measured ratio 2.85:1 against the 4.5:1 floor and G18 as the fix direction. The ratio was computed from the declared colors with the Recommendation's formula, which the key permits as a computation from the source. The first paragraph and heading were checked and declared passing, not reported. A content note that the faint paragraph carries the time-sensitive warning was raised as manual review, as the key allows. Nothing from the must-not list. No file modified.

## Report as returned (findings and scan)

### [Definite] Gray note text fails minimum contrast
- Where: `input.html` line 9, rule `.note { color: #999999; background: #fff; font-size: 1rem; }`, applied to the `p class="note"` on line 19
- What: Normal-size text (1rem, roughly 16 CSS px, not bold) in `#999999` on a `#ffffff` background has a computed contrast ratio of 2.85:1, below the 4.5:1 floor for non-large text; no exemption applies (it is live content, not decoration, not a logo, not an inactive control).
- Criterion: WCAG 2.2 SC 1.4.3 Contrast (Minimum) (Level AA), tier 1
- Source: knowledge/wcag/sc-1.4.3-contrast-minimum.md (verified 2026-10-22)
- Fix direction: Darken the note color until it measures at least 4.5:1 against white (around `#767676` or darker), or drop the gray and let it inherit body text color; keep setting foreground and background together.

No other defects found. Body text 17.4:1; focus outline 7.14:1 (no focusable elements, so inert). `lang="en"`, `title`, single `h1`, `header` and `main`. No images, media, forms, links, scripts, or motion.

Content: reading level grade 3.2 by a script with a syllable heuristic; heading matches title; "p.m." unexpanded raised as manual review; "department calendar" not linked noted as a usability gap, manual review.

Manual checks remaining: confirm visually and in forced-colors mode; 200% and 320px reflow; screen reader reading order; a human judgment on whether de-emphasizing the exam-week note is the right intent.

Automated scan: axe-core 4.14.0, 1 violation, rule `color-contrast`, 1 occurrence at `.note`. Matches the Definite finding; nothing else fired.
