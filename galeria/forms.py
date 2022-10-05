from email.policy import default
from django import forms
from .models import Imagen, Actividad, Año, Grupo

class ImageForm(forms.Form):
    Fecha = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'type':"date"})
    )
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    grupos_querrySet = Grupo.objects.filter(año__nombre = Año.objects.last().nombre)
    Grupos = forms.ModelMultipleChoiceField(
        queryset=grupos_querrySet,
        widget=forms.CheckboxSelectMultiple
    ) 