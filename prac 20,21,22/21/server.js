const express = require("express");
const app = express();
const port = 3000;

app.use(express.json()); // Middleware to parse JSON

let users = [{ id: 1, name: "Alice" }];

// GET all users
app.get("/users", (req, res) => res.json(users));

// GET user by ID
app.get("/users/:id", (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    user ? res.json(user) : res.status(404).json({ message: "User not found" });
});

// POST a new user
app.post("/users", (req, res) => {
    const newUser = { id: users.length + 1, name: req.body.name };
    users.push(newUser);
    res.status(201).json(newUser);
});

// Start server
app.listen(port, () => console.log(`Server running on port ${port}`));
