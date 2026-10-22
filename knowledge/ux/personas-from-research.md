# UX need-finding: Personas from research

- Sources:
  - Taylor Dykes, "Personas Make Users Memorable", Nielsen Norman Group, 3 October 2025. https://www.nngroup.com/articles/persona/
  - Page Laubheimer, "3 Persona Types: Lightweight, Qualitative, and Statistical", Nielsen Norman Group, 21 June 2020. https://www.nngroup.com/articles/persona-types/
  - Kim Flaherty, "Why Personas Fail", Nielsen Norman Group, 28 January 2018. https://www.nngroup.com/articles/why-personas-fail/
  - GOV.UK Service Manual, User research community, "Understanding users who do not use digital services", last updated 28 June 2016. https://www.gov.uk/service-manual/user-research/understanding-users-who-dont-use-digital-services
  - W3C, Making Content Usable for People with Cognitive and Learning Disabilities, Working Group Note, 29 April 2021, section 6, Use Cases / Personas (tier 2). https://www.w3.org/TR/coga-usable/#x6-use-cases-personas
- Tier: 3 for NN/g (on `knowledge/SOURCES.md`, UX claims only) and GOV.UK (user-research guide added in this package, awaiting team confirmation); 2 for the W3C Note.
- Related entries: `ux/learning-who-uses-a-thing.md`, `ux/writing-a-need-statement.md`
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

This entry supports consult and the project spec. It produces no verifier findings. A persona never stands in for testing with real people (principle 7).

## What the sources say

- **What a persona is.** An invented but believable person who stands for a group of real users, used to keep a team focused on real people and to give it a shared name for a group of users. Every detail should earn its place by affecting a design decision (Dykes).
- **It must come from research.** Personas are made-up people built on information about real people (Dykes). NN/g describes three kinds by how much research is behind them (Laubheimer):
  - **Proto personas** come from a workshop of the team's existing knowledge and guesses, with no new research. They make assumptions visible, and they can also lock those assumptions in.
  - **Qualitative personas** come from interviews or usability sessions with roughly five to thirty people, grouped by shared goals, pain points, and expectations. NN/g recommends this for most teams.
  - **Statistical personas** add a large survey and cluster analysis. They are costly, need a statistician, and often end up close to the qualitative ones.
- **Demographics are not enough.** NN/g advises against personas built only from demographic or analytics data, because they say nothing about why people do what they do (Laubheimer).
- **Why personas fail.** They are made but never used; leaders think they already know the users; the UX team builds them alone and imposes them; nobody explains how to use them; or a persona built for one purpose, such as marketing, is reused for another, such as designing a single feature (Flaherty).
- **Personas for people who need help.** GOV.UK suggests personas built from research to understand people who will need assisted digital support, and publishes a starting set ("Understanding users who do not use digital services").
- **The W3C personas are fictional examples.** The Note says plainly that its personas describe fictional people, written to show the challenges people with cognitive and learning disabilities face (section 6). They are a useful reference and a checklist of situations to look for, not personas for any particular project.

## How consult uses it

1. If the spec's audience is written as personas, consult asks where they came from. Proto personas are recorded as assumptions; qualitative ones can support a need statement.
2. A need statement names a person in a situation. A persona can supply that person, but only if it came from research about this project's users.
3. Consult can use the W3C personas to ask whether a situation has been considered, such as someone who cannot remember a password or who reads slowly, without claiming those people are in the project's audience.

## Common mistakes

- Inventing personas and treating them as research.
- Personas full of irrelevant detail, or built only on demographics.
- A persona that represents a disabled person but was written without disabled people's input.
- Using a persona, or a model, to say what a disabled user would experience. Doctor Accessible produces test protocols for real people instead (principle 7).
