from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('servicios',views.servicio, name="Servicios" ),
    path('tienda',views.tienda,name="Tienda"),
    path('contacto',views.contact,name="Contacto"),
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)