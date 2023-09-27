const admin = require('firebase-admin');
const serviceAccount = require('./serviceAccountKey.json'); // Replace with your service account key

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: './image-7ac5d-firebase-adminsdk-qyh13-85345609db.json', // Replace with your Firebase project URL
});

const db = admin.firestore();

function writeImage(imageString, id) {
    // Write the image data to Firestore
    const imageRef = db.collection('images').doc(id);
    return imageRef.set({ image_data: imageString });
}

function fetchImage(id) {
    // Fetch the image data from Firestore
    const imageRef = db.collection('images').doc(id);
    return imageRef.get().then((doc) => {
        if (doc.exists) {
            return doc.data().image_data;
        } else {
            throw new Error('Image not found');
        }
    });
}

module.exports = { writeImage, fetchImage };
