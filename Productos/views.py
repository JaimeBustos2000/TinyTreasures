from django.shortcuts import render
from Data.querys import dataOperations
from Data.users import User

categorias = [
    "Electrónica",
    "Ropa",
    "Hogar",
    "Salud y Belleza",
    "Alimentos y Bebidas",
    "Deportes",
    "Juguetes",
    "Automotriz",
    "Tecnología",
    "Libros",
    "Mascotas",
    "Jardinería",
    "Muebles",
    "Accesorios",
    "Herramientas",
    "Otros"
]

colores = [
    "Rojo",
    "Azul",
    "Verde",
    "Amarillo",
    "Naranja",
    "Rosa",
    "Morado",
    "Blanco"
    ]

def productos(request):
    user = User()
    bdref = user.bd_references()
    operation = dataOperations(bdref)
    user_data = operation.obtain_products()
    print('user_data:', user_data)
    user.delete_app()
    return render(request,'productos.html',context={"categorias":categorias,"colores":colores})

def detalle_producto(request,product_code):
    user = User()
    bdref = user.bd_references()
    operation = dataOperations(bdref)
    user_id = request.session['user_id']
    product = operation.get_one_product(user_id,product_code)
    # concatenar base server 127.0.0.1:8000 a la url
    product['url'] = 'http://127.0.0.1:8000/'+product['url']
    product['stock'] = int(product['stock'])
    stock_list = list(range(1, int(product['stock']) + 1))
    user.delete_app()
    return render(request,'detalle_producto.html',context={"product":product,"stock_list":stock_list})