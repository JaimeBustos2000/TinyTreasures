import firebase_admin
from firebase_admin import credentials,firestore,auth
import firebase_admin.auth

"""
Clase que permite la conexion y en primera instancia creacion de colecciones si no existen

params: 
        cred: firebase credentials from json file
        app: aplicacion de firebase
        db: base de datos de firebase
"""

class Auth:
    def __init__(self):
        self.cred = credentials.Certificate("Data/firebase-credentials.json")
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        
    def bd_references(self):
        return self.db

    def valid_credentials(self,email):
        try:
            self.user = auth.get_user_by_email(email)
        except auth.UserNotFoundError:
            print('Usuario no encontrado')
            return False
        
        self.uid = self.user.uid
        
        if self.user and self.uid:
            return self.uid
        else:
            return False