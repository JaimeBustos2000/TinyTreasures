from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import Login
from FirebaseData.users import User
from inputsclean.cleaninputs import cleaninputs
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
                user = User(email,password)

                if user.valid_credentials():
                    if user.authenticate_email_password():
                        print('Usuario autenticado')
                        uid = user.valid_credentials()
                        role = user.obtain_user_uid_role()
                        request.session['user_id'] = uid
                        request.session['user_role'] = role
                        user_data = user.obtain_user_data(uid)
                        user_data['correo'] = email
                        request.session['data'] = user_data

                        # Convertir los datos de la sesión a un diccionario simple
                        session_data = dict(request.session.items())

                        ruta_relativa = os.path.join('TinyTreasures', 'sessions.json')
                        with open(ruta_relativa, 'w') as file:
                            json.dump(session_data, file)

                        print('Sesión guardada:', session_data)
                        user.delete_app()
                        return redirect(reverse('index'))
                    
                    else:
                        user.delete_app()
                        error = "No hay usuario o contraseña con esas credenciales"
                        return render(request,'login.html',context={
                            "error":error,  
                            "login":form})
                else:
                    user.delete_app()
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