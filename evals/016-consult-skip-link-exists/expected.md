# Eval 016: consult on a skip link the template already has

Input: `request.md`. A developer, prompted by a tool, asks to add a skip link. The template they paste already has one: a link to `#main` that is visually hidden until focused, with a `main` element that can receive focus, plus a labeled `nav` landmark and an `h1`.

Intended outcome: the right answer to question two is "already met, build nothing." The skill reads the code, recognizes the existing mechanism, and says so. It then says what remains to be checked by a person.

## Expected

1. **Who and what** comes from the spec: prospective students on phones and alumni, trying to get past the header to the content. Named AT: NVDA with Chrome, VoiceOver on iOS, keyboard only.
2. **Smallest thing** says the need is already met: the template has a skip link that appears on focus and targets a focusable `main`, and landmarks and a heading are present as well. "Already met", "nothing to build", or equivalent words appear. The answer explains why the checker may have flagged it, as a possibility rather than a certainty: the link is off-screen until focused, which some tools do not detect, or the tool was run on a page built from a different template.
3. **Criteria** cited from the entry: SC 2.4.1 Bypass Blocks (Level A), tier 1, from `knowledge/wcag/sc-2.4.1-bypass-blocks.md`, including its note that landmarks alone would pass and a visible-on-focus skip link is the conservative choice. SC 2.4.7 Focus Visible and SC 2.4.3 Focus Order are acceptable additions for the link itself.
4. **Manual tests owed** are specific to what exists: press Tab once from page load and confirm the skip link appears and is readable; activate it and confirm focus lands on `main` and the next Tab goes to the first thing inside it; repeat with NVDA and VoiceOver; confirm the hidden-until-focus style does not break at 400% zoom or in forced-colors mode.
5. **Need statement** is proposed in the template's format with "We will build: nothing" and "Why this is right" explaining that the mechanism exists and the owed work is testing, not building.
6. **Content** notes that "Skip to main content" is clear link text and leaves it alone.

## Also acceptable

- Suggesting the developer run the checker against the live page and share the exact finding, since a tool's message and a tool's rule can differ.
- A note that `tabindex="-1"` on `main` is what makes the target reliably focusable in all browsers, as an observation about why the existing code works.

## Must not

- Add a second skip link, or rewrite the existing one.
- Write any code.
- Treat the checker's message as authoritative over the code and the entry.
- State a criterion number, title, or level not in `knowledge/INDEX.md` without marking it unverified.
- Say the page "passes" without naming the manual tests still owed.

## Pass condition

Items 1 through 5 are present, the answer to question two is that the need is already met, and nothing from the Must not list appears.
