from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import Login
from FirebaseData.users import User

def login(request):
    login = Login()
    return render(request,'login.html',context={"login":login})


def loginIn(request):
    if request.method=="POST":
        form = Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = User(email,password)
            if user.valid_credentials():
                if user.authenticate_email_password():
                    print('Usuario autenticado')
                    return redirect(reverse('index'))
            else:
                return render(request,'login.html',context={"error:":"Error al ingresar usuario o contraseña incorrectos"})
            
        else:
            return render(request,'login.html',context={"error:":"Error al ingresar usuario o contraseña incorrectos"})
        
        
    return render(request,'login_in.html',context={"error:":"Error al ingresar usuario o contraseña incorrectos"})