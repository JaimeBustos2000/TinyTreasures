from django import forms
import datetime


class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100,required=True)
    
    asunto = forms.ChoiceField(label='Asunto', 
                               choices=[('1','Sugerencia'),('2','Reclamo'),('3','Felicitaciones')],
                               widget=forms.Select(attrs={'class':'asunto'}))
    
    correo = forms.EmailField(label='Correo', max_length=100,required=True)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea,required=True,min_length=20)
    fecha = forms.DateTimeField(label='Fecha', initial=datetime.datetime.now, widget=forms.HiddenInput)