import bcrypt
from dotenv import load_dotenv, set_key
import os

class PasswordManager:
    def __init__(self):
        self.__salt_rounds = 12  # Atributo privado
        print("Password manager creado")
        
    def hash_credentials(self, arg):
        hashed_arg = bcrypt.hashpw(arg.encode('utf-8'), bcrypt.gensalt(self.__salt_rounds))
        return hashed_arg.decode('utf-8')  # Decodificar para guardar como cadena

    def check_data(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Instanciar PasswordManager
passmana = PasswordManager()

# Hashear y guardar el correo electrónico
hashed_email = passmana.hash_credentials("jamesburk3000@gmail.com")
load_dotenv(".env")
set_key(".env", "email_address", hashed_email)

# Hashear y guardar la contraseña de la aplicación
hashed_app_password = passmana.hash_credentials("hodo ewee mcjs jfsy")
set_key(".env", "app_pwd", hashed_app_password)

# Mostrar los hashes
print(f"Hash del correo electrónico guardado: {hashed_email}")
print(f"Hash de la contraseña de la aplicación guardado: {hashed_app_password}")
