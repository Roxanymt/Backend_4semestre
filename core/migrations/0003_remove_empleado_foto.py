# Generated by Django 5.1 on 2024-12-11 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_empleado_foto_empleado_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='foto',
        ),
    ]