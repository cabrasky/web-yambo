from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<grupo_de_edad>/', views.grupo, name="grupo")
]