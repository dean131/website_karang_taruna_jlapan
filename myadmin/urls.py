from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.jumbotron_beranda, name='jumbotron_beranda'),
    path('jumbotron_profile/', views.jumbotron_profile, name='jumbotron_profile'),
    path('kependudukan/', views.kependudukan, name='kependudukan'),
]
