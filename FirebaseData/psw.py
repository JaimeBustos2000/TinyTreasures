import bcrypt

class PasswordManager:
    def __init__(self):
        self.__salt_rounds = 12  # Atributo privado
        print("Password manager creado")
        
    def hash_credencials(self, arg):
        hashed_arg = bcrypt.hashpw(arg.encode('utf-8'), bcrypt.gensalt(self.__salt_rounds))
        return hashed_arg

    def check_data(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    