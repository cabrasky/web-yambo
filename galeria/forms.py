from email.policy import default
from django import forms
from .models import Imagen, Actividad, Year, Grupo


class ImageForm(forms.Form):
    Fecha = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'type': "date",
            'class': 'form-control mb-2',
            'style': "width: 15%"
        })
    )
    images = forms.ImageField(label="Fotos", widget=forms.ClearableFileInput(attrs={
        'multiple': True,
        'class': 'form-control mb-2',
        'style': "width: 35%"
    }))
    grupos_querrySet = Grupo.objects.filter(
        year__nombre=Year.objects.last().nombre)
    Grupos = forms.ModelMultipleChoiceField(
        label="Grupos",
        queryset=grupos_querrySet,
        widget=forms.CheckboxSelectMultiple()

    )


class LoginGaleriaForm(forms.Form):

    password = forms.CharField(required=True, label="Contraseña", widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Contraseña',
        'type': 'password',
    }))


class UserLoginGaleriaForm(forms.Form):
    username = forms.CharField(required=True, label="Usuario", widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Usuario',
        'type': 'text',
    }))

    password = forms.CharField(required=True, label="Contraseña", widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Contraseña',
        'type': 'password',
    }))
