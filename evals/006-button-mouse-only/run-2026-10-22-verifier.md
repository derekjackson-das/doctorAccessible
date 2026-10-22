# Verifier run, 2026-10-22, eval 006

Blind run through the registered `verifier` agent (`verifier.md` at commit 6a54d17), given the file path, the index, the content standards, and the axe command, and told not to open `expected.md`, `RESULTS.md`, or any run file.

Result against `expected.md`: **pass**. One Definite finding, SC 2.1.1 Keyboard (Level A), tier 1, sourced to the entry with the matching pattern and F54 named, at `span.toggle[role="button"]`, with H91 and G90 as fix directions. The agent explicitly declined to report SC 4.1.2 because name, role, and state are all present, which is the point of the eval. Nothing from the must-not list. axe inside the agent: 0 violations, and the agent said the clean result was expected because axe cannot see a focusable control with no key handler. No file modified.

Observation: reading level came out at grade 10.2 on a twenty-word sample dominated by proper nouns; the agent correctly called it not meaningfully measured rather than failing.

## Report as returned (findings and scan)

### [Definite] Disclosure control cannot be activated from the keyboard
- Where: `input.html` line 21, `span.toggle[role="button"]`; script at lines 28 to 35
- What: The control is a `span` with `role="button"` and `tabindex="0"`, so it receives focus, but its only handler is `onclick`; there is no `keydown` or `keyup` handling for Enter or Space, and a `span` does not fire `click` on those keys the way a native `button` does, so the syllabus can be opened only with a pointer.
- Criterion: WCAG 2.2 SC 2.1.1 Keyboard (Level A), tier 1
- Source: knowledge/wcag/sc-2.1.1-keyboard.md (entry lists this exact pattern as Definite, failure F54)
- Fix direction: Replace the `span` with a native `button type="button"` so Enter and Space activate it without script (Technique H91); if the custom element must stay, add a `keydown` handler for Enter and Space alongside `click` (Technique G90).

Not reported as a second finding: name, role, and state are all present, so SC 4.1.2 is met. Using a `span` instead of `button` is a departure from native-HTML-first, a best practice rather than a criterion failure on its own.

Content: reading level grade 10.2 on twenty words, dominated by proper nouns; treated as not meaningfully measured. Headings describe their sections. Control label matches its name, so 2.5.3 is not at issue.

Manual checks remaining: Tab to the control and press Enter and Space; screen reader announcement of button, name, and expanded state; focus indicator visible; panel content reachable after toggle; 400% reflow; voice control "click Show syllabus".

Automated scan: axe-core 4.14.0, 0 violations. The 2.1.1 entry notes axe does not detect this defect.
