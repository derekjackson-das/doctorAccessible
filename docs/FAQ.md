# Doctor Accessible: frequently asked questions

## Is this a tool that makes my site accessible?

No. It is an assistant. It helps a person build accessibly and check their work, and it is honest about what it cannot judge. A person reviews every finding it produces, decides what to do, and tests the result with real assistive technology before anything ships. Nothing in this repo removes that responsibility, and nothing in it is a conformance claim. If someone tells you a page is accessible because Doctor Accessible said so, they have misunderstood what it is.

## Does it certify WCAG conformance?

No. It reports findings against WCAG 2.2 Level AA with a confidence level: definite, likely, or manual review. "Definite" means the finding is rule-based and would fail an audit. "Likely" means the pattern suggests a failure and a person should confirm. "Manual review" means the code cannot settle it. A page with no definite findings has not passed; it has passed the part a machine and a reading can judge. The manual tests it lists are still owed.

## What standard does it build to?

WCAG 2.2 Level AA, the W3C Recommendation of 12 December 2024. Harvard's policy names WCAG 2.1 AA; building to 2.2 AA satisfies it. The verifier says when a finding is Level AAA or a best practice rather than a requirement. Working drafts such as WCAG 3.0 are awareness only and are never cited as requirements.

## Where does it get its facts?

From its own library, `knowledge/`, and nowhere else. Every entry cites a source from `knowledge/SOURCES.md` with a tier: tier 1 is the standard itself, tier 2 is the W3C explaining the standard, tier 3 is named practitioners and usability research. Nothing is pasted; entries are written in our words with the source linked. If no entry covers a question, the skills say "no entry yet" and mark any claim unverified. They do not fill the gap from memory.

## Can I trust a number it gives me, like a contrast ratio?

Only when it says where the number came from. The rules forbid stating thresholds from memory. A contrast ratio computed from your declared colors is fine, and the report says it was computed and from which colors, after opening the entry that holds the threshold. A figure from a document the agent did not open in that run is treated as memory and left out or marked unverified.

## Why does it keep asking who the feature is for?

Because the cheapest accessibility fix is not building the wrong thing. Consult asks who, what they are trying to do, and what the smallest thing that meets that need is, before it asks how. "Users" is not an answer. A specific person in a specific situation is. Sometimes consult will say a list serves better than a carousel, or that the thing you asked for is already met. That is the mode working, not the mode being difficult.

## What is `a11y-spec.md` and do I have to fill it in?

It is your project's accessibility spec, one per project, copied from `templates/a11y-spec.md`. It holds the conformance target, who the project serves, the assistive technology you test with, the need statement for each feature, pattern decisions, banned patterns, and the manual tests still owed. Every mode reads it first and writes decisions back to it. Build does not start on a feature without a need statement in it. Yes, fill it in; `/planning` walks you through it.

## Does it run automated scans?

It runs axe, and only axe, with the WCAG 2.2 tags, because the default axe run skips those rules. axe finds a minority of defects reliably. The verifier reads the code itself for the rest and never treats a clean scan as a pass. Lighthouse is not used.

## Will it simulate a screen reader user for me?

No. Principle 7: humans do the final test. It will write the test script, from the assistive technology listed in your spec, with what to do and what to record. It will not say what a user "would experience" or what a screen reader "would announce." A person runs the test and reports what happened.

## It found something I disagree with. What do I do?

Open the entry it cited. Every finding names a file under `knowledge/`. If the entry supports the finding, the disagreement is with the standard, and the conservative reading wins. If the entry is wrong or missing, fix the entry by pull request; that is how the library gets better. If the finding is a judgment call, it should already be marked likely or manual review, and the call is yours.

## Can I use it with React, Vue, or a CMS?

Plain HTML, CSS, and JavaScript are the reference. There is a `react-jsx` skill that layers over the native patterns. Other frameworks and CMS layers are on the roadmap. The library entries apply to the rendered HTML whatever produced it, so the verifier works on any page it can load.

## How do I know a change to the tool made it better and not worse?

Evals. The repo holds forty small pages and requests with known defects and answer keys. Any change to an agent, a skill, or an entry runs the relevant evals, and the results are recorded in `evals/RESULTS.md`. A headless runner and a checker do this without a person comparing reports by hand. No eval, no merge.

## What does it cost to run?

Each verifier run or skill run is a Claude Code session's worth of tokens. The headless eval runner starts one session per eval. axe and the reading-level tool run locally and are free.

## How do I add a knowledge entry, a skill, or a source?

Read `CONTRIBUTING.md` and `docs/how-we-work.md`. In short: claim the issue, branch, write in your own words from a source on the list, cite tier and date, add the entry to `knowledge/INDEX.md`, write an eval if the change needs one, run it, open a pull request. Adding a source is itself a pull request to `knowledge/SOURCES.md`, with a reason, and tier 3 sources must pass an admission rule.

## Who maintains it, and how current is the library?

Derek Jackson's team at Harvard, in public on GitHub. Every entry carries the date it was verified against the live source. Entries re-verify when W3C revises WCAG 2.2 and quarterly otherwise. The sources list is re-checked each quarter.

## What should I do first?

Read `docs/TLDR.md`, copy the files into a small real project, fill the spec with `/planning`, and run `/consult` on one feature. The first real project teaches more than any amount of reading.
