from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

 # Se crean los formularios para las 2 clases y para la autenticación
 #Forms 2 clases

class formulario_artista(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()
    estilo = forms.CharField()

class formulario_proyecto(forms.Form):
    nombre = forms.CharField()
    cantidad = forms.IntegerField()
    imagen = forms.ImageField()

#Forms Autenticación
class RegistroFormulario(UserCreationForm):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Ingrese una contraseña:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña:",widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]