from django.db import models

# Create your models here.
#Se crea la clase de cliente para RNDM DCKS(Nombre de la empresa de creación de NFTs)

#Se crea la clase artista para RNDM DCKS
class artista(models.Model):
    nombre = models.CharField(max_length=40) #Mensajes de texto pequeños
    apellido = models.CharField(max_length=40) #Mensajes de texto pequeños
    email = models.EmailField(max_length=254)
    edad = models.IntegerField(default = None)
    estilo = models.CharField(max_length=40)
    def __str__(self):
        return f"Name: {self.nombre} - Apellido {self.apellido} - Email {self.email} - Estilo {self.estilo} "
#Se crea la clase proyecto para RNDM DCKS
class proyectos(models.Model):
    nombre = models.CharField(max_length=40) #Mensajes de texto pequeños
    #instagram = models.EmailField()
    cantidad = models.IntegerField(default = None)
    imagen = models.ImageField(upload_to = 'NFTs', null=True)
    def __str__(self):
        return f"Name: {self.nombre} - Number {self.cantidad} "


