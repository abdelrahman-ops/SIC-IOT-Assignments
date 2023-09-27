import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

os.chdir("D:/Documents/IOT Training/Assignments/Assignment 10/node_listens")

cred = credentials.Certificate("fb-project-933a9-firebase-adminsdk-2ib2y-48d0717b07.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_data():
    doc_ref = db.collection('abdelrahman').document('abdelrahman')
    doc_ref.set({
        'name': 'Ahmed',
        'height': '180 cm',
        'gender': 'Male'

    })
    print("Data added.")


if __name__ == '__main__':
    add_data()
