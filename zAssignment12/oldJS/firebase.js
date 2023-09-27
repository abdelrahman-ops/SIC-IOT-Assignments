const admin = require('firebase-admin');

// Initialize Firebase Admin SDK
const serviceAccount = require('./image-7ac5d-firebase-adminsdk-qyh13-85345609db.json');
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

// ... Rest of the code
// ... Rest of the code

app.use(bodyParser.json());

// Get image by ID
app.get('/img/:id', async (req, res) => {
  const { id } = req.params;
  const img = await fetchImage(id);
  res.json({ image: img });
});

// Post image
app.post('/img', (req, res) => {
  const { id, image } = req.body;
  writeImage(image, id);
  res.send('OK');
});

async function fetchImage(id) {
  const docRef = db.collection('images').doc(id);
  const doc = await docRef.get();
  return doc.data().image_data;
}

function writeImage(imageString, id) {
  const docRef = db.collection('images').doc(id);
  docRef.set({ image_data: imageString });
}

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
