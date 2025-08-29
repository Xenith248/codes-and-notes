const mongoose = require('mongoose');

const employeeSchema = new mongoose.Schema({
    name: String,
    email: String,
    gender: String,
    department: String,
    skills: [String],
    address: String
});

module.exports = mongoose.model('Employee', employeeSchema);
