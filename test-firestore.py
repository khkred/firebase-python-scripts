import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the Firebase app if it hasn't been initialized yet
if not firebase_admin._apps:
        #YOU SHOULD SET THE PATH FOR YOUR OWN PRIVATE KEY
    cred = credentials.Certificate('/Users/khkr/Documents/khkr-docs/Developer/PictureMenu/firebase-keys/pm-firebase-python-key.json')
    firebase_admin.initialize_app(cred)

# Access Firestore
db = firestore.client()

# Define the data to be added
test_data = {
    'name': 'Test User',
    'timestamp': firestore.SERVER_TIMESTAMP,
    'active': True,
    'score': 100
}

# Reference to the Firestore collection
collection_ref = db.collection('python-test')

# Add data to the collection
try:
    doc_ref = collection_ref.add(test_data)
    print(f'Data added to Firestore with document ID: {doc_ref[1].id}')
except Exception as e:
    print(f'Failed to add data to Firestore: {e}')
