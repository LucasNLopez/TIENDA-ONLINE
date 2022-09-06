from django.shortcuts import render, HttpResponse

from contextvars import Context
from datetime import datetime
from string import Template
from django.http import HttpResponse
from django.template import Template, Context, loader
from servicios.models import servicio

# Create your views here.

def inicio(request):
    return render(request,"ProyectoWebApp/home.html")

def servicio(request):
    servicio=servicio.objects.all()
    return render(request,"ProyectoWebApp/servicio.html",{"servicio":servicio})

def tienda(request):
    return render(request,"ProyectoWebApp/tienda.html")


def contact(request):
    return render(request,"ProyectoWebApp/contacto.html")
