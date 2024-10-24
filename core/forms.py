from django import forms
from django.forms import ModelForm
from .models import *

class EmpleadoForm(ModelForm):

    class Meta:
        model = Empleado
        fields = ['rut','nombre','apellido','edad','telefono','direccion','tipo']


class TipoEmpleadoForm(ModelForm):

    class Meta:
        model = TipoEmpleado
        fields = ['descripcion']