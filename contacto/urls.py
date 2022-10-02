from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto, name='contacto'),
	path('mandar_email', views.mandar_email, name="mandar_email"),

]