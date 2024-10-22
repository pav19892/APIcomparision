const express = require('express');
const app = express();

// Middleware to log requests with timestamp
app.use((req, res, next) => {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] ${req.method} ${req.url}`);
    next();
});

// Small data load
app.get('/small', (req, res) => {
    res.json({ message: 'This is a small payload', data: [1, 2, 3] });
});

// Medium data load
app.get('/medium', (req, res) => {
    const mediumData = Array(100).fill({ id: 1, name: 'John Doe' });
    res.json({ message: 'This is a medium payload', data: mediumData });
});

// Heavy data load
app.get('/heavy', (req, res) => {
    const heavyData = Array(100000).fill({ id: 1, name: 'John Doe' });
    res.json({ message: 'This is a heavy payload', data: heavyData });
});

const PORT = 8012;
app.listen(PORT,'0.0.0.0', () => {
    console.log(`Server is running on port ${PORT}`);
});
