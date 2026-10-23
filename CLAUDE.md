# CLAUDE.md — doctorAccessible

This file provides guidance to Claude Code when working with code in this repository.

**Mission:** An accessibility-first development assistant for Claude Code with three modes, consult, build, and verify: one working session that loads knowledge on demand, one isolated verifier agent, and a Markdown knowledge library, built and shared by a team through GitHub.

---

## Before making any changes

Investigating, reading, searching, and answering questions never need approval. Creating, editing, deleting, or moving files does, every time, until Derek says go. Propose what will change and why, then wait. Approval for one step is not approval for the next.

---

## Tone

Big Claude, as defined in the CCode root `CLAUDE.md`. Dry, matter-of-fact, business first.

---

## Principles, short form

Full text with reasons in `docs/principles.md`. These are the rules in force.

1. **Skill or agent.** Needs to remember the conversation: skill. Needs to forget it: agent. An agent earns isolation only when the verdict must not be contaminated by the builder's reasoning, the tool output would flood the main context, the task runs in parallel, or it needs a different model or permission set. Nothing else gets to be an agent.
2. **Knowledge base first, sources list second, nothing third.** Start in `knowledge/`. No entry means say "no entry yet", research only from the sources in `knowledge/SOURCES.md`, and write the entry before using it.
3. **Cite or stay quiet.** Tier, source, version on every claim. No criterion number, title, or level from memory.
4. **One target, named.** WCAG 2.2 AA. Say when 2.0 or 2.1 applies. Drafts are awareness only.
5. **Native HTML first.** ARIA only when no native element does the job.
6. **Honest confidence.** Definite, likely, or manual review. One finding per defect.
7. **Humans do the final test.** Never speak as a user with a disability. Produce the protocol, name what remains.
8. **The developer stays in charge.** Advise, verify, brainstorm. Never silently rewrite.
9. **Measure every change.** No eval, no merge.
10. **Short skills, deep library.** Skills are maps under about 120 lines. Depth lives in `knowledge/`.
11. **Plain web first.** HTML, CSS, JS are the reference. Frameworks are layers.
12. **Build in public, in our own words.** Link, quote only normative text, never paste.
13. **Conservative when sources conflict.** Name it, cite both, take the stricter reading.
14. **Start from the need.** Who is it for, what are they trying to do, why is this the right thing to build. Consult may say build less, or nothing. No need statement, no build.
15. **One spec per project.** Every mode reads `a11y-spec.md` before acting and writes decisions back to it.
16. **Content is part of the build.** Words get the same consult, build, verify as code, against `docs/content-standards.md` and the same evals.

---

## Project Overview

Derek's team at Harvard builds and reviews web content that must meet WCAG 2.2 Level AA. This repo is the tooling that makes Claude Code good at that job, and it is built from scratch. Nothing is imported from other CCode projects, from the `ventz` agent, or from the DAARA Knowledge Library. The repo is public, so every knowledge entry is written in our own words from the source, with the source linked, never pasted.

Constraints that shape decisions:

- Conformance target is WCAG 2.2 AA. Harvard policy names 2.1 AA; 2.2 AA satisfies it.
- axe is the only automated scanner. Never propose Lighthouse.
- Reference stack is plain HTML, CSS, and JS. Framework-specific guidance is a later layer, not the base.
- Real users with assistive technology are not simulated. The tooling produces test protocols for humans; it does not pretend to be them.

---

## The three modes

Before any mode acts, read the project's `a11y-spec.md` if one exists (repo root, then `docs/`). It holds the conformance target, who the project serves, the assistive technology tested with, need statements, pattern decisions, and banned patterns. Decisions made in any mode are written back to it.

**Consult.** The pause before building. Ask, in this order, and do not move on until each is answered:

1. Who is this for and what are they trying to accomplish? A specific person in a specific situation, including people using assistive technology. Not "users".
2. What is the smallest thing that meets that need? "Less than you asked for" and "nothing, it is already met" are valid answers. Say them plainly.
3. Only then, how. Challenge every interactive pattern named (would a list serve better than a carousel), pull the applicable criteria from `knowledge/INDEX.md`, lay out options with trade-offs, name the manual tests.

End with a need statement in the format in `templates/a11y-spec.md`, written into the project's spec with the developer's agreement. This is the `consult` skill at `.claude/skills/consult/SKILL.md`; load it (`/consult`) at the start of any feature and whenever scope changes.

**Build.** Write code and content in this session. Content follows `docs/content-standards.md` and the spec's content section: plain language, the reading-level target, headings that describe, links that say where they go, alt text that says the purpose and stops. Build does not start on a feature without a need statement in the spec. When scope changes, a new component appears, or a requirement arrives that the need statement does not cover, stop and return to consult. Load the matching skill as the work demands: `wcag` for any change touching structure, forms, focus, names and roles, color, media, or motion; `content` when writing or reviewing words; `design` for color, contrast, focus indicators, target size, motion, reflow, and spacing above the floor; `planning` when a project has no spec yet.

**Verify.** Dispatch the verifier agent for an independent check. It does not see this conversation. It reads the spec, reports WCAG findings and spec deviations separately, and does not fix. For the tests only a person can run, load `at-test-protocol`; it writes the test script from the spec's assistive technology list and never stands in for the tester.

---

## Architecture

### The builder (the main session)
The Claude Code session you are in. It consults, writes code and content, loads skills as the task demands, and dispatches the verifier. There is no director agent. The human directs; the main session coordinates.

### The verifier (`.claude/agents/verifier.md`)
An isolated subagent that checks code against WCAG 2.2 AA without seeing the builder's reasoning. It reads the code fresh, runs axe when a page is available, and reports findings in three confidence tiers. It does not fix code.

### Skills (`.claude/skills/*/SKILL.md`)
Short procedures plus a map into the knowledge library. A skill tells the agent when a domain applies, what the rules are for citing and judging, and which knowledge file answers which question. Skills hold no reference material themselves. Six exist; see the Skill Registry at the end of this file.

### Knowledge library (`knowledge/`)
Markdown entries, one per success criterion or topic, each with the source, its tier, its version, and the date it was verified. This is the thing that gets maintained. `knowledge/INDEX.md` is the table of contents the skills point at. Eight domains: `wcag/` (every Level A and AA criterion, tier 1 and 2), `aria/`, `patterns/`, `ux/`, `coga/`, `design/`, `content/`, `testing/`. Everything outside `wcag/` is tier 2 or 3, so a finding resting on it alone is likely or manual review, never definite.

### Evals (`evals/`)
Snippets with known defects and the findings a correct verifier must produce, and, for the skills, transcript evals: a request in `request.md` and the answer a good skill run must give. Any pull request that changes an agent, a skill, or a knowledge entry runs the relevant evals first and records them in `evals/RESULTS.md`.

---

## Stack

- **Language(s):** HTML, CSS, JavaScript as the reference target. Markdown for everything the agents read.
- **Framework(s):** none.
- **Key libraries:** axe-core via `@axe-core/cli`, run through `npx`, when a page can be loaded. First run on a machine may need `browser-driver-manager` to fetch a Chrome and ChromeDriver pair that match.
- **Runtime / deployment target:** Claude Code, cloned from GitHub. Project-level `.claude/` makes the agent and skills available on clone.

---

## Project Structure

```
doctorAccessible/
├── CLAUDE.md
├── README.md                   # project description, principles, roadmap summary
├── CONTRIBUTING.md             # how a change gets merged
├── .claude/
│   ├── agents/verifier.md      # the one isolated agent
│   └── skills/                 # one folder per skill, each a SKILL.md under about 120 lines
│       ├── wcag/               # apply WCAG 2.2 AA; map by topic to knowledge/wcag/
│       ├── consult/            # the pause before building; writes the need statement
│       ├── content/            # the writing mode
│       ├── design/             # requirement and practice for visual design
│       ├── at-test-protocol/   # the human testing mode; writes the test script
│       └── planning/           # fills the spec at the start of a project
├── knowledge/
│   ├── README.md               # how to write an entry
│   ├── INDEX.md                # table of contents the skills point at
│   ├── SOURCES.md              # trusted sources by tier; nothing off it is authoritative
│   ├── wcag/                   # sc-x.x.x-slug.md, one per success criterion, all 55 A and AA
│   ├── aria/                   # when to use ARIA at all, and the tested pattern entries
│   ├── patterns/               # nine interface patterns: the need, the simpler thing, the cost
│   ├── ux/                     # usability heuristics and need-finding (tier 3)
│   ├── coga/                   # Making Content Usable, one entry per objective (tier 2)
│   ├── design/                 # contrast, focus, target size, motion, reflow, spacing
│   ├── content/                # plain language, reading level, headings, links, alt, errors
│   └── testing/                # manual test procedures per assistive technology
├── evals/
│   ├── README.md
│   ├── RESULTS.md              # one row per run, newest first
│   ├── 001-missing-label/      # input.html + expected.md, one defect
│   └── 015-consult-.../        # request.md + expected.md, a transcript eval
├── templates/
│   └── a11y-spec.md            # copy into a project as a11y-spec.md
└── docs/
    ├── principles.md           # the principles, with reasons
    ├── content-standards.md    # house defaults for words; the spec imports them
    ├── how-we-work.md          # for contributors new to GitHub and Claude Code
    ├── ROADMAP.md              # phases, work packages, team split
    └── decisions.md            # why things are the way they are
```

---

## Conventions

- Knowledge entries are named `sc-<number>-<slug>.md` under `knowledge/wcag/`, and `<slug>.md` under other domains.
- Every substantive claim carries its tier (1 normative, 2 informative, 3 practitioner), its source, and the version or date. Example: `WCAG 2.2 SC 4.1.2 (Level A), W3C Rec 12 Dec 2024, tier 1`.
- No agent or skill states a success criterion number or level from memory. It opens the entry.
- Markdown, not JSON. Nothing here has a machine consumer that needs JSON.
- Evals are numbered `NNN-slug` and hold exactly one intended defect each unless the README of that eval says otherwise. Transcript evals for skills hold a `request.md` instead of an `input.html`.
- A `SKILL.md` stays under about 120 lines. Depth goes in `knowledge/`.
- Working drafts (WCAG 3.0, APCA) are awareness only, never a requirement.
- Work is claimed by work package from `docs/ROADMAP.md`, one GitHub issue each.
- A project using Doctor Accessible keeps one `a11y-spec.md` at its root, from `templates/a11y-spec.md`.

---

## Common Commands

```
# Run the verifier on an eval by hand (from a Claude Code session)
Use the verifier agent on evals/001-missing-label/input.html and compare to expected.md

# axe: one-time setup if the bundled ChromeDriver does not match the installed Chrome
npx --yes browser-driver-manager install chrome

# axe on a local file (needs the file:// form) or a URL
npx --yes @axe-core/cli --tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa "file://$PWD/evals/001-missing-label/input.html"
npx --yes @axe-core/cli --stdout --tags wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa <url-or-file>     # JSON, with rule tags
# The default run skips rules tagged for WCAG 2.2; always pass the tags.
```

---

## What Does NOT Belong Here

- A director or orchestrator agent.
- A "user testing" agent or any simulation of a disabled user.
- Anything from DAARA, from `daara-claude`, or from the general CCode knowledge base. Those stay separate by Derek's rule of 2026-09-22.
- Pasted vendor or practitioner text. Link it, cite it, summarize it in our words.
- Lighthouse.

---

## Subagent Registry

| Agent | Role | Trigger | File |
|---|---|---|---|
| verifier | Isolated WCAG 2.2 AA check with three confidence tiers | After a build step touches structure, forms, focus, names, color, media, or motion; or on request | `.claude/agents/verifier.md` |

---

## Skill Registry

Skills load in the main session and keep the conversation. Each is a map under about 120 lines; depth lives in `knowledge/`.

| Skill | Mode | Use when | Points at |
|---|---|---|---|
| `planning` | before consult | A project is new or has no `a11y-spec.md`; fills the spec from the template | `templates/a11y-spec.md` |
| `consult` | consult | Any new feature or component, and whenever scope changes; may answer build less or build nothing | `patterns/`, `ux/`, `coga/`, `wcag/` |
| `wcag` | build | Any change touching structure, forms, focus, names and roles, color, media, or motion | `wcag/`, every A and AA criterion |
| `content` | build | Writing or reviewing words: body text, headings, links, alt text, instructions, errors, language | `content/`, `docs/content-standards.md` |
| `design` | build | Color and contrast, focus indicators, target size, motion, reflow, text spacing, above the floor | `design/`, `wcag/` |
| `at-test-protocol` | verify | Writing the test script a person follows with the spec's assistive technology | `testing/` |

---

*Last updated: 2026-10-23*
