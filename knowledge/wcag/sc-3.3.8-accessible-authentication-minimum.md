# SC 3.3.8 Accessible Authentication (Minimum)

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: AA
- Principle and guideline: 3 Understandable / 3.3 Input Assistance
- Tier 1 source: https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html
- Also in: WCAG 2.2 only. New in 2.2; not in 2.0 or 2.1.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> A cognitive function test (such as remembering a password or solving a puzzle) is not required for any step in an authentication process unless that step provides at least one of the following:
>
> **Alternative.** Another authentication method that does not rely on a cognitive function test.
>
> **Mechanism.** A mechanism is available to assist the user in completing the cognitive function test.
>
> **Object Recognition.** The cognitive function test is to recognize objects.
>
> **Personal Content.** The cognitive function test is to identify non-text content the user provided to the website.
>
> Note 1: "Object recognition" and "Personal content" may be represented by images, video, or audio.
>
> Note 2: Examples of mechanisms that satisfy this criterion include:
>
> - support for password entry by password managers to reduce memory need, and
> - copy and paste to reduce the cognitive burden of re-typing.

## What it requires, in our words

Logging in must not depend on memory or puzzle-solving unless there is help. Remembering a password is a memory test; transcribing a code from one device to another is a transcription test; solving a distorted-text CAPTCHA is a puzzle. Each is a barrier for people with cognitive disabilities, and each is allowed only if the page offers a way around it: let a password manager fill the field, let the user paste the code, offer a sign-in link by email, or use a method that does not test cognition such as a passkey. In practice most login forms pass by doing nothing to block password managers and paste, and fail by actively blocking them. A test that asks the user to pick the picture of a cat passes as object recognition; a test that asks for a word they typed earlier does not.

## How it fails in code

- A password or one-time-code field that blocks paste (`onpaste` returning false, or script clearing pasted input), with no alternative method. Definite. F109.
- A password field with `autocomplete="off"` or a non-standard field type that stops password managers from filling it, with no alternative method and paste also blocked. Definite when both mechanisms are blocked; Likely when only autocomplete is blocked, since paste may still serve.
- A code sent to another device that must be transcribed, where the input also blocks paste. Definite.
- A text-based CAPTCHA (distorted words, arithmetic) with no alternative that is not a cognitive function test. Definite.
- A picture-selection CAPTCHA ("select all the images with a bus"). Passes by object recognition.
- An ordinary username and password form with `autocomplete` tokens and paste allowed. Passes by mechanism.
- A sign-in link sent by email, or a passkey. Passes by alternative.

## How to meet it

- Technique H100, "Providing properly marked up email and password inputs": `autocomplete="username"`, `autocomplete="current-password"` or `new-password`, `autocomplete="one-time-code"`, and no paste blocking.
- Technique G218, "Email link authentication", as an alternative method.
- Do not block paste. Do not clear a field on paste. Do not split a code across one-character boxes that defeat paste.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 1.1.1 Non-text Content (`wcag/sc-1.1.1-non-text-content.md`). The CAPTCHA clause requires alternative forms for different senses.
- SC 3.3.7 Redundant Entry (entry in this package). The other WCAG 2.2 memory-burden criterion.
- SC 1.3.5 Identify Input Purpose (`wcag/sc-1.3.5-identify-input-purpose.md`). The `autocomplete` tokens that let password managers work.
- SC 2.2.1 Timing Adjustable (`wcag/sc-2.2.1-timing-adjustable.md`). A code that expires before a slow user can enter it.
- SC 3.3.9 Accessible Authentication (Enhanced) is Level AAA and removes the object recognition and personal content allowances; not a requirement here.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Paste blocking and autocomplete suppression are found by reading the form's attributes and script, or by trying to paste. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
