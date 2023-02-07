from django import forms
 # Se crean los formularios para las 3 clases.
class formulario_cliente(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()

class formulario_artista(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()
    estilo = forms.CharField()

class formulario_proyecto(forms.Form):
    nombre = forms.CharField()
    cantidad = forms.IntegerField()