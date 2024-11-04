import re
import hashlib
import requests

class cleaninputs:
    def __init__(self, entry:str):
        self.entry = entry
        
    def cleaninput(self):
        self.entry = self.entry.strip()
    
    def clean_email(self):
        self.entry = self.entry.lower()
        valid_email = self.check_format_email()
        
        if isinstance(valid_email, tuple):
            error = valid_email[1]
            valid_email = valid_email[0]
            
            if valid_email:
                self.cleaninput()
                return True
            else:
                return False, error
        
        elif isinstance(valid_email, bool):
            if valid_email:
                self.cleaninput()
                return True
        
        
        if valid_email:
            self.cleaninput()
            return True
        else:
            return False,error
    

    def check_format_email(self):
        before_arroba = self.entry.split('@')[0]
        regex = r'^[a-zA-Z][a-zA-Z0-9]*(\.[a-zA-Z0-9]+)?$'
        
        first_condition = bool(re.match(regex, before_arroba))
        
        if not first_condition:
            error = 'Email inválido: formato incorrecto antes de @'
            return False, error
        
        try:
            after_arroba = self.entry.split('@')[1]
            after_arroba_split = after_arroba.split('.')
        except IndexError:
            error = 'Email inválido: falta @'
            return False, error

        # Verificar que after_arroba contiene un punto y es un dominio permitido
        if len(after_arroba_split) < 2 or not all(part.isalnum() for part in after_arroba_split):
            error = 'Email inválido: formato incorrecto después de @'
            return False, error
        
        domain = after_arroba_split[0]
        if domain not in ['gmail', 'hotmail', 'outlook', 'yahoo']:
            error= 'Email inválido: dominio no permitido, solo se permiten gmail, hotmail, outlook y yahoo'
            return False, error
        
        if self.entry.endswith('.com') or self.entry.endswith('.cl') or self.entry.endswith('.net'):
            return True
        else:
            error = 'Email inválido: sufijo no permitido'
            return False, error


    def check_format_rut(self):
        if '-' not in self.entry:
            error = 'RUT inválido: falta guión separador'
            print(error)
            return False, error

        # Invertir el RUT y limpiar caracteres
        rut_reverse = self.entry[::-1]
        rut_split = rut_reverse.replace('-', '').strip()
        rut_split = rut_split.replace('.', '').strip()

        digito_verificador = rut_split[0]  
        rut_numeros = (rut_split[1:])     

        print("rut_numeros:", rut_numeros)
        if not rut_numeros.isdigit():
            error = 'RUT inválido: caracteres no numéricos en la parte numérica'
            return False, error

        serie = [2, 3, 4, 5, 6, 7]
        serie_index = 0
        suma = 0

        for numero in rut_numeros:
            suma += int(numero) * serie[serie_index]
            serie_index += 1
            if serie_index == len(serie):
                serie_index = 0

        resto = suma % 11
        digito_calculado = 11 - resto
        if digito_calculado == 10:
            digito_calculado = "K"
        elif digito_calculado == 11:
            digito_calculado = "0"  

        if str(digito_calculado) == digito_verificador.upper():  # Asegurarse de que la comparación no sea sensible a mayúsculas
            print('RUT válido')
            return True
        else:
            error = 'RUT inválido: dígito verificador incorrecto'
            return False, error

    def is_password_secure(self):
        
        # Obtener el hash de la contraseña en formato SHA-1
        sha1_hash = hashlib.sha1(self.entry.encode()).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]

        # Hacer la solicitud a la API de HIBP
        response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")

        if response.status_code != 200:
            raise RuntimeError(f"Error fetching: {response.status_code}")

        # Comprobar si el sufijo del hash está en la respuesta
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return True

        return False



"""
explain use example:

email_checker = cleaninputs('jaimebustos@gmail.com')
is_valid_email = email_checker.clean_email()"""

"""rut_checker = cleaninputs('7810239-k')
rut_checker.check_format_rut()"""

