const fetch = require('node-fetch');
const fs = require('fs');
const path = require('path');
const { decodeImage, encodeImage } = require('./utility'); // Utility functions

const SERVER_URL = 'http://localhost:5000'; // Replace with your server URL

async function fetchImage(id) {
    try {
        const endPoint = `/img/${id}`;
        const response = await fetch(`${SERVER_URL}${endPoint}`);
        const data = await response.json();
        const img = data.image;
        decodeImage(img); // Use your decodeImage function to display the fetched image
    } catch (error) {
        console.error('Error fetching image:', error);
    }
}

async function postImage(filePath, id) {
    try {
        const img = encodeImage(filePath); // Use your encodeImage function to encode the image
        const endPoint = '/img';
        const data = {
            id,
            image: img,
        };

        const response = await fetch(`${SERVER_URL}${endPoint}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            console.log('Image added successfully!');
        } else {
            console.error('Error posting image:', response.statusText);
        }
    } catch (error) {
        console.error('Error posting image:', error);
    }
}

// Example usage
const imageIdToFetch = 'samlogo';
fetchImage(imageIdToFetch);

const imageFilePathToPost = path.join(__dirname, 'path', 'to', 'your', 'image.jpg');
const imageIdToPost = 'unique_image_id';
postImage(imageFilePathToPost, imageIdToPost);
