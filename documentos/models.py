from django.db import models
from inicio.models import Proyecto

class Documento(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    documento = models.FileField(upload_to ='docs/%Y/%m/%d/', default="")
    proyecto = models.ManyToManyField(Proyecto)
    def __str__(self):
        return self.nombre + '-' + self.fecha.isoformat().replace('-', '/')