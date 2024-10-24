from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = "index"),
    path('contacto/', contacto, name = "contacto"),
    path('quienessomos/', quienessomos, name = "quienessomos"),
    #CRUD empleado
    path('addempleado/', addempleado, name = "addempleado"),
    path('listempleados/', listempleados, name = "listempleados"),
    path('updateempleado/<id>/', updateempleado, name = "updateempleado"),
    path('deleteempleado/<id>/', deleteempleado, name = "deleteempleado"),
]
