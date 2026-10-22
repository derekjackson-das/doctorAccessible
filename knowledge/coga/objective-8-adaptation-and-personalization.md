# COGA Objective 8: Support adaptation and personalization

- Source: W3C, Making Content Usable for People with Cognitive and Learning Disabilities, Working Group Note, 29 April 2021
- Tier: 2, informative from W3C. A Working Group Note is guidance, not a conformance requirement. Meeting it is not needed to conform to WCAG 2.2, and missing it is not a WCAG failure.
- Objective: https://www.w3.org/TR/coga-usable/#x4-9-objective-8-support-adaptation-and-personalization
- User stories: https://www.w3.org/TR/coga-usable/#x3-8-objective-8-support-adaptation-and-personalization
- User-need map: https://www.w3.org/TR/coga-usable/#a-8-objective-8-support-adaptation-and-personalization
- Verified against the live source: 2026-10-22 by Caesar Alam with Claude Code, direct fetch of the Note and of the WCAG 2.2 Recommendation for every criterion cited

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. When the same defect also fails a WCAG criterion, report it once, under that criterion and its entry, and name this entry as context. The Note points to the W3C personalization semantics work for one technique; that specification is not on `knowledge/SOURCES.md` and is not cited here.

## The objective in plain words

For a large share of people with cognitive and learning disabilities, the assistive technology is a browser extension, a password manager, a reading tool, or a symbol toolbar. Content must not break them. Beyond that, let people shape the interface: hide what they do not use, choose a simpler version, keep a familiar layout, adjust spacing and type, and control when things move or change. Standard HTML and standard semantics are what make this possible.

## User needs it serves

- **Adapt.** People with memory or executive function impairments, including people with dementia, need an interface that stays familiar: controls where they expect them, a version they recognize, simpler language or formats they can choose, symbols and pictures they already know, extra white space when they need it, alternatives to math, and less content with extras available on request.
- **Extensions and APIs.** People who use add-ons as assistive technology need them to work: spelling and grammar tools, read-aloud, password managers, and toolbars that add symbols or reformat the page.

## Patterns W3C lists

- [Let users control when the content moves or changes](https://www.w3.org/TR/coga-usable/#x4-9-1-let-users-control-when-the-content-moves-or-changes-pattern): changes of context, settings, route, and orientation only on request, with a way back.
- [Enable APIs and extensions](https://www.w3.org/TR/coga-usable/#x4-9-2-enable-apis-and-extensions-pattern): content that works with the user's extensions and standard interfaces.
- [Support simplification](https://www.w3.org/TR/coga-usable/#x4-9-3-support-simplification-pattern): hide non-essential features, offer simpler text or another format, with extras still findable.
- [Support a personalized and familiar interface](https://www.w3.org/TR/coga-usable/#x4-9-4-support-a-personalized-and-familiar-interface-pattern): user choice of font, size, spacing, and contrast; rollback to a familiar version; semantics such as `autocomplete` that let tools adapt the page.

## WCAG criteria that touch it

Numbers, titles, and levels checked against the WCAG 2.2 Recommendation of 12 December 2024. Level AAA rows are not our target; they show how far WCAG reaches.

| SC | Title | Level | Entry | Overlap |
|---|---|---|---|---|
| 1.3.5 | Identify Input Purpose | AA | `wcag/sc-1.3.5-identify-input-purpose.md` | Field purpose in code, so autofill and symbol tools can act on it |
| 1.4.4 | Resize Text | AA | `wcag/sc-1.4.4-resize-text.md` | Text can be enlarged without loss |
| 1.4.10 | Reflow | AA | `wcag/sc-1.4.10-reflow.md` | Content works at narrow widths and high zoom |
| 1.4.12 | Text Spacing | AA | `wcag/sc-1.4.12-text-spacing.md` | Content survives user-set spacing, the hook for spacing tools |
| 4.1.2 | Name, Role, Value | A | `wcag/sc-4.1.2-name-role-value.md` | Exposed names and roles let tools understand controls |
| 2.2.2 | Pause, Stop, Hide | A | `wcag/sc-2.2.2-pause-stop-hide.md` | User control over moving and updating content |
| 3.2.1 | On Focus | A | no entry yet | Receiving focus does not change context |
| 3.2.2 | On Input | A | no entry yet | Changing a setting does not change context unless the user was told first |
| 1.3.4 | Orientation | AA | `wcag/sc-1.3.4-orientation.md` | Content is not locked to portrait or landscape unless essential |
| 1.3.6 | Identify Purpose | AAA | no entry yet | Purpose of components, icons, and regions programmatically determinable |
| 3.2.5 | Change on Request | AAA | no entry yet | Changes of context only on request, or can be turned off |
| 1.4.8 | Visual Presentation | AAA | no entry yet | User-selectable colors and comfortable line length and spacing |

## Where WCAG stops

WCAG at A and AA requires that content survives the user's own adjustments to text size, spacing, and width, and that fields about the user carry their purpose. On Focus and On Input stop focus or an unannounced setting change from switching context, and Orientation stops content locking to one orientation; full user control over changes of context is AAA. It does not require that a site offers a simplified version, lets people hide features, keeps a familiar version available after a redesign, or exposes the purpose of icons and regions (AAA). Nothing at our target forbids code that blocks extensions, such as disabling paste outside authentication, overriding spellcheck, or rendering text into a canvas, unless another criterion catches the specific case.

## How it is used

- **Verify** might report: `spellcheck="false"` or a paste block on a free-text field (likely, this entry); text drawn into a canvas element that read-aloud tools cannot reach (check 1.4.5 and 1.1.1 first and report once there if either fails; otherwise likely, this entry); a redesign with no way back to the previous layout (manual review).
- **Consult** asks whether the audience in the spec relies on add-ons, and whether a planned redesign leaves returning users a familiar path.
- **aria** entries, when they exist, carry the semantics side.
