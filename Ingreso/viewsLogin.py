from django.shortcuts import render

def login(request):
    return render(request,'login.html')


def loginIn(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username=="admin" and password=="admin":
            return render(request,'login_in.html')
        else:
            return render(request,'login.html')
        
    return render(request,'login_in.html',context={"error:":"Error al ingresar usuario o contraseña incorrectos"})