# Design run, 2026-10-23, eval 022

Method: as for eval 021, with the skill at commit 66bdcaa. axe was not run: Node.js is not installed on this machine. The 2.2.2 entry says axe does not detect CSS animation.

Result against `expected.md`: **pass**.

- **No requirement failures**, stated plainly.
- **The motion finding:** a practice finding at **likely**, not definite.
  - What: the sweep-and-scale animation ignores `prefers-reduced-motion`.
  - Basis: SC 2.3.3 (Level AAA, beyond our target) and technique C39.
  - Where: `.summary.entering` and the `swoop` keyframes.
  - Classification: correctly treated as motion animation, since position and size change, not as a fade.
  - Fix directions: wrap it in a `no-preference` query, or use an opacity fade under `reduce`.
- **2.2.2 and 2.3.1:** explained as met, because the motion is user-triggered, lasts 0.8 seconds, and does not flash.
- **Passes:** button, focus, and contrast are reported only as passes, with ratios computed.
- **Manual test:** a reduced-motion check from `testing/reduced-motion.md`.

Nothing from the Must not list. Observation: like 021, it adds a 44px target-size practice point at manual review, correctly framed.
