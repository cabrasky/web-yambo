from django.urls import path

from . import views

urlpatterns = [
    # TODO: cambiar los nombres de las views a unos más especificos (son globales a todo el proyecto)
    path('', views.index, name='monitores'),
    path('<str:grupo_de_edad>/', views.grupo, name="grupo_monitores")
]