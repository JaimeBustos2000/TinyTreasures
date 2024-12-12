from django.urls import path,include
from .viewsLogin import login_page, loginIn
from .viewsRegistro import register_page,sucess_register

urlpatterns = [
    path('registro/', register_page,name='registro'),
    path('login/', login_page,name='login'),
    path('loginIn/', loginIn,name='loginIn'),
    path('auth/',sucess_register,name='auth'),
]
