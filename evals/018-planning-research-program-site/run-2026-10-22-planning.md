# Planning run, 2026-10-22, eval 018

Method: a general-purpose agent read `.claude/skills/planning/SKILL.md` at commit ddb25ed and followed it, then answered `request.md`. `expected.md`, run files, and `RESULTS.md` were off limits, and it wrote no files. This is a prompt test of the skill text, not a fresh-session load of `/planning`, the same method as the consult runs in 015 to 017. Onboarding runs can repeat it as a true fresh-session run.

Result against `expected.md`: **pass**.

- **Conformance target:** WCAG 2.2 AA, with the Harvard 2.1 AA note taken from `CLAUDE.md` and principle 4, not from memory.
- **Who it serves:**
  - Applicants on phones, many from outside the US and reading in a second language; faculty; and the coordinator. All are marked assumed.
  - It added a group the brief left out: whoever reviews applications.
  - It named who is missing from the evidence and proposed a three-part research step from `ux/learning-who-uses-a-thing.md`.
- **AT list:** VoiceOver with Safari on iPhone and TalkBack with Chrome on Android first, then NVDA with Chrome and VoiceOver with macOS Safari, keyboard only, 200% and 400% zoom, reduced motion, and forced colors. It said plainly that the team's laptops in Chrome cover only part of the desktop row.
- **Content:** house defaults; the coordinator and faculty named as writers; tightenings for second-language readers proposed, to confirm.
- **Consult:** the five features from the brief listed as owing need statements, with none written.
- **Verify:** Lighthouse replaced by the verifier and axe after each build step, plus fixed points. It said that checking only at the end is too late.
- **Human testing:**
  - Recruiting to start in week 1, citing the lead times in the ux entry.
  - Rounds placed in "Open manual tests" with weeks.
  - Principle 7 cited.
- **Banner:** sent to consult as "pending consult", not designed. The reasons point to `ux/carousels.md`, `patterns/carousel.md`, and the 2.2.2 entry.
- **Draft spec:** in the template's sections, proposed, not written.
- **Next step:** consult on the application form first.

Nothing from the Must not list.

Observation: the answer runs long. It is a full draft spec plus a checklist. That is the skill's output shape, but a team may want the checklist alone first. Not a failure; worth watching in onboarding runs.
