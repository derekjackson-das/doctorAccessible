# SC 2.5.4 Motion Actuation

- Standard: WCAG 2.2, W3C Recommendation 12 December 2024
- Level: A
- Principle and guideline: 2 Operable / 2.5 Input Modalities
- Tier 1 source: https://www.w3.org/TR/WCAG22/#motion-actuation
- Tier 2 source: https://www.w3.org/WAI/WCAG22/Understanding/motion-actuation.html
- Also in: WCAG 2.1, same level. Not in WCAG 2.0.
- Verified against the live source: 2026-10-22 by Derek Jackson with Claude Code, direct fetch of the Recommendation page and the W3C WCAG 2.2 JSON

## Normative text (tier 1, quoted)

> Functionality that can be operated by device motion or user motion can also be operated by user interface components and responding to the motion can be disabled to prevent accidental actuation, except when:
>
> **Supported Interface.** The motion is used to operate functionality through an accessibility supported interface;
>
> **Essential.** The motion is essential for the function and doing so would invalidate the activity.

## What it requires, in our words

If shaking the phone undoes an action, or tilting it scrolls, or waving at the camera advances a slide, there must also be an ordinary control that does the same thing, and the user must be able to turn the motion response off. Someone whose device is mounted to a wheelchair cannot shake it; someone with a tremor shakes it by accident. Motion that comes through the operating system's own accessibility features is exempt, as is motion that is the activity, such as a pedometer. In web content this mostly concerns pages using the device orientation or motion sensor APIs.

## How it fails in code

- A page that listens to device motion or orientation events to trigger a function, with no equivalent button and no setting to disable it. Definite. F106.
- A motion-triggered function with a button equivalent but no way to disable the motion. Definite. F106.
- A step counter or a level that reads the sensor as its purpose. Passes; essential.
- A page that uses no motion sensors at all. Not applicable; most pages.

## How to meet it

- Technique G213, "Provide conventional controls and an application setting for motion activated input": a visible control for the function, and a setting that turns the motion listener off.

All techniques are tier 2, from the Understanding page linked above.

## Related criteria

- SC 2.1.4 Character Key Shortcuts (entry in this package). The same accidental-activation concern for keys.
- SC 2.5.1 Pointer Gestures (entry in this package). Alternatives to complex input, for pointers.
- SC 2.1.1 Keyboard (entry in this package). The conventional control should be keyboard operable.

## Automated coverage (tier 3)

axe-core has no rule tagged to this criterion. Motion listeners are found by searching the script for device motion and orientation events. Rule descriptions: https://dequeuniversity.com/rules/axe/ (axe-core 4.14 rule list).
