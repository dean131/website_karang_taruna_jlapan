from django.urls import path

from . import views


urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),

    path('', views.jumbotron_beranda, name='jumbotron_beranda'),
    path('jumbotron_profile/', views.jumbotron_profile, name='jumbotron_profile'),
    path('kependudukan/', views.kependudukan, name='kependudukan'),
    path('karangtaruna/', views.karangtaruna, name='karangtaruna'),

    path('anggota/', views.anggota, name='anggota'),
    path('delete_anggota/<str:id>/', views.delete_anggota, name='delete_anggota'),

    path('divisi/', views.divisi, name='divisi'),
    path('delete_divisi/<str:id>/', views.delete_divisi, name='delete_divisi'),

    path('admin_pengumuman/', views.admin_pengumuman, name='admin_pengumuman'),
    path('delete_pengumuman/<str:id>/', views.delete_pengumuman, name='delete_pengumuman'),

    path('pimpinan/', views.pimpinan, name='pimpinan'),
    path('delete_pimpinan/<str:id>/', views.delete_pimpinan, name='delete_pimpinan'),
]
