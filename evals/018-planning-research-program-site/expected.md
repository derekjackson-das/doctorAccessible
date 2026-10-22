# Eval 018: planning a new research-program site

Input: `request.md`. A two-paragraph brief for a new site, with no `a11y-spec.md`. The brief carries several things a planning pass should catch: an audience that arrives on phones, many second-language readers, a testing plan that is desktop-only and ends with a scanner the project does not use, and a pattern already promised by the dean.

Intended outcome: the planning skill works through its checklist, proposes a draft spec from `templates/a11y-spec.md` with defaults marked for the team to confirm, raises the problems in the brief plainly, and points to consult for the first feature. It does not design the features.

## Expected

1. **Conformance target** is WCAG 2.2 Level AA, with the note from `CLAUDE.md` that Harvard policy names 2.1 AA and 2.2 AA satisfies it. Taken from the document, not from memory.
2. **Who it serves** names the groups in their situations: undergraduate applicants arriving on phones from email or social media, many from outside the US and reading in a second language; faculty posting projects; the program coordinator writing content. It says these are drawn from the brief and not yet backed by research, and offers a small research step, drawing on `knowledge/ux/learning-who-uses-a-thing.md`.
3. **AT and browsers** is a concrete proposed list that includes a mobile screen reader (VoiceOver on iOS, TalkBack on Android, or both) because the audience arrives on phones, plus a desktop screen reader and browser pair, keyboard only, and zoom. It says plainly that "our own laptops in Chrome" does not cover the audience, and marks the list for the team to confirm.
4. **Content** applies `docs/content-standards.md` defaults, names the coordinator as the writer, and raises second-language readers as a reason to keep the reading-level target strict or tighten it.
5. **Consult** is placed before each feature, and the first features are listed from the brief: project listings, the application form with CV upload, announcements and key dates, the homepage banner. No need statements are written here.
6. **Verify** replaces "Lighthouse the week before launch": the verifier agent runs after build steps that touch structure, forms, focus, names, color, media, or motion; axe is the only scanner; checking at the end alone is called out as too late.
7. **Human testing** names who runs the manual tests and when, puts first rounds in "Open manual tests" with owners, and says recruiting people from the audience, including disabled students, must start early given the ten-week schedule.
8. **The dean's rotating banner** is flagged, not designed: it goes to consult first, with `knowledge/ux/carousels.md` or `knowledge/patterns/carousel.md` named as where the reasons live. A proposed pattern decision or open question is acceptable; a final ban without the team is not.
9. **Draft spec** follows the template's sections, defaults marked "to confirm", and is proposed, not written.
10. **Next step** points to the consult skill for the first feature.

## Also acceptable

- Recommending the application form as the first feature to consult, since it has the deadline.
- Asking who owns the faculty side, since faculty are also users.
- Proposing that the coordinator learn to request the verifier or run the content checks.

## Must not

- Write code or design any feature, including the form or the banner.
- Write need statements; those are consult's.
- Propose Lighthouse or any scanner other than axe.
- Accept desktop Chrome on the team's laptops as the test list.
- Speak as a user with a disability or say what one "would experience".
- State a criterion number, title, or level, or a policy, from memory without marking it unverified.
- Write `a11y-spec.md` without the team's agreement.

## Pass condition

Items 1 to 3, 6, 8, 9, and 10 are present; the mobile screen reader is on the proposed list; Lighthouse is replaced by the verifier and axe; nothing from the Must not list appears.
