# Pattern: Accordion

- W3C patterns (tier 2): ARIA Authoring Practices Guide, "Accordion Pattern (Sections With Show/Hide Functionality)" and "Disclosure (Show/Hide) Pattern", accessed 2026-10-22 (the pages show no date). https://www.w3.org/WAI/ARIA/apg/patterns/accordion/ and https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/ Patterns, not requirements.
- W3C tutorial: none.
- Practitioner sources (tier 3, on `knowledge/SOURCES.md`):
  - Adrian Roselli, "Disclosure Widgets", 20 May 2020, updated 28 January 2024. https://adrianroselli.com/2020/05/disclosure-widgets.html Compared a single native `<details>`/`<summary>` with a single button-based disclosure in JAWS 2019 with Chrome 81, NVDA 2019 with Firefox 76, VoiceOver on macOS 10.15 with Safari, TalkBack on Android 10 with Chrome and Firefox, and VoiceOver on iPadOS 13.4 (2020), retested on iPadOS 16.5 (August 2023) and 17.3 (January 2024).
  - Scott O'Hara, "The details and summary elements, again", 12 September 2022. https://www.scottohara.me/blog/2022/09/12/details-summary.html How `<summary>` is exposed across NVDA, JAWS, Narrator, VoiceOver, and TalkBack with several browsers (versions not given), and what breaks when it is restyled or given a role.
  - Heydon Pickering, "Collapsible Sections", Inclusive Components, 26 October 2017. https://inclusive-components.design/collapsible-sections/ Build guidance; notes `aria-controls` worked only in JAWS at the time.
- Related entries: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-1.3.1-info-and-relationships.md`, `patterns/tabs.md`, `coga/objective-2-find-what-they-need.md`; `aria/` once that domain exists.
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

The criteria listed below decide whether code fails WCAG; report a failure once, under its criterion. Everything else here is advice. Using this pattern, or not using the simpler alternative, is never a finding on its own. A departure from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier.

**Testing gap.** The listed tests are of single disclosures, not of a full accordion of headed sections. Roselli's desktop results date from 2020 and O'Hara's 2022 results give no versions. Nothing on the list tests the newer exclusive accordion (several `<details>` sharing a `name`, so only one opens at a time), voice control, or magnification. a11ysupport.io, also on the list, renders its results with script and could not be read for this entry.

## The need

A long page of sections, such as questions and answers or a form split into parts, where people want an overview first and then open only the parts they need. Collapsing also spares keyboard users from tabbing past every control in the sections they skip (Pickering).

## The simpler alternative and its cost

- **Leave the sections open.** Headings that describe each section, with a short table of contents of same-page links at the top. Everything is visible, searchable with the browser's find, printable, and needs no script or state. The cost: a longer page with more scrolling, and no at-a-glance list of section titles unless the table of contents provides one.
- **Native `<details>` and `<summary>`.** A working show-and-hide with no script. O'Hara notes it also works in browser reader modes, and that Chromium browsers now open a closed `<details>` when find-in-page matches text inside it; Firefox and Safari did not at the time. Roselli considers it a good fit for a simple summary-then-details case. The cost: screen readers expose `<summary>` inconsistently, and restyling it breaks things (below).

## What doing it right requires

- **A real button inside a real heading.** Each header is a heading element containing only a `<button>`; do not put a button role on the heading itself, which removes it from heading navigation (Authoring Practices; Pickering).
- **State on the button:** `aria-expanded` true or false, kept in step with what is shown (Authoring Practices; Roselli).
- **`aria-controls`: the sources differ.** The Authoring Practices accordion pattern includes it on each header button; the disclosure pattern makes it optional. Roselli calls it optional with sparse support, and Pickering found in 2017 that only JAWS used it. Include it to match the accordion pattern, but do not rely on it: the panel must follow its button in the source either way.
- **The panel immediately follows its button**, and hidden panels are truly hidden with `hidden` or `display: none`, so their content is out of the tab order (Roselli; Pickering).
- **Do not move focus** when a panel opens; a person who triggered it by accident can press it again (Roselli).
- **Group and name the set** (Roselli). The Authoring Practices make panel regions optional and warn against them beyond about six panels open at once.
- **One open at a time, or many: the sources differ.** Roselli prefers only one panel open and the whole accordion no taller than the viewport, with panels scrolling inside. The Authoring Practices allow either. Decide from the need statement and test it.
- **If using `<details>` and `<summary>`**, keep the summary plain. In the tests:
  - `<summary>` was announced as "button", "summary", or "disclosure triangle" by different screen reader and browser pairs, and with no role in some (O'Hara, 2022; Roselli, 2020). Roselli's NVDA with Firefox gave no role for the button-based version either, while O'Hara reports NVDA saying "button"; the two disagree.
  - TalkBack with Firefox skipped `<summary>` entirely when moving by controls, with no state (Roselli, 2020).
  - VoiceOver on iPadOS did not expose an expanded `<summary>` as interactive in 2020, announced no state on 16.5 in 2023, and announced both states again on 17.3 in January 2024 (Roselli).
  - Removing the default marker made the state unclear in VoiceOver, JAWS, and NVDA, and adding a button role to `<summary>` dropped the state in Safari and any heading inside it (O'Hara).
- **Native or custom.** If those results matter for the assistive technology in the project's spec, build the button pattern instead. What is lost: the no-script fallback, reader-mode support, and the find-in-page opening that Chromium gives `<details>`.

## Criteria it touches

| SC | Title | Level | Entry | Why it comes up |
|---|---|---|---|---|
| 4.1.2 | Name, Role, Value | A | `wcag/sc-4.1.2-name-role-value.md` | Button role and expanded state exposed and kept current |
| 1.3.1 | Info and Relationships | A | `wcag/sc-1.3.1-info-and-relationships.md` | Section headings kept as headings |
| 2.1.1 | Keyboard | A | `wcag/sc-2.1.1-keyboard.md` | Opening and closing with Enter and Space |
| 2.4.3 | Focus Order | A | `wcag/sc-2.4.3-focus-order.md` | Hidden content taking focus; panels far from their buttons |
| 2.4.6 | Headings and Labels | AA | `wcag/sc-2.4.6-headings-and-labels.md` | Header text that says what the section holds |
| 2.4.7 | Focus Visible | AA | `wcag/sc-2.4.7-focus-visible.md` | Headers restyled to look like plain text |
| 1.4.11 | Non-text Contrast | AA | `wcag/sc-1.4.11-non-text-contrast.md` | The expand and collapse indicator |
| 1.4.10 | Reflow | AA | `wcag/sc-1.4.10-reflow.md` | Headers and panels at narrow widths and high zoom |
| 1.4.13 | Content on Hover or Focus | AA | `wcag/sc-1.4.13-content-on-hover-or-focus.md` | Only if panels open on hover or focus, which Roselli advises against |

## Manual tests

With the assistive technology named in the project's `a11y-spec.md`:
- Keyboard only: Tab reaches each header; Enter and Space toggle it; focus stays on the header; nothing in a closed panel takes focus.
- Screen reader, button pattern: each header is announced as a button with its expanded or collapsed state, and is found when navigating by headings; the state changes on activation; the opened content is read next.
- Screen reader, `<details>`: each summary is announced as something that expands, with its state, whatever role name the pairing uses; record pairings that give no state.
- Mobile screen readers (VoiceOver on iOS or iPadOS, TalkBack): the state is announced, especially for `<details>`.
- Voice control: each header can be activated by its visible text.
- Zoom to 400%: headers and panels reflow, and the expand indicator stays visible.
