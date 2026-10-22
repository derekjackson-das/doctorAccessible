# UX need-finding: Writing a need statement

- Sources:
  - GOV.UK Service Manual, User research community, "Learning about users and their needs", last updated 23 March 2017. https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs
  - GOV.UK Service Manual, Agile delivery community, "Writing user stories", last updated 23 May 2016. https://www.gov.uk/service-manual/agile-delivery/writing-user-stories
  - W3C, Making Content Usable for People with Cognitive and Learning Disabilities, Working Group Note, 29 April 2021, section 3, User Stories (tier 2). https://www.w3.org/TR/coga-usable/#x3-user-stories
- Tier: 3 for GOV.UK (user-research and agile-delivery guides added to `knowledge/SOURCES.md` in this package, awaiting team confirmation); 2 for the W3C Note.
- Related entries: `ux/learning-who-uses-a-thing.md`, `ux/personas-from-research.md`, `templates/a11y-spec.md` (the format), `coga/` entries (user needs by objective)
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

This entry supports consult and the project spec. The verifier reads need statements from the spec and reports where the code does not appear to serve one, as manual review; it never judges the statement itself.

## What the sources say

- **The common form.** GOV.UK writes a user need as: I need, want, or expect to do something, so that I reach some goal. Optionally it adds who the user is, what triggers the need, and any circumstance that constrains them ("Learning about users"). A user story uses the same parts: the actor, what they need, and why ("Writing user stories").
- **The goal matters most.** If a team cannot state why someone needs a feature, it should question the feature ("Writing user stories").
- **What a good need looks like.** A real user could plausibly have said it, it rests on research rather than assumption, and it describes the problem, not a solution: needing a reminder, not needing an email ("Learning about users").
- **Use the user's words.** Needs are written from the person's point of view, in terms they would use, and the list is kept short enough to manage ("Learning about users"). For Doctor Accessible this means the words come from research notes, quoted or closely paraphrased. Consult never invents first-person wording for a user, least of all a disabled one (principle 7).
- **Needs are broad and stable; stories are specific.** Keep track of which need each piece of work serves ("Learning about users").
- **W3C writes cognitive accessibility needs the same way.** Each user story in the Note names a group of people, what they need, and why (W3C, section 3). These are general categories, not a real person in a real situation, so they are a checklist of needs to ask about in research, never text for the `For` or `Trying to` lines.

## How consult uses it

Consult ends with a need statement in `templates/a11y-spec.md`, which asks for six lines. Each one answers a GOV.UK question:

| Spec line | GOV.UK part | What makes it good |
|---|---|---|
| For | As a…, When…, Because… | A person in a situation, with any constraint that matters, such as the device or assistive technology they use. Not "users". |
| Trying to | I need to…, So that… | The task and its goal, in their words. No solution named. |
| We will build | (the story) | The smallest thing that meets the need. |
| Instead of | (none) | What was asked for or considered. This is where "build less" is recorded. |
| Why this is right | Validation | The evidence: research, data, or a source in `knowledge/`. |
| Manual tests owed | Acceptance criteria | What a person with assistive technology still has to try before the need counts as met. |

### An illustration

This shows the shape only. A real statement comes from research, not from this file.

- **For:** a part-time student checking library hours on a phone between classes, using VoiceOver.
- **Trying to:** find out whether the library is open now, so they can decide whether to walk there.
- **We will build:** today's hours as plain text near the top of the library home page.
- **Instead of:** a rotating banner of library news with hours on the third frame (see `ux/carousels.md`).
- **Why this is right:** hours are the most-searched item on the site (assumed here; a real statement cites the data).
- **Manual tests owed:** VoiceOver on iOS reaches the hours within the first few swipes; text at 200% zoom.

## Common mistakes

- Writing the solution into the need ("needs a carousel").
- Naming "users" or "everyone" instead of a person in a situation.
- A need with no evidence behind it.
- Skipping "Instead of", which hides the decision consult made.
