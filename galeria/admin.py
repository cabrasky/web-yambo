from django.contrib import admin
from .models import Imagen, Grupo, Year, Actividad

admin.site.register(Imagen)
admin.site.register(Grupo)
admin.site.register(Actividad)
admin.site.register(Year)