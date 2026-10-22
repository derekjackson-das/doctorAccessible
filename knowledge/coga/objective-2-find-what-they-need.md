# COGA Objective 2: Help users find what they need

- Source: W3C, Making Content Usable for People with Cognitive and Learning Disabilities, Working Group Note, 29 April 2021
- Tier: 2, informative from W3C. A Working Group Note is guidance, not a conformance requirement. Meeting it is not needed to conform to WCAG 2.2, and missing it is not a WCAG failure.
- Objective: https://www.w3.org/TR/coga-usable/#x4-3-objective-2-help-users-find-what-they-need
- User stories: https://www.w3.org/TR/coga-usable/#x3-2-objective-2-help-users-find-what-they-need
- User-need map: https://www.w3.org/TR/coga-usable/#a-2-objective-2-help-users-find-what-they-need
- Verified against the live source: 2026-10-22 by Caesar Alam with Claude Code, direct fetch of the Note and of the WCAG 2.2 Recommendation for every criterion cited

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. When the same defect also fails a WCAG criterion, report it once, under that criterion and its entry, and name this entry as context.

## The objective in plain words

The most important tasks and information should be the easiest things to find: near the top, visually prominent, and reachable in few steps. The site's structure and its menus should make sense to the people using it, so they guess right the first time. Long media should come in short, labeled parts. Search should forgive spelling and help people find what they searched for before.

## User needs it serves

- **Findable.** People with memory, executive function, or language processing impairments need key information and controls to stand out, to be visible without scrolling or hovering, to be reachable in a small number of easy steps, and to sit where they expect them.
- **Searchable.** People who have learned to rely on search need it to be available, to work with imprecise terms, and to bring back earlier searches.
- **Clear navigation.** People who browse need menu categories and page structure that make sense to them and that they can scan to see what matters most.
- **Media.** People with attention or executive function impairments need video and audio in short, labeled segments they can jump between, with a transcript they can find.

## Patterns W3C lists

- [Make it easy to find the most important tasks and features of the site](https://www.w3.org/TR/coga-usable/#x4-3-1-make-it-easy-to-find-the-most-important-tasks-and-features-of-the-site-pattern): call out key tasks on the home page, near the top, in the source order as well as visually.
- [Make the site hierarchy easy to understand and navigate](https://www.w3.org/TR/coga-usable/#x4-3-2-make-the-site-hierarchy-easy-to-understand-and-navigate-pattern): logical sections, menu terms people use, and sub-menus that are obvious and easy to open.
- [Use a clear and understandable page structure](https://www.w3.org/TR/coga-usable/#x4-3-3-use-a-clear-and-understandable-page-structure-pattern): logical sections, clear visual separation, headings that say what each region is.
- [Make it easy to find the most important actions and information on the page](https://www.w3.org/TR/coga-usable/#x4-3-4-make-it-easy-to-find-the-most-important-actions-and-information-on-the-page-pattern): critical actions and safety information visible without scrolling or hover.
- [Break media into chunks](https://www.w3.org/TR/coga-usable/#x4-3-5-break-media-into-chunks-pattern): short, logical, labeled segments that can be reached directly.
- [Provide search](https://www.w3.org/TR/coga-usable/#x4-3-6-provide-search-pattern): with autocomplete, spelling help, grouped results, and access to past searches.

## WCAG criteria that touch it

Numbers, titles, and levels checked against the WCAG 2.2 Recommendation of 12 December 2024. Level AAA rows are not our target; they show how far WCAG reaches.

| SC | Title | Level | Entry | Overlap |
|---|---|---|---|---|
| 1.3.1 | Info and Relationships | A | `wcag/sc-1.3.1-info-and-relationships.md` | Structure shown visually is also in the code: headings, lists, regions |
| 2.4.1 | Bypass Blocks | A | `wcag/sc-2.4.1-bypass-blocks.md` | A way past repeated blocks to the main content |
| 2.4.5 | Multiple Ways | AA | `wcag/sc-2.4.5-multiple-ways.md` | More than one way to locate a page; search is one option |
| 2.4.6 | Headings and Labels | AA | `wcag/sc-2.4.6-headings-and-labels.md` | Headings that describe what a section holds |
| 1.4.13 | Content on Hover or Focus | AA | `wcag/sc-1.4.13-content-on-hover-or-focus.md` | Menus revealed on hover must be dismissible, hoverable, and persistent |
| 3.2.3 | Consistent Navigation | AA | no entry yet | Menus in the same relative order on every page |
| 2.4.10 | Section Headings | AAA | no entry yet | Headings used to organize content |

## Where WCAG stops

WCAG requires that structure is coded, that there is more than one way to reach a page, and that headings describe. It does not require that the important task is prominent or above the fold, that menu categories match how the audience thinks, that sub-menus are noticeable, that a path to a key task is short, that search tolerates misspelling or remembers past queries, or that long media is chunked and labeled. Multiple Ways is satisfied by a site map that a person with an executive function impairment may never think to use.

## How it is used

- **Consult** asks what the one or two most important tasks are for the people in the spec and checks that the design puts them first; it challenges deep menus and hover-only sub-menus.
- **Verify** might report: a key action reachable only through a hover menu (likely, this entry, with 1.4.13 checked separately); a long video with no chapters or transcript link (manual review, this entry; captions are a separate WCAG question under 1.2.2).
- **ux** entries, when they exist, carry the research on menu labeling and findability.
