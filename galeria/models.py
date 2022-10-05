from distutils.command.upload import upload
from django.db import models

<<<<<<< HEAD
def setImgUploadToPath(model, path):
    return model.path

class Año(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    año = models.ForeignKey(Año, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nombre.title() + " " + self.año.__str__()



class Actividad(models.Model):
    dia = models.CharField(max_length=20)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.dia + " " + self.grupo.__str__().title()

    def toId(self):
        return self.dia.replace("-", "_")

class Imagen(models.Model):
    path = models.CharField(max_length=200, null=True)
    img = models.ImageField(upload_to = setImgUploadToPath, null=True, max_length=200)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.img.name + " " + self.actividad.__str__()
=======
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=True)
 
    def __str__(self):
        return self.title
 
class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
 
    def __str__(self):
        return self.post.title






# Ruta real
# Año > Grupo > Fecha > Entidades Foto 
# /media/galeria/2022-2023/Peques/2022/09/01/{{Foto.EXT}}



# Ruta logica WEB
# /galeria/2022-2023/Peques/
# Grupos
# Fecha 1
# Carrousel

#Fecha 2 ....
# Carrousel
>>>>>>> cabrasky
