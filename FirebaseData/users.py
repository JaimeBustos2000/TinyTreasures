from firebase_admin import auth
import requests
import firebase_admin.auth
from .psw import PasswordManager
from .auth import Auth

class User(Auth,PasswordManager):
    def __init__(self,email,password):
        super().__init__()
        self.__email = email
        self.__password = password
        self.valid_created = False

    def valid_credentials(self):
        self.auth = auth.get_user_by_email(self.__email)
        self.uid = self.auth.uid
        
        if self.auth and self.uid:
            return self.uid
        else:
            return False

    def set_auth(self):
        try:
            self.auth = auth.create_user(email=self.__email, password=self.__password)
            print('Usuario creado exitosamente:', self.auth.uid)
            self.valid_created = True
            return self.auth
        except auth.EmailAlreadyExistsError:
            print('El correo electrónico ya está en uso.')
            return None
        except Exception as e:
            print('Error al crear el usuario:', e)
            return None

    def is_valid_created_user(self):
        return self.valid_created

    def obtain_user_uid_role(self):
        self.uid = self.valid_credentials()
        role = self.users.document(self.uid).get().to_dict()['usertype']
        
        if self.users:
            print('Usuario encontrado:', self.users)
            return role
        

    def send_verification_email(self):
        try:
            auth.generate_email_verification_link(self.auth)
            print('Correo de verificación enviado')
        except Exception as e:
            print('Error al enviar correo de verificación:', e)
            
    def authenticate_email_password(self):
        # Usa la Web API Key que encontraste en la consola de Firebase
        api_key = 'AIzaSyBUW2nB7m5o7UNGW24a8CcViSD5ZE6ySBY'  # Reemplaza con tu Web API Key
        url = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}'

        payload = {
            'email': self.__email,
            'password': self.__password,
            'returnSecureToken': True
        }

        response = requests.post(url, json=payload)
        if response.status_code == 200:
            user_data = response.json()
            id_token = user_data.get('idToken')
            role = self.obtain_user_uid_role()
            print('role:', role)
            return id_token
        else:
            print("Error al iniciar sesión:", response.json())
            return None

