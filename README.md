# doctorAccessible

An accessibility-first development assistant for Claude Code. One working session that loads knowledge on demand, one isolated verifier agent, and a Markdown knowledge library, built and shared by a team through GitHub.

Conformance target: WCAG 2.2 Level AA. Automated scanner: axe only.

## How it works

- **You work in the main Claude Code session.** It writes code and content. When a task touches accessibility, it loads the matching skill, which tells it which knowledge entry to read and how to cite it.
- **The verifier checks the result in isolation.** It never sees how the code was written. It reads fresh, runs axe when it can, and reports findings as Definite, Likely, or Manual review.
- **The knowledge library is the source of truth.** Every entry cites its source, tier, version, and verification date. No agent cites a success criterion from memory.
- **Evals keep changes honest.** Known-defect snippets with expected findings. Change a prompt, run the evals.

## Where things live

| Path | What |
|---|---|
| `CLAUDE.md` | Rules for Claude Code in this repo. Read it first. |
| `.claude/agents/verifier.md` | The verifier agent. |
| `.claude/skills/wcag/SKILL.md` | The WCAG skill: when it applies, how to cite, where to look. |
| `knowledge/INDEX.md` | Table of contents for the library. |
| `knowledge/wcag/` | One entry per success criterion. |
| `evals/` | Known-defect snippets and the findings a correct verifier must produce. |
| `docs/decisions.md` | Why things are the way they are. |

## Using it

1. Clone the repo.
2. Open a terminal in the repo folder and run `claude`.
3. Build as usual. Type `/wcag` to load the WCAG skill by hand, or let the session pick it up.
4. Ask for the verifier when you want an independent check.

## Working on it as a team

- Knowledge entries follow `knowledge/README.md`. Source, tier, version, verified date, or it does not merge.
- A pull request that changes an agent, a skill, or a knowledge entry says which evals were run and what they produced.
- Write entries in your own words from the source. This repo is public. Link, do not paste.
- New skill? Start from `.claude/skills/wcag/SKILL.md`. Keep it short. Depth goes in `knowledge/`.

## Status

2026-10-22: initial scaffold. One agent, one skill, one knowledge entry, one eval. The pattern is in place; the library is nearly empty.
