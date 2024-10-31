from django.shortcuts import render
from .forms import Registrar,Login

def registro(request):
    registrar = Registrar()
    return render(request,'registro.html',{"registrar":registrar})

def registrado(request):
    login = Login()
    return render(request,'login.html',{"login":login})