---
name: planning
description: Accessibility at the start of a project. Use when a project, site, or application is new, has no a11y-spec.md yet, or is being re-planned. Walks the team through a short checklist that fills the project spec from templates/a11y-spec.md: conformance target, who it serves, the assistive technology it will be tested with, content standards, and when consult, verify, and human testing happen. Ends by pointing to consult for the first feature.
---

# Planning

This skill is a checklist and a map. It holds no facts: the knowledge is in `knowledge/` and `docs/`, and the format is `templates/a11y-spec.md`. The rules for citing are in the `wcag` skill and apply here unchanged.

## When this applies

A new project, or an existing one with no `a11y-spec.md` (repo root first, then `docs/`). Also when a project changes audience, platform, or regulation enough that the spec no longer describes it. For a single feature inside a planned project, use `consult` instead.

## Before anything else

Look for an existing `a11y-spec.md`. If one exists, this is a review: go through the checklist against it and propose changes, not a new file. If none exists, the output is a draft spec from `templates/a11y-spec.md`.

## The checklist, in order

Ask the team; do not answer for them. Where the brief does not say, propose a default, say it is a default, and mark it for the team to confirm. An unanswered item is a finding, not a gap to fill with a guess.

1. **Conformance target.** WCAG 2.2 Level AA unless a regulation or policy names another version; if one does, record which and why. Read `docs/principles.md` (principle 4) and the project overview in `CLAUDE.md` before writing this line. Working drafts are never the target.
2. **Who it serves.** The people, in their situations, including those who use assistive technology. Not "users" or "the public". Draw on `knowledge/ux/learning-who-uses-a-thing.md`: what evidence exists, who is missing from it, and the smallest research step that would fill the gap. Mark anything not backed by evidence as assumed. Where people's difficulty is memory, attention, or understanding, note the `knowledge/coga/` objectives that apply.
3. **Assistive technology and browser pairs.** The concrete list the team will test with: screen reader and browser pairs for each platform the audience uses, keyboard only, zoom levels, and display settings such as reduced motion and forced colors. The template gives examples. The list must match the platforms named in item 2; a phone-heavy audience needs a mobile screen reader on it.
4. **Design system and components.** What exists and is approved. If nothing exists, say so; the first components will go through consult one at a time.
5. **Content standards.** The house defaults in `docs/content-standards.md` apply unless changed, including the reading-level target. Ask who writes the words. If the audience includes readers who need easier text, or second-language readers, consider tightening a default, and record why.
6. **When consult runs.** Before every feature, component, page, or piece of content, and whenever scope changes mid-build (`.claude/skills/consult/SKILL.md`). List the first features the brief names; each needs a need statement before build starts. Do not write those need statements here.
7. **When verify runs.** The verifier agent (`.claude/agents/verifier.md`) after any build step that touches structure, forms, focus, names and roles, color, media, or motion, and on request; agree whether the team will also request it at fixed points, such as before each release. axe is the only automated scanner (`CLAUDE.md`). Agree who dispatches it and where its reports go.
8. **Who does human testing, and when.** Doctor Accessible never stands in for a person with a disability (`docs/principles.md`, principle 7). Name who will run the manual tests owed: team members working through the AT list from item 3, and, for usability, people from the audience in item 2, recruited early (`knowledge/ux/learning-who-uses-a-thing.md` covers lead times and how to recruit). Put the first rounds in the spec's "Open manual tests" with an owner and a point in the schedule.
9. **Pattern decisions and banned patterns.** Usually empty at the start. Record any the brief already settles, such as "no carousels on the homepage", with the reason; `knowledge/patterns/` and `knowledge/ux/` supply the reasons.

## Rules

1. Never state a criterion number, title, or level, or a policy, from memory. Open the entry or the document. If there is none, say so and mark the claim unverified.
2. Propose the spec; write `a11y-spec.md` only when the team agrees (principle 8). Record the date and who agreed in the spec's change log.
3. Do not write code, and do not design features. Planning sets up the project; consult decides each feature.
4. Keep it to what the team will use. A spec nobody reads is a spec that does not exist.

## Output shape

```
## Checklist
1. Conformance target: <target, and why if not 2.2 AA>
2. Who it serves: <people and situations; assumed or evidenced; research step if needed>
3. AT and browsers: <the list, matched to item 2's platforms>
4. Design system: <what exists, or "none yet">
5. Content: <defaults or changes, with reasons; who writes the words>
6. Consult: <the first features that need a need statement>
7. Verify: <when, who dispatches, where reports go>
8. Human testing: <who, when, which rounds go in Open manual tests>
9. Patterns: <any decisions the brief already settles, or "none yet">
Open questions for the team: <each unanswered item>

## Draft a11y-spec.md (proposed)
<the template, filled from the checklist; defaults marked "to confirm">

## Next step
Run consult on <the first feature> before any build starts.
```

## Where to look

| Question | Read |
|---|---|
| The spec's sections and format | `templates/a11y-spec.md` |
| Conformance target and why | `docs/principles.md` (principle 4); `CLAUDE.md`, project overview |
| Who uses a thing; recruiting disabled participants | `knowledge/ux/learning-who-uses-a-thing.md`, `knowledge/ux/personas-from-research.md` |
| Memory, attention, understanding | `knowledge/coga/`, one entry per objective (tier 2) |
| Content defaults and reading level | `docs/content-standards.md` |
| What happens per feature | `.claude/skills/consult/SKILL.md` |
| What the verifier checks and when | `.claude/agents/verifier.md` |
| Why humans do the final test | `docs/principles.md`, principle 7 |
