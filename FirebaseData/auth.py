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
        self.cred = credentials.Certificate("FirebaseData/firebase-credentials.json")
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

"""    async def create_collections(self):    
        try:
            if self.users.get() or self.products.get() or self.db.collection("productos").get():
                print("Colecciones ya existen")
                return
            self.principal_db = self.db.collection("productos").document().set({"Producto prueba":"Producto 1"})
            self.secondary_db = self.db.collection("users").document().set({"Usuario prueba":"Usuario 1","pasword":"1234"})
            
        except Exception as e:
            print("Error al crear colecciones: ",e)
            
    async def main(self):
        await self.create_collections() """
        


""" cred = credentials.Certificate("FirebaseData/firebase-credentials.json")
app = firebase_admin.initialize_app(cred)
print(app.name)

db = firestore.client()

data = {
    "name": "John Doe",
    "age": 30,
    "email": "jhondoe12345"
    }

doc_ref = db.collection("users").document()
doc_ref.set(data)

print("Document id: ", doc_ref.id) """