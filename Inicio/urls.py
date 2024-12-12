from django.urls import path, include
from .views import index, desconectar, perfil
from rest_framework import routers
from .Api import companies_api
from .Api import products_user_api
from .Api import all_products

router = routers.DefaultRouter()
router.register(r'companies', companies_api, basename='companies')
router.register(r'products', products_user_api, basename='products')
router.register(r'all_products', all_products, basename='all_products')

urlpatterns = [
    path('', index,name='index'),
    path('perfil/', perfil,name='perfil'),
    path('desconectar/', desconectar,name='desconectar'),
    path('api/', include(router.urls)),
]
