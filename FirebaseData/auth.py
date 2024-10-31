import firebase_admin
from firebase_admin import credentials,firestore,exceptions,auth
import asyncio

import firebase_admin.auth



class Auth:
    def __init__(self):
        self.cred = credentials.Certificate("FirebaseData/firebase-credentials.json")
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        self.users = self.db.collection("users")
        self.products = self.db.collection("productos")
        asyncio.run(self.main())
        
    def get_db(self):
        return self.db
    
    async def create_collections(self):    
        try:
            if self.users.get() or self.products.get() or self.db.collection("productos").get():
                print("Colecciones ya existen")
                return
            self.principal_db = self.db.collection("productos").document().set({"Producto prueba":"Producto 1"})
            self.secondary_db = self.db.collection("users").document().set({"Usuario prueba":"Usuario 1","pasword":"1234"})
            
        except Exception as e:
            print("Error al crear colecciones: ",e)
            
    async def main(self):
        await self.create_collections()
        


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