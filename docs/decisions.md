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
## 2026-10-22: axe runs, and eval 001 has one defect

**axe is available.** `@axe-core/cli` through `npx`, no global install. The bundled ChromeDriver lagged the installed Chrome, so `browser-driver-manager` fetches a matching Chrome for Testing and driver pair into the user's home cache. Recorded in the common commands.

**Eval 001 confirmed.** axe-core 4.14.0 reports exactly one violation, the `label` rule on the search input, tagged `wcag412`. Twenty-one rules passed. The tag matches the knowledge entry for SC 4.1.2. Roadmap package 1.3 done; results live in `evals/RESULTS.md`.

## 2026-10-22: the roadmap past WCAG

**Phase 3 already reaches past WCAG.** patterns, ux, content, design, and at-test-protocol are where "build less," plain language, design judgment above the minimum, and human testing live. The question was what else belongs and where.

**Two additions to Phase 3.** `ux` (3.9) gains a need-finding set, so consult has something to stand on when it asks who a thing is for. A new `coga` domain (3.10) reads Making Content Usable, the largest body of beyond-WCAG guidance from W3C itself, already on the sources list and read by no package until now.

**Phase 5 gets a named candidates list (5.5).** Mobile and touch, localization and language, document formats, and CMS layers. Visible so the shape is known; unclaimed so nobody is committed.

**One boundary.** Anything that is not a WCAG failure or a spec deviation is reported as likely or manual review, never definite. That keeps the verifier credible when the advice is "this carousel is a bad idea" rather than "this input has no name."

## 2026-10-22: the verifier's rules tightened from eleven eval runs

**Numbers are covered by the no-memory rule.** The original rule forbade stating a criterion number, title, or level from memory. Across eleven runs the agent stated thresholds from memory three times: computed contrast ratios in pass observations twice, and flash-threshold luminance figures once, attributed to an entry that holds no such figures. The rule now covers thresholds, ratios, sizes, and rates: they come from the entry or are not stated. Computing a value from the code is allowed once the entry holding the threshold has been opened, and the report must say the value was computed and from what. Nothing may be attributed to an entry that the entry does not say.

**axe runs with the WCAG 2.2 tags, and a clean run is not a pass.** The `@axe-core/cli` default run executes no rule tagged `wcag22aa`; eval 010's target-size defect appeared in no result bucket until the rule was requested. The verifier's axe step now carries the tags flag, reads all four result buckets, treats "incomplete" as a lead, and never treats zero violations as a pass. Evals 004, 006, 008, and 009 are deliberately invisible to axe to keep this honest.

**"Expected to announce" is simulation.** The first run on eval 001 wrote what a screen reader would announce before and after the fix. The rule against simulating a user now names that pattern: write the test step and what the tester records.

**Scratch files stay out of the repo.** Agents had kept axe output and measurement scripts out of the repository only because each dispatch prompt named a temp directory. The rule is now in the agent file.

**Why now.** The most recent run before this change, eval 001 after package 2.5, showed the agent declining to cite contrast ratios without opening the entries, on its own. The behavior is reachable; the rule makes it hold. Measured by re-running evals 001, 005, 008, and 010, the four where the old behavior appeared.

## 2026-10-22: the consult skill and transcript evals

**Consult is a skill, not an agent.** It needs the conversation: the developer's request, their answers to the three questions, the spec. Principle 1 says that is a skill. It loads on demand in the main session and writes to the spec only with the developer's agreement (principle 8).

**It asks before it answers.** The skill does not fill in "who is this for" from its own imagination. If the developer cannot say, the finding is that the feature is not ready. "Build less" and "build nothing" are written as need statements too, so the record exists and the request does not return unexamined.

**No patterns or ux entries exist yet.** The skill says so each time and reasons from the WCAG entries a pattern touches, stating that basis. When packages 3.2 and 3.9 land, the skill's map points at them without other change.

**Transcript evals are a new eval shape.** A `request.md` in place of `input.html`, with the answer key describing what a good consult answer contains. The first three cover a build-less case (a carousel that should be a list), an already-met case (a skip link that exists), and a full consult (a registration form). Until Phase 4 automates them, they run in a fresh session or, as a stand-in, in a general-purpose agent carrying the skill's text, and the record says which.

## 2026-10-23: no second agent

**The decision: the verifier stays the only agent.** Every logged verifier failure was reviewed against principle 1's four conditions. None of them would have been prevented by a second agent. Each has a cheaper remedy that is already in place or is a key owner's call. The judge inside `evals/check.py` is a fresh session too, but it is part of the eval tooling, not a mode of the product.

**What was reviewed.** About seventy verifier rows in `evals/RESULTS.md` to 2026-10-23, the run index in `evals/run-2026-10-23-all.md`, and the checker's results in `evals/check-2026-10-23.md`. Every failure or flagged observation falls into one of five kinds.

- **A miss.** Eval 031's options were chosen on `mousedown`, a definite 2.5.2 failure. Three runs did not catch it; the fourth opened the 2.5.2 entry and did. The cause was coverage on a page built to test something else, and the remedy was to fix the page and keep re-running.
- **Over-reporting.** Manual-review notes on items a key forbade: 031 and 032, then 003, 008, 010, and 034 under the checker. None got the main finding wrong. Each is a disagreement about how strict a key should be. 031 and 032 were amended; the other four are for their owners.
- **Underclaiming.** Eval 012 graded likely where the key expected definite, and the key itself allows that downgrade. The remedy was in the checker, not the verifier.
- **Format gaps.** Spec deviations in 038 and 039 had no confidence label, because the verifier's output format never asked for one. Fixed in `verifier.md`.
- **Environment.** No shell on Windows, so no axe and no readability tool, in every run before WP 4.1. Fixed by adding PowerShell to the verifier's tools.

**Against the four conditions.**

1. **Contamination.** A second agent would help only if the verifier's verdict were contaminated by the builder's reasoning. It never is: the verifier already runs isolated. The misses came from coverage and the over-reporting from key strictness, and another isolated reader would share both.
2. **Tool output flooding.** axe and the readability tool run inside the verifier. `tools/axe.py` keeps raw output in a file and prints a summary, so nothing floods the main session.
3. **Parallel work.** `evals/run.sh` already runs verifier sessions in parallel. No mode of the product needs two agents at once.
4. **A different model or permission set.** The only permission gap was the shell, now closed. No failure pointed to a model that could not do the work.

**What would reopen it.**

- The same kind of miss on the same criterion recurring across runs after its entry and an eval exist.
- A domain whose checks need tools or permissions the verifier should not hold, such as the document formats in 5.5.
- Verifier reports long enough that tool output starts to crowd the main session.

Any one of these is a reason to look again, under principle 1.

## 2026-10-23: distribution: plugin or copy by hand

**The choice: a Claude Code plugin, built from this repo, is how developers get Doctor Accessible. Until the build exists (package 5.4), copy by hand is the documented interim.** The knowledge library is the thing that changes, often several entries a day. A plugin carries those changes to every project with `claude plugin update`. A copied folder freezes them on the day of the copy, and nobody re-copies.

**What was tried, 2026-10-23, Claude Code 2.1.309 on Windows.** Each route was tested on a scratch project with eval 001's page as the sample, in a fresh headless session (`claude -p`) asked to run the verifier. Tools were limited to read-only ones, so axe did not run in these trials.

- **Copy `.claude/` and the spec template only, as the issue first suggested: it does not work.** The verifier ran and found the label defect from the code alone. But `knowledge/INDEX.md` and `docs/content-standards.md` were missing, so it could cite nothing and had no thresholds. The agent and every skill name files outside `.claude/` by repo-relative path: `knowledge/`, `docs/content-standards.md`, `docs/principles.md`, `templates/a11y-spec.md`.
- **Copy `.claude/`, `knowledge/`, those two docs, and `templates/`: it works.** The finding was cited to the 4.1.2 and 1.3.1 entries, contrast was computed from the entries' thresholds, and no file was missing. The cost is about 830 KB of library inside the developer's project, frozen at the copy. Updating means copying again, and local edits get overwritten or drift.
- **A plugin: it works, with one change.** A trial plugin had `.claude-plugin/plugin.json` (name `doctor-accessible`), `agents/`, `skills/`, `knowledge/`, `docs/`, and `templates/`. It passed `claude plugin validate` and was loaded with `--plugin-dir`. The session listed `doctor-accessible:verifier` and seven skills, and the verifier cited the plugin's own knowledge entries. The project held only `a11y-spec.md` and the page. The change: inside a plugin, a path like `knowledge/INDEX.md` resolves against the developer's project, so the trial rewrote 127 path references to `${CLAUDE_PLUGIN_ROOT}/knowledge/...`. The docs say that variable is substituted inside skill and agent Markdown.

**Why not make this repo the plugin directly.** The same rewrite would break this repo's own sessions: here the skills load as project skills, where `${CLAUDE_PLUGIN_ROOT}` means nothing. So the plugin is built from the repo by a script, and the repo keeps its relative paths. That build, a marketplace entry, and an install test in a fresh project are package 5.4.

**What changes for a developer.** The names are namespaced: `/doctor-accessible:wcag`, and the agent is `doctor-accessible:verifier`. `CLAUDE.md` is not part of a plugin (the docs say a plugin's CLAUDE.md is not loaded). So the three-mode instructions a developer needs have to live in a skill, or in a short block the developer pastes into their own `CLAUDE.md`. 5.4 decides which. The spec stays a file in the developer's project, `a11y-spec.md` from the template.

**Updates, from the docs, not yet tested.** With no `version` in `plugin.json`, the version is the git commit, so `claude plugin update` picks up new commits. Auto-update is off by default for marketplaces other than Anthropic's. A project can turn it on, and register the marketplace for everyone, in the `settings.json` it commits under its own `.claude/` folder (`extraKnownMarketplaces` with `autoUpdate`, and `enabledPlugins`); each teammate still installs once. 5.4 tests this.

**Since the trial: `tools/`.** After these trials the verifier gained `tools/axe.py` and `tools/readability.py`, run by repo-relative path, so `tools/` joins the interim copy list and the plugin build.

**The interim route, end to end, 2026-10-23.** A new project outside this repo (a one-page department site in its own git repository) was set up from the copy list in `README.md`, and each mode ran in a fresh headless session there, with axe allowed. Planning filled `a11y-spec.md` from the brief, marking the audience as assumed and flagging a missing mobile screen reader. Consult refused to write a need statement until the developer answered who the list is for; given the answer, it wrote one into the spec. Build refused to start before the need statement existed, then added a heading and a plain list of four workshops with distinct link text. The verifier read the spec, ran axe-core 4.14.0 and `tools/readability.py` from the copied `tools/`, found no definite or likely defect and no spec deviation, and filed a manual-review note that `signup.html` does not exist. This was a project made for the test, not a team's live site; the first live project will repeat it.

**Rejected: copy by hand as the long-term route.** It works, but it turns every project into a fork of the library that never hears about corrections. The interim instructions in `README.md` say so.
