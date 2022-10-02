from django.db import models


class Grupo(models.Model):
    nombre = models.CharField(max_length=30)
    description = models.TextField(max_length=600)
    edad_min = models.IntegerField()
    edad_max = models.IntegerField()


    def __str__(self):
        return self.nombre


class Monitor(models.Model): 
    nombre = models.CharField(max_length=30)
    description = models.TextField(max_length=600)
    img = models.ImageField(upload_to ='fotos_monitores/', null=True, max_length=200)
    grupos = models.ManyToManyField(Grupo)
    def __str__(self):
        return self.nombre