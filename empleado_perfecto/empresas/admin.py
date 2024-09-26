from django.contrib import admin

from django.contrib import admin
from .models import Empresa, Empleado

# Registra los modelos en el admin
admin.site.register(Empresa)
admin.site.register(Empleado)
