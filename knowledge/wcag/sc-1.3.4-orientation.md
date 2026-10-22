# SC 1.3.4 Orientation

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 1 Perceivable / 1.3 Adaptable
- Tier 1 source: https://www.w3.org/TR/WCAG22/#orientation
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/orientation.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Content does not restrict its view and operation to a single display orientation, such as portrait or landscape, unless a specific display orientation is essential.
>
> Note: Examples where a particular display orientation may be essential are a bank check, a piano application, slides for a projector or television, or virtual reality content where content is not necessarily restricted to landscape or portrait display orientation.

## What it requires, in our words

A page must work whether the device is held upright or sideways. Some people mount a tablet to a wheelchair in one fixed orientation and cannot turn it. If the content locks itself to landscape, or shows a "please rotate your device" screen, those people are shut out. The content may look different in each orientation; it just has to be usable in both. The exception is content where one orientation is genuinely essential to the thing itself, such as a piano keyboard.

## How it fails in code

- CSS that hides or disables content in one orientation, such as a media query on `orientation: portrait` that sets the main content to `display: none` or rotates it with a transform. Definite. F97.
- JavaScript or a manifest setting that locks screen orientation (for example the Screen Orientation API's lock method, or `"orientation": "landscape"` in a web app manifest) without an essential reason. Definite. F97.
- A message asking the user to rotate the device, with the content unavailable until they do. Definite. F100.
- Whether a particular orientation is essential. Manual review.

## How to meet it

- Do nothing special. Responsive layouts that reflow to the viewport pass by default.
- Technique G214, "Using a control to allow access to content in different orientations which is otherwise restricted", when a default orientation is wanted but must not be enforced.
- Do not use orientation media queries to remove content; use them only to rearrange it.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.4.10 Reflow (entry in this package). Both are about content adapting to the viewport.
- SC 1.4.4 Resize Text (entry in this package). Orientation changes often change the available width, so the two are tested together.

## Automated coverage (tier 3)

axe-core tags `css-orientation-lock` to this criterion. It looks for CSS orientation media queries that apply transforms locking the view. It does not see JavaScript locks or manifest settings, and it cannot judge whether an orientation is essential. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
