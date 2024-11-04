from django import forms

class Login(forms.Form):
    email = forms.EmailField(label='Email', max_length=50,required=True)
    password = forms.CharField(label='Contraseña',min_length=6, max_length=30,required=True,widget=forms.PasswordInput)


class Registrar(forms.Form):
    rut = forms.CharField(label='Rut',min_length=9, max_length=10,required=True,widget=forms.TextInput(attrs={'placeholder':'12345678-9'}))
    nombre = forms.CharField(label='Nombre',min_length=5, max_length=50,required=True)
    telefono = forms.CharField(label='Telefono',min_length=12, max_length=12,required=True,initial='+569')
    email = forms.EmailField(label='Correo',min_length=15,max_length=50,required=True,widget=forms.EmailInput.is_required)
    password = forms.CharField(label='Contraseña',min_length=6,max_length=30,required=True,widget=forms.PasswordInput)
