import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase Admin SDK
cred = credentials.Certificate(
    "./image-7ac5d-firebase-adminsdk-qyh13-db4b60ec72.json")
firebase_admin.initialize_app(cred, {"store1": "storing"})

# Create a reference to the Firebase Storage bucket
bucket = storage.bucket()

# Replace "image.jpg" with the actual image file name you want to check
image_name = "logo.jpg"

# Check if the image exists in Firebase Storage
blob = bucket.blob(image_name)
exists = blob.exists()

if exists:
    print(f"The image '{image_name}' exists in Firebase Storage.")
else:
    print(f"The image '{image_name}' does not exist in Firebase Storage.")
