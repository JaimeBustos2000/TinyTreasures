from django.shortcuts import render
from .forms import ContactoForm

def contacto(request):
    form = ContactoForm()
    return render(request,'contacto.html', {'contacto_form': form})

def enviarCorreo(request):
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']
            asunto = form.cleaned_data['asunto']
            fecha = form.cleaned_data['fecha']
        else:
            return render(request,'contacto.html', {"mensaje": "Error al enviar el mensaje, por favor verifique los datos."})
        
    return render(request,'contacto.html', {"mensaje": "Mensaje enviado con éxito, gracias por contactarnos."})