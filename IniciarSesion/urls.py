from django.urls import path
from .viewsLogin import login
from .viewsRegistro import registro

urlpatterns = [
    path('registro/', registro,name='registro'),
    path('login/', login,name='login'),
]
