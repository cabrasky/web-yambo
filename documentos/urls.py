from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='documentos'),
    path('<str:nombre_proyecto>/', views.proyecto, name="documentos_proyecto")
]