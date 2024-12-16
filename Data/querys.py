import firebase_admin
from firebase_admin import credentials,firestore,auth
import firebase_admin.auth
from google.cloud.firestore_v1 import FieldFilter

# Esta clase se encarga de realizar las operaciones de lectura y escritura en la base de datos de Firebase

class dataOperations:
    def __init__(self,db):
        self.__conn = db
    
    def obtain_user_role_from_uid(self,uid):
        userstable = self.__conn.collection('users')
        role = userstable.document(uid).get().to_dict()['usertype']
        
        if userstable:
            print('Usuario encontrado:', userstable)
            return role
    
    def obtain_user_data(self,uid):
        userstable = self.__conn.collection('users')
        user_data = userstable.document(uid).get().to_dict()
        return user_data
    
    def set_data(self,data):
        userstable = self.__conn.collection('users')
        try:
            userdata = {
                'nombre':data['nombre'],
                'rut':data['rut'],
                'email':data['email'],
                'usertype':data['usertype'],
                'telefono':data['telefono'],
                'verified':False,
            }
            userstable.document(data['uid']).set(userdata)
            return True
        except:
            return False
        
    def user_exist(self, email):
        user_table = self.__conn.collection('users')
        filter = FieldFilter('email', '==', email)
        user = user_table.where(filter=filter).limit(1).get()
        return bool(user)
        
    def create_user(self,email,passw):
        try:
            authentication = auth.create_user(email=email,password=passw)
            print('Usuario creado exitosamente:', authentication.uid)
            return True, "Usuario creado exitosamente", authentication.uid
        
        except auth.EmailAlreadyExistsError:
            error = 'El correo electrónico ya está en uso.'
            print(error)
            return False, error
        
        except Exception as e:
            error = f'Error al crear el usuario:', e
            print(error)
            return False, error
        
    def get_companies(self):
        company_table = self.__conn.collection('users')
        companies_snapshot = company_table.get()
        
        companies = []
        for company in companies_snapshot:
            company_dict = company.to_dict()
            print('Empresas:', company_dict)
            if company_dict['usertype'] == 'empresa':
                companies.append(company_dict['nombre'].lower())
            

        companies = list(set(companies))
        print('Empresas encontradas:', companies)
        return companies
        
    def get_products_from_user(self,uid):
        product_table = self.__conn.collection(uid)

        products = product_table.get()
        
        products_list = []
        for product in products:
            product_dict = product.to_dict()
            products_list.append(product_dict)
            
        return products_list
        
    def rut_exist_db(self,rut):
        userstable = self.__conn.collection('users')
        filter = FieldFilter('rut', '==', rut)
        user = userstable.where(filter=filter).limit(1).get()
        if user:
            return False
        else:
            return True
        
    def obtain_products(self):
        users_table = self.__conn.collection('users')
        users = users_table.get()
        users_ids = []
        
        for user in users:
            user_id = user.id
            print('Usuario:', user_id)
            user_dict = user.to_dict()
            
            if user_dict["usertype"] != 'empresa':
                continue
            
            users_ids.append(user_id)
            
        print('Usuarios encontrados:', users_ids)
        
        products_list = {}
        for user_id in users_ids:
            product_table = self.__conn.collection(user_id)
            products = product_table.get()
            for i,product in enumerate(products):
                product_dict = product.to_dict()
                products_list[i] = product_dict
        
        return products_list

    def create_new_product_to_user(self,uid,data):
        try:
            product_table = self.__conn.collection(uid)
            _,product_id = product_table.add(data)
            print('Producto creado:', product_id.id)
            return True, product_id.id
            
        except Exception as e:
            print('Error al crear el producto:', e)
            return False, None
        
    def append_characteristic_to_product(self,uid,product_id,characteristic):
        """
        Agrega la caracteristica a un producto en la base de datos
        
        :param uid: Id del usuario
        :param product_id: Id del producto autogenerado por Firebase
        :param characteristic: Caracteristica a agregar al producto en formato diccionario
        :return: True si se agrega correctamente, False si no
        """
        try:
            product_table = self.__conn.collection(uid)
            product_table.document(product_id).update(characteristic)
            return True
        except Exception as e:
            print('Error al agregar característica:', e)
            return False
        
        
    def folder_exist_in_user(self,uid):
        user_table = self.__conn.collection('users')
        folder = user_table.document(uid).get().to_dict()
        
        
        if 'folder' in folder:
            if folder['folder']:
                return True
            else:
                return False
        else:
            # Si la clave 'folder' no está presente, también retornamos False
            return False
        
    def get_one_product(self,uid,product_id):
        print('UID:', uid)
        print('Product ID:', product_id)
        
        product_table = self.__conn.collection(uid)
        product = product_table.document(product_id).get().to_dict()
        print('Producto:', product)
        return product