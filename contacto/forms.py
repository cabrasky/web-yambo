from django import forms

class EmailForm(forms.Form):
	nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class' : 'form-control mb-3',
		'placeholder': 'Nombre',
	}))
	email = forms.EmailField(required=True, label="Tu correo electrónico", widget=forms.TextInput(attrs={
		'class' : 'form-control mb-3',
		'placeholder': 'Tu email',
		'type': 'email',
	}))
	asunto = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class' : 'form-control mb-3',
		'placeholder': 'Asunto',
	}))
	contenido = forms.CharField(required=True, widget=forms.Textarea(attrs={
		'class' : 'form-control mb-3',
		'placeholder': 'Lo que nos quieras decir :)',
	}))
