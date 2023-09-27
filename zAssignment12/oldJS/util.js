const fs = require('fs');
const { promisify } = require('util');
const { Storage } = require('@google-cloud/storage');
const { v4: uuidv4 } = require('uuid');

const storage = new Storage();
const bucketName = 'your-bucket-name';

async function decodeImage(imageData) {
  // Implement image decoding logic
  // Example: Display image in the browser
}

function encodeImg(path) {
  const image = fs.readFileSync(path);
  const base64Image = image.toString('base64');
  return base64Image;
}

module.exports = { decodeImage, encodeImg };
