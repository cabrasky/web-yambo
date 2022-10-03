from django.db import models

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