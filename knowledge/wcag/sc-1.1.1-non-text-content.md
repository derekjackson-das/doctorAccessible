# SC 1.1.1 Non-text Content

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 1 Perceivable / 1.1 Text Alternatives
- Tier 1 source: https://www.w3.org/TR/WCAG22/#non-text-content
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
- Also in: WCAG 2.0 and 2.1, same level
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> All non-text content that is presented to the user has a text alternative that serves the equivalent purpose, except for the situations listed below.
>
> **Controls, Input.** If non-text content is a control or accepts user input, then it has a name that describes its purpose. (Refer to Success Criterion 4.1.2 for additional requirements for controls and content that accepts user input.)
>
> **Time-Based Media.** If non-text content is time-based media, then text alternatives at least provide descriptive identification of the non-text content. (Refer to Guideline 1.2 for additional requirements for media.)
>
> **Test.** If non-text content is a test or exercise that would be invalid if presented in text, then text alternatives at least provide descriptive identification of the non-text content.
>
> **Sensory.** If non-text content is primarily intended to create a specific sensory experience, then text alternatives at least provide descriptive identification of the non-text content.
>
> **CAPTCHA.** If the purpose of non-text content is to confirm that content is being accessed by a person rather than a computer, then text alternatives that identify and describe the purpose of the non-text content are provided, and alternative forms of CAPTCHA using output modes for different types of sensory perception are provided to accommodate different disabilities.
>
> **Decoration, Formatting, Invisible.** If non-text content is pure decoration, is used only for visual formatting, or is not presented to users, then it is implemented in a way that it can be ignored by assistive technology.

## What it requires, in our words

Anything on the page that is not text, such as an image, icon, chart, audio clip, or video, needs a text version that does the same job for someone who cannot see or hear it. The job is the point: a photo of a building on a contact page might need "Main entrance, 12 Oxford Street" rather than a description of the architecture. Images that carry no information are marked so that assistive technology skips them. Controls that are images, such as an icon button, need a name that says what they do, not what they look like. Media gets at least a label here, and its full requirements are in Guideline 1.2.

## How it fails in code

- An `img` with no `alt` attribute at all. Definite. The W3C failure technique is F65.
- An `input type="image"` or an image-map `area` with no `alt`. Definite. Also F65.
- A decorative image with a non-empty alt such as "spacer" or "image" when it should be ignored. Definite. F39.
- A decorative image not marked up so assistive technology can skip it, such as an inline `img` with alt text that repeats adjacent text. Likely; needs a judgment about whether the image carries information. F38.
- Alt text that is a filename or placeholder, such as "IMG_2041.jpg" or "photo". Definite. F30.
- Information conveyed only through a CSS background image, with no text equivalent. Definite once the image is confirmed to carry information. F3.
- An `svg` or an element with `role="img"` that has no accessible name. Definite.
- Alt text present but not equivalent: a chart with alt "chart", or an alt that leaves out what a color difference in the image conveys. Manual review; a person must compare the image to its text. F13 covers the color case.
- Text drawn as ASCII art or with look-alike characters, with no text alternative. Definite. F71 and F72.

## How to meet it

- Native HTML first. Technique H37, "Using alt attributes on img elements". Write the purpose and stop; see `docs/content-standards.md` for how to word it.
- Technique H67, "Using null alt text and no title attribute on img elements for images that assistive technology should ignore", for decoration. Or Technique C9, "Using CSS to include decorative images", so decoration never reaches the markup.
- Technique H36, "Using alt attributes on images used as submit buttons", and Technique H24 for image-map areas.
- Technique G94 for short alternatives that do the same job, and G95 with G73, G74, or G92 when a short alternative cannot (a complex chart needs a long description nearby or linked).
- Technique ARIA6, "Using aria-label to provide labels for objects", and ARIA10, "Using aria-labelledby to provide a text alternative for non-text content", when the element has no native alt mechanism, such as an inline `svg`.
- Technique H86, "Providing text alternatives for emojis, emoticons, ASCII art, and leetspeak".
- For CAPTCHA, both G143 and G144 together: describe the purpose and offer another form using a different sense.

All techniques are tier 2, from the Understanding page linked above, which lists them as sufficient by situation.

## Related criteria

- SC 4.1.2 Name, Role, Value (`wcag/sc-4.1.2-name-role-value.md`). The name of an image control falls under both; report once, under 1.1.1 for the alt text and 4.1.2 for the control name, unless the entry for the defect says otherwise.
- SC 1.4.1 Use of Color (entry in this package). An alt text that drops color-coded information fails both; F13.
- SC 1.4.5 Images of Text (entry in this package). When the "image" is a picture of words, 1.4.5 asks why it is not text.
- SC 1.2.1 through 1.2.5 (entries in this package). Media needs a label here and its alternatives there.

## Automated coverage (tier 3)

axe-core tags these rules to this criterion: `image-alt`, `input-image-alt`, `object-alt`, `role-img-alt`, `svg-img-alt`, `aria-meter-name`, `aria-progressbar-name`. axe reliably finds a missing alt attribute or an empty accessible name. It cannot tell whether an alt text is equivalent, whether an image is decorative, or whether a background image carries information. Those remain manual. Rule descriptions: https://dequeuniversity.com/rules/axe/ (checked against the rule list for axe-core 4.14).
