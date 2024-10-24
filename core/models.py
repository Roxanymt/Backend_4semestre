from django.db import models

# Create your models here.
class TipoEmpleado(models.Model):
    descripcion = models.CharField(max_length = 40)
    
    def __str__(self):
        return self.descripcion
    
class Empleado(models.Model):
    rut = models.CharField(max_length = 12)
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    edad = models.IntegerField()
    telefono = models.CharField(max_length = 12)
    direccion = models.CharField(max_length = 60)
    tipo = models.ForeignKey(TipoEmpleado, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.rut
    