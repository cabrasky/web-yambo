from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def inicio(req):
	proyectos = Proyecto.objects.all
	return render(req, "inicio/inicio.html", {
		'proyectos': proyectos
	})