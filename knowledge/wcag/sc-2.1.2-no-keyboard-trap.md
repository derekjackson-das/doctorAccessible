# SC 2.1.2 No Keyboard Trap

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.1 Keyboard Accessible
- Tier 1 source: https://www.w3.org/TR/WCAG22/#no-keyboard-trap
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> If keyboard focus can be moved to a component of the page using a keyboard interface, then focus can be moved away from that component using only a keyboard interface, and, if it requires more than unmodified arrow or tab keys or other standard exit methods, the user is advised of the method for moving focus away.
>
> Note: Since any content that does not meet this success criterion can interfere with a user's ability to use the whole page, all content on the web page (whether it is used to meet other success criteria or not) must meet this success criterion. See Conformance Requirement 5: Non-Interference.

## What it requires, in our words

Once a keyboard user tabs into something, they must be able to tab back out. A trap is a widget, embedded player, or dialog that swallows Tab and Shift+Tab so focus cycles inside it forever. If leaving needs a special key, the page has to say so before the person is stuck. The note makes this a non-interference requirement: one trap anywhere fails the whole page, because a keyboard user cannot get past it to anything else. A modal dialog that holds focus inside itself on purpose is fine as long as Escape or a close button lets the user out.

## How it fails in code

- A custom widget or embedded `iframe` whose script captures Tab and prevents default without ever releasing focus to the rest of the page. Definite once observed. F10.
- A modal dialog with focus held inside and no keyboard way to close it: no Escape handler and no focusable close button. Definite.
- A rich text editor or code editor where Tab inserts a character and there is no advertised way to leave. Definite if no exit is documented on the page.
- A focus trap that releases on a non-standard key the page does explain. Passes; manual review to confirm the instruction is reachable before entry.

## How to meet it

- Technique G21, "Ensuring that users are not trapped in content": let Tab and Shift+Tab leave every component, or provide Escape, and say so where a special key is needed.
- Native HTML: the `dialog` element with `showModal()` closes on Escape by default.
- Test by tabbing through the whole page from top to bottom and back; this is the one check no scanner replaces.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.1.1 Keyboard (entry in this package). Getting in and operating, as distinct from getting out.
- SC 2.4.3 Focus Order (entry in this package). A dialog that holds focus should also return it to the trigger on close.
- SC 2.4.11 Focus Not Obscured (Minimum) (entry in this package). Focus may be reachable but hidden.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Traps are found by tabbing through the page with a keyboard, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
