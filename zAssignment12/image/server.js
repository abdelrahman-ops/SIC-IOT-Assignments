const express = require('express');
const admin = require('firebase-admin');
const serviceAccount = require('./image-7ac5d-firebase-adminsdk-qyh13-db4b60ec72.json');

const app = express();
const port = 5000;

// Initialize Firebase Admin SDK
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: 'firebase-adminsdk-qyh13@image-7ac5d.iam.gserviceaccount.com'
});

const db = admin.firestore();

// Middleware to parse JSON requests
app.use(express.json());

app.get('/img/:id', async (req, res) => {
  const id = req.params.id;
  try {
    const docRef = db.collection('images').doc(id);
    const doc = await docRef.get();
    if (!doc.exists) {
      return res.status(404).json({ error: 'Image not found' });
    }
    const image_data = doc.data().image_data;
    res.json({ image: image_data });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/img', async (req, res) => {
  const { image, id } = req.body;
  try {
    const docRef = db.collection('images').doc(id);
    await docRef.set({ image_data: image });
    res.status(201).send('OK');
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
