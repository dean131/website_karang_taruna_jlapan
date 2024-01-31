from django.shortcuts import render

from base.models import KarangTaruna

def login(request):
    return render(request, 'myadmin/login.html')

def beranda_jumbotron(request):
    if request.method == 'POST':
        karangtaruna = KarangTaruna.objects.first()
        nama = request.POST.get('nama')
        deskripsi_halaman_utama = request.POST.get('deskripsi_halaman_utama')
        foto_halaman_utama = request.FILES.get('foto_halaman_utama')

        if nama:
            karangtaruna.nama = nama
        if deskripsi_halaman_utama:
            karangtaruna.deskripsi_halaman_utama = deskripsi_halaman_utama
        if foto_halaman_utama:
            karangtaruna.foto_halaman_utama = foto_halaman_utama
        karangtaruna.save()

    karangtaruna = KarangTaruna.objects.first()
    context = {
        'karangtaruna': karangtaruna
    }
    return render(request, 'myadmin/beranda_jumbotron.html', context)
