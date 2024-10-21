from django.urls import path
from .views import edicionProductos

urlpatterns = [
    path('', edicionProductos,name='edicionProductos'),
]
