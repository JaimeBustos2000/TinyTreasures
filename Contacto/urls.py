from django.urls import path
from .views import contacto, enviarCorreo

urlpatterns = [
    path('', contacto,name='contacto'),
    path('enviarCorreo/', enviarCorreo,name='enviarCorreo'),
]