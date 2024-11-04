from django.shortcuts import render
from .forms import Registrar,Login
from inputsclean.cleaninputs import cleaninputs
from FirebaseData.querys import dataOperations
from FirebaseData.users import User

def registro(request):
    registrar = Registrar()
    return render(request,'registro.html',{"registrar":registrar})

def registrado(request):
    login = Login()
    data_form = Registrar(request.POST)
    if data_form.is_valid() and request.method == 'POST':
        data = data_form.cleaned_data
        cleaner = cleaninputs(data['email'])
        try:
            valid_entry, error = cleaner.clean_email()
            print("error",error)
        except:
            valid_entry = cleaner.clean_email()
        
        if valid_entry:
            rut_cleaner = cleaninputs(data['rut'])
            try:
                rut_valido,error = rut_cleaner.check_format_rut()
            except:
                rut_valido = rut_cleaner.check_format_rut()

            if rut_valido:
                usermana = User()
                bdref = usermana.bd_references()
                operation = dataOperations(bdref)
                email_exist = operation.user_exist(data['email'])
                
                if not email_exist:
                    tipo_cuenta = bool(request.POST.get('tipo'))
                    tipo_cuenta = 'empresa' if tipo_cuenta else 'individual'
                    data['usertype'] = tipo_cuenta
                    user_op = list(operation.create_user(data['email'],data['password']))
                    data['uid'] = user_op[2]
                    
                    if user_op[0]:
                        bs_insertion_correct = operation.set_data(data)
                        if bs_insertion_correct:
                            usermana.delete_app()
                            return render(request,'login.html',{"login":login,"registrado":True})
                        else:
                            usermana.delete_app()
                            return render(request,'registro.html',{"registrar":data_form,"registrado":False,'error':'Error al insertar datos.'})
                    else:
                        usermana.delete_app()
                        return render(request,'registro.html',{"registrar":data_form,"registrado":False,'error':user_op[1]})
                return render(request,'registro.html',{"registrar":data_form,"registrado":False,'error':'El correo electrónico ya está en uso.'})
            else:
                return render(request,'registro.html',{"registrar":data_form,"registrado":False,'error':error})
        else:
            return render(request,'registro.html',{"registrar":data_form,"registrado":False,'error':error})
        
    return render(request,'registro.html',{"registrar":data_form,"registrado":False})

