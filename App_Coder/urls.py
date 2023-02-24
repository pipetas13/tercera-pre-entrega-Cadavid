from django.urls import path 
from App_Coder.views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static  import static
from django.conf import settings
urlpatterns = [
    path('',inicio, name='Inicio'),
    #urls autenticacion de usuario
    path("registro/",registro, name="Sign Up"),
    path("login/",iniciar_sesion, name="Sign In"),
    path("logout/",LogoutView.as_view(template_name="App_Coder/autentication/logout.html"), name="Logout"),
    path("editarUsuario", editarUsuario, name="Editar Usuario"),
    #urls clases 
    path('about/',about, name='About'),
    path('artista/',artista_formulario, name='Artists'),
    path('proyecto/',leerProyectos, name='Projects'),

    #urls busqueda
    path('busquedaProyecto/',busquedaProyecto,name='BusquedaProyecto'),
    path('resultadosBusqueda/', resultados,name='ResultadosBusqueda'),

    # cruds 
    #CRUD de Proyectos
    path("editarproyecto/<proyecto_nombre>", editarProyecto, name="Editar Proyecto"),
    path('añadirproyecto',proyecto_formulario, name='Añadir Proyecto'),
    #path('borrarproyecto',borrarproyecto, name='Borrar Proyecto'),
    path('proyecto/',proyectos, name='Proyectos'),
    path("Proyectos/lista", ProyectoLista.as_view(), name = "Ver Proyectos"),
]

