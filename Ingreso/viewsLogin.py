from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import Login
from FirebaseData.users import User
from inputsclean.cleaninputs import cleaninputs
from FirebaseData.querys import dataOperations
import json
import os

def login(request):
    login = Login()
    return render(request,'login.html',context={"login":login})


def loginIn(request):
    if request.method=="POST":
        form = Login(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data['email']
            cleaner = cleaninputs(email)

            try:
                valid_entry, error = cleaner.clean_email()
                print("error",error)
            except:
                valid_entry = cleaner.clean_email()

            if valid_entry:
                password = form.cleaned_data['password']
                
                # Crear una instancia de la clase User que realiza la autenticación
                usermana = User(email,password)
                # Se pasa la referencia de la base de datos de la clase user a la clase dataOperations
                db = usermana.bd_references()
                # Se crea una instancia de la clase dataOperations que manipula los datos de la base de datos
                operationDB = dataOperations(db)
                
                # Se verifica si el usuario existe en la base de datos de firebase
                if usermana.valid_credentials(email):
                    # Se simula un inicio de sesion a firebase
                    if usermana.authenticate_email_password():
                        # Se obtiene el uid del usuario para obtener su rol solo por medio de la otra clase
                        uid = usermana.valid_credentials(email)
                        role = operationDB.obtain_user_role_from_uid(uid)
                        
                        user_data = operationDB.obtain_user_data(uid)
                        request.session['user_id'] = uid
                        request.session['user_role'] = role
                        user_data['correo'] = email
                        request.session['data'] = user_data

                        # Convertir los datos de la sesión a un diccionario simple
                        session_data = dict(request.session.items())

                        ruta_relativa = os.path.join('TinyTreasures', 'sessions.json')
                        with open(ruta_relativa, 'w') as file:
                            json.dump(session_data, file)

                        print('Sesión guardada:', session_data)
                        usermana.delete_app()
                        return redirect(reverse('index'))
                    
                    else:
                        usermana.delete_app()
                        error = "No hay usuario o contraseña con esas credenciales"
                        return render(request,'login.html',context={
                            "error":error,  
                            "login":form})
                else:
                    usermana.delete_app()
                    error = "No se pudo autenticar el usuario, error al ingresar el email o contraseña"
                    return render(request,'login.html',context={
                        "error":error,
                        "login":form})

            else:
                return render(request,'login.html',context={"error":error,
                                                            "login":form})
        else:
            error = "Error al ingresar usuario o contraseña incorrectos mal formato"
            return render(request,'login.html',context={"error":error,
                                                        "login":form})
    
    error = "Error al ingresar usuario o contraseña incorrectos"   
    return render(request,'login.html',context={
        "error":error, 
        "login":form})