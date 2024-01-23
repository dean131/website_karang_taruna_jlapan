from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('pengumuman/', views.pengumuman, name='pengumuman'),
    path('detail_pengumuman/<str:pk>/', views.detail_pengumuman, name='detail_pengumuman'),
]
