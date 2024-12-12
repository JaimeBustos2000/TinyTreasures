from django.urls import path
from .views import mis_productos_page,product_view,new_product


urlpatterns = [
    path('', mis_productos_page,name='edicion_page'),
    path('add/', product_view,name='add_product'),
    path('addproduct/', new_product,name='addproduct'),
]
