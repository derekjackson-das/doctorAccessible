# COGA Objective 1: Help users understand what things are and how to use them

- Source: W3C, Making Content Usable for People with Cognitive and Learning Disabilities, Working Group Note, 29 April 2021
- Tier: 2, informative from W3C. A Working Group Note is guidance, not a conformance requirement. Meeting it is not needed to conform to WCAG 2.2, and missing it is not a WCAG failure.
- Objective: https://www.w3.org/TR/coga-usable/#x4-2-objective-1-help-users-understand-what-things-are-and-how-to-use-them
- User stories: https://www.w3.org/TR/coga-usable/#x3-1-objective-1-help-users-understand-what-things-are-and-how-to-use-them
- User-need map: https://www.w3.org/TR/coga-usable/#a-1-objective-1-help-users-understand-what-things-are-and-how-to-use-them
- Verified against the live source: 2026-10-22 by Caesar Alam with Claude Code, direct fetch of the Note and of the WCAG 2.2 Recommendation for every criterion cited

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. When the same defect also fails a WCAG criterion, report it once, under that criterion and its entry, and name this entry as context.

## The objective in plain words

A person should be able to tell, without learning anything new, what a page is for, where they are, what the controls are, and what each control will do. The surest way is to use designs people already know: links that look like links, buttons that look like buttons, layouts that match the rest of the web and the rest of the site. Every new icon, term, or interaction is something a person with a memory or learning impairment may not manage to learn.

## User needs it serves

The Note groups this objective under three user stories.

- **Clear purpose.** People with memory, attention, or executive function impairments, and people who communicate with symbols, need to know what a site and a page offer, whether they are in the right place, and where they are in a site or a multi-step process, including after they have been distracted. The same holds inside video: what it contains and how to get back to the point they lost.
- **Clear operation.** People with memory impairments, learning disabilities, or executive function impairments, and people who communicate with symbols, find new interface conventions hard to learn. They need to know which things are controls and which are not, how each control works, what will happen when they use it, and that controls will not move or be easy to trigger by accident.
- **Symbols.** People with language impairments may rely on familiar symbols placed with key content such as controls and headings, ideally symbols they already know or can personalize.

## Patterns W3C lists

- [Make the purpose of your page clear](https://www.w3.org/TR/coga-usable/#x4-2-1-make-the-purpose-of-your-page-clear-pattern): a title or heading that says what the page is for, or another signpost tested with users.
- [Use a familiar hierarchy and design](https://www.w3.org/TR/coga-usable/#x4-2-2-use-a-familiar-hierarchy-and-design-pattern): common layouts, affordances, and visual hierarchy rather than novel ones.
- [Use a consistent visual design](https://www.w3.org/TR/coga-usable/#x4-2-3-use-a-consistent-visual-design-pattern): the same look and placement across related pages.
- [Make each step clear](https://www.w3.org/TR/coga-usable/#x4-2-4-make-each-step-clear-pattern): breadcrumbs or headings for orientation; in a process, show steps done, the current step, steps left, and key choices made.
- [Clearly identify controls and their use](https://www.w3.org/TR/coga-usable/#x4-2-5-clearly-identify-controls-and-their-use-pattern): controls styled and behaving the way people expect, so it is obvious what can be activated, and big enough to hit without catching the one beside it.
- [Make the relationship clear between controls and the content they affect](https://www.w3.org/TR/coga-usable/#x4-2-6-make-the-relationship-clear-between-controls-and-the-content-they-affect-pattern): group controls with their content, separate regions clearly, and avoid nested scrolling areas.
- [Use icons that help the user](https://www.w3.org/TR/coga-usable/#x4-2-7-use-icons-that-help-the-user-pattern): familiar icons beside important controls and headings, one meaning each.

## WCAG criteria that touch it

Numbers, titles, and levels checked against the WCAG 2.2 Recommendation of 12 December 2024. Level AAA rows are not our target; they show how far WCAG reaches.

| SC | Title | Level | Entry | Overlap |
|---|---|---|---|---|
| 2.4.2 | Page Titled | A | `wcag/sc-2.4.2-page-titled.md` | A title that describes the page; the code side of a clear purpose |
| 2.4.6 | Headings and Labels | AA | `wcag/sc-2.4.6-headings-and-labels.md` | Headings and labels that describe topic or purpose |
| 3.2.3 | Consistent Navigation | AA | no entry yet | Repeated navigation in the same relative order across pages |
| 3.2.4 | Consistent Identification | AA | no entry yet | The same function identified the same way across pages |
| 4.1.2 | Name, Role, Value | A | `wcag/sc-4.1.2-name-role-value.md` | Controls expose what they are to assistive technology |
| 1.1.1 | Non-text Content | A | `wcag/sc-1.1.1-non-text-content.md` | Icons that act as controls or carry meaning need a text alternative |
| 1.4.11 | Non-text Contrast | AA | `wcag/sc-1.4.11-non-text-contrast.md` | The visual cues that identify a control must be perceivable |
| 1.4.1 | Use of Color | A | `wcag/sc-1.4.1-use-of-color.md` | Color is not the only cue, so a link told apart from text by color alone fails |
| 2.5.8 | Target Size (Minimum) | AA | `wcag/sc-2.5.8-target-size-minimum.md` | A floor on pointer target size or spacing, against accidental activation; new in WCAG 2.2 |
| 2.4.8 | Location | AAA | no entry yet | Information about where the user is in a set of pages |
| 1.3.6 | Identify Purpose | AAA | no entry yet | The purpose of components, icons, and regions is programmatically determinable |

## Where WCAG stops

WCAG at A and AA asks that a page has a descriptive title, that headings and labels describe, that controls expose a name and role, and that navigation and identification are consistent. Use of Color rules out color as the only cue and Target Size sets a minimum size, but neither asks that controls look like the controls people already know. WCAG does not ask that the purpose is understandable to someone with a memory or attention impairment, that a site uses conventions people already know, that icons are familiar, that a multi-step process shows progress (location is AAA), or that controls sit next to the content they change. A page can conform and still be unusable for a person who cannot learn a new interface.

## How it is used

- **Consult** asks whether the page's purpose is clear in the first screen, whether any pattern or icon is new to the audience in the spec, and whether a process needs a progress indicator.
- **Verify** might report: a multi-step form with no indication of the current step (likely, this entry; 2.4.8 named as AAA context); an icon-only control with no accessible name (definite under 1.1.1 or 4.1.2, not under this entry); a named but unfamiliar icon (manual review, this entry).
- **Content** reads it with `docs/content-standards.md` for headings and labels.
