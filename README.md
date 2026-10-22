# Doctor Accessible

Doctor Accessible is an accessibility-first development assistant for Claude Code, built by Derek Jackson's team at Harvard and shared through this public repo. It helps a developer build web content that meets WCAG 2.2 Level AA, and it is honest about what it cannot judge.

## New here? Start with this

This section is for two kinds of reader: people who have never used Claude Code, and contributors who are new to development and want to know what they are working on. It is longer than the rest of the README on purpose.

### What Claude Code is

Claude Code is a program that runs in your terminal. You type what you want in plain English. It reads files, writes files, and runs commands for you, and it shows you what it did. It is made by Anthropic and uses the Claude AI model.

When you start Claude Code inside a folder, it looks for a file called `CLAUDE.md` and reads it first. That file holds the rules for the project. Everything Claude does in that folder follows those rules. This repo has one, and it is the most important file here.

### What Doctor Accessible is

Doctor Accessible is not an app you install. It is a set of files that teach Claude Code one job: helping a developer build web pages that work for people with disabilities, to a standard called WCAG 2.2 Level AA.

When you run Claude Code in this repo, or copy these files into another project, Claude follows them. It will ask who a page is for before it writes code. It will check its own work against the standard. It will say when it is not sure and a person needs to test. It will not pretend to be a blind user or guess at a rule it cannot cite.

### The four kinds of file

| Kind | Where | What it is |
|---|---|---|
| **Agent** | `.claude/agents/` | A separate Claude with its own instructions and no memory of your conversation. We have one, the verifier. It checks finished work the way a reviewer who was not in the room would. |
| **Skill** | `.claude/skills/` | A short procedure Claude loads when a task needs it. A skill says when it applies, how to cite, and which reference note answers which question. It holds no facts itself. |
| **Knowledge entry** | `knowledge/` | One Markdown page about one accessibility rule or topic, written in our own words from the official source, with a link, the source's tier, its version, and the date someone checked it. This is where the facts live. |
| **Eval** | `evals/` | A small web page with one known defect, plus a note saying what a correct check must find and must not find. Evals test whether a change to an agent, skill, or entry made Claude better or worse. |

Everything else in the repo is documentation: the principles, the roadmap, the content standards, and the record of decisions.

### How the pieces work together

A developer asks Claude for a search box. Claude pauses and asks who will use it and what they need. That is **consult**. Once the need is written down, Claude writes the form, loading the WCAG skill, which points it at the knowledge entries for labels and names. That is **build**. Then the developer asks for a check. The verifier agent reads the form cold, runs the axe scanner, opens the same knowledge entries, and reports that the input has no label, citing the rule. That is **verify**. The developer fixes it. A real person using a screen reader does the final test.

Each project that uses Doctor Accessible keeps one file, `a11y-spec.md`, that records who the project serves, what assistive technology it is tested with, and the decisions made along the way. Every mode reads it first.

### What contributors actually do

Most of the work is writing knowledge entries. For each rule in WCAG, someone reads the W3C page, explains the rule in plain words, says how it fails in code and how to fix it, cites the source, and writes one small broken page as an eval. That is reading, writing, and care. It is not programming. You do not need to know JavaScript to do it well.

Later work adds entries beyond WCAG: which interface patterns serve people and which do not, how to write content people can read, how to design focus and contrast above the minimum, how to run tests with real assistive technology.

If GitHub, branches, and pull requests are new to you, read [`docs/how-we-work.md`](docs/how-we-work.md) first. It explains every word and walks through one piece of work from start to finish.

Your first contribution, step by step:

1. Clone this repo and open a terminal in its folder.
2. Run `claude`. Read what it says. Type `/wcag` to see a skill load.
3. Ask it to run the verifier on `evals/001-missing-label/input.html`. Compare what comes back to `evals/001-missing-label/expected.md`.
4. Pick an open issue labeled `good first issue`. Put your name in the owner field. Follow its steps.
5. Open a pull request. The template tells you what to include. Someone reviews it against the same checklist.

### Words you will see

- **WCAG.** Web Content Accessibility Guidelines, the W3C standard. Version 2.2 is current. We build to Level AA.
- **Success criterion, or SC.** One testable rule in WCAG. There are 55 at Levels A and AA. Each gets its own knowledge entry.
- **Level A, AA, AAA.** How strict a rule is. A is the floor. AA is the common legal target. AAA is beyond what most policies require.
- **Tier.** How much authority a source has. Tier 1 is the standard itself. Tier 2 is the W3C explaining the standard. Tier 3 is experienced practitioners. We cite the tier every time.
- **axe.** The automated scanner we use. It finds some problems reliably and misses most. It is the only scanner here.
- **Assistive technology, or AT.** Screen readers, magnifiers, switch devices, voice control. The tools people use to work around barriers.
- **Need statement.** A short paragraph saying who a feature is for and what they are trying to do. Build does not start without one.

## The three modes

It works in three modes:

- **Consult.** The pause before building. Doctor Accessible asks who this is for and what they are trying to do, then what the smallest thing that meets that need is, and only then how. It may answer "build less" or "build nothing." It challenges the pattern (does this page need a carousel, or would a list serve the reader better), pulls the criteria that apply from the knowledge library, lays out options with their trade-offs, names the tests a human still has to run, and writes a need statement into the project spec. A thinking partner, not a lecture.
- **Build.** The developer writes code and content in the main Claude Code session. Skills load on demand and point at the knowledge entries for the task. Content is built to `docs/content-standards.md`: plain language, a reading-level target, descriptive headings and links, purposeful alt text.
- **Verify.** An isolated agent checks the result without seeing how it was built. It runs axe when it can, reads everything itself, and reports findings as definite, likely, or needing manual review.

The library is not only WCAG. It draws on the ARIA specs, the HTML Living Standard, W3C's explanatory material, and named practitioners and usability research, each labeled by tier in `knowledge/SOURCES.md`. There is no director agent and no simulated user. The developer directs; real people with assistive technology do the final testing.

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
16. **Content is part of the build.** Words get the same consult, build, verify as code, against `docs/content-standards.md` and the same evals.

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
| `docs/how-we-work.md` | For contributors new to GitHub, Claude Code, or development: the words, the workflow start to finish, and what finished work looks like. |
| `docs/content-standards.md` | What good content looks like: plain language, reading level, headings, links, alt text, errors. |
| `docs/ROADMAP.md` | Phases, work packages, and how the team divides the work. |
| `docs/decisions.md` | Why things are the way they are, dated. |
| `CONTRIBUTING.md` | The procedure for getting a change merged. |

## Roadmap

Full detail, including every work package with its deliverables and done-when, is in [`docs/ROADMAP.md`](docs/ROADMAP.md).

| Phase | Name | Goal | Done when |
|---|---|---|---|
| 0 | Foundation | One agent, one skill, one entry, one eval | Done 2026-10-22 |
| 1 | Team setup | Repo live, contribution rules, pattern proven | Public repo, PR template, axe installed, eval 001 passes |
| 2 | WCAG library | Every Level A and AA criterion has a verified entry | 55 entries in the index with source, tier, version, verified date |
| 3 | Domain skills | The procedures that use the library | consult, patterns, content, html-patterns, design, at-test-protocol, aria, ux, each with evals |
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

The full procedure is in [`CONTRIBUTING.md`](CONTRIBUTING.md).

- Claim a work package from `docs/ROADMAP.md` by opening an issue from the work-package template.
- Knowledge entries follow `knowledge/README.md`. Source, tier, version, verified date, or it does not merge.
- A pull request that changes an agent, a skill, or a knowledge entry says which evals were run and what they produced.
- Write entries in your own words from the source. This repo is public. Link, do not paste.
- New skill? Start from `.claude/skills/wcag/SKILL.md`. Keep it short. Depth goes in `knowledge/`.
- New decision? Add a dated entry to `docs/decisions.md`. Do not rewrite old ones.

## Status

2026-10-22: Phase 0 complete. Phase 1 nearly complete: public repo, contribution rules, axe running, eval 001 passing through the registered verifier. Work-package issues open for Phases 1 to 3. Remaining in Phase 1: onboarding runs (1.6) and the distribution decision (1.7).
