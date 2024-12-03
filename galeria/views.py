from builtins import print
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import MediaForm, LoginGaleriaForm, UserLoginGaleriaForm
from django.shortcuts import redirect
from .models import Media, Actividad, Year, Grupo
from django.template import loader
import os
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login

@login_required
def grupo(request, grupo_de_edad):
	grupos = Grupo.objects.filter(year=Year.objects.last(), nombre=grupo_de_edad)
	grupo = grupos[0]
	actividades = Actividad.objects.filter(grupo=grupo).order_by('-dia')
	for i in range(len(actividades)):
		actividades[i].mediaList = []
		actividades[i].mediaList = actividades[i].media_set.all()
	

	template = loader.get_template('galeria/principal.html')
	context = {
		'grupo': grupo,
		'actividades': actividades
	}
	return HttpResponse(template.render(context, request))


@permission_required('galeria.add_actividad')
def upload(request):
    if request.method == 'POST':
        form_p = MediaForm(request.POST, request.FILES)
        grupos = form_p.data.getlist("Grupos")
        print(grupos)
        
        for grupo in grupos:
            grupoN = Grupo.objects.get(id=grupo)
            
            if Actividad.objects.filter(dia=form_p.data.get("Fecha"), grupo=grupoN).exists():
                a = Actividad.objects.get(dia=form_p.data.get("Fecha"), grupo=grupoN)
                intI = Media.objects.filter(actividad=a).__len__()
                
                for file in request.FILES.getlist('media'):
                    path = os.path.join(
                        "galeria", Year.objects.last().__str__(), grupoN.nombre, form_p.data.get("Fecha"),
                        f"{intI}{os.path.splitext(file.name)[1]}"
                    )
                    
                    try:
                        validate_file_extension(file)
                        i = Media.objects.create(path=path, is_video=is_file_video(file))
                        i.media = file
                        i.actividad = a
                        i.save()
                        intI += 1
                    except ValidationError as e:
                        print(e)
            else:
                a = Actividad.objects.create(dia=form_p.data.get("Fecha"))
                intI = 0
                
                for file in request.FILES.getlist('media'):
                    path = os.path.join(
                        "galeria", Year.objects.last().__str__(), grupoN.nombre, form_p.data.get("Fecha"),
                        f"{intI}{os.path.splitext(file.name)[1]}"
                    )
                    
                    try:
                        validate_file_extension(file)
                        i = Media.objects.create(path=path, is_video=is_file_video(file))
                        i.media = file
                        i.actividad = a
                        i.save()
                        intI += 1
                    except ValidationError as e:
                        print(e)
                
                a.grupo = grupoN
                a.save()

        return redirect('/')
    else:
        form = MediaForm()
        context = {'form': form}
        return render(request, 'galeria/subir_fotos.html', context)


def validate_file_extension(file):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.avi', '.mov']
    ext = os.path.splitext(file.name)[1]
    
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def is_file_video(file):
    video_extensions = ['.mp4', '.avi', '.mov']
    ext = os.path.splitext(file.name)[1]
    
    return ext.lower() in video_extensions
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
