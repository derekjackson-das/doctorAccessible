# Consult runs, 2026-10-22, eval 015

Method, both runs: a general-purpose agent given the repo, told to read `.claude/skills/consult/SKILL.md` and follow it, then read `request.md`, with `expected.md`, run files, and `RESULTS.md` off limits and no file writes. The skill registered in the session after the branch was created, so these are prompt tests of the skill text, not fresh-session loads of `/consult`. Onboarding runs can repeat them as true fresh-session runs.

## Run 1, SKILL.md at commit b3f41fa (before the ux and coga domains were mapped): pass

Who and what from the spec, not the request; marketing's rotation named as a presentation preference and moved to "Instead of". Build less: a list of five linked events, no motion, no script. Carousel, auto-rotation, swipe, and big images each challenged with "no entry yet" for patterns and the WCAG entries as the stated basis; two COGA entries used as tier 2 context after the agent found them in the index. Twenty-one criteria cited, every one from an opened entry. Three options with costs. Manual tests from the spec's AT list. Need statement proposed, not written; pattern decision and banned pattern proposed. No code. Nothing from the must-not list.

Observation: thorough past the point of use. Twenty-one criteria for a list of five links is the build mode's pass, not consult's. Led to the brevity sentence in the output section.

## Run 2, SKILL.md at commit d294e50 (ux and coga mapped; brevity sentence not yet in the file but given in the dispatch): pass

Same conclusion, tighter. Research claims about carousels taken from `knowledge/ux/carousels.md`, labeled tier 3 and likely, with the entry's own "build less" line quoted. Need-finding entry used to call marketing's wish a stakeholder assumption to test, and to say plainly that if no evidence shows students come to the homepage for events, the feature is not ready. Criteria split into the eight the list must meet and the five that decide against the carousel. Auto-rotation excluded from the options list with the reason. Need statement, pattern decision, and ban proposed, with the "Trying to" line marked as paraphrased from the spec pending research notes. No code. Nothing from the must-not list.

Both runs: the answer to question two is a list, not a carousel.
