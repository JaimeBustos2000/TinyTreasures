import re


class cleaninputs:
    def __init__(self, entry:str):
        self.entry = entry
        
    def cleaninput(self):
        self.entry = self.entry.strip()
    
    def clean_email(self):
        self.entry = self.entry.lower()
        
        if self.check_format_email():
            self.cleaninput()
            return self.entry 
        else:
            return self.entry
    

    def check_format_email(self):
        before_arroba = self.entry.split('@')[0]
        regex = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?$'
        
        first_condition = bool(re.match(regex, before_arroba))
        
        if not first_condition:
            print('Email inválido: formato incorrecto antes de @')
            return False
        
        print(f'Parte antes del arroba: {before_arroba}')
        
        try:
            after_arroba = self.entry.split('@')[1]
            after_arroba_split = after_arroba.split('.')
            print("Parte después del arroba (dividida):", after_arroba_split)
        except IndexError:
            print('Email inválido: falta @')
            return False

        # Verificar que after_arroba contiene un punto y es un dominio permitido
        if len(after_arroba_split) < 2 or not all(part.isalnum() for part in after_arroba_split):
            print('Email inválido: formato incorrecto después de @')
            return False
        
        domain = after_arroba_split[0]
        if domain not in ['gmail', 'hotmail', 'outlook', 'yahoo']:
            print('Email inválido: dominio no permitido')
            return False
        
        if self.entry.endswith('.com') or self.entry.endswith('.cl') or self.entry.endswith('.net'):
            print('Email válido')
            return True
        else:
            print('Email inválido: sufijo no permitido')
            return False


    def check_format_rut(self):
        if '-' not in self.entry:
            print('RUT inválido: falta guión')
            return False

        # Invertir el RUT y limpiar caracteres
        rut_reverse = self.entry[::-1]
        rut_split = rut_reverse.replace('-', '').strip()
        rut_split = rut_split.replace('.', '').strip()

        digito_verificador = rut_split[0]  
        rut_numeros = (rut_split[1:])     

        print("rut_numeros:", rut_numeros)
        if not rut_numeros.isdigit():
            print('RUT inválido: caracteres no numéricos en la parte numérica')
            return False

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
            print('RUT inválido: dígito verificador incorrecto')
            return False

        
"""email_checker = cleaninputs('jaimebustos@gmail.com')
is_valid_email = email_checker.clean_email()"""

rut_checker = cleaninputs('7810239-k')
rut_checker.check_format_rut()

