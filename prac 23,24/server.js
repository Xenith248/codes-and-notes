const express = require("express");
const cookieParser = require("cookie-parser");
const bodyParser = require("body-parser");

const app = express();
const port = 3023;

// Middleware
app.use(cookieParser());
app.use(bodyParser.urlencoded({ extended: true }));
app.set("view engine", "ejs");

// GET route to display the form
app.get("/", (req, res) => {
    res.render("form");
});

// POST route to set cookies and stay on the same page
app.post("/set-cookies", (req, res) => {
    const { name, age } = req.body;

    // Set cookies with a 1-minute expiry time
    res.cookie("name", name, { maxAge: 60000 });
    res.cookie("age", age, { maxAge: 6000 });

    res.send("Cookies have been set! You can now view them <a href='/view-cookies'>here</a>.");
});

// GET route to display stored cookies
app.get("/view-cookies", (req, res) => {
    res.render("view-cookies", { cookies: req.cookies });
});

// Start server
app.listen(port, () => console.log(`Server running on http://localhost:${port}`));
