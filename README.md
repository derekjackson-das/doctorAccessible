# Doctor Accessible

Doctor Accessible is an accessibility-first development assistant for Claude Code, built by Derek Jackson's team at Harvard and shared through this public repo. It helps a developer build web content that meets WCAG 2.2 Level AA, and it is honest about what it cannot judge.

It works in three modes:

- **Consult.** The pause before building. Doctor Accessible asks who this is for and what they are trying to do, then what the smallest thing that meets that need is, and only then how. It may answer "build less" or "build nothing." It challenges the pattern (does this page need a carousel, or would a list serve the reader better), pulls the criteria that apply from the knowledge library, lays out options with their trade-offs, names the tests a human still has to run, and writes a need statement into the project spec. A thinking partner, not a lecture.
- **Build.** The developer writes code and content in the main Claude Code session. Skills load on demand and point at the knowledge entries for the task.
- **Verify.** An isolated agent checks the result without seeing how it was built. It runs axe when it can, reads everything itself, and reports findings as definite, likely, or needing manual review.

The library is not only WCAG. It draws on the ARIA specs, the HTML Living Standard, W3C's explanatory material, and named practitioners and usability research, each labeled by tier in `knowledge/SOURCES.md`. Under the modes sit four parts: one verifier agent, a set of short skills that act as maps, a Markdown knowledge library where every entry cites its source, tier, version, and verification date, and an eval corpus of known defects that makes every change measurable. Each project keeps one `a11y-spec.md`, its own requirements and decisions, which every mode reads first. Build does not start on a feature without a need statement in it. There is no director agent and no simulated user. The developer directs; real people with assistive technology do the final testing.

Conformance target: WCAG 2.2 Level AA. Automated scanner: axe only. Reference stack: plain HTML, CSS, and JavaScript.

## Principles

The short form. Rationale for each is in [`docs/principles.md`](docs/principles.md).

1. **Skill or agent.** Needs to remember the conversation: skill. Needs to forget it: agent. Nothing else gets to be an agent.
2. **Knowledge base first, sources list second, nothing third.** Every answer starts in `knowledge/`. No entry means say so, research only from `knowledge/SOURCES.md`, and write the entry before using it.
3. **Cite or stay quiet.** Tier, source, and version on every claim. Nothing from memory.
4. **One target, named.** WCAG 2.2 AA. Say when 2.0 or 2.1 applies. Drafts are awareness only.
5. **Native HTML first.** ARIA only when no native element does the job.
6. **Honest confidence.** Definite, likely, or manual review. One finding per defect.
7. **Humans do the final test.** Doctor Accessible never speaks as a user with a disability.
8. **The developer stays in charge.** Advise, verify, brainstorm. Never silently rewrite.
9. **Measure every change.** No eval, no merge.
10. **Short skills, deep library.** Skills are maps. Depth lives in `knowledge/`.
11. **Plain web first.** Frameworks are layers added later.
12. **Build in public, in our own words.** Link, quote only normative text, never paste.
13. **Conservative when sources conflict.** Name it, cite both, take the stricter reading.
14. **Start from the need.** Who is it for, what are they trying to do, why is this the right thing to build. Consult may say build less, or nothing. No need statement, no build.
15. **One spec per project.** Every mode reads `a11y-spec.md` before acting and writes decisions back to it.

## Where things live

| Path | What |
|---|---|
| `CLAUDE.md` | Rules for Claude Code in this repo. Read it first. |
| `.claude/agents/verifier.md` | The verifier agent. |
| `.claude/skills/wcag/SKILL.md` | The WCAG skill: when it applies, how to cite, where to look. |
| `knowledge/INDEX.md` | Table of contents for the library. |
| `knowledge/SOURCES.md` | The trusted sources by tier. Nothing off it is authoritative. |
| `knowledge/wcag/` | One entry per success criterion. |
| `evals/` | Known-defect snippets and the findings a correct verifier must produce. |
| `templates/a11y-spec.md` | The project spec template. Copy it to the root of your project. |
| `docs/principles.md` | The principles, with reasons. |
| `docs/ROADMAP.md` | Phases, work packages, and how the team divides the work. |
| `docs/decisions.md` | Why things are the way they are, dated. |

## Roadmap

Full detail, including every work package with its deliverables and done-when, is in [`docs/ROADMAP.md`](docs/ROADMAP.md).

| Phase | Name | Goal | Done when |
|---|---|---|---|
| 0 | Foundation | One agent, one skill, one entry, one eval | Done 2026-10-22 |
| 1 | Team setup | Repo live, contribution rules, pattern proven | Public repo, PR template, axe installed, eval 001 passes |
| 2 | WCAG library | Every Level A and AA criterion has a verified entry | 55 entries in the index with source, tier, version, verified date |
| 3 | Domain skills | The procedures that use the library | consult, patterns, html-patterns, content, design, at-test-protocol, each with evals |
| 4 | Eval automation | Changes are measurable | Evals run headless and their results appear in every PR |
| 5 | Expansion | Layers on top of the base | Framework skills, ARIA pattern entries, v1.0 |

Work is claimed by work package, not by phase. Each package is one GitHub issue with six fields: goal, deliverables, done when, depends on, size, owner.

## Using it

1. Clone the repo.
2. Open a terminal in the repo folder and run `claude`.
3. Copy `templates/a11y-spec.md` into your project as `a11y-spec.md` and fill in the target and audiences.
4. Start with consult: say who you are building for and what they need. Build once the need statement is in the spec. Type `/wcag` to load the WCAG skill by hand.
5. Ask for the verifier when you want an independent check.

## Working on it as a team

- Claim a work package from `docs/ROADMAP.md` by taking its issue.
- Knowledge entries follow `knowledge/README.md`. Source, tier, version, verified date, or it does not merge.
- A pull request that changes an agent, a skill, or a knowledge entry says which evals were run and what they produced.
- Write entries in your own words from the source. This repo is public. Link, do not paste.
- New skill? Start from `.claude/skills/wcag/SKILL.md`. Keep it short. Depth goes in `knowledge/`.
- New decision? Add a dated entry to `docs/decisions.md`. Do not rewrite old ones.

## Status

2026-10-22: Phase 0 complete. One agent, one skill, one verified knowledge entry, one eval. Principles and roadmap adopted. Phase 1 next.
