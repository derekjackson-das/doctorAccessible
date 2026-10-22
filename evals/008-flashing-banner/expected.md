# Eval 008: alert banner that flashes five times a second

Input: `input.html`. A campus closure notice with a full-width alert banner.

Intended defect: the `.alert` banner has a CSS animation that alternates its background between yellow and near-black every 0.2 seconds for 20 cycles, which is five flashes per second for four seconds. That is more than three flashes in a one-second period over a large area with a strong luminance change. It stops after four seconds, so SC 2.2.2 (which needs more than five seconds) does not apply; the defect is 2.3.1 alone. Everything else is clean: language set, title present, one `h1`, landmarks, contrast above the thresholds in both animation states, visible focus, `role="alert"` on the notice.

## Expected findings

1. **[Definite]** Banner flashes more than three times per second.
   - Criterion: WCAG 2.2 SC 2.3.1 Three Flashes or Below Threshold (Level A), tier 1
   - Source: `knowledge/wcag/sc-2.3.1-three-flashes-or-below-threshold.md`
   - Where: the `.alert` rule and `@keyframes flash` in the stylesheet, applied to the `p.alert` inside `main`
   - Acceptable fix directions: remove the animation (technique G19); the yellow background and the `role="alert"` already draw attention. If motion is wanted, use a single fade-in rather than a flash. Likely is acceptable instead of Definite if the verifier notes the thresholds depend on area and viewing distance and wants a human to confirm; Definite is the better answer here because a full-width bar at 5 Hz with a yellow-to-black swing is well over the general flash threshold.

## Also acceptable

- A note that SC 2.2.2 does not apply because the animation ends within five seconds, showing the verifier checked the duration rather than assuming.
- A note that the animation should respect the user's reduced-motion preference, as a practice rather than a requirement.
- A manual-review note to confirm the rendered flash with a flash analysis tool.

## Must not

- Report SC 2.2.2 as a failure; the animation lasts four seconds.
- Report the `role="alert"`; it is appropriate for a closure notice.
- Report the heading, landmarks, focus style, language, or contrast. Both animation states pass 4.5:1 for the bold 1.25rem text.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is expected to report no violations. It has no rule for flash rate; the defect is found by reading the CSS animation timing. A verifier that treats the clean scan as a pass has failed this eval.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
