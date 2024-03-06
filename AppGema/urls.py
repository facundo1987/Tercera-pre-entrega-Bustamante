from django.urls import path
from AppGema.views import *

urlpatterns = [
    path ("", inicio, name = "Inicio"),
    path("pasajero/", huesped, name = "Huesped" ),
    path("reservar/", reserva, name = "Reserva" ),
    path('habitaciones/', habitacion, name = "Habitacion"),
    path("resultado_busqueda/", buscar_huesped, name = "Busqueda")
]