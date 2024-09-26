from rest_framework import serializers
from .models import Empresa, Empleado

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    empresa = serializers.PrimaryKeyRelatedField(queryset=Empresa.objects.all())  # Para la creación, solo acepta ID

    class Meta:
        model = Empleado
        fields = ['id', 'nombre_completo', 'rut', 'email', 'empresa']

    def to_representation(self, instance):
        # Para la representación (respuesta), utilizamos el serializer de Empresa completo
        representation = super().to_representation(instance)
        representation['empresa'] = EmpresaSerializer(instance.empresa).data  # Muestra los detalles de la empresa
        return representation

