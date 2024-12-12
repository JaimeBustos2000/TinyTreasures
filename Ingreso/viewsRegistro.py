from django.shortcuts import render
from .forms import Registrar,Login
from inputsclean.cleaninputs import cleaninputs
from Data.querys import dataOperations
from Data.users import User
from .models import Users

def register_page(request):
    registrar = Registrar()
    return render(request,'registro.html',{"registrar":registrar})

def sucess_register(request):
    login = Login()
    data_form = Registrar(request.POST)
    
    if data_form.is_valid() and request.method == 'POST':
        data = data_form.cleaned_data
        cleaner = cleaninputs(data['email'])
        
        try:
            valid_entry, error = cleaner.clean_email()
        except Exception as e:
            valid_entry = cleaner.clean_email()

        if valid_entry:
            rut_cleaner = cleaninputs(data['rut'])
            try:
                rut_valido, error = rut_cleaner.check_format_rut()
            except Exception as e:
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
                    
                    passw = data['password']
                    is_secure = cleaner.is_password_secure(passw)
                    print('is_secure: ', is_secure)
                    
                    if cleaner.is_password_secure(passw):
                        user_rut_exist = operation.user_exist(data['rut'])
                        
                        if user_rut_exist:
                            error_message = 'El rut ya está en uso.'
                            return render(request, 'registro.html', {"registrar": data_form, "registrado": False, 'error': error_message})
                        else:
                            user_op = list(operation.create_user(data['email'], data['password']))
                        
                            user_exist_django = Users.objects.filter(email=data['email'])
                        
                            if user_op[0] and not user_exist_django:
                                data['uid'] = user_op[2]
                                bs_insertion_correct = operation.set_data(data)
                                
                                if bs_insertion_correct:
                                    usermana.delete_app()
                                    create_user = Users(user_op[2], data['email'])
                                    create_user.set_password(data['password'])
                                    create_user.save()
                                    return render(request, 'login.html', {"login": login, "registrado": True})
                                else:
                                    usermana.delete_app()
                                    error_message = "Error al insertar datos."
                                    return render(request, 'registro.html', {"registrar": data_form, "registrado": False, 'error': error_message})
                            else:
                                usermana.delete_app()
                                error_message = user_op[1]
                                return render(request, 'registro.html', {"registrar": data_form, "registrado": False, 'error': error_message})
                    else:
                        error_message = 'Contraseña no segura.'
                        usermana.delete_app()
                        return render(request, 'registro.html', {"registrar": data_form, "registrado": False, 'error': error_message})
                    
                error_message = 'El correo electrónico ya está en uso.'
                usermana.delete_app()
                return render(request, 'registro.html', {"registrar": data_form, "registrado": False, 'error': error_message})
            else:
                return render(request, 'registro.html', {"registrar": data_form, "registrado": False, 'error': error})
        else:
            return render(request, 'registro.html', {"registrar": data_form, "registrado": False, 'error': error})

    return render(request, 'registro.html', {"registrar": data_form, "registrado": False})
