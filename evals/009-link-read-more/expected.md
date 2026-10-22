# Eval 009: three "Read more" links with no programmatic context

Input: `input.html`. A news page with three short items, each ending in a "Read more" link.

Intended defect: the three links all read "Read more" and go to different places. Each link is alone in its own paragraph, so there is no programmatically determined context: the enclosing paragraph contains nothing but the link, and the heading above it is not programmatic context at Level A (the heading technique H80 is advisory only). A screen reader user listing the links hears "Read more, Read more, Read more." Everything else is clean: language set, title present, one `h1` and three `h2`, landmarks, `article` elements, visible focus, contrast above the thresholds, links underlined.

## Expected findings

1. **[Definite]** Link text does not describe the destination, and no programmatic context completes it.
   - Criterion: WCAG 2.2 SC 2.4.4 Link Purpose (In Context) (Level A), tier 1
   - Source: `knowledge/wcag/sc-2.4.4-link-purpose-in-context.md`
   - Where: the three `a` elements inside `main`, one per `article`
   - Acceptable fix directions: make each link's text say what it leads to, such as "Read more about extended exam hours" (technique G91, H30); or move the link into the descriptive paragraph so the sentence supplies context (technique H78); or add visually hidden text inside the link (technique C7). If `aria-label` is used, it must still contain the visible words "Read more" (SC 2.5.3, entry in the same package).

One finding covering all three links is correct. Three separate findings for the same defect is padding.

## Also acceptable

- A note that the `article` element and the preceding `h2` do not count as programmatic context for this criterion at Level A, showing the verifier checked rather than assumed.
- A content note against `docs/content-standards.md` that link text should say where it goes.
- A cross-reference to SC 2.5.3 Label in Name warning about the `aria-label` trap.

## Must not

- Report the headings; each describes its item.
- Report SC 4.1.2; every link has a name.
- Report landmarks, focus style, language, or contrast.
- State a criterion number, title, or level that is not in `knowledge/INDEX.md` without marking it unverified.
- Rewrite the code.

## Automated scan

axe-core is expected to report no violations. Its `link-name` rule checks only that a name exists. Whether the name describes the destination is a reading judgment. A verifier that treats the clean scan as a pass has failed this eval.

## Pass condition

Finding 1 is present with the right criterion, level, and tier, and nothing from the Must not list appears.
