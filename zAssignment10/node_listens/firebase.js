const admin = require('firebase-admin');

// Initialize Firebase
const serviceAccount = require('./node_listens/fb-project-933a9-firebase-adminsdk-2ib2y-48d0717b07.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

// Listen for data changes on the entire collection
const collectionRef = db.collection('abdelrahman');

const observer = collectionRef.onSnapshot(querySnapshot => {
  console.log('Received collection snapshot');
  querySnapshot.forEach(docSnapshot => {
    console.log(`Document ID: ${docSnapshot.id}`);
    console.log(docSnapshot.data());
  });
}, err => {
  console.log(`Encountered error: ${err}`);
});
