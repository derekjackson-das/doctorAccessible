# Pattern: Tooltip and toggletip

- W3C pattern (tier 2): ARIA Authoring Practices Guide, "Tooltip Pattern", accessed 2026-10-22 (the page shows no date). https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/ A pattern, not a requirement. The page itself says it is a work in progress without task force consensus, and it has no example.
- W3C tutorial: none.
- Practitioner sources (tier 3, on `knowledge/SOURCES.md`). None reports a test of tooltips with assistive technology:
  - Sarah Higley, "Tooltips in the time of WCAG 2.1", 17 August 2019. https://sarahmhigley.com/writing/tooltips-in-wcag-21/ Requirements and best practices.
  - Heydon Pickering, "Tooltips & Toggletips", Inclusive Components, 25 July 2017. https://inclusive-components.design/tooltips-toggletips/ Build guidance for both.
  - Hidde de Vries, "Semantics and the popover attribute: which role to use when?", 16 May 2023, updated 30 April 2024. https://hidde.blog/popover-semantics/ Which role to give popover-based tooltips.
  - Hidde de Vries and Scott O'Hara, "On popover accessibility: what the browser does and doesn't do", 21 March 2024, updated 15 March 2025. https://hidde.blog/popover-accessibility/ Tested what the `popover` attribute exposes, with JAWS 2023 and NVDA 2023.3.4 in Edge 124. Relevant to toggletips built with `popover`.
- Related entries: `wcag/sc-1.4.13-content-on-hover-or-focus.md`, `wcag/sc-4.1.2-name-role-value.md`, `patterns/modal-dialog.md`, `patterns/accordion.md`; `aria/patterns/tooltip.md` (the roles, states, naming, keyboard, and the ARIA test results).
- Verified against the live sources: 2026-10-22 by Caesar Alam with Claude Code

## Status and reporting

The criteria listed below decide whether code fails WCAG; report a failure once, under its criterion. Everything else here is advice. Using this pattern, or not using the simpler alternative, is never a finding on its own. A departure from the Authoring Practices is likely or manual review at most, and only when a criterion entry or a practitioner test ties it to a real barrier.

**Testing gap.** No source on the list reports testing a tooltip or toggletip with assistive technology, and the W3C pattern lacks task force consensus. The guidance below is expert advice from 2017 to 2019, plus one 2024 test of the `popover` attribute. Every point needs confirming in the manual tests. a11ysupport.io, also on the list, renders its results with script and could not be read for this entry.

## The need

A short hint about a control without taking up space on screen: what an icon-only button does, or what a form field expects.

## The simpler alternative and its cost

- **Show the text.** A visible label beside an icon, or visible hint text under a field. Every person sees it, on every device, with no hover, focus, or script. Higley's advice is that nothing needed to use the interface should be in a tooltip. The cost: screen space and visual density, and longer labels in some languages.
- **A toggletip.** A small button, often marked "i", that shows the note when pressed and works the same for mouse, keyboard, and touch (Pickering). The cost: an extra press and one more control. The sources do not agree on how to build one (below).

## What doing it right requires

- **The name never depends on the tooltip alone.** An icon-only button needs an accessible name whether or not a tooltip repeats it; Higley allows a tooltip to supply that name through `aria-labelledby`, but the tip itself may never be seen.
- **Never essential, never interactive.** A tooltip holds plain text that helps but is not needed, with no links or buttons inside (Higley). If the content needs structure or controls, use a non-modal dialog instead (de Vries, 2023).
- **Do not use the `title` attribute** as the tooltip. It is unreliable for keyboard, touch, and screen reader users (Higley; Pickering).
- **Connect it to the control.** The Authoring Practices give the tip the `tooltip` role and point to it from the trigger with `aria-describedby`. How much the role helps is disputed: Higley found it did not change screen reader announcements; Pickering saw it as making the description work more reliably; de Vries notes it matters most when the trigger is not itself interactive. Use both, and rely on `aria-describedby`. Only interactive elements should trigger tooltips (Higley).
- **Show on hover and focus; let people dismiss it and reach it.** Escape dismisses it and the pointer can move onto it without it closing (Authoring Practices; Higley). The sources differ on when it closes: the Authoring Practices close it on blur and when the pointer leaves both trigger and tip, which SC 1.4.13 allows; Higley prefers it to stay until dismissed or no longer relevant, with no timeout. Either way, a timeout alone is not enough. Higley notes Escape suits keyboard users but not mouse users, so offer a pointer way to dismiss too.
- **Touch and eye gaze could not reach tooltips on buttons or links** when Higley wrote in 2019, because those inputs cannot focus without activating. This is the strongest reason to show the text or use a toggletip.
- **Toggletips: the sources differ on the build.** Pickering's toggletip writes the note into a `role="status"` live region when the button is pressed, so it is announced on request. Higley advises against creating a control only to show a tip, and against live regions for tooltips. De Vries suggests a non-modal dialog opened on click for anything beyond plain text. A disclosure button that shows the note in place (`patterns/accordion.md`) is a fourth option. All four meet the need; choose one, and test it.
- **Built with `popover`:** browsers return focus to the trigger on close if focus was inside the popover, and desktop browsers put the popover's content next in the tab order after its trigger. When the popover does not directly follow its trigger in the accessibility tree, browsers add a "has details" link; de Vries and O'Hara found it was not announced until the popover had opened, and only after moving away and back, in JAWS and NVDA with Edge in 2024. Safari set only the expanded state.

## Criteria it touches

| SC | Title | Level | Entry | Why it comes up |
|---|---|---|---|---|
| 1.4.13 | Content on Hover or Focus | AA | `wcag/sc-1.4.13-content-on-hover-or-focus.md` | Dismissible, hoverable, and persistent |
| 4.1.2 | Name, Role, Value | A | `wcag/sc-4.1.2-name-role-value.md` | An icon-only control's accessible name |
| 1.1.1 | Non-text Content | A | `wcag/sc-1.1.1-non-text-content.md` | Text alternative for the icon itself |
| 2.1.1 | Keyboard | A | `wcag/sc-2.1.1-keyboard.md` | Tooltip shown on keyboard focus; toggletip operable by keyboard |
| 2.5.3 | Label in Name | A | `wcag/sc-2.5.3-label-in-name.md` | When visible tooltip text acts as the label |
| 3.3.2 | Labels or Instructions | A | `wcag/sc-3.3.2-labels-or-instructions.md` | A field's instructions shown only in a tooltip |
| 1.4.3 | Contrast (Minimum) | AA | `wcag/sc-1.4.3-contrast-minimum.md` | Tooltip text against its background |
| 2.5.8 | Target Size (Minimum) | AA | `wcag/sc-2.5.8-target-size-minimum.md` | A small "i" toggletip button |
| 2.4.11 | Focus Not Obscured (Minimum) | AA | `wcag/sc-2.4.11-focus-not-obscured-minimum.md` | A tooltip or bubble covering the focused control |
| 1.4.10 | Reflow | AA | `wcag/sc-1.4.10-reflow.md` | The tip at narrow widths and high zoom |
| 4.1.3 | Status Messages | AA | `wcag/sc-4.1.3-status-messages.md` | Only if a toggletip uses a live region; a dialog or disclosure toggletip is not a status message |

## Manual tests

With the assistive technology named in the project's `a11y-spec.md`:
- Keyboard only: the tooltip appears on focus and Escape hides it without moving focus; a toggletip opens and closes with Enter or Space.
- Mouse: the pointer can move onto the tooltip without it closing; it can be dismissed with the pointer; it does not close on a timer.
- Touch and, if in scope, eye gaze: the information is available some other way, such as visible text or a toggletip.
- Screen reader: the control's name is announced; the tooltip text is exposed as its description (whether it is spoken can depend on the user's verbosity settings); a toggletip's note is announced or reachable after pressing.
- Zoom and magnification at 400%: the tooltip is fully visible and stays open while the view moves to read it.
