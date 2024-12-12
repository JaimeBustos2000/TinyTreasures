from django.shortcuts import render
from django.contrib.auth.decorators import  user_passes_test
from Data.users import User
from Data.querys import dataOperations
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Data.directories import DirectoriManager

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


def mis_productos_page(request):
    return render(request,'misproductos.html')


def product_view(request):
    marca=request.session["data"]["nombre"]
    
    user = User()
    bd_ref = user.bd_references()
    data_instance = dataOperations(bd_ref)
    user_data = data_instance.obtain_products()
    user.delete_app()
    
    return render(request,'nuevo.html',context={
        "categorias":categorias,
        "colores":colores,
        "marca":marca,
        "productos":user_data})

@csrf_exempt
def new_product(request):
    if request.method == "POST":
        # Flujo de clases de interaccion con firebase y la base de datos
        user = User()
        bd_ref = user.bd_references()
        data_instance = dataOperations(bd_ref)
        try:
            # Obtener objeto imagen
            form_data_files = request.FILES['image']
            # Obtener uid de usuario de la sesion
            uid = request.session["user_id"]
            
            # crear producto en la base de datos con el texto plano del formulario
            product_data = request.POST.dict()
            
            # Eliminar token de seguridad del formulario
            del product_data['csrfmiddlewaretoken']
            # Crear documento del producto
            try:
                response_db = data_instance.create_new_product_to_user(uid,product_data)
                print("Respuesta DB:",response_db)
            except Exception as e:
                print("Error al crear producto:",e)
                return JsonResponse({"status":"ERROR","message":"Error al crear producto"},status=500)
            
            # Obtener id de producto generado
            id_producto = response_db[1]
            print("ID producto:",id_producto)
            
            # Crear carpetas en el backend para almacenar la imagen
            directory = DirectoriManager()
            directory.create_user_directory(uid)
            directory.subfolder_from_directory(uid,id_producto)
            directory.save_image_from_uid_and_product_id(uid,id_producto,form_data_files)
            
            data_instance.append_characteristic_to_product(uid,
                                                           id_producto,
                                                           {'url':f'public/{uid}/{id_producto}/{form_data_files.name}'})
            
            if response_db[0]:
                print("Producto agregado correctamente")
                user.delete_app()
                return JsonResponse({"status":"OK","message":"Producto agregado"},status=200)
            else:
                print("Error al agregar producto")
                user.delete_app()
                return JsonResponse({"status":"ERROR","message":"Error al agregar producto"},status=500)

        except Exception as e:
            # user.delete_app()
            print("Error al agregar producto:",e)
            return JsonResponse({"status":"ERROR","message":"Error al agregar producto"},status=500)
        # user.delete_app()
        
    # user.delete_app()
    return JsonResponse({"status":"ERROR","message":"Peticion invalida"},status=400)