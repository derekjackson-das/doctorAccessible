# ARIA: Live regions

- Sources:
  - W3C, "WAI-ARIA 1.2", W3C Recommendation 6 June 2023. https://www.w3.org/TR/wai-aria-1.2/ Tier 1: the live region attributes (section 6.6.2, `#attrs_liveregions`), the live region roles (section 5.3.5, `#live_region_roles`), and the role definitions for `alert`, `status`, `log`, `marquee`, `timer`, and `alertdialog`.
  - W3C, "HTML Accessibility API Mappings 1.0", W3C Working Draft 26 October 2026. https://www.w3.org/TR/html-aam/#el-output Tier 2: `output` maps to the `status` role.
  - W3C, "Understanding SC 4.1.3 Status Messages", updated 4 October 2026. https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html Tier 2: what counts as a status message, the techniques, and the warning about applications that are too "chatty".
  - Sara Soueidan, "Accessible notifications with ARIA Live Regions (Part 1)", 15 January 2024. https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-1/ Tier 3: how live regions work, the attributes and roles, `output`, and support, with NVDA and VoiceOver demos (no versions given).
  - Sara Soueidan, "Accessible notifications with ARIA Live Regions (Part 2)", 15 January 2024. https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-2/ Tier 3: what live regions cannot do, the alternatives, and practice for when one is needed. Demos with VoiceOver and Safari, and NVDA and Firefox (no versions given).
  - Scott O'Hara, "Are we live?", 5 February 2022, updated 22 August 2022. https://www.scottohara.me/blog/2022/02/05/are-we-live.html Tier 3: the three ways to make a live region and why an injected one fails. Tested 2019 and re-checked, no versions given.
  - Scott O'Hara, "Considering dynamic search results and content", 5 February 2022, updated 6 February 2022. https://www.scottohara.me/blog/2022/02/05/dynamic-results.html Tier 3: search and filter results without a live region; the no-results exception. TalkBack named; no versions.
  - Scott O'Hara, "A toast to an accessible toast...", 8 July 2019, updated 1 May 2025. https://www.scottohara.me/blog/2019/07/08/a-toast-to-a11y-toasts.html Tier 3: toasts, `status` and `log`, interactive content.
  - Scott O'Hara, "output: HTML's native live region element", 10 July 2019, updated 16 July 2020. https://www.scottohara.me/blog/2019/07/10/the-output-element.html Tier 3: `output` support, tested with VoiceOver and TalkBack in 2019 and 2020; no versions.
  - Adrian Roselli, "Defining 'Toast' Messages", 14 January 2020, updated 21 August 2026. https://adrianroselli.com/2020/01/defining-toast-messages.html Tier 3: the criteria toasts put at risk, and three alternatives. No test results.
  - Adrian Roselli, "More Accessible Skeletons", 29 November 2020, updated 14 April 2026. https://adrianroselli.com/2020/11/more-accessible-skeletons.html Tier 3: `aria-busy` support, tested with named versions in 2020.
- Related: `aria/using-aria.md`, `aria/accessible-name.md`, `aria/patterns/infinite-scroll.md`, `html/forms.md`, `html/dialogs.md`, `content/error-messages.md`, `aria/roles/alert.md`, `aria/roles/status.md`, `aria/roles/log.md`, `aria/roles/marquee.md`, `aria/roles/timer.md`, `aria/roles/alertdialog.md`
- WCAG: `wcag/sc-4.1.3-status-messages.md` (the criterion live regions usually meet), `wcag/sc-2.2.1-timing-adjustable.md`, `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.3-focus-order.md`, `wcag/sc-4.1.2-name-role-value.md`, `wcag/sc-3.3.1-error-identification.md`, `wcag/sc-1.3.2-meaningful-sequence.md`
- Verified against the live sources: 2026-11-20 by Derek Jackson with Claude Code. WAI-ARIA 1.2 and HTML-AAM quotes checked against a downloaded copy of each page; the practitioner articles and the Understanding page read in full by fetch.

## Status and reporting

WCAG does not say how to use a live region. This entry is how-to, not a criterion. A defect is reported once, under the criterion it breaks, at the confidence that criterion's entry gives:

- A status message with no role or property that exposes it, and no focus move: `wcag/sc-4.1.3-status-messages.md`.
- A message that disappears on a timer the user cannot turn off, adjust, or extend: `wcag/sc-2.2.1-timing-adjustable.md`.
- A control inside a message the user cannot reach by keyboard, or reaches only after it has gone: `wcag/sc-2.1.1-keyboard.md`, `wcag/sc-2.4.3-focus-order.md`.
- An error message not tied to its field: `wcag/sc-3.3.1-error-identification.md`.

Everything else here is practice. Too many regions, a whole results list made live, `assertive` used for routine news, a region that talks on every keystroke: likely or manual review at most, never definite on this entry alone.

**Two things in flux.** `wcag/sc-4.1.3-status-messages.md` calls an over-busy live region "not a failure of this criterion" (issue #107 asks for a re-check). The Understanding page, updated 4 October 2026, says an application can become too "chatty" and that user testing should settle the level of feedback. It also lists a failure technique with no ID yet, for `role="alert"` or `aria-live="assertive"` on content that is not important and time-sensitive. Until that technique is published with an ID, treat assertive misuse as likely, cite the Understanding page and the date, and mark it pending.

**Principle 7 applies to every result below.** They say what a tester recorded, in the past tense. When using them, say what the code exposes and what a person should test, never what a user hears or experiences.

**Testing gap.** No source on the list gives screen reader and browser versions for live region behavior after 2020. Soueidan (2024) and O'Hara (2022) name the screen readers and browsers but no versions. Roselli's 2020 `aria-busy` results are the only ones with versions, and they are six years old. a11ysupport.io was not checked for this entry. Treat every support claim below as a lead to test, not a result.

## What it is

A screen reader reads one thing at a time, at the point where the user is. When script changes the page somewhere else ("Saved", "3 results", "Upload failed"), a sighted user sees it and a screen reader user does not, unless focus moves there or the change is marked so assistive technology announces it. A live region is that mark: an element whose changes are announced wherever focus is. WAI-ARIA 1.2 describes live regions as perceivable regions "updated as a result of an external event when user focus may be elsewhere" (section 2, non-normative).

An announcement is spoken once and then gone. The user cannot replay it, cannot navigate into it as a structure, and cannot act on anything in it. That shapes every decision below (Soueidan 2024, part 1).

## Before reaching for a live region

Both Soueidan (2024, part 2) and O'Hara (2022) put it bluntly: the fewer live regions the better, and none is best. Check these first.

1. **A state attribute already does it.** A disclosure that opens says so through `aria-expanded`; a toggle through `aria-pressed`. A live region on top repeats or contradicts it (Soueidan 2024, part 2). Expanding content is a 4.1.2 matter, not a status message (Understanding 4.1.3).
2. **Say what will happen, before it happens.** A field that filters results as the user types gets a description, "Results update as you type", tied with `aria-describedby`. Visible is better; visually hidden is acceptable. Then the results themselves need no announcement (O'Hara 2022, dynamic results; Soueidan 2024, part 2).
3. **Move focus, when the change is the direct result of what the user just did.** Pressing Enter in a search can move focus to the results heading, which carries the count. A single-page view change moves focus to the new view's heading and updates `document.title`. Adding to a cart can open the cart as a dialog. Do not move focus for something the user did not ask for, such as a message that arrives later (Soueidan 2024, part 2). Moving focus is a change of context, so 4.1.3 does not apply to it (Understanding 4.1.3).
4. **Keep the message on the page.** A message that stays where it appeared, until the user dismisses it, avoids the timing and reach problems of a toast (Roselli 2020, "static messages").
5. **Ask whether the message is needed at all** (Roselli 2020, "do nothing"). Understanding 4.1.3 says the criterion does not require new status messages; it covers the ones that exist.

## When a live region is the right tool

A short, plain-text, non-interactive status message that does not move focus and cannot be conveyed another way: "Saved", "Item added", "No results", "Upload failed", a running chat or activity log (Soueidan 2024, part 2). These are the cases the sufficient techniques for 4.1.3 cover: ARIA22 (`role="status"`), ARIA19 (`role="alert"` or a live region for errors), ARIA23 (`role="log"`), ARIA25 and ARIA27 (progress) (Understanding 4.1.3, 4 October 2026).

If the message holds a link or a button, it is not a live region and not a toast. Move focus to it and keep it until the user closes it: an `alertdialog` for an urgent message that needs a response, otherwise a dialog (Soueidan 2024, part 2; O'Hara 2019; Roselli 2020). WAI-ARIA 1.2 on `alert`: "If an author desires focus to move to a message when it is conveyed, the author SHOULD use alertdialog instead of alert."

## Three ways to make one

| Method | Use when | Implicit behavior (WAI-ARIA 1.2 unless noted) |
|---|---|---|
| `role="status"` | Advisory news: saved, sent, added, results. The default choice. | "an implicit aria-live value of polite and an implicit aria-atomic value of true" |
| `role="alert"` | Important, time-sensitive news that needs attention now: a submission error, a session about to end | "an implicit aria-live value of assertive, and an implicit aria-atomic value of true" |
| `role="log"` | Entries added in order, newest at the end: chat, activity history | "an implicit aria-live value of polite"; atomic not stated |
| `aria-live` on an element | The element's own role must stay, for example a `ul` whose new items are announced (O'Hara 2022) | `off` by default; `polite` or `assertive` as set |
| `output` | The result of a calculation or a user action, such as a total | Maps to `status` (HTML-AAM, WD 26 Oct 2026). Can be labelled with `label`. Support uneven (below) |

`marquee` and `timer` have an implicit `aria-live` of `off`, so their changes are not announced by default. Both Soueidan (2024) and Roselli (2020) say to avoid them and note they may be removed from ARIA. A role also gives the region a name it can announce, where a bare `aria-live` `div` cannot reliably carry one (Soueidan 2024, part 1; O'Hara 2019).

## The attributes

All four are in WAI-ARIA 1.2, section 6.6.2. Soueidan (2024, part 1) reports support for `aria-atomic`, `aria-relevant`, and `aria-busy` as inconsistent across screen reader and browser pairs: test before relying on them.

- **`aria-live`:** `off` (default), `polite`, `assertive`. Polite waits "at the next graceful opportunity, such as at the end of speaking the current sentence or when the user pauses typing". Assertive interrupts, and "User agents or assistive technologies MAY choose to clear queued changes when an assertive change occurs", so an assertive message can wipe out polite ones waiting in line. The spec's rule for authors: "authors SHOULD NOT use the assertive value unless the interruption is imperative."
- **`aria-atomic`:** `false` (default) announces only what changed; `true` announces the whole region, "including the author-defined label if one exists". Use `true` when the changed part makes no sense alone, such as a song title inside "Now playing: …" (Soueidan 2024, part 1).
- **`aria-relevant`:** which changes count. Default `additions text`; `removals` and `all` also exist. The spec's note: "aria-relevant values of removals or all are to be used sparingly." Removal matters only when it means something, such as a person leaving a chat.
- **`aria-busy`:** marks a region as mid-update so assistive technology "MAY want to wait". In Roselli's 2020 tests only JAWS 2020 honored it; Narrator with Edge 87, NVDA 2020.2 with Chrome 87 and Firefox 83, TalkBack on Android 11, and VoiceOver on iOS 14 and macOS 11 read the busy content anyway. His workaround: hide the busy content with `aria-hidden="true"` until it is ready, and announce "Loading" and "Loaded" through a separate polite region.

## Doing it right

From Soueidan (2024, part 2) unless noted, with O'Hara and Roselli where they agree or differ.

1. **The region is in the page before the message.** Put the empty container in the HTML at load and write text into it later. Adding the region and its text at the same moment, or switching it from `display: none` to visible, often goes unannounced; O'Hara (2022) found injection the least supported method outside macOS VoiceOver. Roselli (2020) and Soueidan agree.
2. **Hide it visually, never from the accessibility tree.** A visually hidden class is fine. `display: none` (which includes the `hidden` attribute), `aria-hidden="true"`, or anything else that removes it from the accessibility tree silences it. To keep an empty region from taking space, style it only when it has content, for example with `:not(:empty)` (Soueidan 2024, part 1).
3. **Few regions.** Soueidan suggests two for a page, one polite and one assertive, created at load and fed by script. Several regions talking at once interfere, and assertive changes may clear polite ones (WAI-ARIA 1.2, above).
4. **Write the whole message at once.** Building it with several DOM changes can be read as fragments.
5. **Short, plain text.** A live region announces text only. A button, link, heading, or list inside it is read as words, with no role (Soueidan 2024, part 2; O'Hara 2022). Never make a whole results list or page section live; it is read as one long string.
6. **Clear it after a short pause** when the message is not visible to everyone or disappears on its own: about 350 to 500 ms. Clearing is not needed for the next announcement, but it stops repeats and stops a user finding stale text later. Wait a moment before writing the next message.
7. **`status` for routine news, `alert` only when the interruption is imperative.** O'Hara (2019) puts toasts in `status`, or `log` if they are kept for review. For "no results" on a live search, O'Hara (2022) uses an empty `div` with `aria-live="assertive"` and `aria-atomic="true"`, not `role="alert"`, because TalkBack announced an empty alert when the page rendered.
8. **Do not focus a status or an alert, and do not make the user close an alert.** WAI-ARIA 1.2: "Authors SHOULD ensure an element with role status does not receive focus as a result of change in status." "Since alerts are not required to receive focus, authors SHOULD NOT require users to close an alert."
9. **Re-test regularly.** Behavior changes with browser and screen reader releases (O'Hara 2022). The NerdeRegion browser extension logs every live region and each change with a time stamp (Soueidan 2024, part 2). It is a debugging aid, not a test.

## What testing found

All reported by the authors, mostly without versions; see the testing gap.

- A button written into a live region was announced as its text, with no role (VoiceOver with Safari; Soueidan 2024, part 2).
- NVDA said "Alert" before content in `role="alert"` but not before the same content in `aria-live="assertive"` (Soueidan 2024, part 1).
- `output`: VoiceOver with Safari and NVDA with Firefox announced the content without its label, and VoiceOver with Chrome announced both (Soueidan 2024). VoiceOver with Safari also read the old total before the new one. O'Hara (2019 to 2020) found TalkBack with Firefox silent on injected text, and TalkBack with Chrome announcing only the label of a named `output`. His workaround: add `role="status"` to the `output`. Old results; re-test.
- `aria-busy` ignored by everything but JAWS (Roselli 2020, versions above).

## Where sources differ

- **A list made live.** O'Hara's 2022 "Are we live?" shows `aria-live="polite"` on a `ul` so new items are announced. His dynamic-results article rejects making a results list live. The difference is scope: one new item added versus the whole list replaced at once. Follow the second for search and filter results.
- **Toast role.** Many component libraries use `role="alert"` for every toast. O'Hara (2019) uses `status`. WAI-ARIA 1.2 limits `assertive` to imperative interruptions. Take the stricter reading: `status` unless the message is urgent.
- **Toasts at all.** Roselli (2020) recommends not using timed, animated toasts and lists nine criteria they put at risk. O'Hara (2019) describes how to make one less harmful. Both agree a toast must not hold controls that exist nowhere else.

## How it fails in code

- A visible message written by script into an element with no live-region role and no `aria-live`, with focus left elsewhere. 4.1.3; definite per its entry (F103).
- The region created and filled in the same moment, or unhidden as it is filled. 4.1.3; likely per its entry, and a person confirms.
- A live region hidden with `display: none`, `hidden`, or `aria-hidden="true"`. 4.1.3 when it is the only way the message is exposed; likely.
- A toast that disappears on a timer with no way to keep it. 2.2.1; likely, because its entry has no toast case yet (Roselli 2020 calls 2.2.1 the criterion most relevant to toasts). Check the entry's exceptions.
- A toast or live region holding a link or button that exists nowhere else. 2.1.1 or 2.4.3 when the control cannot be reached in time; likely, and a person confirms.
- Focus moved into a `status` or `alert`, or an `alert` that must be closed. Advice from WAI-ARIA 1.2; report under 2.4.3 only if focus is lost or misplaced.
- `aria-live="assertive"` or `role="alert"` on routine news ("Saved", result counts). Likely; cite the pending failure technique in Understanding 4.1.3 with its date.
- A whole results list or page section made live; a region rewritten on every keystroke; several regions announcing at once. Manual review; practice, not a criterion, until #107 settles the 4.1.3 reading.
- `marquee` or `timer` used to announce something. Advice; their changes are off by default.

## Manual tests

With the screen readers on the project's list (`testing/screen-reader-windows.md`, `testing/screen-reader-apple.md`):

1. Trigger each message with focus on the control that caused it. Record whether it was announced, the exact words, and whether anything else was cut off.
2. Trigger two messages close together, one polite and one assertive if both exist. Record which were announced and in what order.
3. For a message that disappears, note how long it stays and whether it can be found again.
4. For a message with a control in it, record whether the control can be reached by keyboard and by screen reader before the message goes.
5. Type in any field that updates content as you type. Record what is announced per keystroke.

Record the screen reader, browser, and their versions with each result. A tester new to a screen reader may miss a polite announcement that was made; repeat a missed step once before recording it as not announced.
