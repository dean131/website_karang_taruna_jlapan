from django.shortcuts import render
from django.db.models import Q

from .models import KarangTaruna, Kependudukan, Pengumuman, Divisi, Pimpinan, Jumbotron


def home(request):
    jumbotron = Jumbotron.objects.get(nama='jumbotron_beranda')
    karangtaruna = KarangTaruna.objects.first()
    kependudukan = Kependudukan.objects.first()
    pengumumans = Pengumuman.objects.all().order_by('-tanggal')[:10]

    context = {
        'jumbotron': jumbotron,
        'karangtaruna': karangtaruna,
        'kependudukan': kependudukan,
        'pengumumans': pengumumans,
    }
    return render(request, 'base/home.html', context)

def profile(request):
    jumbotron = Jumbotron.objects.get(nama='jumbotron_profile')
    karangtaruna = KarangTaruna.objects.first()
    divisis = Divisi.objects.all()
    pimpinans = Pimpinan.objects.all()

    context = {
        'jumbotron': jumbotron,
        'pimpinans': pimpinans,
        'divisis': divisis,
        'karangtaruna': karangtaruna,
    }
    return render(request, 'base/profile.html', context)

def pengumuman(request):
    cari = request.GET.get('cari')
    dari = request.GET.get('dari')
    sampai = request.GET.get('sampai')
    karangtaruna = KarangTaruna.objects.first()
    pengumumans = Pengumuman.objects.all().order_by('-tanggal')[:10]
    pengumuman_terbaru = pengumumans[:5]
    if dari and sampai:
        pengumumans = Pengumuman.objects.filter(tanggal__range=[dari, sampai]).order_by('-tanggal')
    if cari:
        pengumumans = Pengumuman.objects.filter(
            Q(judul__icontains=cari) |
            Q(deskripsi__icontains=cari)|
            Q(tanggal__icontains=cari)
            ).order_by('-tanggal')
    context = {
        'pengumuman_terbaru': pengumuman_terbaru,
        'pengumumans': pengumumans,
        'karangtaruna': karangtaruna,
    }
    return render(request, 'base/pengumuman.html', context)

def detail_pengumuman(request, pk):
    karangtaruna = KarangTaruna.objects.first()
    pengumuman = Pengumuman.objects.get(id=pk)
    pengumuman_terbaru = Pengumuman.objects.all().order_by('-tanggal')[:5]
    context = {
        'pengumuman_terbaru': pengumuman_terbaru,
        'karangtaruna': karangtaruna,
        'pengumuman': pengumuman,
    }
    return render(request, 'base/detail_pengumuman.html', context)