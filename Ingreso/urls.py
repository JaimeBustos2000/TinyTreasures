from django.urls import path,include
from .viewsLogin import login, loginIn
from .viewsRegistro import registro,registrado

urlpatterns = [
    path('registro/', registro,name='registro'),
    path('login/', login,name='login'),
    path('loginIn/', loginIn,name='loginIn'),
    path('auth/',registrado,name='auth'),
    path('logued/',include('Inicio.urls'),name='logued'),
]
