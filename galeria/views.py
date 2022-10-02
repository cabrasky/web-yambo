from django.shortcuts import render

# Create your views here.
def upload(request):
    # ignorar, por ahora dejarlo para que aparezca el formulario
    # TODO: hacer un forms.py y enlazarlo ahi con bd
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            pass
    return render(request, 'galeria/subir_fotos.html', {'images': images})