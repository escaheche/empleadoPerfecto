from django.contrib.auth.hashers import make_password
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
        fields = ['id', 'nombre_completo', 'rut', 'email', 'password', 'empresa']  # Asegúrate de incluir el campo 'password'

    def to_representation(self, instance):
        # Para la representación (respuesta), utilizamos el serializer de Empresa completo
        representation = super().to_representation(instance)
        representation['empresa'] = EmpresaSerializer(instance.empresa).data  # Muestra los detalles de la empresa
        return representation

    def create(self, validated_data):
        # Encripta la contraseña antes de crear el empleado
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


