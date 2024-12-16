from Data.users import User
from Data.querys import dataOperations
from rest_framework import viewsets
from rest_framework.response import Response

class companies_api(viewsets.ViewSet):
    # Obtencion de todas las compañias de cada usuario unico y pasarlas en una api al frontend
    def list(self, request):
        user = User()
        db = user.bd_references()
        data_op = dataOperations(db)
        companies = data_op.get_companies()
        user.delete_app()
        return Response({"companies": companies})
    
class products_user_api(viewsets.ViewSet):
    # Obtencion de todos los productos de un usuario unico y pasarlos en una api al frontend
    def list(self, request):
        user = User()
        db = user.bd_references()
        data_op = dataOperations(db)
        data = request.session['user_id']
        products = data_op.get_products_from_user(data)
        user.delete_app()
        return Response({"productos": products})
    
class all_products(viewsets.ViewSet):
    # Obtencion de todos los productos de todos los usuarios y pasarlos en una api al frontend
    def list(self, request):
        user = User()
        db = user.bd_references()
        data_op = dataOperations(db)
        products = data_op.obtain_products()
        user.delete_app()
        return Response({"productos": products})