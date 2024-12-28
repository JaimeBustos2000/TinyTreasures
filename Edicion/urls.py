from django.urls import path
from .views import mis_productos_page,product_view,new_product,edit_product,apply_changues


urlpatterns = [
    path('', mis_productos_page,name='edicion_page'),
    path('add/', product_view,name='add_product'),
    path('addproduct/', new_product,name='addproduct'),
    path('edit/<str:product_code>/', edit_product,name ='editproduct'),
    path('edit/apply/<str:product_code>/', apply_changues,name ='confirm_editproduct'),
]
