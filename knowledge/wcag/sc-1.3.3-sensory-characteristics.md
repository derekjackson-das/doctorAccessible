# SC 1.3.3 Sensory Characteristics

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 1 Perceivable / 1.3 Adaptable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#sensory-characteristics
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Instructions provided for understanding and operating content do not rely solely on sensory characteristics of components such as shape, color, size, visual location, orientation, or sound.
>
> Note: For requirements related to color, refer to Guideline 1.4.

## What it requires, in our words

Instructions must work for someone who cannot see the layout or hear the sound. "Click the round button," "use the menu on the right," "fields marked in red are required," and "wait for the beep" all fail on their own, because a screen reader user does not know what is round or on the right, a colorblind user does not see the red, and a deaf user does not hear the beep. The fix is to add a cue that does not depend on a sense: the button's name, the menu's heading, the word "required." Sensory cues can stay as long as they are not the only cue. This criterion is about instructions; color used in content itself is SC 1.4.1.

## How it fails in code

- Instruction text that refers to a control only by shape, size, or position: "the button on the left," "the large green button." Definite when no other identification is given. F14.
- A graphical symbol used alone to carry an instruction, such as an unlabeled asterisk meaning "required" with no key. Definite. F26.
- Instructions that rely on a sound alone: "when you hear the chime, proceed." Definite.
- Instructions that give both a sensory cue and a name: "the Submit button on the left." Passes.

## How to meet it

- Technique G96, "Providing textual identification of items that otherwise rely only on sensory information to be understood": name the control or section in the instruction, and let shape, color, or position be a second cue.
- Content: see `docs/content-standards.md` for how to word instructions and error messages.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.4.1 Use of Color (entry in this package). Color as the only means of conveying information in content. The note in this criterion points there.
- SC 1.3.1 Info and Relationships (entry in this package). A required-field mark that is only visual also raises 1.3.1 if the required state is not in the code.
- SC 3.3.2 Labels or Instructions (no entry yet). Whether instructions exist at all.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Finding an instruction that depends on a sense means reading the text, which is manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
