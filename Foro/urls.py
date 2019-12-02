from django.urls import path, include, re_path
#api
from django.conf.urls import url, include
from rest_framework import routers
from Foro.quickstart import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#---fin api
from . import views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

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

    path('password_reset_form', PasswordResetView.as_view(template_name='registration/password_reset_form.html', email_template_name="registration/password_reset_email.html"), name = 'password_reset'),

    path('password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name = 'password_reset_done'),

    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirms.html'), name = 'password_reset_confirm'),
    
    path('password_reset_complete',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html') , name = 'password_reset_complete'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #api
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #---fin api
]
