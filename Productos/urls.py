from django.urls import path
from .views import productos,detalle_producto

urlpatterns = [
    path('', productos,name='productos'),
    path('detail/<str:product_code>/', detalle_producto,name='detalle_producto'),
]
