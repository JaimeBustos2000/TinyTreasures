from django.shortcuts import render

def ayuda(request):
    return render(request,'ayuda.html')

def terminos(request):
    return render(request,'terminos.html')