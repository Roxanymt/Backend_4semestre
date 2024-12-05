from django.shortcuts import render, redirect
from .models import *
from .forms import *

#API
from rest_framework import viewsets, filters
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend
import requests

#VIEWSET PARA TRABAJAR CON LAS API (GET, PUT, POST, DELETE)
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['tipo','edad']
    search_fields = ['nombre','rut']
    renderer_classes = [JSONRenderer]

class TipoEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = TipoEmpleado.objects.all()
    serializer_class = EmpleadoSerializer
    renderer_classes = [JSONRenderer]

def empleadosapi(request):
    response = requests.get("http://127.0.0.1:8000/api/empleados/")

    if response.status_code == 200:
        empleados = response.json()
        datos = {'listaEmpleados' : empleados}
    else:
        empleados = []

    return render(request, 'core/empleados/empleadosapi.html',datos)

# PAGINAS
def index(request):
    return render(request,'core/index.html')

def contacto(request):
    return render(request,'core/contacto.html')

def quienessomos(request):
    return render(request, 'core/quienessomos.html')

#CRUD EMPLEADO
def addempleado(request):
    #MEDIO DE TRANSPORTE
    datos = { 'form' : EmpleadoForm() }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save();
            datos['msj'] = "Empleado guardado correctamente"
        
    return render(request, 'core/empleados/add.html', datos)

def listempleados(request):
    #ACCEDEMOS A LA BD
    listaEmpleados = Empleado.objects.all() # SELECT * FROM Empleado

    #Medio de transporte
    datos = { 'lista' : listaEmpleados }

    return render(request, 'core/empleados/list.html', datos)

def updateempleado(request, id):
    empleado = Empleado.objects.get(id=id)
    datos = { 'form' : EmpleadoForm( instance = empleado ) }

    if request.method == 'POST':
        formulario = EmpleadoForm(data = request.POST, instance = empleado)
        if formulario.is_valid():
            formulario.save();
            datos['msj'] = "Empleado actualizado correctamente!"
            datos['form'] = formulario
        
    return render(request, 'core/empleados/update.html', datos)

def deleteempleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to="listempleados")

