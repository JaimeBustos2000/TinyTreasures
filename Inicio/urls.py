from django.urls import path
from .views import index, desconectar, perfil


urlpatterns = [
    path('', index,name='index'),
    path('perfil/', perfil,name='perfil'),
    path('desconectar/', desconectar,name='desconectar'),
]
