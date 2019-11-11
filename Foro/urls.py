from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Registro', views.Registro, name='Registro'),
    path('foro', views.foro, name='foro'),
    path('Download', views.Download, name='Download'),
    path('Sesion', views.Sesion, name='Sesion'),
    path('Devs', views.Devs, name='Devs'),
    path('Juego', views.Juego, name='Juego'),
    path('Desarrollo', views.Desarrollo, name='Desarrollo'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
