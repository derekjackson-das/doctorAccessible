# SC 2.1.4 Character Key Shortcuts

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.1 Keyboard Accessible
- Tier 1 source: https://www.w3.org/TR/WCAG22/#character-key-shortcuts
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/character-key-shortcuts.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> If a keyboard shortcut is implemented in content using only letter (including upper- and lower-case letters), punctuation, number, or symbol characters, then at least one of the following is true:
>
> **Turn off.** A mechanism is available to turn the shortcut off;
>
> **Remap.** A mechanism is available to remap the shortcut to include one or more non-printable keyboard keys (e.g., Ctrl, Alt);
>
> **Active only on focus.** The keyboard shortcut for a user interface component is only active when that component has focus.

## What it requires, in our words

A shortcut made of a single printable key, such as pressing "s" to search or "j" to move to the next item, is dangerous for people who use speech recognition, because spoken words get interpreted as keystrokes, and for people who hit keys by accident. If a page uses such shortcuts, the user must be able to turn them off, change them to include a modifier like Ctrl or Alt, or the shortcut must work only while the relevant control has focus. Shortcuts that already include a modifier are not covered.

## How it fails in code

- A page-wide `keydown` or `keypress` listener that triggers an action on a single letter, number, or symbol with no modifier, and offers no setting to disable or remap it. Definite. F99.
- The same shortcut scoped to a focused component, such as arrow keys inside a listbox or "Delete" while an item is selected. Passes by the third condition.
- A shortcut using Ctrl, Alt, or Meta plus a character. Not covered by this criterion.

## How to meet it

- Technique G217, "Providing a mechanism to allow users to remap or turn off character key shortcuts": a settings control the user can reach by keyboard.
- Or scope the shortcut to a focused component, or require a modifier from the start.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.1.1 Keyboard (entry in this package). Shortcuts are a keyboard convenience; they must not be the only way to do something either.
- SC 2.5.4 Motion Actuation (entry in this package). The same "accidental activation" concern for motion.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Shortcuts live in script and are found by reading it or pressing keys. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
