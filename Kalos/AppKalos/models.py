from django.db import models

# Create your models here.
class Pacientes (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=8, unique=True)
        
class Profesionales (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    profesion = models.CharField(max_length=30)

class Consultorios (models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)

class Tratamientos (models.Model):
    codigo = models.CharField(max_length=4)
    descripcion = models.CharField(max_length=50)
