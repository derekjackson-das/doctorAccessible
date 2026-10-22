# Verifier run, 2026-10-22, eval 008

Blind run through the registered `verifier` agent (`verifier.md` at commit 6a54d17), given the file path, the index, the content standards, and the axe command, and told not to open `expected.md`, `RESULTS.md`, or any run file.

Result against `expected.md`: **pass**. One Definite finding, SC 2.3.1 Three Flashes or Below Threshold (Level A), tier 1, sourced to the entry, at `.alert` and `@keyframes flash`, with G19 as the fix direction. The agent measured the rendered banner in headless Chrome at three viewport widths to argue the area exception does not apply, and took the stricter reading under principle 13. It correctly noted that SC 2.2.2 does not apply because the animation runs four seconds, and that reduced-motion is a best practice here. Nothing from the must-not list. axe inside the agent: 0 violations, expected. No file modified.

Observation for the verifier prompt: the report says the luminance swing is "far more than the 10% change the entry describes" and that the darker state is "well under 0.80". The 2.3.1 entry describes no such figures. Those are flash-threshold details stated from memory and attributed to the entry. The finding itself is sound, but the attribution is wrong, and principle 3 forbids the number. Third observation of this kind across the eval runs; it belongs in the verifier-tightening PR.

## Report as returned (findings and scan)

### [Definite] Alert banner flashes five times per second for four seconds
- Where: `input.html` lines 10 to 21, selector `.alert` and `@keyframes flash`
- What: `animation: flash 0.2s steps(1) 20` with keyframes that swap `background` between `#ffd400` and `#1a1a1a` at the 50% mark produces an abrupt light/dark/light cycle every 0.2 s, which is 5 flashes in every one-second period, for 4.0 s total, across the whole banner.
- Criterion: WCAG 2.2 SC 2.3.1 Three Flashes or Below Threshold (Level A), tier 1
- Source: knowledge/wcag/sc-2.3.1-three-flashes-or-below-threshold.md
- Supporting measurements: rendered banner is 640 by 94 px at 1024 and 1366 px wide, 436 by 94 px at 500 px wide. The entry treats the small-area exception as being for a blinking cursor or tiny status dot (G176); a full-content-width bold banner is not that. Per principle 13 the stricter reading is taken. (The report also stated luminance threshold figures attributed to the entry; see the observation above.)
- Fix direction: do not flash the banner (G19); draw attention with a static high-contrast style, an icon with a text label, or a single non-repeating transition.

Not a finding: the animation runs 4.0 s, so SC 2.2.2 does not apply on its own. No `prefers-reduced-motion` query is a best practice gap, not a 2.2 AA requirement.

Checked and passing: text contrast in both animation states; landmarks and leading `h1`; `lang`; title matches `h1`.

Content: reading level grade 4.0; heading describes the page; the closure is the first sentence. Manual review on whether "check your email from your department" is enough instruction.

Manual checks remaining: observe the flash on real devices and at zoom, with a flash analysis tool if the area question is contested; screen reader handling of a `role="alert"` present at load; reduced-motion behavior; whether an alert page with no links is intended.

Automated scan: axe-core 4.14.0, 0 violations. Consistent with the entry's note that axe has no rule for flash rate or area.
