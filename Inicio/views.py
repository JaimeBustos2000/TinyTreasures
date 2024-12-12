from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html')

def perfil(request):
    data = request.session.get('data', {})
    return render(request,'perfil.html',context={"data":data})

def desconectar(request):
    request.session.flush()
    return render(request,'index.html')