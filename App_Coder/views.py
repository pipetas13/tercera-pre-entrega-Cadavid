from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#superuser : pipetas password: pipetas

# Create your views here.
from App_Coder.models import *
from App_Coder.forms import *

def inicio (request):
    return render(request, 'App_Coder/inicio.html')

def about (request):
    return render(request, 'App_Coder/about.html')

#Autentications Views
def registro(request):

    if request.method == "POST":

        miFormulario = RegistroFormulario(request.POST) #obtener los datos que están en el formulario
    
        if miFormulario.is_valid():

            miFormulario.save()

            return render(request, "App_Coder/inicio.html")

    else:

        miFormulario = RegistroFormulario()
    
    return render(request, "App_Coder/autentication/registro.html", {"formulario1":miFormulario})

def iniciar_sesion(request):

    if request.method == "POST":

        miFormulario = AuthenticationForm(request, data = request.POST) #obtener los datos que están en el formulario
    
        if miFormulario.is_valid():
            

            usuario = miFormulario.cleaned_data.get("username") #obteniendo el usuario y la contra ingresados
            contra = miFormulario.cleaned_data.get("password")

            miUsuario = authenticate(username=usuario, password=contra) #autentica que los datos de inicio sean correctos

            if miUsuario:

                login(request, miUsuario)
                mensaje = f"{miUsuario}"

                return render(request, "App_Coder/inicio.html", {"mensaje":mensaje})

        else:

            mensaje = f"Error. Ingresaste mal los datos."

            return render(request, "App_Coder/inicio.html", {"mensaje":mensaje})

    else:

        miFormulario = AuthenticationForm()
    
    return render(request, "App_Coder/autentication/login.html", {"formulario1":miFormulario})


#Vista para Editar Usuarios (Parte del CRUD)
@login_required
def editarUsuario(request):

    usuario = request.user #usuario activo (el que ha iniciado sesión)

    if request.method == "POST":    #al presionar el botón

        miFormulario = RegistroFormulario(request.POST) #el formulario es el del usuario

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data     #info en modo diccionario

            #actualizar la info del usuario activo
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "App_Coder/inicio.html")

    else:

        miFormulario= RegistroFormulario(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "AppReseñas/editarusuario.html",{'miFormulario':miFormulario, 'usuario':usuario.username})



#Solo usuarios con permisos de staff pueden crear artistas.
@login_required
def artista_formulario(request):
    if request.method =='POST':
        formulario2 = formulario_artista(request.POST)
        print(formulario2)
        if formulario2.is_valid():
            informacion = formulario2.cleaned_data
            Artista1 = artista(nombre = informacion['nombre'], apellido = informacion['apellido'] , email=informacion['email'], edad = informacion['edad'],estilo = informacion['estilo'])
            Artista1.save()
            return render (request, 'App_Coder/inicio.html')
    
    else:
        formulario2 = formulario_artista()
    return render (request, 'App_Coder/artistas.html', {'formulario2':formulario2}) 

#Solo los artistas pueden crear proyectos.
@login_required
def proyecto_formulario(request):
    if request.method =='POST':
        formulario3 = formulario_proyecto(request.POST)
        print(formulario3)
        if formulario3.is_valid():
            informacion = formulario3.cleaned_data
            Proyecto1 = proyectos(nombre = informacion['nombre'], cantidad = informacion['cantidad'], imagen = informacion['imagen']  )
            Proyecto1.save()
            return render (request, 'App_Coder/inicio.html')
    
    else:
        formulario3 = formulario_proyecto()
    return render (request, 'App_Coder/añadirproyecto.html', {'formulario3':formulario3}) 

@login_required
def editarProyecto(request, proyecto_nombre, numero):

    proy = proyectos.objects.get(nombre=proyecto_nombre, cantidad=numero)

    if request.method == "POST":

        miFormulario = formulario_proyecto(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            proy.nombre = informacion['nombre']
            proy.cantidad = informacion['cantidad']
            proy.imagen = informacion['imagen']

            proy.save()

            return render(request, "App_Coder/inicio.html")

    else:

        miFormulario= formulario_proyecto(initial={'nombre':proy.nombre, 'numero':proy.cantidad,
        'imagen':proy.imagen})

    return render(request, "App_Coder/editarproyecto.html",{'miFormulario':miFormulario, 'resultado':proyecto_nombre})

@login_required
def borrarproyecto(request, proyecto_nombre):

    proy = proyectos.objects.get(nombre=proyecto_nombre)
    
    proy.delete()
    
    proyecto = proyectos.objects.all()

    return render(request, "App_Coder/proyectos.html",{'resultados':proyecto})

#CRUD de Projectos con vistas basadas en clases
class ProyectoLista(ListView): #por defecto el template name se llama curso_list.html
    model = proyectos
    template_name = "App_Coder/Proyectos/proyectos_list.html"
    
class ProyectoCrear(LoginRequiredMixin, CreateView): #por defecto el template name se llama curso_form.html
    model = proyectos
    fields = ["nombre", "cantidad","imagen"]
    success_url = "/App_Coder/Proyectos/lista"
    template_name = "App_Coder/Proyectos/proyectos_form.html"

class ProyectoBorrar(LoginRequiredMixin, DeleteView): #por defecto el template name se llama curso_confirm_delete.html
    model = proyectos
    success_url = "/AppCoder/Proyectos/lista"
    template_name = "App_Coder/Proyectos/proyectos_borrar.html"

class ProyectoEditar(LoginRequiredMixin, UpdateView): #usa el mismo html que el CreateView (curso_form.html)
    model = proyectos
    fields = ["nombre", "cantidad","imagen"]
    success_url = "/App_Coder/Proyectos/lista"
    template_name = "App_Coder/Proyectos/proyectos_form.html"

#Se crea la vista de busqueda

def busquedaProyecto(request):
    return render(request , 'App_Coder/busquedaProyecto.html')

def resultados(request):
    if request.GET["cantidad"]:
    #respuesta= f'Estoy buscando el proyecto: {request.get["nombre"]}'
        cantidad = request.GET['cantidad']
        proyecto = proyectos.objects.filter(cantidad__icontains=cantidad)
        return render(request,"App_Coder/resultadosBusqueda.html", {'proyecto':proyecto, 'cantidad':cantidad})
    else:
        respuesta='No existe el proyecto'
    return HttpResponse(respuesta)

#Vista proyectos
def leerProyectos(request):

      proyecto = proyectos.objects.all() #trae todos los proyectos

      contexto= {"proyecto":proyecto} 

      return render(request, "App_Coder/proyectos.html",contexto)
