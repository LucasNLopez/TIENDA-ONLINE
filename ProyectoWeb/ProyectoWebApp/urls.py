from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('servicios',views.servicio, name="Servicios" ),
    path('tienda',views.tienda,name="Tienda"),
    path('contacto',views.saludo,name="Contacto"),

]
