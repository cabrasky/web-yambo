from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=600)
    logo = models.ImageField(upload_to ='static/resources/logos')

    def __str__(self):
        return self.nombre