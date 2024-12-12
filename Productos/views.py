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
