import os
from PIL import Image


class DirectoriManager:
    def __init__(self):
        """Inicializa la creacion del directorio publico e instancia el generador de UIDs."""
        self.create_public_directory()

    def create_public_directory(self):
        if not os.path.exists('public'):
            os.makedirs('public')
            print("Directory 'public' created.")
        else:
            print("Directory 'public' already exists.")

    def create_user_directory(self, uid):
        """Crea un directorio para un usuario."""
        user_dir = os.path.join('public', uid)
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
            print(f"Directory '{user_dir}' created.")
        else:
            print(f"Directory '{user_dir}' already exists.")
            
    def subfolder_from_directory(self,uid,subfolder_name):
        """Crea un subdirectorio en la carpeta del usuario."""
        user_dir = os.path.join('public', uid)
        subfolder_dir = os.path.join(user_dir, subfolder_name)
        if not os.path.exists(subfolder_dir):
            os.makedirs(subfolder_dir)
            print(f"Directory '{subfolder_dir}' created.")
        else:
            print(f"Directory '{subfolder_dir}' already exists.")

    def save_image_from_uid_and_product_id(self,uid,product_id,image):
        """Guarda una imagen en la carpeta del usuario y producto especifico."""
        # Ruta de la carpeta del usuario
        user_dir = os.path.join('public', uid)
        # Ruta de la carpeta del producto
        product_dir = os.path.join(user_dir, product_id)
        
        # Crear la carpeta del producto si no existe
        if not os.path.exists(product_dir):
            os.makedirs(product_dir)
            print(f"Directory '{product_dir}' created.")
        else:
            print(f"Directory '{product_dir}' already exists.")
        
        image_path = os.path.join(product_dir, image.name)
        with open(image_path, 'wb') as img_file:
            for chunk in image.chunks():
                img_file.write(chunk)
        print(f"Image saved at '{image_path}'.")
        
    def obtain_images_from_user(self,uid):
        """Obtiene las imagenes de un usuario. Recorre cada subcarpeta producto_id en busca de la imagen"""
        user_dir = os.path.join('public', uid)
        images = []
        
        # Recorrer cada carpeta del usuario, subcarpeta de producto y luego comparar si esta vacia, sino guardar la ruta de la imagen
        for product_id in os.listdir(user_dir):
            product_dir = os.path.join(user_dir, product_id)
            
            if self.directory_empty(product_dir):
                continue
            
            for image in os.listdir(product_dir):
                images.append(os.path.join(product_dir, image))
        return images
            
    def directory_empty(self,uid):
        """Verifica si la carpeta del usuario esta vacia."""
        user_dir = os.path.join('public', uid)
        if not os.path.exists(user_dir):
            raise FileNotFoundError(f"Directory '{user_dir}' not found.")
        
        return len(os.listdir(user_dir)) == 0



