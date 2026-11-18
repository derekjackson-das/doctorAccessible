# Request

The developer types:

> I only need to test the room request form on this page, not the rest of it. Can you give me a manual testing checklist for just that form, with expected outcomes?
>
> ```html
> <!doctype html>
> <html lang="en">
> <head>
>   <meta charset="utf-8">
>   <title>Book a study room</title>
>   <style>
>     :focus-visible { outline: 2px solid #1d5fb0; outline-offset: 2px; }
>     .errors { color: #b00020; }
>   </style>
> </head>
> <body>
>   <header>
>     <nav aria-label="Main"><a href="/">Home</a> <a href="/rooms">Rooms</a> <a href="/help">Help</a></nav>
>   </header>
>
>   <main>
>     <h1>Book a study room</h1>
>
>     <form id="room-form" novalidate>
>       <div id="form-errors" class="errors"></div>
>
>       <label for="name">Your name</label>
>       <input id="name" name="name" type="text" required>
>
>       <label for="email">Email</label>
>       <input id="email" name="email" type="email" required>
>
>       <label for="date">Date</label>
>       <input id="date" name="date" type="date" required>
>
>       <p>Room size</p>
>       <label><input type="radio" name="size" value="2"> Up to 2 people</label>
>       <label><input type="radio" name="size" value="6"> Up to 6 people</label>
>       <label><input type="radio" name="size" value="12"> Up to 12 people</label>
>
>       <button type="submit">Request room</button>
>     </form>
>
>     <div id="sent" role="status"></div>
>   </main>
>
>   <footer>
>     <form id="newsletter">
>       <label for="nl-email">Get library news by email</label>
>       <input id="nl-email" type="email">
>       <button type="submit">Subscribe</button>
>     </form>
>   </footer>
>
>   <script>
>     const form = document.getElementById("room-form");
>     form.addEventListener("submit", (e) => {
>       e.preventDefault();
>       const problems = [];
>       if (!form.name.value.trim()) problems.push("Enter your name.");
>       if (!form.email.value.includes("@")) problems.push("Enter an email address like name@example.edu.");
>       if (!form.date.value) problems.push("Choose a date.");
>       if (!form.size.value) problems.push("Choose a room size.");
>       const box = document.getElementById("form-errors");
>       if (problems.length) {
>         box.innerHTML = "<ul>" + problems.map((p) => "<li>" + p + "</li>").join("") + "</ul>";
>         return;
>       }
>       box.textContent = "";
>       document.getElementById("sent").textContent = "Request sent. We'll email you within one working day.";
>       form.reset();
>     });
>   </script>
> </body>
> </html>
> ```

Project context given with the request: `a11y-spec.md` exists. "Who we are building for" lists: "Tested with keyboard only, NVDA with Firefox, 200% and 400% zoom."
