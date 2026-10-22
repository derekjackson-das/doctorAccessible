# Testing: Mode name

One entry per way a person tests: what to set up, what to do, what passing looks like, what to write down. These are procedures for a human tester. Doctor Accessible produces them; it never performs them and never says what a user "would experience" (principle 7).

- Sources: author or organization, "Title", date (and updated date if shown), URL, tier. From `knowledge/SOURCES.md` only.
- Related entries: `wcag/...` for the criteria the steps check, `patterns/...` for patterns with their own manual tests.
- Verified against the live sources: YYYY-MM-DD by <name>

## Status and reporting

A failed step is evidence for a finding under the criterion it checks, reported once under that criterion. A step with no criterion behind it is a manual-review note, not a WCAG failure. A tester new to a tool can mistake their own unfamiliarity for a defect; record what happened, and have a practiced user confirm before calling it a failure.

## Setup

The tool, its version, the browser, and the settings to change or leave alone.

## The steps

Numbered, in the order a tester would do them. Each step says what to do and what to look for.

## What passing looks like

Observable results, one per step, tied to a criterion entry where one applies.

## What to record

What goes in the spec's "Open manual tests" or the test log: tool and browser versions, the step, what happened, pass or fail, and who tested.
