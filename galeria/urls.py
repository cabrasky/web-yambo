from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<str:grupo_de_edad>/', views.grupo, name='grupo_galeria'),
    path('subir_fotos', views.upload, name='upload'),
    path('', views.iniciar_sesion, name='galeria_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)