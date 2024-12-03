from distutils.command.upload import upload
from django.db import models

def setMediaUploadToPath(model, path):
    return model.path

class Year(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nombre.title() + " " + self.year.__str__()



class Actividad(models.Model):
    dia = models.CharField(max_length=20)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.dia + " " + self.grupo.__str__().title()

    def toId(self):
        return self.dia.replace("-", "_")

class Media(models.Model):
    path = models.CharField(max_length=200, null=True)
    media = models.ImageField(upload_to = setMediaUploadToPath, null=True, max_length=200)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True)
    is_video = models.BooleanField(default=False)
    def __str__(self):
        return self.media.name + " " + self.actividad. __str__()
