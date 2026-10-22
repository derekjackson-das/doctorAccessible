# CLAUDE.md — doctorAccessible

This file provides guidance to Claude Code when working with code in this repository.

**Mission:** An accessibility-first development assistant for Claude Code: one working session that loads knowledge on demand, one isolated verifier agent, and a Markdown knowledge library, built and shared by a team through GitHub.

---

## Before making any changes

Investigating, reading, searching, and answering questions never need approval. Creating, editing, deleting, or moving files does, every time, until Derek says go. Propose what will change and why, then wait. Approval for one step is not approval for the next.

---

## Tone

Big Claude, as defined in the CCode root `CLAUDE.md`. Dry, matter-of-fact, business first.

---

## Project Overview

Derek's team at Harvard builds and reviews web content that must meet WCAG 2.2 Level AA. This repo is the tooling that makes Claude Code good at that job, and it is built from scratch. Nothing is imported from other CCode projects, from the `ventz` agent, or from the DAARA Knowledge Library. The repo is public, so every knowledge entry is written in our own words from the source, with the source linked, never pasted.

Constraints that shape decisions:

- Conformance target is WCAG 2.2 AA. Harvard policy names 2.1 AA; 2.2 AA satisfies it.
- axe is the only automated scanner. Never propose Lighthouse.
- Reference stack is plain HTML, CSS, and JS. Framework-specific guidance is a later layer, not the base.
- Real users with assistive technology are not simulated. The tooling produces test protocols for humans; it does not pretend to be them.

---

## Architecture

### The builder (the main session)
The Claude Code session you are in. It writes code and content, loads skills as the task demands, and dispatches the verifier. There is no director agent. The human directs; the main session coordinates.

### The verifier (`.claude/agents/verifier.md`)
An isolated subagent that checks code against WCAG 2.2 AA without seeing the builder's reasoning. It reads the code fresh, runs axe when a page is available, and reports findings in three confidence tiers. It does not fix code.

### Skills (`.claude/skills/*/SKILL.md`)
Short procedures plus a map into the knowledge library. A skill tells the agent when a domain applies, what the rules are for citing and judging, and which knowledge file answers which question. Skills hold no reference material themselves.

### Knowledge library (`knowledge/`)
Markdown entries, one per success criterion or topic, each with the source, its tier, its version, and the date it was verified. This is the thing that gets maintained. `knowledge/INDEX.md` is the table of contents the skills point at.

### Evals (`evals/`)
Snippets with known defects and the findings a correct verifier must produce. Any pull request that changes an agent, a skill, or a knowledge entry runs the evals first.

### The rule for agent versus skill
If the work needs to remember the conversation, it is a skill. If the work needs to forget it, it is an agent. An agent earns its isolation only when the verdict must not be contaminated by the builder's reasoning, when tool output would flood the main context, when the task runs in parallel, or when it needs a different model or permission set.

---

## Stack

- **Language(s):** HTML, CSS, JavaScript as the reference target. Markdown for everything the agents read.
- **Framework(s):** none.
- **Key libraries:** axe-core, via the CLI, when a page can be loaded. Not yet installed.
- **Runtime / deployment target:** Claude Code, cloned from GitHub. Project-level `.claude/` makes the agent and skills available on clone.

---

## Project Structure

```
doctorAccessible/
├── CLAUDE.md
├── README.md
├── .claude/
│   ├── agents/verifier.md      # the one isolated agent
│   └── skills/wcag/SKILL.md    # one folder per knowledge domain
├── knowledge/
│   ├── README.md               # how to write an entry
│   ├── INDEX.md                # table of contents the skills point at
│   └── wcag/                   # sc-x.x.x-slug.md, one per success criterion
├── evals/
│   ├── README.md
│   └── 001-missing-label/      # input.html + expected.md
└── docs/
    └── decisions.md            # why things are the way they are
```

---

## Conventions

- Knowledge entries are named `sc-<number>-<slug>.md` under `knowledge/wcag/`, and `<slug>.md` under other domains.
- Every substantive claim carries its tier (1 normative, 2 informative, 3 practitioner), its source, and the version or date. Example: `WCAG 2.2 SC 4.1.2 (Level A), W3C Rec 12 Dec 2024, tier 1`.
- No agent or skill states a success criterion number or level from memory. It opens the entry.
- Markdown, not JSON. Nothing here has a machine consumer that needs JSON.
- Evals are numbered `NNN-slug` and hold exactly one intended defect each unless the README of that eval says otherwise.
- A `SKILL.md` stays under about 120 lines. Depth goes in `knowledge/`.
- Working drafts (WCAG 3.0, APCA) are awareness only, never a requirement.

---

## Common Commands

```
# Run the verifier on an eval by hand (from a Claude Code session)
Use the verifier agent on evals/001-missing-label/input.html and compare to expected.md

# axe (once installed)
npx @axe-core/cli <url-or-file>
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

*Last updated: 2026-10-22*
