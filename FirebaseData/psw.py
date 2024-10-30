import bcrypt

class PasswordManager:
    def __init__(self):
        self.__salt_rounds = 12  # Atributo privado
        
    def hash_credencials(self, arg):
        hashed_arg = bcrypt.hashpw(arg.encode('utf-8'), bcrypt.gensalt(self.__salt_rounds))
        return hashed_arg

    def check_data(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    

pswmana = PasswordManager()
hashed_password = pswmana.hash_credencials("1234")
psw = input("Ingrese contraseña: ")

users = {
    "user1":hashed_password
}

if pswmana.check_data(psw, users["user1"]):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")