from email.headerregistry import ContentDispositionHeader
from tabnanny import verbose
from django.db import models

# Create your models here.

class servicio(models.Model):
    titulo=models.CharField(max_length=20)
    contenido=models.CharField(max_length=100)
    img=models.ImageField(upload_to="servicios")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class meta:
        verbose_name="servicio"
        verbose_name_plural="servicios"

    def __str__(self):
        return self.titulo