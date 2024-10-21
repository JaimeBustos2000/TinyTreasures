from django.urls import path
from .views import ayuda

urlpatterns = [
    path('', ayuda,name='ayuda'),
]
