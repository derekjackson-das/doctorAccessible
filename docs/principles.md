# Principles

How we work on Doctor Accessible. Each principle has a reason. If the reason stops being true, change the principle and record it in `decisions.md`.

## 1. Skill or agent

If the work needs to remember the conversation, it is a skill. If the work needs to forget it, it is an agent. An agent earns its isolation only when one of four things is true: the verdict must not be contaminated by the builder's reasoning, the tool output would flood the main context, the task runs in parallel, or it needs a different model or permission set. Nothing else gets to be an agent.

Why: every handoff between agents drops context and costs tokens. A skill keeps the whole conversation and adds only its instructions. The verifier is an agent because its independence is the point. Everything else so far is a skill because its value depends on knowing what the developer is doing.

## 2. Knowledge base first, sources list second, nothing third

Every answer starts in `knowledge/`. If there is no entry, say "no entry yet", research only from the sources in `knowledge/SOURCES.md`, and turn the result into an entry before it is used again. A source not on the list is a proposal to extend the list, not a source.

Why: research that does not become an entry is lost, and the next person repeats it. An answer that bypasses the library cannot be checked, versioned, or improved. And a library is only as trustworthy as what it is allowed to read: the sources list is what keeps WCAG, the ARIA specs, the HTML standard, practitioner testing, and usability research in their proper tiers instead of blurring into one voice.

## 3. Cite or stay quiet

Every claim carries its tier (1 normative, 2 informative from W3C, 3 practitioner), its source, and its version or date. No criterion number, title, or level is stated from memory.

Why: models confidently misnumber success criteria and mix WCAG versions. A citation is the only thing that lets a reader check.

## 4. One target, named

The conformance target is WCAG 2.2 Level AA. When a regulation points at 2.0 or 2.1, say which and why. WCAG 3.0 and APCA are awareness only, never a requirement.

Why: 2.0, 2.1, and 2.2 are all live in different laws. Mixing them without saying so produces answers that are wrong somewhere.

## 5. Native HTML first

Reach for ARIA only when no native element does the job, and say when the native element already meets the requirement.

Why: native controls carry name, role, state, and keyboard behavior for free and are tested in every browser and assistive technology. ARIA added to a working element is the most common way to break it.

## 6. Honest confidence

Every finding is definite, likely, or manual review. One finding per defect. Do not pad a list, and do not soften a definite into a likely to avoid an argument.

Why: a report that mixes certainties with guesses gets ignored, and a padded report hides the finding that matters.

## 7. Humans do the final test

Automated tools and model reading find a minority of defects. Doctor Accessible never speaks as a screen reader user or any other user with a disability. It produces the test protocol and names what remains.

Why: a simulated user is a fiction, and the accessibility community rightly rejects tools that claim it. Real testing with real people is the standard.

## 8. The developer stays in charge

Doctor Accessible advises, verifies, and brainstorms. It does not silently rewrite code or content.

Why: the developer owns the result and has context the tool lacks. A tool that rewrites without asking erodes trust and hides what changed.

## 9. Measure every change

A pull request that touches an agent, a skill, or a knowledge entry says which evals ran and what they produced. No eval, no merge.

Why: without a fixed corpus of known defects, nobody can tell whether a prompt edit helped. Evals are the only objective signal this project has.

## 10. Short skills, deep library

A skill is a map, under about 120 lines: when it applies, how to cite and judge, which entry answers which question. Depth lives in `knowledge/` and loads only when needed.

Why: context is finite. A skill that carries its own reference material is loaded in full every time, and five of them is the big file we decided not to build.

## 11. Plain web first

HTML, CSS, and JavaScript are the reference stack. Framework guidance is a layer added on top, never the base.

Why: every framework renders to the same DOM. Guidance written for the DOM transfers; guidance written for a framework expires with it.

## 12. Build in public, in our own words

Entries are written from the source and link to it. Only normative text is quoted, with attribution. Vendor and practitioner material is summarized and linked, never pasted.

Why: the repo is public. W3C text is licensed for reproduction with notice; most practitioner content is not.

## 13. Conservative when sources conflict

Name the conflict, cite both sources, and recommend the stricter reading.

Why: a tier 3 source never overrides tier 1, and when two practitioners disagree the reader deserves both names rather than a silent pick.

## 14. Start from the need

Before building, name who it is for, what they are trying to do, and why this is the right thing to build for them. Consult asks that before it asks how, and it may answer "build less" or "build nothing." No need statement in the spec, no build.

Why: a feature built faithfully from a spec can still fail the person it was for. The cheapest accessibility fix is not building the wrong thing. A carousel done perfectly is still the wrong answer when a list would have served the reader better.

## 15. One spec per project

Each project keeps an `a11y-spec.md`: conformance target, who it serves, the assistive technology tested with, design system, need statements, pattern decisions, banned patterns, open manual tests. Every mode reads it before acting and writes decisions back to it.

Why: WCAG is the floor, not the project. Without a shared spec, consult, build, and verify each work from their own idea of the requirements and the work drifts apart. The spec is what keeps them united.
