const express = require('express');
const bodyParser = require('body-parser');
const { encodeImage, decodeImage } = require('./utility'); // Utility functions
const app = express();
const port = 5000; // Port number

app.use(bodyParser.json());

app.post('/img', (req, res) => {
    try {
        const { id, image } = req.body;
        // Handle image upload logic here
        res.status(200).send('OK');
    } catch (error) {
        console.error('Error handling image upload:', error);
        res.status(500).send('Internal Server Error');
    }
});

app.get('/img/:id', (req, res) => {
    try {
        const { id } = req.params;
        // Handle image retrieval logic here
        res.status(200).json({ image: 'base64_encoded_image_data' });
    } catch (error) {
        console.error('Error handling image retrieval:', error);
        res.status(500).send('Internal Server Error');
    }
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
