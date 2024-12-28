from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Data.directories import DirectoriManager

def index(request):
    dm = DirectoriManager()
    get_images = dm.get_random_images()
    url_base = 'http://127.0.0.1:8000/'
    for i in range(len(get_images)):
        # Cambiar los slash por slash simples
        get_images[i] = get_images[i].replace('\\','/')
        get_images[i] = url_base + get_images[i]
    
    print(get_images)
    return render(request,'index.html',context={"images":get_images})

def perfil(request):
    data = request.session.get('data', {})
    return render(request,'perfil.html',context={"data":data})

def desconectar(request):
    request.session.flush()
    dm = DirectoriManager()
    get_images = dm.get_random_images()
    url_base = 'http://127.0.0.1:8000/'
    for i in range(len(get_images)):
        # Cambiar los slash por slash simples
        get_images[i] = get_images[i].replace('\\','/')
        get_images[i] = url_base + get_images[i]
    
    print(get_images)
    return render(request,'index.html',context={"images":get_images})