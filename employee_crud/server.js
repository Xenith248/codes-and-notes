require('dotenv').config(); // Load .env file
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const methodOverride = require('method-override');
const { exec } = require('child_process');

const app = express();

// Use environment variables
const PORT = process.env.PORT || 3000;
const MONGO_URI = process.env.MONGO_URI;

// Start MongoDB server
const mongoPath = '"C:\\Program Files\\MongoDB\\Server\\8.0\\bin\\mongod.exe" --dbpath C:\\data\\db';
exec(mongoPath, (err, stdout, stderr) => {
    if (err) {
        console.error('Failed to start MongoDB:', stderr);
        return;
    }
    console.log('MongoDB started successfully');

    // Connect to MongoDB
    mongoose.connect(MONGO_URI, {
        useNewUrlParser: true,
        useUnifiedTopology: true
    }).then(() => console.log('MongoDB Connected'))
    .catch(err => console.error('MongoDB connection error:', err));
});

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(methodOverride('_method'));

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
