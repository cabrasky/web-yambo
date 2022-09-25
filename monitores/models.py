from django.db import models

class Monitor(models.Model): 
    nombre = models.CharField(max_length=30)
    description = models.TextField(max_length=600)
    img = models.ImageField(upload_to ='monitores/static/monitores/resources/fotos', null=True)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=30)
    description = models.TextField(max_length=600)
    edad_min = models.IntegerField()
    edad_max = models.IntegerField()
    monis = models.ManyToManyField(Monitor)


    def __str__(self):
        return self.nombre