from django.db import models
from django.contrib.auth.models import User
#Si hay algun error al migrar, eliminar todos los archivos de la carpeta "migrations"
#Si migrate no funciona correr python manage.py migrate --fake <app>
#Si quieres agregar una columna a la tabla corre:
#python manage.py migrate --fake APPNAME zero despues
#python manage.py migrate APPNAME
#***El problema Es que borra todo en la tabla***
# Create your models here.
class proyecto(models.Model):
    folio = models.CharField(max_length=100,primary_key=True)
    tomo = models.CharField(max_length=20)
    slug = models.SlugField()
    numero_instrumento = models.CharField(max_length=30)
    enajenante = models.CharField(max_length = 100)
    adquirente =  models.CharField(max_length= 100)
    tipo = models.CharField(max_length=32)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    localizacion = models.CharField(max_length=20,default=None)
    prueba = models.CharField(max_length=10, default=None, null=True)

    # @property
    # def owner(self):
    #     return self.autor

    # def __str__(self):
    #     diccionario = {}
    #     diccionario['1'] = "Compra-Venta"
    #     diccionario['2'] = "Escritura"
    #     diccionario['3'] = "Ratificacion de firmas"
    #     diccionario['4'] = "testamento"
    #     diccionario['5'] = "Divorcio"
    #     diccionario['2341234'] = "no-sirve"
    #     diccionario['55'] ="none"
    #     diccionario['10'] = "none"
    #     return diccionario[self.tipo] + "-" + self.enajenante
    # def tipo_proyecto(self):
    #     diccionario = {}
    #     diccionario['1'] = "Compra-Venta"
    #     diccionario['2'] = "Escritura"
    #     diccionario['3'] = "Ratificacion de firmas"
    #     diccionario['4'] = "testamento"
    #     diccionario['5'] = "Divorsio"
    #     diccionario['2341234'] = "no-sirve"
    #     diccionario['55'] ="none"
    #     diccionario['10'] = "none"
    #     return diccionario[self.tipo]


class clientes(models.Model):
    clienteID = models.AutoField(primary_key=True)
    nombre =  models.CharField(max_length=100)
    apellidoP = models.CharField(max_length=100)
    slug =  models.SlugField()
    escritura = models.ForeignKey(proyecto,on_delete=models.CASCADE,default=None)
    correo = models.CharField(max_length=100, default=None)
    def __str__(self):
        return self.nombre

class progreso(models.Model):
    idProgreso = models.AutoField(primary_key=True)
    id_proyecto = models.ForeignKey(proyecto,on_delete=models.CASCADE, default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=128)
    estado = models.BooleanField(default=False)
    titulo = models.CharField(max_length=64, default=None)

    def __str__(self):
        return self.id_proyecto
