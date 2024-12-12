import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendEmail():
    def __init__(self):
        try:
            self.__server = smtplib.SMTP('smtp.gmail.com', 587)
            self.__server.starttls()
            self.__server.login('jamesburk3000@gmail.com', 'hodo ewee mcjs jfsy')
            print("Conexión al servidor SMTP establecida y autenticada correctamente.")
        except Exception as e:
            print(f"Error al conectar o autenticar con el servidor SMTP: {e}")

    def send_email(self, to_email, message):
        try:
            subject = 'Verificación de correo electrónico'
            msg = MIMEMultipart()
            msg['From'] = 'jamesburk3000@gmail.com'
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Adjuntar el cuerpo del mensaje
            msg.attach(MIMEText(message, 'plain'))
            
            # Enviar el correo
            self.__server.send_message(msg)
            print("Correo enviado exitosamente.")
        except Exception as e:
            print(f"Error al enviar correo: {e}")
        finally:
            try:
                self.__server.quit()
            except Exception as e:
                print(f"Error al cerrar la conexión SMTP: {e}")

    def __del__(self):
        try:
            self.__server.quit()
        except:
            pass
        print("Destructor ejecutado")
        
    def __str__(self):
        return "Se ha enviado el correo"
    
    def __repr__(self):
        return "Se ha enviado el correo"