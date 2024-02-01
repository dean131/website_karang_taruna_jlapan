from django.shortcuts import render

from base.models import Jumbotron

def login(request):
    return render(request, 'myadmin/login.html')

def jumbotron_beranda(request):
    if request.method == 'POST':
        jumbotron = Jumbotron.objects.filter(nama='jumbotron_beranda').first()
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        foto = request.FILES.get('foto')

        if judul:
            jumbotron.judul = judul
        if deskripsi:
            jumbotron.deskripsi = deskripsi
        if foto:
            jumbotron.foto = foto
        jumbotron.save()

    jumbotron, created = Jumbotron.objects.get_or_create(nama='jumbotron_beranda')
    if created:
        jumbotron.judul = 'Selamat Datang di Website Karang Taruna'
        jumbotron.deskripsi = 'Ini adalah website resmi Karang Taruna'
        jumbotron.save()

    context = {
        'jumbotron': jumbotron
    }
    return render(request, 'myadmin/jumbotron_beranda.html', context)

def jumbotron_profile(request):
    if request.method == 'POST':
        jumbotron = Jumbotron.objects.filter(nama='jumbotron_profile').first()
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        foto = request.FILES.get('foto')

        if judul:
            jumbotron.judul = judul
        if deskripsi:
            jumbotron.deskripsi = deskripsi
        if foto:
            jumbotron.foto = foto
        jumbotron.save()

    jumbotron, created = Jumbotron.objects.get_or_create(nama='jumbotron_profile')
    if created:
        jumbotron.judul = 'Selamat Datang di Website Karang Taruna'
        jumbotron.deskripsi = 'Ini adalah website resmi Karang Taruna'
        jumbotron.save()

    context = {
        'jumbotron': jumbotron
    }
    return render(request, 'myadmin/jumbotron_profile.html', context)
