from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.jumbotron_beranda, name='jumbotron_beranda'),
    path('jumbotron_profile/', views.jumbotron_profile, name='jumbotron_profile'),
    path('kependudukan/', views.kependudukan, name='kependudukan'),
    path('karangtaruna/', views.karangtaruna, name='karangtaruna'),
    path('admin_pengumuman/', views.admin_pengumuman, name='admin_pengumuman'),
]
