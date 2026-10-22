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
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Web content requirements. Target: Level AA. | W3C Recommendation 12 December 2024 | WCAG 2.2 SC x.x.x (Level) | 2026-10-22, re-confirmed |
| [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) | Roles, states, properties | W3C Recommendation 6 June 2023 | WAI-ARIA 1.2 §… | 2026-10-22 |
| [ARIA in HTML](https://www.w3.org/TR/html-aria/) | Which roles and attributes are allowed on which elements | W3C Recommendation 11 August 2026 | ARIA in HTML, W3C Rec 11 Aug 2026 | 2026-10-22 |
| [Accessible Name and Description Computation 1.1](https://www.w3.org/TR/accname-1.1/) | How accessible names are computed | W3C Recommendation 18 December 2018. The 1.2 draft at https://www.w3.org/TR/accname-1.2/ was a Working Draft (21 October 2026) when checked; awareness only under rule 4 until it reaches Recommendation. | AccName 1.1 | 2026-10-22 |
| [HTML Living Standard](https://html.spec.whatwg.org/multipage/) | Native element semantics and behavior | WHATWG, evergreen; no dated versions. Cite the section and the date accessed. | HTML Living Standard, §section, accessed YYYY-MM-DD | 2026-10-22 |

### Policy that names a standard

| Source | For | What it requires | Verified |
|---|---|---|---|
| [Harvard Digital Accessibility Policy](https://accessibility.huit.harvard.edu/digital-accessibility-policy) | Harvard's binding standard | WCAG 2.1 AA. Building to 2.2 AA satisfies it. Policy last updated 1 June 2023. The page blocks automated fetching; verify in a browser. | 2026-10-22 |
| [Revised Section 508 Standards](https://www.section508.gov/manage/laws-and-policies/) | US federal ICT | WCAG 2.0 AA | 2026-10-22 |
| [ADA Title II web rule](https://www.ada.gov/resources/2024-03-08-web-rule/) | US state and local government | WCAG 2.1 AA (rule of 8 March 2024) | 2026-10-22 |
| [EN 301 549](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf) | EU ICT, made binding by the European Accessibility Act | WCAG 2.1 AA via clause 9 (v3.2.1, 2021) | 2026-10-22 |

## Tier 2, informative, from the standards body

| Source | For | Verified |
|---|---|---|
| [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/) | Intent, benefits, examples, and the sufficient techniques for each criterion. Page updated 11 February 2026. | 2026-10-22 |
| [Techniques for WCAG 2.2](https://www.w3.org/WAI/WCAG22/Techniques/) | Sufficient, advisory, and failure techniques by ID. Page updated 11 May 2026. | 2026-10-22 |
| [How to Meet WCAG, Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) | Filterable list of criteria and techniques. Page updated 22 September 2025. | 2026-10-22 |
| [WAI Tutorials](https://www.w3.org/WAI/tutorials/) | Images, tables, forms, carousels, menus, page structure | 2026-10-22 |
| [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) | Widget patterns and keyboard conventions. **Patterns, not requirements.** Never cite as a hard rule. | 2026-10-22 |
| [Using ARIA](https://www.w3.org/TR/using-aria/) | The rules for when to use ARIA at all; the source of "no ARIA is better than bad ARIA". **W3C Discontinued Draft 24 February 2026.** The W3C keeps it for historical reference and points to the Authoring Practices Guide for live guidance. Cite the rules as historical W3C guidance, dated. | 2026-10-22 |
| [HTML Accessibility API Mappings 1.0](https://www.w3.org/TR/html-aam/) | How HTML maps to platform accessibility APIs. W3C Working Draft (21 October 2026 when checked); implementation reference, not normative. Moved from tier 1 on verification under rule 4. | 2026-10-22 |
| [Writing for Web Accessibility](https://www.w3.org/WAI/tips/writing/) | W3C WAI tips on plain language, headings, links, alt text, instructions | 2026-10-22 |
| [Making Content Usable for People with Cognitive and Learning Disabilities](https://www.w3.org/TR/coga-usable/) | W3C Working Group Note, 29 April 2021. Plain language, structure, and design for cognitive accessibility. A Note, not a Recommendation: guidance, not requirements. | 2026-10-22 |
| [Section508.gov](https://www.section508.gov/) and [U.S. Access Board ICT](https://www.access-board.gov/ict/) | US federal guidance and testing baseline | 2026-10-22 |

## Tier 3, practitioner

### Organizations and reference

| Source | For | Verified |
|---|---|---|
| [WebAIM](https://webaim.org/) | Foundational articles, contrast checker, Screen Reader User Survey, WebAIM Million | 2026-10-22, confirmed by Derek Jackson |
| [Deque axe rule descriptions](https://dequeuniversity.com/rules/axe/) | What each axe rule checks and which criteria it maps to. The reference for every axe finding. | 2026-10-22, confirmed by Derek Jackson |
| [MDN Web Docs, Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) | Implementation reference for HTML, CSS, JS, ARIA. Reference, not normative. Index page last modified 2 October 2025. | 2026-10-22, confirmed by Derek Jackson |
| [Nielsen Norman Group](https://www.nngroup.com/) | Usability research and UX heuristics. Used in the design moment to ask whether a thing should be built. Not an accessibility authority; summarize and link, never paste. | 2026-10-22, confirmed by Derek Jackson for UX claims only |
| [a11ysupport.io](https://a11ysupport.io/) | Tested support for HTML and ARIA features across screen reader and browser pairs. Each test shows its last-update date; results on one sampled feature ranged from 2024 back to eight years old, and the site itself warns results may be stale. Cite only tests updated within three years, and give the date. | 2026-10-22, confirmed by Derek Jackson with that usage rule |
| [GOV.UK accessibility guidance](https://www.gov.uk/service-manual/helping-people-to-use-your-service) | Service-manual guidance on testing with assistive technology and on what automated tools miss. Page first published 7 April 2016; maintained as part of the GOV.UK Service Manual. | 2026-10-22, confirmed by Derek Jackson |
| [GOV.UK Service Manual, user research](https://www.gov.uk/service-manual/user-research), plus the agile-delivery guide [Writing user stories](https://www.gov.uk/service-manual/agile-delivery/writing-user-stories) | User research and need-finding: learning about users and their needs, writing user needs and user stories, finding participants including disabled participants, running sessions with disabled people, users who do not use digital services. Same publisher as the row above. Each guide shows its own last-updated date; cite it. | 2026-10-22, checked by Caesar Alam with Claude Code; awaiting team confirmation in the package 3.9 pull request |
| [Federal Plain Language Guidelines](https://digital.gov/guides/plain-language) | US government plain language rules: audience, organization, words, sentences, testing. The plainlanguage.gov guidelines URL now redirects to Digital.gov's plain language guide series. | 2026-10-22, URL updated, confirmed by Derek Jackson |
| Readability formulas (Flesch-Kincaid Grade Level and similar) | A signal for reading level, computed locally. Measures sentence and word length, not clarity. Never a pass on its own. | n/a |

### Named practitioners

Checked 2026-10-22: every site below is live and publishing under a real name. Confirmed by Derek Jackson on 2026-10-22 under the admission rule.

| Source | For | Verified |
|---|---|---|
| [Adrian Roselli](https://adrianroselli.com/) | Pattern critiques with screen reader test results; tables, dialogs, carousels, toggles | 2026-10-22, confirmed by Derek Jackson |
| [Scott O'Hara](https://www.scottohara.me/) | ARIA and HTML control behavior, tested across assistive technology | 2026-10-22, confirmed by Derek Jackson |
| [Sara Soueidan](https://www.sarasoueidan.com/blog/) | Accessible components, SVG, forms | 2026-10-22, confirmed by Derek Jackson |
| [Heydon Pickering, Inclusive Components](https://inclusive-components.design/) | Component patterns built accessibly from the start. Last article 4 June 2018; clearly dated, so staleness is visible, but check against current support before relying on a pattern. | 2026-10-22, confirmed by Derek Jackson |
| [Léonie Watson](https://tink.uk/) | Screen reader behavior from a screen reader user and W3C participant | 2026-10-22, confirmed by Derek Jackson |
| [Steve Faulkner, TPGi](https://vispero.com/resources/category/blog/) | HTML accessibility, ARIA in HTML editor. The TPGi blog URL now redirects to the Vispero blog; TPGi is part of Vispero. | 2026-10-22, URL updated, confirmed by Derek Jackson |
| [Eric Bailey](https://ericwbailey.website/) | Design systems, focus, reduced motion | 2026-10-22, confirmed by Derek Jackson |
| [Sarah Higley](https://sarahmhigley.com/) | Complex widgets, tooltips, comboboxes, with test data | 2026-10-22, confirmed by Derek Jackson |
| [Hidde de Vries](https://hidde.blog/) | Standards process, WCAG interpretation | 2026-10-22, confirmed by Derek Jackson |

## Change log

| Date | Change | By |
|---|---|---|
| 2026-10-22 | List created. Tier 1 and 2 seeded from W3C and WHATWG. Tier 3 proposed for team confirmation. | Derek Jackson with Claude Code |
| 2026-10-22 | Content sources added: Writing for Web Accessibility and Making Content Usable (tier 2), Federal Plain Language Guidelines and readability formulas (tier 3). | Derek Jackson with Claude Code |
| 2026-10-22 | Package 2.6 first pass. Every URL opened and its status recorded. ARIA in HTML is now a dated Recommendation (11 Aug 2026). AccName row moved from the 1.2 Working Draft to the 1.1 Recommendation; 1.2 noted as awareness only. HTML-AAM moved from tier 1 to tier 2 as a Working Draft. Using ARIA marked as a Discontinued Draft (24 Feb 2026), kept for the historical rules. Plain Language Guidelines URL now Digital.gov; TPGi blog URL now Vispero. Tier 3 rows marked checked with notes; confirmation left to the team. | Derek Jackson with Claude Code |
| 2026-10-22 | GOV.UK Service Manual user-research section and "Writing user stories" proposed (tier 3) for package 3.9 need-finding entries; the existing GOV.UK row covers only the accessibility section. Admission tests: real organization and dated, yes (each guide names its community and shows a last-updated date); maintained, yes (one guide updated 22 September 2026, though others date from 2016 and 2017); checkable claims, yes (concrete, procedural advice); cites or cited by tier 1 or 2, only indirectly (the user-research guides do not cite W3C; the same manual's accessibility introduction links W3C WAI material). Awaiting team confirmation. | Caesar Alam with Claude Code |
