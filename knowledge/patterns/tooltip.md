# Pattern: Tooltip

- Sources:
  - W3C, "Tooltip Pattern", ARIA Authoring Practices Guide, https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/. Tier 2. A pattern, not a requirement, and the page itself says it is work in progress without task force consensus.
  - Sarah Higley, "Tooltips in the time of WCAG 2.1", 17 August 2019, https://sarahmhigley.com/writing/tooltips-in-wcag-21/. Tier 3.
  - Heydon Pickering, "Tooltips & Toggletips", Inclusive Components, 25 July 2017, https://inclusive-components.design/tooltips-toggletips/. Tier 3.
- Related entries: `coga/objective-1-understand-what-things-are.md`, `wcag/sc-1.4.13-content-on-hover-or-focus.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.5.8-target-size-minimum.md`
- Verified against the live sources: 2026-10-22 by Derek Jackson with Claude Code

## Status and reporting

A finding that rests only on this entry is reported as likely or manual review, never definite. A WCAG failure in the tooltip is reported once, under its criterion. In consult, this entry supports a question or a recommendation; it does not decide for the developer.

## The need it usually serves

A control is unclear, usually an icon with no text, and the team adds a small popup to explain it. Or there is helpful detail the design has no room for. Both are symptoms: the control should have a visible name, and the detail should have a visible place.

## The simpler thing that often serves, and what is lost

Visible text. Pickering (2017) puts it plainly: most of the time the icon should have text beside it, and a field should have a permanently visible label, because real text is understood by everyone and read by screen readers without any extra work. Higley (2019) narrows the word "tooltip" to purely supplemental hint text that is never required to operate the control; anything that is the control's name belongs in the name, and anything interactive or rich is not a tooltip and should be a disclosure or a dialog. What is lost by choosing visible text: a little space and a cleaner look. What is gained: no hover, no delay, no dismissal problem, nothing hidden from touch users, and `coga/objective-1-understand-what-things-are.md` is met without effort.

## What doing it right requires

There is no adequate native tooltip. Both practitioners rule out the HTML `title` attribute: Pickering found it exposed reliably by screen readers only on form controls and never shown to touch or keyboard users; Higley traces the same mouse-only design back to the attribute's origins. The 1.4.13 entry notes the browser's own `title` tooltip is exempt from that criterion precisely because the author does not control it, which is not the same as it being good.

The APG pattern's expectations, in our words: the tooltip appears on focus or hover of its trigger after a small delay, is dismissed by Escape or when the pointer leaves, and never takes focus itself; a popup that contains anything focusable is not a tooltip but a non-modal dialog. The 1.4.13 entry supplies the three behaviors a custom tooltip must have: dismissible without moving focus, hoverable, and persistent.

Pickering's two shapes: a true tooltip, tied to its trigger with a description relationship so a screen reader reads it on focus, used only for supplementary text; and a "toggletip", a button that reveals a short message in a live region on press, for information the person asks for rather than stumbles on. He notes the tooltip role's practical value is to make the description association reliable.

What the APG does not say: it has no consensus, by its own notice. Treat it as the least settled pattern in the guide.

## What practitioners found when they tested it

- **Pickering, 2017.** The `title` attribute worked reliably in screen readers only on form elements; keyboard and touch users never saw it. A tooltip that is really the control's label should be the label; a tooltip that adds detail is supplementary and goes in the description, not the name.
- **Higley, 2019.** Every historical tooltip mechanism made it easy to build for mouse users with good vision and forget everyone else. Her specification for an acceptable tooltip: readable by mouse, keyboard, screen reader, and zoom software; never required to operate the control; never blocking any other action. She points at the 2.1 criteria that made hover content a conformance matter.

## Criteria it touches

Behavior of the popup: `wcag/sc-1.4.13-content-on-hover-or-focus.md`. The trigger's name and the tooltip's association: `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-2.5.3-label-in-name.md` if the visible text and the name differ. Keyboard reach of the trigger: `wcag/sc-2.1.1-keyboard.md`. Icon-only trigger size and contrast: `wcag/sc-2.5.8-target-size-minimum.md`, `wcag/sc-1.4.11-non-text-contrast.md`. Tooltip text contrast: `wcag/sc-1.4.3-contrast-minimum.md`. A tooltip that appears on focus must not change context: `wcag/sc-3.2.1-on-focus.md`. Instructions that live only in a tooltip: `wcag/sc-3.3.2-labels-or-instructions.md`.

## Manual tests it demands

- Keyboard: Tab to the trigger; record whether the tooltip appears, whether Escape dismisses it without moving focus, and whether anything inside it can be reached.
- Pointer: hover the trigger, move onto the tooltip; record whether it stays. Wait; record whether it disappears on a timer.
- Screen reader, each pair in the spec: record what is announced on the trigger, and whether the tooltip text is read as name, description, or not at all.
- Touch: record whether the information is reachable at all.
- Zoom and magnification: record whether the tooltip stays within the viewport and near its trigger.

## What consult should say

1. What is this text for? If it is the control's name, make it visible text and stop.
2. Does the person need it to use the control? If yes, it is an instruction and belongs on the page.
3. If a tooltip stays: supplementary only, the 1.4.13 behaviors, no `title` attribute, and a toggletip if the information is asked for rather than hovered over.
