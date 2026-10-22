# Trusted sources

The sources Doctor Accessible is allowed to rely on, by tier. Nothing off this list is authoritative until a pull request adds it. Every knowledge entry cites a source from this list, with its tier and its version or date.

Owner: whoever holds roadmap package 2.6. Re-verify quarterly. The **Verified** column is the date someone opened the live source and confirmed the version and status; "proposed" means the source is on the list pending the team's confirmation.

## How the tiers work

- **Tier 1, normative.** Settles what a requirement is. Wins any conflict.
- **Tier 2, informative, from the standards body.** Explains how to read and meet the requirement. Authoritative, not binding.
- **Tier 3, practitioner.** Judgment, real-world support, usability research, and how things actually behave. Cited by name. Never the sole source for what a requirement is.

Rules of use:

1. Look in `knowledge/` first, then here. Research outside this list is not research; it is a proposal to extend the list.
2. Cite tier, source, and version or date on every claim: "WCAG 2.2 SC 1.4.11 (Level AA), W3C Rec 12 Dec 2024, tier 1".
3. Say which version an answer applies to. WCAG 2.0, 2.1, and 2.2 are all live in different regulations.
4. Working drafts (WCAG 3.0, APCA) are awareness only.
5. When sources conflict, name the conflict, cite both, and take the stricter reading. A tier 3 source never overrides tier 1.
6. This repo is public. Quote only tier 1 text, with attribution. Summarize and link everything else.

## Admitting a tier 3 source

A source is added when all of these hold:

- Published under a real name or a named organization, and dated.
- Cites tier 1 or tier 2 material, or is cited by it.
- Makes claims that can be checked: demos, test results, references, or reproducible method.
- Maintained, or clearly dated so staleness is visible.

A source is removed when it contradicts tier 1 without acknowledging it, or when support data it publishes is more than three years old without an update. Add or remove by pull request with a one-line reason in the change log below.

## Tier 1, normative

| Source | For | Version or date | Cite as | Verified |
|---|---|---|---|---|
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Web content requirements. Target: Level AA. | W3C Recommendation 12 December 2024 | WCAG 2.2 SC x.x.x (Level) | 2026-10-22 |
| [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) | Roles, states, properties | W3C Recommendation 6 June 2023 | WAI-ARIA 1.2 §… | proposed |
| [ARIA in HTML](https://www.w3.org/TR/html-aria/) | Which roles and attributes are allowed on which elements | W3C Recommendation, evergreen | ARIA in HTML | proposed |
| [Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/) | How accessible names are computed | W3C; confirm current status when verifying | AccName 1.2 | proposed |
| [HTML Living Standard](https://html.spec.whatwg.org/multipage/) | Native element semantics and behavior | WHATWG, evergreen | HTML Living Standard | proposed |
| [HTML Accessibility API Mappings](https://www.w3.org/TR/html-aam/) | How HTML maps to platform accessibility APIs | W3C; confirm current status when verifying | HTML-AAM | proposed |

### Policy that names a standard

| Source | For | What it requires | Verified |
|---|---|---|---|
| [Harvard Digital Accessibility Policy](https://accessibility.huit.harvard.edu/digital-accessibility-policy) | Harvard's binding standard | WCAG 2.1 AA. Building to 2.2 AA satisfies it. | proposed |
| [Revised Section 508 Standards](https://www.section508.gov/manage/laws-and-policies/) | US federal ICT | WCAG 2.0 AA | proposed |
| [ADA Title II web rule](https://www.ada.gov/resources/2024-03-08-web-rule/) | US state and local government | WCAG 2.1 AA | proposed |
| [EN 301 549](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf) | EU ICT, made binding by the European Accessibility Act | WCAG 2.1 AA via clause 9 | proposed |

## Tier 2, informative, from the standards body

| Source | For | Verified |
|---|---|---|
| [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/) | Intent, benefits, examples, and the sufficient techniques for each criterion | 2026-10-22 (4.1.2 page) |
| [Techniques for WCAG 2.2](https://www.w3.org/WAI/WCAG22/Techniques/) | Sufficient, advisory, and failure techniques by ID | proposed |
| [How to Meet WCAG, Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) | Filterable list of criteria and techniques | proposed |
| [WAI Tutorials](https://www.w3.org/WAI/tutorials/) | Images, tables, forms, carousels, menus, page structure | proposed |
| [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) | Widget patterns and keyboard conventions. **Patterns, not requirements.** Never cite as a hard rule. | proposed |
| [Using ARIA](https://www.w3.org/TR/using-aria/) | W3C guidance on when to use ARIA at all; the source of "no ARIA is better than bad ARIA" | proposed |
| [Writing for Web Accessibility](https://www.w3.org/WAI/tips/writing/) | W3C WAI tips on plain language, headings, links, alt text, instructions | proposed |
| [Making Content Usable for People with Cognitive and Learning Disabilities](https://www.w3.org/TR/coga-usable/) | W3C Working Group Note, 29 April 2021. Plain language, structure, and design for cognitive accessibility. A Note, not a Recommendation: guidance, not requirements. | proposed |
| [Section508.gov](https://www.section508.gov/) and [U.S. Access Board ICT](https://www.access-board.gov/ict/) | US federal guidance and testing baseline | proposed |

## Tier 3, practitioner

### Organizations and reference

| Source | For | Verified |
|---|---|---|
| [WebAIM](https://webaim.org/) | Foundational articles, contrast checker, Screen Reader User Survey, WebAIM Million | proposed |
| [Deque axe rule descriptions](https://dequeuniversity.com/rules/axe/) | What each axe rule checks and which criteria it maps to. The reference for every axe finding. | proposed |
| [MDN Web Docs, Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) | Implementation reference for HTML, CSS, JS, ARIA. Reference, not normative. | proposed |
| [Nielsen Norman Group](https://www.nngroup.com/) | Usability research and UX heuristics. Used in the design moment to ask whether a thing should be built. Not an accessibility authority; summarize and link, never paste. | proposed |
| [a11ysupport.io](https://a11ysupport.io/) | Tested support for HTML and ARIA features across screen reader and browser pairs | proposed |
| [GOV.UK accessibility guidance](https://www.gov.uk/service-manual/helping-people-to-use-your-service) | Service-manual guidance on testing with assistive technology and on what automated tools miss | proposed |
| [Federal Plain Language Guidelines](https://www.plainlanguage.gov/guidelines/) | US government plain language rules: audience, organization, words, sentences, testing | proposed |
| Readability formulas (Flesch-Kincaid Grade Level and similar) | A signal for reading level, computed locally. Measures sentence and word length, not clarity. Never a pass on its own. | n/a |

### Named practitioners

Proposed for the team to confirm. Each publishes under their own name, dates their work, and shows their tests.

| Source | For | Verified |
|---|---|---|
| [Adrian Roselli](https://adrianroselli.com/) | Pattern critiques with screen reader test results; tables, dialogs, carousels, toggles | proposed |
| [Scott O'Hara](https://www.scottohara.me/) | ARIA and HTML control behavior, tested across assistive technology | proposed |
| [Sara Soueidan](https://www.sarasoueidan.com/blog/) | Accessible components, SVG, forms | proposed |
| [Heydon Pickering, Inclusive Components](https://inclusive-components.design/) | Component patterns built accessibly from the start | proposed |
| [Léonie Watson](https://tink.uk/) | Screen reader behavior from a screen reader user and W3C participant | proposed |
| [Steve Faulkner, TPGi](https://www.tpgi.com/blog/) | HTML accessibility, ARIA in HTML editor | proposed |
| [Eric Bailey](https://ericwbailey.website/) | Design systems, focus, reduced motion | proposed |
| [Sarah Higley](https://sarahmhigley.com/) | Complex widgets, tooltips, comboboxes, with test data | proposed |
| [Hidde de Vries](https://hidde.blog/) | Standards process, WCAG interpretation | proposed |

## Change log

| Date | Change | By |
|---|---|---|
| 2026-10-22 | List created. Tier 1 and 2 seeded from W3C and WHATWG. Tier 3 proposed for team confirmation. | Derek Jackson with Claude Code |
| 2026-10-22 | Content sources added: Writing for Web Accessibility and Making Content Usable (tier 2), Federal Plain Language Guidelines and readability formulas (tier 3). | Derek Jackson with Claude Code |
