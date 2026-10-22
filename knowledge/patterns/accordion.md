# Pattern: Accordion

- Sources:
  - W3C, "Accordion Pattern (Sections With Show/Hide Functionality)", ARIA Authoring Practices Guide, https://www.w3.org/WAI/ARIA/apg/patterns/accordion/. Tier 2. A pattern, not a requirement.
  - W3C, "Disclosure (Show/Hide) Pattern", ARIA Authoring Practices Guide, https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/. Tier 2.
  - Adrian Roselli, "Progressively Enhanced HTML Accordion", 9 August 2023, updated 30 September 2025, https://adrianroselli.com/2023/08/progressively-enhanced-html-accordion.html. Tier 3.
  - Sara Soueidan, "How do you mark up an accordion?", 3 September 2018, https://www.sarasoueidan.com/blog/accordion-markup/. Tier 3.
  - Heydon Pickering, "Collapsible Sections", Inclusive Components, 26 October 2017, https://inclusive-components.design/collapsible-sections/. Tier 3.
- Related entries: `coga/objective-2-find-what-they-need.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.6-headings-and-labels.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the accordion is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer.

## The need it usually serves

A page has several sections and the team wants it to look shorter. The person wants to find the one section they need and read it. Frequently asked questions pages are the usual case. The accordion hides every answer until its question is pressed.

## The simpler thing that often serves, and what is lost

Headings and visible content, with a table of contents at the top if the page is long. Soueidan (2018) walks through the markup choices for a question-and-answer list and arrives at headings with answers beneath them as the sound base, with the accordion as an enhancement on top. What is lost by not collapsing: the short first impression, and the ability to scan questions without answers in between. What is gained: find-in-page works, every answer is in the accessibility tree, printing works, and nothing is built. `coga/objective-2-find-what-they-need.md` covers the cognitive side: key information visible without extra steps.

If collapsing stays, the question is whether it is one disclosure or an accordion. Roselli (2023) holds that an accordion means only one section open at a time; otherwise it is a set of independent disclosures that may not need to be grouped at all.

## What doing it right requires

Native first: the HTML `details` and `summary` elements give a keyboard-operable disclosure with exposed state and no script. Roselli (2023) builds an accordion from a set of them, wrapped in a named group, with a few lines of script to close the others when one opens, and notes that without the script the page still works. His caveat from testing: Chromium browsers expand a `details` element when find-in-page matches text inside it, which Firefox and Safari did not do at the time, so a one-open-at-a-time rule has to tolerate the browser opening several.

The APG accordion pattern's expectations, in our words: each header is a control; Enter or Space toggles its section; every header is in the page tab sequence; if only one may be open, opening one closes the other. The APG disclosure pattern is the single-section case with the same Enter and Space behavior.

Pickering (2017) describes the scripted version when the native elements will not do: a real `button` inside the heading, so the heading keeps its level for navigation and the button carries the state in `aria-expanded`; never a heading given a button role, which destroys the heading. He found `aria-controls` was honored only by JAWS at the time, and recommends relying on source order instead. He ties the visual indicator to the state attribute so the two cannot drift apart.

What the APG does not say: whether the content should be hidden at all, and what to do about find-in-page and printing.

## What practitioners found when they tested it

- **Roselli, 2023, updated 2025.** `details` and `summary` work with a keyboard in all evergreen browsers; the find-in-page expansion in Chromium is the behavior to design around. A named `section` becomes a region for screen reader users, which may be noise; a group role is the quieter choice.
- **Pickering, 2017.** With the button inside the heading, a screen reader announces the button and the heading level together, so the user keeps both. `aria-controls` support was JAWS-only.
- **Soueidan, 2018.** Marking up questions and answers as a definition list with wrapper `div` elements was valid HTML but, citing Steve Faulkner's tests, changed how some browsers exposed the list to screen readers; headings plus content avoided the problem.

## Criteria it touches

Structure: `wcag/sc-1.3.1-info-and-relationships.md` for real headings and the relationship between control and content. Control name, role, and expanded state: `wcag/sc-4.1.2-name-role-value.md`. Keyboard operation: `wcag/sc-2.1.1-keyboard.md`. Header text: `wcag/sc-2.4.6-headings-and-labels.md`. Focus: `wcag/sc-2.4.7-focus-visible.md`, `wcag/sc-2.4.3-focus-order.md`. Indicator contrast: `wcag/sc-1.4.11-non-text-contrast.md`. Hidden content that must survive text spacing and reflow when opened: `wcag/sc-1.4.12-text-spacing.md`, `wcag/sc-1.4.10-reflow.md`.

## Manual tests it demands

- Keyboard: Tab to each header; press Enter, then Space; record that each toggles and that focus stays on the header.
- Screen reader, each pair in the spec: record what is announced on the header (name, role, expanded or collapsed, heading level) and after toggling.
- Find-in-page for a word inside a closed section; record what each browser does.
- Print preview; record whether closed sections print.
- 400% zoom and text spacing override on an open section; record clipping.

## What consult should say

1. Would the person rather scan questions or read answers? If they came for one answer, a heading they can jump to serves them; collapsing adds a step.
2. One open at a time, or independent? If independent, plain `details` elements, no accordion.
3. If it stays: native elements first, headings kept, find-in-page and print checked.
