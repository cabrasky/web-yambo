from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from .forms import EmailForm

# Create your views here.
def contacto(req):
	formulario_email = EmailForm
	return render(req, "contacto/contacto.html", {
		'formulario_email': formulario_email
	})

def mandar_email(req):
	if req.method == "POST":
		nombre = req.POST['nombre']
		email = req.POST['email']
		asunto = req.POST['asunto']
		contenido = req.POST['contenido']

		template = render_to_string("contacto/email_to_admins.html", {
			'nombre': nombre,
			'email': email,
			'contenido': contenido,
		})

		email = EmailMessage(asunto, template, None, [settings.EMAIL_RECIPIENT])
		email.fail_silently = False
		email.send()

		# en teoria lo mismo pero más corto
		#send_mail(asunto, template, settings.EMAIL_HOST_USER, email, fail_silently=False)

		messages.success(req, "Se ha enviado el correo")
		return redirect("contacto")
