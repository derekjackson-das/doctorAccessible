# Content: Error messages and instructions

- House standard: `docs/content-standards.md`, section 7.
- Sources:
  - W3C WAI Tutorials, "User Notification" (Forms), updated 3 June 2022. https://www.w3.org/WAI/tutorials/forms/notifications/ Tier 2.
  - W3C WAI Tutorials, "Form Instructions", updated 13 May 2024. https://www.w3.org/WAI/tutorials/forms/instructions/ Tier 2.
  - W3C WAI, "Writing for Web Accessibility", updated 5 August 2022. https://www.w3.org/WAI/tips/writing/ Tier 2.
  - `coga/objective-4-avoid-mistakes.md` (tier 2).
- WCAG: `wcag/sc-3.3.1-error-identification.md` (Level A), `wcag/sc-3.3.2-labels-or-instructions.md` (Level A), `wcag/sc-3.3.3-error-suggestion.md` (Level AA), `wcag/sc-1.4.1-use-of-color.md` (Level A, for required or error states shown by color alone).
- Verified against the live sources: 2026-10-23 by Caesar Alam with Claude Code

## Status and reporting

An error that is not identified in text, a missing label or instruction, or a known correction not suggested fails the matching criterion; report it there at the confidence its entry gives. A message that meets those criteria but is vague, blaming, or technical misses the house standard. That is likely or manual review, never definite. A project's `a11y-spec.md` may change the standard; the spec wins.

## What it is

The words that tell a person what a form needs before they fill it in, and what went wrong and how to fix it afterwards.

## Why it matters

A form is where a reader has to act, and an unclear message stops them. Readers who find it hard to recover from mistakes need the fix spelled out (`coga/objective-4-avoid-mistakes.md`).

## How to do it

- **Instructions before the field.** Give overall instructions before the form: which fields are required, allowed formats, time limits (W3C Form Instructions). Put field-specific instructions, such as a date format, in or next to the label.
- **Placeholder text is not a label.** It disappears and is often low contrast (W3C Form Instructions).
- **Say what went wrong and what to do.** A message the reader can follow, with plain steps to put it right (W3C User Notification).
- **Name the field.** When listing errors at the top of a page, reference each field's label, describe the error concisely, say how to correct it, and link to the field (W3C User Notification).
- **Plain, non-technical words.** Skip jargon the reader does not need, and spell out what an input expects, such as the date format (W3C writing tips).
- **Required fields marked in text,** not by color alone (house standard; `wcag/sc-1.4.1-use-of-color.md`).

## How to check it

- Submit the form empty and with typical mistakes. Read each message: does it name the field, say what is wrong, and say what to do?
- Check that instructions come before the fields they apply to.
- Check that required fields are marked in text.
