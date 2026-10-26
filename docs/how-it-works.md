# How Doctor Accessible is put together

A full description of the system for people and for AI tools that need to understand it: what it is for, the parts, how a request flows through them, the rules that govern every part, how it is measured, what it can and cannot do, and how to extend it. The short version is `docs/TLDR.md`; the questions people ask first are in `docs/FAQ.md`.

If you are an AI tool reading this repo, start with `CLAUDE.md` (the operating rules), then `knowledge/INDEX.md` (the table of contents), then the skill you need. Never state a criterion, level, or threshold that is not in an entry you have opened.

## 1. Purpose and position

Doctor Accessible is an accessibility-first development assistant for Claude Code. It helps a developer build web content that meets WCAG 2.2 Level AA and is honest about what it cannot judge. It is built by Derek Jackson's team at Harvard, in public, from scratch, with nothing imported from other projects.

It is an assistant, not an authority. It never certifies conformance. Every finding is reviewed by a person; every page is tested by a person with assistive technology before it ships. The tooling produces findings, options, need statements, and test scripts. People make the decisions and run the tests.

Three constraints shape every design choice:

- The conformance target is WCAG 2.2 Level AA (W3C Recommendation, 12 December 2024). Harvard's policy names 2.1 AA; 2.2 AA satisfies it.
- axe is the only automated scanner, and it is run with the WCAG 2.2 tags because its default run skips those rules.
- Plain HTML, CSS, and JavaScript are the reference stack. Frameworks are layers over it, never replacements.

## 2. The parts

There are no services, no database, and no build step. Doctor Accessible is a directory of Markdown files that Claude Code reads, plus three small Python tools and one shell script. The parts, in the order a session meets them:

### 2.1 `CLAUDE.md`

The operating rules. Claude Code reads it at launch in any folder that holds it. It states the mission, the sixteen principles in short form, the three modes, the architecture, the conventions, the common commands, what does not belong in the repo, and two registries: one agent and eight skills. Everything else in the repo is reachable from it.

### 2.2 The spec: `a11y-spec.md`

One per project, copied from `templates/a11y-spec.md` into the project root. It is the project's own requirements: conformance target, who the project serves, the assistive technology and browser pairs the team tests with, the design system, content standards and overrides, one need statement per feature, pattern decisions, banned patterns, open manual tests, and a change log. Every mode reads it before acting and writes decisions back to it. Build does not start on a feature without a need statement in it (principle 14). WCAG is the floor; the spec is the project.

### 2.3 Skills: `.claude/skills/*/SKILL.md`

A skill is a short procedure plus a map. It loads in the main Claude Code session and keeps the conversation. It says when it applies, what the rules are for citing and judging, and which knowledge entry answers which question. A skill holds no facts; each stays under about 120 lines, and depth lives in the library (principle 10). Eight exist:

| Skill | Mode | What it does |
|---|---|---|
| `planning` | before consult | Walks a new project through filling the spec, then points to consult |
| `consult` | consult | Asks who, what is the smallest thing, then how; may answer build less or build nothing; proposes the need statement |
| `wcag` | build | Applies WCAG 2.2 AA to structure, forms, focus, names and roles, color, media, motion; maps every topic to an entry |
| `html-patterns` | build | Native HTML first for forms, tables, landmarks, headings, images, links, buttons, dialogs, custom controls; ARIA only from the aria entries |
| `react-jsx` | build | How React writes the native patterns; defects React causes on its own |
| `content` | build | The writing mode: plain language, reading level, headings, links, alt text, instructions, errors, language |
| `design` | build | Visual judgment above the floor: contrast, focus indicators, target size, motion, reflow, text spacing, with Requirement kept apart from Practice |
| `at-test-protocol` | verify | Writes the numbered test script a person follows with the spec's assistive technology |

A skill is the right shape when the task needs the conversation. An agent is the right shape when it must not have it (principle 1).

### 2.4 The verifier: `.claude/agents/verifier.md`

The one agent. An isolated subagent that checks code against WCAG 2.2 AA without seeing the builder's reasoning. Its tools are Read, Grep, Glob, Bash, and PowerShell on Windows; it has no web access, by design, so it can cite only what is in the library. It reads the spec first, inventories what it was given, runs axe with the WCAG 2.2 tags when a page is available and reads all four result buckets, reads the code in full, opens the entry for every criterion it cites, checks the words against the content standards, and reports in a fixed shape: Checked, Findings in three confidence tiers, Content, Spec deviations, Manual checks remaining, Automated scan. It reports; it never fixes. It never speaks as a user. It never states a number that is not in an opened entry or computed from the code with the computation shown. Its rules were tightened from the first eleven eval runs and re-measured.

A written review (roadmap 5.2) concluded that no second agent is needed under principle 1's four conditions.

### 2.5 The knowledge library: `knowledge/`

The thing that gets maintained. Markdown entries, one per success criterion or topic, each with its source, tier, version or date, and the date someone verified it against the live source. `knowledge/INDEX.md` is the table of contents every skill points at. `knowledge/SOURCES.md` is the list of sources the library may draw on, by tier; nothing off it is authoritative, and adding to it is a pull request with a reason. Ten domains:

| Domain | Entries | Tier | What it holds |
|---|---|---|---|
| `wcag/` | 55 | 1 and 2 | Every Level A and AA criterion: normative text quoted once, what it requires in our words, how it fails in code with confidence per pattern, how to meet it by technique ID, related criteria, what axe can and cannot catch |
| `aria/` | 3 foundation plus 8 pattern entries in `aria/patterns/` | 1, 2, 3 | When to use ARIA at all, what each element allows, how a name is computed, and tested ARIA per interface pattern |
| `html/` | 9 | 1, 2 | The native way to build each common thing, what it gives by default, where people go wrong, when ARIA is needed |
| `patterns/` | 9 | 2, 3 | Nine interface patterns: the need, the simpler thing and its cost, what doing it right requires, what practitioners found when they tested it, criteria touched, manual tests |
| `ux/` | 6 | 3 | Usability research on when a pattern serves people (carousels, modals, infinite scroll) and need-finding (who uses a thing, writing a need statement, personas from research) |
| `coga/` | 8 | 2 | One entry per objective of W3C's Making Content Usable for People with Cognitive and Learning Disabilities |
| `design/` | 6 | 1, 2, 3 | Contrast, focus indicators, target size, motion, reflow, text spacing, Requirement and Practice kept apart |
| `content/` | 8 | 2, 3 | The reasoning behind each house content standard and how to check it |
| `testing/` | 6 | 3 | Manual test procedures: keyboard only, screen readers on Windows and Apple platforms, zoom, reduced motion, forced colors |
| `frameworks/` | 1 | 3 | How React writes the native patterns |

The tiers are the spine of the system. Tier 1 is normative text and settles what a requirement is. Tier 2 is the standards body explaining the standard. Tier 3 is named practitioners and usability research, admitted under a rule and never the sole source for what a requirement is. Anything outside `wcag/` is tier 2 or 3, so a finding that rests on it alone is likely or manual review, never definite. When sources conflict, the entry names the conflict, cites both, and takes the stricter reading (principle 13).

### 2.6 Evals: `evals/`

Forty-two evals, each a folder with an answer key. Page evals hold an `input.html` with exactly one planted defect, kept otherwise clean so false positives show, and an `expected.md` naming the finding a correct verifier must produce, what is also acceptable, and what it must not report. Transcript evals hold a `request.md` (a developer's request plus spec context) or a `text.md`, and an `expected.md` describing what a good skill answer contains. Spec-aware evals ship an `a11y-spec.md` beside the page and expect a spec-deviation finding. `evals/RESULTS.md` records every run: date, eval, tool, versions, result, notes, who. Full reports sit beside each eval as `run-*.md`.

Any change to an agent, a skill, or an entry runs the relevant evals before it merges (principle 9). No eval, no merge.

### 2.7 Tools: `tools/` and `evals/run.sh`

- `tools/axe.py` runs axe with the WCAG 2.2 tags, saves the raw JSON outside the repo, prints every result bucket, and handles the ChromeDriver path problem on Windows.
- `tools/readability.py` computes Flesch-Kincaid Grade Level over the main content of a page, saying what it excluded; a signal, never a verdict.
- `tools/build_axe_rules.py` rebuilds `knowledge/axe-rules.md`, the map from axe rule IDs to criteria and entries.
- `tools/check_links.py` checks every link and every repo path named in the library.
- `evals/run.sh` runs every page eval, every skill eval, or both, headless, one fresh `claude -p` session per eval, so no run sees another's answer and no session can write.
- `evals/check.py` grades the reports: the criterion, level, tier, and confidence of the first finding mechanically; the must-not list and pass condition by a fresh judge session with no tools, quoting the report line behind each failure.

All Python is standard library. axe needs Node.js.

### 2.8 Documents: `docs/`

`principles.md` holds the sixteen principles with their reasons. `content-standards.md` holds the house defaults for words, which the spec imports. `decisions.md` is a dated log of why things are the way they are; old entries are never rewritten. `ROADMAP.md` holds phases and work packages. `how-we-work.md` is for contributors new to GitHub or Claude Code. `CONTRIBUTING.md` at the root is the merge procedure.

## 3. How a request flows

### 3.1 Starting a project

A developer copies the files in (section 6), runs `claude`, and types `/planning`. The skill walks them through the spec: conformance target, who the project serves in their own situations including people using assistive technology, the assistive technology and browser pairs the team will test with, content standards and any overrides, and when consult, verify, and human testing happen. It ends by pointing to consult for the first feature.

### 3.2 Consult

The developer types `/consult` and describes a feature. The skill reads the spec. It asks, in order, and does not move on until each is answered: who is this for and what are they trying to do; what is the smallest thing that meets that need; only then, how. It asks the developer rather than answering for them; if they cannot say who, the finding is that the feature is not ready. For every interactive pattern named, it opens the `patterns/` entry and the `ux/` entry, names the simpler alternative and what is lost, and pulls the criteria the chosen thing touches from the index, citing each from its entry. It lays out options with costs, names the manual tests from the spec's assistive technology list, and proposes a need statement in the template's format. It writes into the spec only when the developer agrees (principle 8). "Build less" and "build nothing" are written as need statements too, so the request does not return unexamined. It writes no code.

### 3.3 Build

The developer writes code and words in the main session, loading skills as the work demands. Each skill routes a question to an entry; the entry carries the requirement, the native-first way to meet it, the failure patterns, and the techniques by ID. Words get the same treatment as code: the content skill applies the house standards and measures reading level as a signal. When scope changes or a new component appears, build stops and returns to consult.

### 3.4 Verify

The developer asks for the verifier on a page or file. It runs in isolation, follows the process in section 2.4, and returns the report. The developer reads it, opens the cited entries where they disagree, fixes what they decide to fix, and runs it again. Then `/at-test-protocol` writes the human test script for the component from the spec's assistive technology list: what to do and what to record, per technology. A person runs it. The results go into the spec's open manual tests and change log.

### 3.5 What never happens

The system never simulates a user with a disability or says what a screen reader would announce. It never cites a criterion, level, or threshold from memory. It never silently rewrites the developer's code. It never treats a clean axe run as a pass. It never writes to the spec without agreement. It never reports a non-WCAG finding as definite.

## 4. The rules that govern every part

The sixteen principles in `docs/principles.md` are the rules in force; `CLAUDE.md` carries the short form. The ones that shape behavior most:

- **Knowledge base first, sources list second, nothing third.** No entry means "no entry yet", research only from the sources list, and the entry is written before it is used.
- **Cite or stay quiet.** Tier, source, and version on every claim. Nothing from memory, including numbers.
- **Native HTML first.** ARIA only when no native element does the job.
- **Honest confidence.** Definite, likely, or manual review. One finding per defect.
- **Humans do the final test.** Produce the protocol; name what remains.
- **The developer stays in charge.** Advise, verify, brainstorm. Never silently rewrite.
- **Measure every change.** No eval, no merge.
- **Start from the need.** No need statement, no build.
- **Conservative when sources conflict.** Name it, cite both, take the stricter reading.

## 5. How it is measured

Every eval has an answer key written from the entry it tests, not from memory. A run is recorded whether it passes or fails; the results table holds first-run failures and their re-runs. The verifier's own rules were changed from what the runs showed: the numbers rule, the axe tags, the ban on announce predictions, and scratch files outside the repo each came from a recorded observation and were re-measured after the change. The headless runner and the checker make a full pass possible without a person comparing reports by hand; the baseline of 2026-10-23 recorded 30 of 30 page evals passing, and skill evals are run with variance checks. The link checker confirms every path and link in the library resolves.

## 6. Getting it into a project

The decision (roadmap 1.7, `docs/decisions.md`, 2026-10-23) is a Claude Code plugin, `doctor-accessible`, which will install the skills, the verifier, the library, and the tools with one command and update when they change. Until it ships, copy by hand into the project root, keeping folder names: `.claude/`, `knowledge/`, `tools/`, `docs/content-standards.md`, `docs/principles.md`, `templates/a11y-spec.md`, and a second copy of the template at the root as `a11y-spec.md`. A copy does not update itself; when the repo changes, copy `knowledge/`, `.claude/`, and `tools/` again.

## 7. What it can do, and what it cannot

It can: pause a build to ask who it is for; argue for a list over a carousel with sources; map any accessibility question to a cited entry; check a page against every Level A and AA criterion with honest confidence; run axe correctly; measure reading level; write a human test script; keep a project's accessibility decisions in one spec; and show, with evals, whether a change to itself helped.

It cannot: test with a screen reader; judge whether a page serves a person; see content a script adds at run time unless given the rendered page; know a framework it has no entry for; replace an audit; or make a decision. Where a judgment is needed it says so and hands it to a person.

## 8. Extending it

- **An entry.** Start from the domain's `_template.md`. Write in your own words from a source on the list. Quote only tier 1 text. Cite tier and date on every claim. Record the date you verified the live page. Add the row to `knowledge/INDEX.md` in the same commit.
- **A skill.** Start from `.claude/skills/wcag/SKILL.md`. Under about 120 lines. A map, not a lecture. Write its evals first, from entries. Add it to the Skill Registry in `CLAUDE.md`.
- **An eval.** Next free number, `NNN-slug`. One defect. Answer key from the entry. Run it, record it.
- **A source.** Pull request to `knowledge/SOURCES.md` with a reason. Tier 3 must pass the admission rule: real name, dated, cites or cited by tier 1 or 2, checkable claims, maintained.
- **An agent.** Only with a written case under principle 1 recorded in `docs/decisions.md` first.

Work is claimed by work package from the roadmap, one issue each. Check the issue's owner and the recent pull requests before starting; the team moves quickly.

## 9. What is next

Roadmap Phase 5: the plugin (5.4), a v1.0 tag (5.3), and four new domains named so they are visible: mobile and touch, localization and language, document formats, and CMS layers (5.6 to 5.9). The thing not yet done that would teach the most is a real project through consult, build, and verify end to end.

## 10. Glossary

- **WCAG.** Web Content Accessibility Guidelines, the W3C standard. Version 2.2, Level AA is the target.
- **Success criterion (SC).** One testable rule in WCAG. 55 at Levels A and AA.
- **Tier.** How much authority a source has: 1 normative, 2 informative from the standards body, 3 practitioner.
- **Spec.** `a11y-spec.md`, the project's own accessibility requirements and decisions.
- **Need statement.** Who a feature is for, what they are trying to do, what will be built, instead of what, why, and the manual tests owed.
- **Skill.** A short procedure Claude Code loads in the main session.
- **Agent.** A separate Claude with its own instructions and no memory of the conversation. There is one.
- **Eval.** A known-defect page or request with an answer key, used to measure a change.
- **axe.** The automated scanner. Run with WCAG 2.2 tags. Finds a minority of defects.
- **Assistive technology (AT).** Screen readers, magnifiers, switch devices, voice control.
