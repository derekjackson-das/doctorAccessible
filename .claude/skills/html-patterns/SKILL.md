---
name: html-patterns
description: Build common things with native HTML first. Use when writing or reviewing markup for forms, tables, landmarks, headings, images, links, buttons, dialogs, or any custom control, and whenever ARIA or a click handler on a div is about to be added. Maps each question to a knowledge entry; reaches for ARIA only when no native element does the job.
---

# HTML patterns

This skill is a map and a set of rules. The knowledge is in `knowledge/html/`, which points to `knowledge/aria/` where ARIA is genuinely needed and to `knowledge/wcag/` for what is required. The rules for citing are in the `wcag` skill and apply here unchanged.

## When this applies

Writing or changing markup: any form, table, page region, heading, image, link, button, dialog, or interactive control. Also when reviewing code that uses `role=`, `aria-*`, `tabindex`, or a click handler on an element that is not a link or a button.

## Rules

1. **Native first.** Before writing ARIA or a custom control, open `knowledge/html/custom-controls.md` and check whether a native element does the job. If it does, say so and use it (`aria/using-aria.md`, rule 1).
2. **A link goes somewhere; a button does something.** Never a `div` or `span` with a click handler.
3. **Not using the native element is never a finding on its own.** Report a failure only through the criterion it breaks, once, at the confidence the `wcag/` entry gives.
4. **HTML conformance is not WCAG.** Breaking an HTML Standard rule, such as a skipped heading level or a plain layout table (one with `th` or `caption` is a 1.3.1 failure), is reported under a WCAG criterion only when that criterion's entry says so; otherwise it is advice, with the HTML section cited.
5. **ARIA only from the `aria/` entries.** When ARIA is needed, open the matching `aria/patterns/` entry and `aria/aria-in-html.md` for what the element allows; check names with `aria/accessible-name.md`.
6. Never state a criterion number, title, or level, or an HTML Standard section, from memory. Open the entry. If there is none, say "no entry yet" and mark the claim unverified.
7. Advise and describe; do not silently rewrite the developer's markup.

## Where to look

| Question | Read |
|---|---|
| How do I label a field, group controls, mark required fields? | `knowledge/html/forms.md` |
| How do I mark up a data table? Can I use a table for layout? | `knowledge/html/tables.md` |
| Which regions does a page need, and how many `nav` or `main`? | `knowledge/html/landmarks.md` |
| Which heading level, and can I skip one? | `knowledge/html/headings.md`; what a heading says: `knowledge/content/headings.md` |
| Does this image need alt text, and what kind? | `knowledge/html/images.md`; what it says: `knowledge/content/alt-text.md` |
| Link or button? What makes a real link? | `knowledge/html/links.md`, `knowledge/html/buttons.md` |
| How do I build a button, a toggle, an icon button? | `knowledge/html/buttons.md` |
| How do I build a modal? | `knowledge/html/dialogs.md`, then `knowledge/aria/patterns/modal-dialog.md` |
| Is there a native element for this control? | `knowledge/html/custom-controls.md` |
| The ARIA for a widget with no native element | `knowledge/aria/patterns/` (`tabs.md`, `tooltip.md`, `carousel.md`, `autocomplete.md`, `infinite-scroll.md`, `date-picker.md`, `accordion.md`, `modal-dialog.md`) |
| Should this widget exist at all? | `knowledge/patterns/`, and the `consult` skill |
| The criteria themselves | `knowledge/INDEX.md`, then the `wcag/` entry |

## Output shape for a finding

```
WCAG 2.2 SC x.x.x Title (Level A or AA), tier 1
Confidence: definite | likely | manual review (from the wcag/ entry)
Where: <selector or file:line>
What: <one sentence>
Native fix: <the element to use, from the html/ entry>
HTML entry: knowledge/html/<topic>.md
```

Advice that breaks no criterion:

```
Advice, not a WCAG finding: <the point>
Source: HTML Living Standard §x.x, accessed <date>, or the aria/ entry
Where: <selector or file:line>
```
