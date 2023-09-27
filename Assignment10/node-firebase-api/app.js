const express = require('express');
const bodyParser = require('body-parser');
const admin = require('firebase-admin');

const app = express();
const port = process.env.PORT || 3000;

// Initialize Firebase Admin SDK using service account credentials
const serviceAccount = require('./node-api-75637-firebase-adminsdk-tg1ho-a0cd4b9353.json');
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

app.use(bodyParser.json());

// Define API route to receive data and add it to Firestore
app.post('/api/data', (req, res) => {
  const data = req.body;

  // Reference to Firestore collection
  const db = admin.firestore();
  const collection = db.collection('node-api');

  // Add the data to Firestore
  collection
    .doc('server-data')
    .set(data)
    .then(() => {
      res.status(200).json({ message: 'Data added to Firestore successfully' });
    })
    .catch((error) => {
      res.status(500).json({ message: 'Data could not be added to Firestore', error });
    });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
