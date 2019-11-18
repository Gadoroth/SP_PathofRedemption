from django.urls import path, include
from . import views
from django.contrib.auth import login
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.index, name='index'),
    path('Registro', views.Registro, name='Registro'),
    path('foro', views.foro, name='foro'),
    path('Download', views.Download, name='Download'),
    path('Devs', views.Devs, name='Devs'),
    path('Juego', views.Juego, name='Juego'),
    path('Desarrollo', views.Desarrollo, name='Desarrollo'),
    path('permiso', views.permiso, name='permiso'),

    path('login', LoginView.as_view(), name='login'),


    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
