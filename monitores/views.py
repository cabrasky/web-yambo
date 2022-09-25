from django.shortcuts import render
from django.http import HttpResponse
from .models import Monitor,Grupo
from django.template import loader



def grupo(request, grupo_de_edad):
    grupo = Grupo.objects.get(nombre=grupo_de_edad)
    grupos_list = Grupo.objects.order_by('id')
    monitor_list = grupo.monis.all()
    template = loader.get_template('monitores/main.html')
    context = {
        'sGrupo': grupo,
        'grupos_list': grupos_list,
        'monitor_list': monitor_list
    }
    return HttpResponse(template.render(context, request))


def index(request):
    monitor_list = Monitor.objects.all
    grupos_list = Grupo.objects.order_by('id')
    template = loader.get_template('monitores/main.html')
    context = {
        'grupos_list': grupos_list,
        'monitor_list': monitor_list
    }
    return HttpResponse(template.render(context, request))