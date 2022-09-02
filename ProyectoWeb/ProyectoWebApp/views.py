from django.shortcuts import render, HttpResponse

from contextvars import Context
from datetime import datetime
from string import Template
from django.http import HttpResponse
from django.template import Template, Context, loader

# Create your views here.

def inicio(request):
    return render(request,"ProyectoWebApp/home.html")

def servicio(request):
    return render(request,"ProyectoWebApp/servicio.html")

def tienda(request):
    return render(request,"ProyectoWebApp/tienda.html")


#def contact(request):
 #   return render(request,"ProyectoWebApp/contacto.html")

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        super().__init__()


def saludo(request):
    p1=Persona("Lucas","Lopez")
    ahora=datetime.now()
    dic={"actualidad":ahora, "nombre_persona":p1.nombre, "apellido_persona":p1.apellido}
    return render(request,"ProyectoWebApp/contacto.html",dic)
