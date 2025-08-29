const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const port = 3030;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public")); // Serve static files
app.set("view engine", "ejs");

// Store submitted employee data
let employees = [];

// GET route to render the employee form
app.get("/", (req, res) => {
    res.render("form");
});

// POST route to handle form submission
app.post("/submit", (req, res) => {
    const { name, email, gender, department, address } = req.body;
    const skills = Array.isArray(req.body.skills) ? req.body.skills : [req.body.skills];

    const employee = { name, email, gender, department, skills, address };
    employees.push(employee);

    res.redirect("/employees");
});

// GET route to display submitted employee data
app.get("/employees", (req, res) => {
    res.render("display", { employees });
});

// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
