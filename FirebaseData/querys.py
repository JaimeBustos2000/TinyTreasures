import firebase_admin
from firebase_admin import credentials,firestore,auth
import firebase_admin.auth
from google.cloud.firestore_v1 import FieldFilter

class dataOperations:
    def __init__(self,db):
        self.__conn = db
    
    def obtain_user_role_from_uid(self,uid):
        userstable = self.__conn.collection('users')
        role = userstable.document(uid).get().to_dict()['usertype']
        
        if userstable:
            print('Usuario encontrado:', userstable)
            return role
    
    def obtain_user_data(self,uid):
        userstable = self.__conn.collection('users')
        user_data = userstable.document(uid).get().to_dict()
        return user_data
    
    def set_data(self,data):
        userstable = self.__conn.collection('users')
        try:
            userdata = {
                'nombre':data['nombre'],
                'rut':data['rut'],
                'email':data['email'],
                'usertype':data['usertype'],
                'telefono':data['telefono'],
                'verified':False,
            }
            userstable.document(data['uid']).set(userdata)
            return True
        except:
            return False
        
    def user_exist(self, email):
        user_table = self.__conn.collection('users')
        filter = FieldFilter('email', '==', email)
        user = user_table.where(filter=filter).limit(1).get()
        return bool(user)
        

    def create_user(self,email,passw):
        try:
            authentication = auth.create_user(email=email,password=passw)
            print('Usuario creado exitosamente:', authentication.uid)
            return True, "Usuario creado exitosamente", authentication.uid
        
        except auth.EmailAlreadyExistsError:
            error = 'El correo electrónico ya está en uso.'
            return False, error
        
        except Exception as e:
            error = f'Error al crear el usuario:', e
            return False, error