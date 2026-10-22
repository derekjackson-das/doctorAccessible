# Request

The developer types:

> Can you give me a test script for our course schedule table before we ship it?
>
> It's an HTML `<table>` with a `<caption>` "Fall course schedule". Columns: Course, Title, Days, Time, Room, Seats left. The first column cells are `<th scope="row">` and the header row uses `<th scope="col">`. Each course code links to the course page. Rows where Seats left is 0 have a light red background and no other marking. On narrow screens the table sits in a horizontally scrolling container with `tabindex="0"` and an `aria-label` of "Course schedule, scrolls sideways".

Project context given with the request: `a11y-spec.md` exists. "Who we are building for" lists: "Students on laptops and phones. Tested with JAWS with Chrome, VoiceOver with Safari on iOS, keyboard only, 400% zoom, Windows Contrast Themes."
