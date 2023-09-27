const axios = require('axios');
const { encodeImg } = require('./util');

const URL = 'http://localhost:5000/';

async function fetchImage(id) {
  const endPoint = `/img/${id}`;
  const response = await axios.get(URL + endPoint);
  const data = response.data;
  decodeImage(data.image);
}

async function postImage(path, id) {
  const image = encodeImg(path);
  const endPoint = '/img';
  const data = {
    id: id,
    image: image
  };
  const response = await axios.post(URL + endPoint, data);
  if (response.data === 'OK') {
    console.log('Added Successfully!');
  }
}

// Usage examples
// Provide the path to the image you want to upload
const imagePath = './logo.jpeg';

// Call the postImage() function with the image path and ID
postImage(imagePath, 'pic');
