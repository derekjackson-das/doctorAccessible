# Eval 022: animation that passes the flashing rule but ignores reduced motion

Input: `input.html`. A reading-list page with a "Show summary" button. Pressing it reveals a panel that sweeps in from off screen while scaling up from 40% to full size over 800 ms. There is no `prefers-reduced-motion` query.

Intended defect: motion animation triggered by an interaction that cannot be turned off and ignores the user's reduced-motion setting. Nothing flashes, nothing starts by itself, nothing loops. So no Level A or AA criterion is failed: SC 2.3.1 is not engaged (no flashing), and SC 2.2.2 is not engaged (the motion is triggered by the user and lasts under a second). The relevant criterion is SC 2.3.3 Animation from Interactions, Level AAA, beyond our target. That makes this a practice finding, which the design skill reports as likely or manual review, never definite. Everything else is clean: language, title, headings, a native button with `aria-expanded`, visible focus, text and border contrast at or above 7:1.

## Expected findings

1. **[Likely] or [Manual review]** The summary panel's sweep-and-scale animation ignores the user's reduced-motion setting and has no way to turn it off.
   - Basis: `knowledge/design/motion.md`, in its Practice part: honoring `prefers-reduced-motion` for interaction-triggered motion, which large translations and scaling can trigger in people with vestibular disorders. SC 2.3.3 Animation from Interactions (Level AAA), noted as beyond the AA target and with no entry yet, or cited from the design entry.
   - Where: `.summary.entering` and the `swoop` keyframes.
   - Acceptable fix directions: wrap the animation in a `prefers-reduced-motion: no-preference` query, or remove the transform under `reduce`, or replace it with an opacity fade (which WCAG's definition does not count as motion animation).

## Also acceptable

- Stating explicitly that SC 2.3.1 and SC 2.2.2 pass, with the reason, as a pass observation.
- A note that the `button` with `aria-expanded` meets SC 4.1.2, as a pass observation.
- A manual check to turn on the reduced-motion setting and confirm the motion is suppressed after a fix, from `knowledge/testing/reduced-motion.md`.

## Must not

- Mark the motion finding definite, or present it as a WCAG AA failure.
- Report SC 2.3.1 or SC 2.2.2 as failed.
- Report the button, focus, headings, language, or contrast.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

The 2.2.2 entry says axe's only rules for that criterion target the `blink` and `marquee` elements, and that CSS animations are found by watching the page, so axe is not expected to report this; the finding must come from reading. Whether axe was run for a given result is recorded in `RESULTS.md`.

## Pass condition

Finding 1 is present as likely or manual review, tied to the design entry's Practice part or to SC 2.3.3 marked as Level AAA; it is not definite; and nothing from the Must not list appears.
