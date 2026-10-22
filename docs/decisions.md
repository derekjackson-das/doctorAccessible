# Decisions

Why things are the way they are. Add a dated entry when a decision changes shape; do not rewrite history.

## 2026-10-22: initial shape

**No director agent.** The main Claude Code session already holds the full context and dispatches subagents. A director agent would be a second coordinator with less information than the first. The human directs.

**One agent, the verifier.** Isolation is the feature: it must not inherit the builder's reasoning. Every other role proposed at the start (design, content, planning, research) is a procedure applied while building, so it becomes a skill, not an agent. The rule: if the work needs to remember the conversation, it is a skill; if it needs to forget, it is an agent.

**No user-testing agent.** A model cannot be a screen reader user. The role becomes a skill that produces a test protocol for human assistive-technology testers.

**Skills are maps, not libraries.** A `SKILL.md` holds when the domain applies, how to cite, how to judge, and which knowledge file answers which question. The knowledge lives in `knowledge/`, where it can be maintained and reviewed on its own.

**Markdown, not JSON.** Agents read Markdown natively, GitHub renders and diffs it, and teammates can edit it without a parser. Nothing here has a machine consumer.

**Built from scratch.** Nothing imported from the `ventz` agent, the general CCode knowledge base, or DAARA. The general knowledge base and DAARA stay separate from this repo in both directions.

**Public repo.** Entries are written in our words from the source, with the source linked. No pasted vendor or practitioner text.

**Evals before features.** A fixed corpus of known-defect snippets is the only way to tell whether a prompt change helped. It was the weakest link in the original plan, so it is in the first commit.

**axe only.** The sole automated scanner. Automated tools find a minority of defects; the verifier's own reading does the rest.

**Folder renamed** from `doctorAccessilbe` to `doctorAccessible`, with the Claude Code memory folder copied to the new path key.

## 2026-10-22: three modes, principles, roadmap

**Three modes: consult, build, verify.** Brainstorming with a developer was always intended but was not in the spec. It becomes an explicit mode with its own skill (`consult`, work package 3.1), because a procedure that needs the developer's context is a skill under principle 1. Build is the main session with skills. Verify is the agent.

**Thirteen working principles adopted.** Recorded in `docs/principles.md` with reasons, short form in the README and `CLAUDE.md`. The two Derek named first: the skill-or-agent rule, and knowledge base first with outside research only when the library has nothing.

**Roadmap adopted.** Five phases after the foundation, work claimed by package through GitHub issues with six fixed fields. Phase 2 splits by WCAG principle so parallel work never touches the same file. Full detail in `docs/ROADMAP.md`.

**Consult comes before the other skills.** It is the mode a developer meets first, and its evals are transcript tests rather than code tests, which is a pattern the team needs early.

## 2026-10-22: the design moment and the project spec

**Consult starts from the need, not the feature.** Three questions in order: who is this for and what are they trying to do; what is the smallest thing that meets it; only then, how. Consult may answer "build less" or "build nothing." The output is a need statement written into the project spec.

**The pause is a gate.** Build does not start on a feature without a need statement. When scope changes, a new component appears, or a requirement arrives that the need statement does not cover, build stops and returns to consult. The main session enforces this on itself through `CLAUDE.md`.

**One spec per project.** `a11y-spec.md`, from `templates/a11y-spec.md`, lives at the root of the developer's project. It holds the project's own requirements and decisions. Every mode reads it first. The verifier reports deviations from it under a separate heading from WCAG findings and hands judgment calls about the need to a human.

**Patterns get their own knowledge domain.** `knowledge/patterns/`, one entry per interactive pattern, each saying when a simpler pattern serves and what the pattern costs to do right. Roadmap package 3.2.

**Open question recorded.** A developer's project needs the agent, the skills, and the spec next to their code. Packaging this repo as a Claude Code plugin is the likely answer. Roadmap package 1.7.

**Principles 14 and 15 adopted.** Start from the need; one spec per project.

## 2026-10-22: knowledge beyond WCAG, and a sources list

**The library draws on more than WCAG.** The ARIA specs, ARIA in HTML, accessible name computation, and the HTML Living Standard are tier 1. W3C's Understanding, Techniques, tutorials, Using ARIA, and the Authoring Practices are tier 2. Named practitioners, support databases, and usability research are tier 3. The tier system already allowed this; the list did not exist.

**`knowledge/SOURCES.md` is the repo's own trusted-sources list.** Built fresh for this public repo, not copied from elsewhere. Nothing off it is authoritative until a pull request adds it. Tier 3 has an admission rule: real name, dated, cites or cited by tier 1 or 2, checkable claims, maintained. Tier 3 rows are marked "proposed" until the team confirms them.

**Nielsen Norman Group belongs in the design moment.** Usability research, not an accessibility authority. It feeds consult's "is this the right thing to build" question through a `ux` knowledge domain (roadmap 3.9), summarized and linked, never pasted.

**ARIA moved up.** The `aria` domain leaves Phase 5 and becomes 3.8, beside `patterns`, because the two feed each other.

**Principle 2 reworded.** Knowledge base first, sources list second, nothing third.

## 2026-10-22: content standards

**A second kind of principle.** The sixteen principles say how the team works. Plain language, reading level, organization, headings, links, alt text, and errors are standards for what the output looks like. They live in `docs/content-standards.md`, each with its source and tier, because WCAG at Level AA says little about plain language and nothing about reading level.

**The spec imports the standards.** A project's `a11y-spec.md` gets a content section with a reading-level target and overrides. House default: grade 8 or below by Flesch-Kincaid Grade Level, as a signal that sends a human to read, never a pass on its own.

**Content moves up.** The `content` skill becomes roadmap 3.3, ahead of `html-patterns`, because content is where most of Harvard's authors live. It is the writing mode, not an accessibility add-on.

**The verifier checks words.** A "Content" heading in its report. A readability tool is roadmap 4.7.

**Principle 16 adopted.** Content is part of the build.

## 2026-10-22: contribution rules; roadmap is for the team

**`CONTRIBUTING.md` and two templates.** The procedure for getting a change merged, a pull request template that asks which evals ran, and an issue template carrying the six work-package fields. Roadmap package 1.2.

**The roadmap lists only what the team can see.** Package 1.5, a listing in Derek's private CCode workspace, is removed and its ID left unused. Private housekeeping stays private.
