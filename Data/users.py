from firebase_admin import auth
import requests
import firebase_admin.auth
from .auth import Auth
from .sendemails import SendEmail
from dotenv import load_dotenv
import os

"""
Archivo para manejar la autenticación de usuarios
"""
class User(Auth):
    def __init__(self,email="",password=""):
        super().__init__()
        self.__email = email
        self.__password = password

    def delete_app(self):
        if self.app:
            firebase_admin.delete_app(self.app)

    def send_verification_email(self,email) -> bool:
        try:
            link = auth.generate_email_verification_link(email)
            email_sender = SendEmail()
            message = f'Haz clic en el siguiente enlace para verificar tu correo electrónico: {link}'
            email_sender.send_email(email, link)
            return True
        except Exception as e:
            print('Error al enviar correo de verificación:', e)
            return False

    def authenticate_email_password(self):
        exists = load_dotenv('Data\.env')
        print(exists)
        if exists:
            api_key = os.getenv('API_KEY')
            print(api_key)
        else:
            return False
        
        url = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}'

        payload = {
            'email': self.__email,
            'password': self.__password,
            'returnSecureToken': False
        }

        response = requests.post(url, json=payload)
        if response.status_code == 200:
            user_data = response.json()
            return True
        else:
            print("Error al iniciar sesión:", response.json())
            return False
        