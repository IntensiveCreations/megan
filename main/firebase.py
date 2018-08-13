import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('res/serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)

#use of Google Application Default Credentials
#default_app = firebase_admin.initialize_app()

