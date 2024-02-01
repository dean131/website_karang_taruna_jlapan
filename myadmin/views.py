from django.shortcuts import render

from base.models import Jumbotron, KarangTaruna, Kependudukan

def login(request):
    return render(request, 'myadmin/login.html')

def jumbotron_beranda(request):
    if request.method == 'POST':
        jumbotron = Jumbotron.objects.filter(nama='jumbotron_beranda').first()
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        foto = request.FILES.get('foto')

        if judul: jumbotron.judul = judul
        if deskripsi: jumbotron.deskripsi = deskripsi
        if foto: jumbotron.foto = foto
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

        if judul: jumbotron.judul = judul
        if deskripsi: jumbotron.deskripsi = deskripsi
        if foto: jumbotron.foto = foto
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

def kependudukan(request):
    if request.method == 'POST':
        kependudukan = Kependudukan.objects.first()
        deskripsi = request.POST.get('deskripsi')
        foto = request.FILES.get('foto')
        jumlah_penduduk_total = request.POST.get('jumlah_penduduk_total')
        jumlah_penduduk_pria = request.POST.get('jumlah_penduduk_pria')
        jumlah_penduduk_perempuan = request.POST.get('jumlah_penduduk_perempuan')

        if deskripsi: kependudukan.deskripsi = deskripsi
        if foto: kependudukan.foto = foto
        if jumlah_penduduk_total: kependudukan.jumlah_penduduk_total = jumlah_penduduk_total
        if jumlah_penduduk_pria: kependudukan.jumlah_penduduk_pria = jumlah_penduduk_pria
        if jumlah_penduduk_perempuan: kependudukan.jumlah_penduduk_perempuan = jumlah_penduduk_perempuan
        kependudukan.save()

    kependudukan = Kependudukan.objects.first()
    if not kependudukan:
        kependudukan = Kependudukan.objects.create(
            deskripsi='Ini adalah deskripsi kependudukan',
            jumlah_penduduk_total=0,
            jumlah_penduduk_pria=0,
            jumlah_penduduk_perempuan=0,
        )

    context = {
        'kependudukan': kependudukan,
    }
    return render(request, 'myadmin/kependudukan.html', context)

def karangtaruna(request):
    if request.method == 'POST':
        karangtaruna = KarangTaruna.objects.first()
        nama = request.POST.get('nama')
        lokasi = request.POST.get('lokasi')
        logo = request.FILES.get('logo')
        alamat = request.POST.get('alamat')
        telepon = request.POST.get('telepon')
        email = request.POST.get('email')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')

        if nama: karangtaruna.nama = nama
        if lokasi: karangtaruna.lokasi = lokasi
        if logo: karangtaruna.logo = logo
        if alamat: karangtaruna.alamat = alamat
        if telepon: karangtaruna.telepon = telepon
        if email: karangtaruna.email = email
        if facebook: karangtaruna.facebook = facebook
        if instagram: karangtaruna.instagram = instagram
        karangtaruna.save()

    karangtaruna = KarangTaruna.objects.first()
    if not karangtaruna:
        karangtaruna = KarangTaruna.objects.create(
            nama='Karang Taruna',
        )

    context = {
        'karangtaruna': karangtaruna,
    }
    return render(request, 'myadmin/karangtaruna.html', context)