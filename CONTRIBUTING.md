# Contributing

How a change gets into Doctor Accessible. The rules come from the README, `docs/principles.md`, and `docs/ROADMAP.md`; this is the procedure.

## 1. Claim work

Find a package in `docs/ROADMAP.md`. Open an issue from the **Work package** template, copy the package's fields in, and put your name in the owner field. One person per package. If you want to do something the roadmap does not list, open the issue anyway and say so; the roadmap gets updated in the same pull request as the work.

## 2. Make the change

- Branch from `main`, named for the package: `wp-2.1-perceivable`, `wp-3.3-content`.
- One package per branch, one branch per pull request.
- Never commit to `main`. Branch protection requires a pull request.
- Commit messages say what changed and why, in a sentence or two.

## 3. What a knowledge entry needs to merge

- Starts from `knowledge/wcag/_template.md` or the domain's equivalent.
- Written in your own words from the source. Only normative text (tier 1) is quoted, with attribution.
- Cites tier, source, and version or date for every claim. Sources come from `knowledge/SOURCES.md` and nowhere else.
- Carries the date you verified it against the live source, and your name.
- Added to `knowledge/INDEX.md` in the same commit.
- Says which WCAG versions the criterion exists in, if the text or level differs.

## 4. What a skill, agent, or eval change needs to merge

- The pull request says which evals ran and what they produced. No eval, no merge.
- If the change needs an eval that does not exist, write the eval first, from the knowledge entry, not from memory.
- A `SKILL.md` stays under about 120 lines. Depth goes in `knowledge/`.
- A new agent needs a written case under principle 1, recorded in `docs/decisions.md`, before it is built.

## 5. Add a source

By pull request to `knowledge/SOURCES.md`. Tier 3 sources must pass the admission rule in that file. Add a one-line reason to its change log.

## 6. Record a decision

When a change alters the shape of the project (a mode, a principle, a package, a rule), add a dated entry to `docs/decisions.md`. Old entries are never rewritten.

## 7. Public repo

Everything here is public. Write in your own words, link to sources, never paste vendor or practitioner material. Nothing from DAARA, from Harvard internal material, or from any other private source.

## 8. Review

A reviewer checks the same list the author used, in the same order: the right package, one branch, entries cited and verified and indexed, evals named with results, sources on the list, decisions recorded, nothing pasted. Reviewers strike what fails and say why. Approval means the list passed, not that the reviewer agrees with every word.
