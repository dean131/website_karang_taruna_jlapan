from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.beranda_jumbotron, name='beranda_jumbotron'),
    path('beranda_kependudukan/', views.beranda_kependudukan, name='beranda_kependudukan'),
]
