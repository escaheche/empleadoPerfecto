# Generated by Django 5.1.1 on 2024-09-25 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_remove_empresa_atributos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='contraseña',
            new_name='password',
        ),
    ]
