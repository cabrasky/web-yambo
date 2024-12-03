from django.shortcuts import render
from django.http import HttpResponse
from .models import Documento
from inicio.models import Proyecto
from django.template import loader



def index(request):
    template = loader.get_template('docs/main.html')
    proyectos_list = Proyecto.objects.all()

    docs = Documento.objects.all()
    for i in range(len(docs)):
        docs[i].proyectoList = []
        docs[i].proyectoList = docs[i].proyecto.all()

    
    context = {
        'proyectos_list' : proyectos_list,
        'documentos_list' : docs
    }
    return HttpResponse(template.render(context, request))


def proyecto(request, nombre_proyecto):
    template = loader.get_template('docs/main.html')
    proyectos_list = Proyecto.objects.all()
    selected_proyecto = Proyecto.objects.get(nombre = nombre_proyecto)
    docs = Documento.objects.filter(proyecto = selected_proyecto)
    for i in range(len(docs)):
        docs[i].proyectoList = []
        docs[i].proyectoList = docs[i].proyecto.all()

    
    context = {
        'proyectos_list' : proyectos_list,
        'documentos_list' : docs,
        'sProyecto' : selected_proyecto
    }
    return HttpResponse(template.render(context, request))

