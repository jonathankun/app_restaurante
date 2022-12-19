from django.db import models

# Create your models here.
class Mesero (models.Model):
    nombre = models.CharField(max_length=40)
    procedencia = models.CharField(max_length=40, default='')
    edad = models.IntegerField(default=0)

    def __str__(self):
        return "{} de tipo {}".format(self.nombre, self.procedencia, self.edad)

class Plato (models.Model):
    nombre = models.CharField(max_length=40)
    precio=  models.CharField(max_length=20)
    procedencia = models.CharField(max_length=40, default='')

    def __str__(self):
        return "{} de tipo {}".format(self.nombre, self.precio, self.procedencia)

class Cliente (models.Model):
    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    dni = models.CharField(max_length=8)

    def __str__(self):
        return "{} de tipo {}".format(self.nombre, self.apellido, self.dni)