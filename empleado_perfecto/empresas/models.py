from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    rut = models.CharField(max_length=20, unique=True)  # RUT único para cada empresa
    telefono = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombre_completo = models.CharField(max_length=255)
    rut = models.CharField(max_length=20, unique=True)  # RUT único para cada empleado
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)  # Relación con Empresa

    def __str__(self):
        return self.nombre_completo

