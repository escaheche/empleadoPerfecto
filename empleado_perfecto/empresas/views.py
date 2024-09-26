from rest_framework import viewsets
from .models import Empresa, Empleado
from .serializers import EmpresaSerializer, EmpleadoSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User



class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated]

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]

