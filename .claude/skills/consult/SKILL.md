---
name: consult
description: The pause before building. Use before writing any feature, component, page, or content, and whenever scope changes mid-build. Asks who it is for and what they are trying to do, then what the smallest thing that meets the need is, and only then how. May answer "build less" or "build nothing". Ends with a need statement written into the project's a11y-spec.md.
---

# Consult

This skill is a procedure and a map. The knowledge is in `knowledge/`. The rules for citing are in the `wcag` skill and apply here unchanged.

## When this applies

Any request to build, add, or change a feature, component, page, or piece of content. Also mid-build, the moment a new component appears, scope grows, or a requirement arrives that the need statement does not cover. Build does not start on a feature without a need statement in the spec (principle 14).

## Before anything else

Read the project's `a11y-spec.md`: repo root first, then `docs/`. It holds the conformance target, who the project serves, the assistive technology it tests with, existing need statements, pattern decisions, and banned patterns. If there is no spec, say so, offer to create one from `templates/a11y-spec.md`, and do not write a need statement anywhere else.

## The three questions, in order

Do not move to the next question until the current one is answered. Ask the developer; do not answer for them. If they cannot answer, that is the finding: the feature is not ready to build.

1. **Who is this for, and what are they trying to accomplish?** Answered when it names a specific person in a specific situation, including people using assistive technology named in the spec, and the task in their words. "Users" and "everyone" are not answers. Draw on `knowledge/ux/` need-finding entries when they exist; say "no entry yet" if they do not.
2. **What is the smallest thing that meets that need?** Answered when you can say what would be built, and what would not. "Less than you asked for" and "nothing, it is already met" are valid answers and are said plainly. Check the spec's existing need statements and pattern decisions first: the need may be met already. Check the code if it is available.
3. **Only then, how.** For every interactive pattern named in the request or the answer, open its entry in `knowledge/patterns/`. If none exists, say "no entry yet" and still ask what simpler pattern would serve, and what would be lost. Pull the criteria the chosen thing touches from `knowledge/INDEX.md`, open each entry, and cite tier and level from the entry. Lay out options with what each costs and what each gives up. Name the manual tests a human with assistive technology still owes, from the spec's AT list.

## Rules

1. Never state a criterion, a pattern's problems, or a usability figure from memory. Open the entry. If there is no entry, say so and mark the claim unverified. No `ux` or `patterns` entries exist yet; until they do, the "simpler alternative" question is asked on reasoning from the WCAG entries the pattern touches, and the answer says that is its basis.
2. Words are part of the feature. Consult the content too: headings, labels, link text, instructions, error messages, against `docs/content-standards.md` and the spec's content section.
3. Do not write code in consult. Describe what would be built. Code is the build mode's job, after the need statement exists.
4. The developer stays in charge. Propose the need statement; write it into the spec only when they agree. Record a pattern decision or a banned pattern in the spec's tables when one is made.
5. When the answer is "build nothing", still write the need statement, with "We will build: nothing" and why. That record stops the request coming back.

## Output shape

```
## Who and what
<the person, the situation, the task; or "not yet answered" and the question back>

## Smallest thing
<what would be built; what would not; "already met" or "build less" if so, with the evidence>

## How
Patterns: <each named pattern, its entry or "no entry yet", the simpler alternative, what is lost>
Criteria: <SC x.x.x Title (Level), tier 1, from knowledge/wcag/<entry>.md; one line each>
Options: <two or three, each with cost and trade-off>
Manual tests owed: <from the spec's AT list; what to do and what to record>

## Need statement (proposed for a11y-spec.md)
### <feature name> (YYYY-MM-DD)
- **For:** ...
- **Trying to:** ...
- **We will build:** ...
- **Instead of:** ...
- **Why this is right:** ...
- **Manual tests owed:** ...
```

## Where to look

| Question | Read |
|---|---|
| The format of a need statement, pattern decision, banned pattern | `templates/a11y-spec.md` |
| Which criteria a thing touches | `knowledge/INDEX.md`, then the entry; the `wcag` skill's map by topic |
| Whether a pattern is worth building | `knowledge/patterns/` (no entries yet; roadmap 3.2) |
| Who uses a thing and how to write a need statement | `knowledge/ux/` (no entries yet; roadmap 3.9) |
| How the words should read | `docs/content-standards.md` |
| Why the pause exists | `docs/principles.md`, principle 14 |
