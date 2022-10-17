from builtins import print
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ImageForm, LoginGaleriaForm, UserLoginGaleriaForm
from django.shortcuts import redirect
from .models import Imagen, Actividad, Año, Grupo
from django.template import loader
import os
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login

@login_required
def grupo(request, grupo_de_edad):
	grupos = Grupo.objects.filter(año=Año.objects.last(), nombre=grupo_de_edad)
	grupo = grupos[0]
	actividades = Actividad.objects.filter(grupo=grupo).order_by('-dia')
	for i in range(len(actividades)):
		actividades[i].imagenList = []
		actividades[i].imagenList = actividades[i].imagen_set.all()
	

	template = loader.get_template('galeria/principal.html')
	context = {
		'grupo': grupo,
		'actividades': actividades
	}
	return HttpResponse(template.render(context, request))


@permission_required('galeria.add_actividad')
def upload(request):
	if request.method == 'POST':
		form_p = ImageForm(request.POST)
		grupos = form_p.data.getlist("Grupos")
		print(grupos)
		for grupo in grupos:
			print(form_p.data.get("Fecha"))
			grupoN = Grupo.objects.get(id=grupo)
			a = Actividad.objects.create(dia=form_p.data.get("Fecha"))
			intI = 0
			for img in request.FILES.getlist('images'):
				path = os.path.join("galeria" ,Año.objects.last().__str__(), grupoN.nombre, form_p.data.get("Fecha"), intI.__str__ () + os.path.splitext(img.name)[1])
				i = Imagen.objects.create(path=path)
				i.img = img
				i.actividad = a
				i.save()
				intI += 1
			a.grupo = grupoN
			a.save()

		return redirect('/')
	else:
		form = ImageForm()
		context = {'form': form}
		return render(request, 'galeria/subir_fotos.html', context)

# Padres
def login_galeria(req, error=0):
	login_form = LoginGaleriaForm
	return render(req, "galeria/login.html", {
		'login_form': login_form,
		'error': error
	})

def iniciar_sesion(req):
	if req.method == "POST":
		username = "padres_galeria"
		password = req.POST['password']
		
		user = authenticate(req, username=username, password=password)
		if user != None:
			login(req, user)
			url_grupo = req.POST['next']
			return redirect(url_grupo)
	return login_galeria(req, 1)

# Subir imagenes

def login_galeria_upload(req, error=0):
	login_form = UserLoginGaleriaForm
	return render(req, "galeria/loginUpload.html", {
		'login_form': login_form,
		'error': error
	})

def iniciar_sesion_upload(req):
	if req.method == "POST":
		username = req.POST['username']
		password = req.POST['password']
		
		user = authenticate(req, username=username, password=password)
		if user != None:
			login(req, user)
			url = req.POST['next']
			return redirect(url)
	return login_galeria_upload(req, 1)
