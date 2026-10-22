# SC 1.4.13 Content on Hover or Focus

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 1 Perceivable / 1.4 Distinguishable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Where receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, the following are true:
>
> **Dismissible.** A mechanism is available to dismiss the additional content without moving pointer hover or keyboard focus, unless the additional content communicates an input error or does not obscure or replace other content;
>
> **Hoverable.** If pointer hover can trigger the additional content, then the pointer can be moved over the additional content without the additional content disappearing;
>
> **Persistent.** The additional content remains visible until the hover or focus trigger is removed, the user dismisses it, or its information is no longer valid.
>
> Exception: The visual presentation of the additional content is controlled by the user agent and is not modified by the author.
>
> Note 1: Examples of additional content controlled by the user agent include browser tooltips created through use of the HTML title attribute [HTML].
>
> Note 2: Custom tooltips, sub-menus, and other nonmodal popups that display on hover and focus are examples of additional content covered by this criterion.
>
> Note 3: This criterion applies to content that appears in addition to the triggering component itself. Since hidden components that are made visible on keyboard focus (such as links used to skip to another part of a page) do not present additional content they are not covered by this criterion.

## What it requires, in our words

Custom tooltips, hover menus, and preview popups must behave in three ways. A person can close them without moving the mouse or focus, usually with Escape, so that a popup covering what they were reading can be got rid of. A person can move the mouse onto the popup without it vanishing, because screen magnifier users need to pan over to read it. The popup stays until the person moves away or dismisses it, rather than disappearing on a timer. The browser's own tooltip from the `title` attribute is exempt because the author does not control it. A skip link that appears on focus is not "additional content" and is not covered.

## How it fails in code

- Content shown on hover that disappears when the pointer moves from the trigger toward it, because the popup is not adjacent or has a gap. Definite once observed. F95.
- A hover or focus popup that obscures other content and cannot be closed with Escape or another non-moving action. Definite once confirmed.
- A tooltip that hides on a timeout while hover or focus remains. Definite.
- A hover popup that cannot be triggered by keyboard focus at all. That is SC 2.1.1 territory, but check this criterion once focus can trigger it.
- A tooltip from the `title` attribute alone. Exempt; note that `title` has its own problems under 4.1.2 and is not reachable by touch.

## How to meet it

- Technique SCR39, "Making content on focus or hover hoverable, dismissible, and persistent": position the popup adjacent to or overlapping the trigger, keep it open while the pointer is over either, close on Escape, and never close on a timer.
- Consider whether the content needs to be a popup at all. Visible helper text beside a field has none of these problems. The `patterns` entry for tooltips, when it exists, carries that discussion.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.1.1 Keyboard (no entry yet). Whether the popup can be opened by keyboard.
- SC 2.4.7 Focus Visible (no entry yet). Whether focus on the trigger is visible.
- SC 3.2.1 On Focus (no entry yet). A popup on focus must not change context.
- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`). Whether the popup's text is associated with its trigger.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. The three behaviors are observed by hovering, focusing, and pressing Escape, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
