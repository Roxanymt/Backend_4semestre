from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
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

