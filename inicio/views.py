from django.shortcuts import render
from monitores.models import Grupo
from .models import Proyecto


# Create your views here.
def inicio(req):
	proyectos = Proyecto.objects.all()
	grupos_list_inicio = Grupo.objects.all()
	return render(req, "inicio/inicio.html", {
		'grupos_list_inicio': grupos_list_inicio,
		'proyectos': proyectos
	})