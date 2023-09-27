import firebase_admin
from firebase_admin import credentials, initialize_app
from firebase_admin.firestore import client


def write_img(image_string: str, id: str):
    cred = credentials.Certificate('./image-7ac5d-firebase-adminsdk-qyh13-db4b60ec72.json')
    initialize_app(cred)
    
    db = client()
    
    doc_ref = db.collection('images').document(id)
    doc_ref.set({'image_data': image_string})


def fetch_image(id: str) -> str:
    cred = credentials.Certificate('./image-7ac5d-firebase-adminsdk-qyh13-db4b60ec72.json')
    firebase_admin.initialize_app(cred)

    db = client()

    doc_ref = db.collection('images').document(id)
    doc = doc_ref.get()
    image_data = doc.get('image_data')
    return image_data
