"""
URL configuration for TinyTreasures project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Inicio.urls')),
    path('Contacto/', include('Contacto.urls')),
    path('Ayuda/', include('Ayuda.urls')),
    path('ListaProductos/', include('ListaProductos.urls')),
    path('LoginRegistro/', include('IniciarSesion.urls')),
    path('EdicionProductos/', include('EdicionProductos.urls')),
]
