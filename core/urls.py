from django.urls import path, include
from .views import *
#API
from rest_framework import routers

router = routers.DefaultRouter()
router.register('empleados', EmpleadoViewSet)
router.register('tipoempleados', TipoEmpleadoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('empleadosapi/', empleadosapi, name = "empleadosapi"),
    path('', index, name = "index"),
    path('contacto/', contacto, name = "contacto"),
    path('sobremi/', sobremi, name = "sobremi"),
    #CRUD empleado
    path('addempleado/', addempleado, name = "addempleado"),
    path('listempleados/', listempleados, name = "listempleados"),
    path('updateempleado/<id>/', updateempleado, name = "updateempleado"),
    path('deleteempleado/<id>/', deleteempleado, name = "deleteempleado"),
    path('registrar', registrar, name = "registrar"),
]
