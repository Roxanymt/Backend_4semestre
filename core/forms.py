from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmpleadoForm(ModelForm):
    rut = forms.CharField(min_length=10, max_length=12)
    edad = forms.IntegerField(min_value=18)

    class Meta:
        model = Empleado
        fields = ['rut','nombre','apellido','edad','telefono','direccion','tipo','nacimiento','foto']

        widgets = {
            'nacimiento' : forms.SelectDateWidget(years=range(1940,2014))
        }
        
class TipoEmpleadoForm(ModelForm):

    class Meta:
        model = TipoEmpleado
        fields = ['descripcion']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']