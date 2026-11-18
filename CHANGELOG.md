# Changelog

Notable changes to Doctor Accessible, one section per release, newest first. Versions stay below 1.0 while the repo is a prototype (`docs/decisions.md`, 2026-11-18). Every release is a GitHub pre-release.

> **Doctor Accessible is a demo and prototype.** It is shared so others can see how it was built and learn from it. Do not use it on live code or in real development work.

## Unreleased

Nothing yet.

## 0.1.0 (2026-11-18)

The first numbered release: the repo as it stands on this date.

### The tool

- **Three modes in one session:** consult, build, and verify, with the project's `a11y-spec.md` read before any mode acts (`CLAUDE.md`, `templates/a11y-spec.md`).
- **One agent:** the verifier, which checks code against WCAG 2.2 AA without seeing the builder's reasoning, runs axe when a page is available, and reports in three confidence tiers (`.claude/agents/verifier.md`).
- **Eight skills:** `planning`, `consult`, `wcag`, `content`, `design`, `html-patterns`, `react-jsx`, and `at-test-protocol`. The last writes a test script, or a checklist with expected outcomes for one component or a whole page (`templates/at-test-checklist.md`).

### The knowledge library

- **WCAG:** an entry for each of the 55 Level A and AA success criteria in WCAG 2.2.
- **Nine more domains:** HTML, ARIA, interface patterns, UX, cognitive accessibility, design, content, testing, and a React layer over HTML.
- **Sources:** every entry cites its source, tier, version, and the date it was checked. Only sources on `knowledge/SOURCES.md` count.
- **axe rules:** each axe rule mapped to its criterion and entry (`knowledge/axe-rules.md`).

### Evals and tools

- **44 evals:** page evals for the verifier, transcript evals for the skills, and spec-deviation evals, each with the answer a correct run must give.
- **Headless runner and grader:** `evals/run.sh` runs each eval in a fresh session, and `evals/check.py` grades the reports. Results are kept in `evals/RESULTS.md`.
- **Tools:** axe with the WCAG 2.2 tags (`tools/axe.py`), reading level (`tools/readability.py`), a link and path checker, and an interim installer that copies the library into a project (`tools/install.py`).

### Not in this release

- The Claude Code plugin (roadmap 5.4).
- The beyond-WCAG packages: mobile, localization, documents, and CMS (roadmap 5.6 to 5.9).
- Manual tests with assistive technology users. The tool writes test protocols; it does not stand in for testers.
