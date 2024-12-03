from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='monitores'),
    path('<str:grupo_de_edad>/', views.grupo, name="grupo_monitores")
]