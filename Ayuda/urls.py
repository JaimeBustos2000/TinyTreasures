from django.urls import path
from .views import ayuda,terminos

urlpatterns = [
    path('', ayuda,name='ayuda'),
    path('terminos-y-condiciones/', terminos,name='terminos-y-condiciones'),
]
