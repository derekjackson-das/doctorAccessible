# Roadmap

Phases, work packages, and how the team divides the work. Updated 2026-10-22 (design moment, project spec, sources list, and content standards added).

Work is claimed by work package, not by phase. Each package becomes one GitHub issue carrying the six fields below, and a person claims the issue. Packages inside a phase are designed not to touch each other's files, so they can run in parallel.

## Phases

| Phase | Name | Goal | Done when |
|---|---|---|---|
| 0 | Foundation | One agent, one skill, one entry, one eval | Done 2026-10-22 |
| 1 | Team setup | Repo live, contribution rules, pattern proven | Public repo, PR template, axe installed, eval 001 passes |
| 2 | WCAG library | Every Level A and AA criterion has a verified entry | 55 entries in the index with source, tier, version, verified date |
| 3 | Domain skills | The procedures that use the library | consult, patterns, content, html-patterns, design, at-test-protocol, aria, ux, each with evals |
| 4 | Eval automation | Changes are measurable | Evals run headless and their results appear in every PR |
| 5 | Expansion | Layers on top of the base | Framework skills, ARIA pattern entries, v1.0 |

## Work package format

Every issue has these six fields. Keep them short.

- **Goal.** One sentence.
- **Deliverables.** The files that will exist when it is done.
- **Done when.** A check someone else can run.
- **Depends on.** Package IDs, or none.
- **Size.** S (an afternoon), M (a few days), L (a couple of weeks part-time).
- **Owner.** Blank until claimed.

## Phase 1: Team setup

ID 1.5 is unused. It was a listing in Derek's private workspace, which is not the team's concern.

| ID | Goal | Deliverables | Done when | Depends on | Size |
|---|---|---|---|---|---|
| 1.1 | Public repo on GitHub | Repo `doctorAccessible`, `main` pushed, branch protection requiring a PR | Teammates can clone | none | S |
| 1.2 | Contribution rules | `CONTRIBUTING.md`, PR template with an "evals run" section, issue template with the six fields | A test PR shows the template | 1.1 | S |
| 1.3 | axe available | `@axe-core/cli` runs via `npx` against `evals/001-missing-label/input.html` | Raw axe output captured in the issue | none | S |
| 1.4 | Prove the pattern | Verifier run on eval 001, result recorded in `evals/RESULTS.md` | Finding matches `expected.md`; nothing from "must not" appears | 1.3 | S |
| 1.6 | Onboarding | Each teammate clones, runs `claude`, runs eval 001 | Each person has a recorded run | 1.4 | S |
| 1.7 | Distribution decision | A written choice between packaging this repo as a Claude Code plugin a developer installs into their project, or copying `.claude/` and `templates/a11y-spec.md` by hand; recorded in `docs/decisions.md` | Decision recorded and one developer project set up the chosen way | 1.1 | S |

## Phase 2: WCAG library

Fifty-five Level A and AA criteria, split by principle so four people never edit the same file. Each package also writes one eval per guideline in its scope, from the entries, not from memory. Verify the criterion list against the W3C quick reference when you claim a package; the lists below were compiled by hand on 2026-10-22.

| ID | Goal | Scope | Entries | Evals | Depends on | Size |
|---|---|---|---|---|---|---|
| 2.1 | Perceivable | Guidelines 1.1 to 1.4, A and AA | 20 | 4 | none | L |
| 2.2 | Operable | Guidelines 2.1 to 2.5, A and AA | 20 | 5 | none | L |
| 2.3 | Understandable | Guidelines 3.1 to 3.3, A and AA | 13 | 3 | none | M |
| 2.4 | Robust | Guideline 4.1, A and AA | 1 remaining | 1 | none | S |
| 2.5 | Index and skill map kept current | `knowledge/INDEX.md` and the "where to look" table in `.claude/skills/wcag/SKILL.md` updated as entries land | ongoing | none | 2.1 to 2.4 | S |
| 2.6 | Sources list kept current | `knowledge/SOURCES.md`: tier 1 and 2 entries verified against the live pages, tier 3 proposals confirmed or removed by the team, quarterly re-verification | Every row has a verified date; no row says "proposed" | none | S |

Robust is small. Whoever takes 2.4 also takes a phase 3 package.

**2.1 Perceivable:** 1.1.1 Non-text Content (A); 1.2.1 Audio-only and Video-only, Prerecorded (A); 1.2.2 Captions, Prerecorded (A); 1.2.3 Audio Description or Media Alternative, Prerecorded (A); 1.2.4 Captions, Live (AA); 1.2.5 Audio Description, Prerecorded (AA); 1.3.1 Info and Relationships (A); 1.3.2 Meaningful Sequence (A); 1.3.3 Sensory Characteristics (A); 1.3.4 Orientation (AA); 1.3.5 Identify Input Purpose (AA); 1.4.1 Use of Color (A); 1.4.2 Audio Control (A); 1.4.3 Contrast, Minimum (AA); 1.4.4 Resize Text (AA); 1.4.5 Images of Text (AA); 1.4.10 Reflow (AA); 1.4.11 Non-text Contrast (AA); 1.4.12 Text Spacing (AA); 1.4.13 Content on Hover or Focus (AA).

**2.2 Operable:** 2.1.1 Keyboard (A); 2.1.2 No Keyboard Trap (A); 2.1.4 Character Key Shortcuts (A); 2.2.1 Timing Adjustable (A); 2.2.2 Pause, Stop, Hide (A); 2.3.1 Three Flashes or Below Threshold (A); 2.4.1 Bypass Blocks (A); 2.4.2 Page Titled (A); 2.4.3 Focus Order (A); 2.4.4 Link Purpose, In Context (A); 2.4.5 Multiple Ways (AA); 2.4.6 Headings and Labels (AA); 2.4.7 Focus Visible (AA); 2.4.11 Focus Not Obscured, Minimum (AA); 2.5.1 Pointer Gestures (A); 2.5.2 Pointer Cancellation (A); 2.5.3 Label in Name (A); 2.5.4 Motion Actuation (A); 2.5.7 Dragging Movements (AA); 2.5.8 Target Size, Minimum (AA).

**2.3 Understandable:** 3.1.1 Language of Page (A); 3.1.2 Language of Parts (AA); 3.2.1 On Focus (A); 3.2.2 On Input (A); 3.2.3 Consistent Navigation (AA); 3.2.4 Consistent Identification (AA); 3.2.6 Consistent Help (A); 3.3.1 Error Identification (A); 3.3.2 Labels or Instructions (A); 3.3.3 Error Suggestion (AA); 3.3.4 Error Prevention, Legal, Financial, Data (AA); 3.3.7 Redundant Entry (A); 3.3.8 Accessible Authentication, Minimum (AA).

**2.4 Robust:** 4.1.2 Name, Role, Value (A), done; 4.1.3 Status Messages (AA).

Done when, for every package: each entry follows `knowledge/wcag/_template.md`, quotes the normative text verbatim with a verified date, lists techniques by ID from the Understanding page, and is in `INDEX.md`; each eval has an `input.html` with one intended defect and an `expected.md` written from the entry.

## Phase 3: Domain skills

Each skill is a `SKILL.md` under about 120 lines, the knowledge entries it points at, and at least two evals. 3.1 comes first because it is the mode a developer meets first, and 3.2 feeds it.

| ID | Goal | Deliverables | Done when | Depends on | Size |
|---|---|---|---|---|---|
| 3.1 | `consult` skill: the pause before building | `.claude/skills/consult/SKILL.md`. A procedure that asks, in order: who is this for and what are they trying to do; what is the smallest thing that meets it, with "build less" and "build nothing" as valid answers; only then how. Challenges every named pattern against `knowledge/patterns/`. Pulls applicable criteria from the index, offers options with trade-offs, names manual tests, and writes a need statement into the project's `a11y-spec.md` in the template's format | Three transcript evals: a described feature in, expected need statement, criteria, options, and manual tests out; at least one eval where the right answer is "build less" | 3.2 for pattern entries; can start with what exists | M |
| 3.2 | `patterns` knowledge domain | `knowledge/patterns/`, one entry each for carousel, modal dialog, accordion, tabs, tooltip, infinite scroll, autocomplete, drag and drop, date picker. Each entry: the need the pattern usually serves, the simpler pattern that often serves it better and what is lost, what the pattern costs to do right with the ARIA Authoring Practices link marked as a pattern not a requirement, the criteria it touches, and the manual tests it demands | Nine entries in `INDEX.md`; each cites tier 2 and tier 3 sources by name | 2.x for criteria to point at | M |
| 3.3 | `content` skill: the writing mode | `SKILL.md` that reads the spec's content section and applies `docs/content-standards.md` while writing; measures reading level before handing text back; entries under `knowledge/content/` for plain language, reading level, organization, headings, link text, alt text, error messages, language | Four evals pass, text in and findings out: a paragraph above the reading-level target, a heading that says "Overview", a link that says "click here", an alt text that starts with "image of" | 2.1, 2.3 | L |
| 3.4 | `html-patterns` skill | `SKILL.md`; entries under `knowledge/html/` for forms, tables, landmarks, headings, images, links, buttons, dialogs and custom controls | Two evals pass | 2.1, 2.2 | L |
| 3.5 | `design` skill | `SKILL.md`; entries under `knowledge/design/` for contrast, focus indicators, target size, motion, reflow, text spacing | Two evals pass | 2.1, 2.2 | M |
| 3.6 | `at-test-protocol` skill: the human testing mode | `SKILL.md`; produces a test script for a component covering keyboard only, screen reader on two platforms, 200% and 400% zoom, reduced motion, forced colors; reads the spec for which assistive technology the project tests with; entries under `knowledge/testing/` | Two evals: a component in, expected protocol items out | 2.x | M |
| 3.7 | `planning` skill, optional | `SKILL.md`; an accessibility checklist across a project lifecycle | One eval | 3.1 | S |
| 3.8 | `aria` knowledge domain | `knowledge/aria/` entries: the rules for using ARIA at all (from W3C's Using ARIA, tier 2), role and attribute allowances per element (ARIA in HTML, tier 1), name computation (AccName, tier 1), and the Authoring Practices patterns marked as patterns not requirements, each with practitioner test results from tier 3 where they exist | Index updated; one eval per pattern claimed; the `patterns` entries in 3.2 link here | 2.x, 3.2 | L |
| 3.9 | `ux` knowledge domain | `knowledge/ux/` entries feeding consult: usability heuristics and research on when a pattern serves a person and when it does not (Nielsen Norman Group and tier 3 practitioners), summarized and linked, never pasted | Consult evals in 3.1 cite at least one `ux` entry in a "build less" answer | 3.1 | M |

## Phase 4: Eval automation

| ID | Goal | Deliverables | Done when | Depends on | Size |
|---|---|---|---|---|---|
| 4.1 | axe wired into the verifier | Verifier runs axe on any eval with a page and captures raw output in its report | Shown on three evals | 1.3 | S |
| 4.2 | axe rule mapping | `knowledge/axe-rules.md`: rule ID to knowledge entry, tier 3, with the Deque rule description linked | Every rule that fires on an eval maps to an entry | 2.x | M |
| 4.3 | Headless eval runner | `evals/run.sh` using `claude -p` to run the verifier on every eval and write one report per eval | A person can read the reports against `expected.md` in one sitting | 1.4 | M |
| 4.4 | Checker | A script that compares a report to `expected.md` for criterion, level, tier, and the must-not list | Pass or fail per eval, no human in the loop | 4.3 | M |
| 4.5 | CI, optional | GitHub Action running 4.4 on PRs | Results on a PR | 4.4 and an API key policy | M |
| 4.6 | Spec-aware evals | Evals that ship an `a11y-spec.md` beside `input.html` and expect a spec deviation finding: a banned pattern used, a pattern decision ignored, a need statement the page does not serve | Three evals pass; 4.4 checks the spec deviation section | 4.4 | M |
| 4.7 | Readability tool | `tools/readability.py`: Flesch-Kincaid Grade Level over the main content of an HTML file, excluding navigation, headings, and code; used by the `content` skill and the verifier | Agrees with a hand count on three samples; the verifier's Content section reports a number | 3.3 | S |

## Phase 5: Expansion

| ID | Goal | Deliverables | Done when | Depends on | Size |
|---|---|---|---|---|---|
| 5.1 | Framework layer | `.claude/skills/react-jsx/SKILL.md` as a layer referencing `html-patterns`, never replacing it | Two evals | 3.2 | M |
| 5.2 | Second agent review | A written assessment of logged verifier failures against the four conditions in principle 1 | Decision recorded in `decisions.md` | 4.4 | S |
| 5.3 | v1.0 | Onboarding doc, CCode listing updated, tag `v1.0` | Tagged | all | S |
| 5.4 | Plugin packaging, if 1.7 chose it | Plugin manifest; install into a fresh project yields the agent, the skills, and the spec template | One developer project installed from the plugin | 1.7, 3.x | M |

## Governance

- Entries re-verify when W3C publishes a revision of WCAG 2.2, and quarterly otherwise. The `Verified` column in `INDEX.md` is the record.
- A PR touching `.claude/` or `knowledge/` states which evals ran and what they produced.
- Only one agent exists until 5.2 proves a second is needed under principle 1.
- Nothing off `knowledge/SOURCES.md` is authoritative. Adding a source is a pull request with a reason.
- Build does not start on a feature without a need statement in the project's `a11y-spec.md` (principle 14). The spec is the project's own requirements; every mode reads it first (principle 15).
- The general CCode knowledge base and DAARA stay separate from this repo in both directions.
- Decisions go in `decisions.md`, dated. Old entries are not rewritten.

## Suggested split for four people

| Person | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| A (Derek) | 1.1, 1.2, 1.7 | 2.4, 2.5, 2.6 | 3.1, 3.2, 3.9 |
| B | 1.3, 1.4 | 2.1 | 3.5, 3.8 |
| C | 1.6 | 2.2 | 3.4 |
| D | | 2.3 | 3.3, 3.6 |

Fewer people: packages stack in ID order. More people: split 2.1 and 2.2 by guideline, and 3.2 by pattern.
