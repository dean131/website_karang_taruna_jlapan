from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from base.models import Anggota, Divisi, Jumbotron, KarangTaruna, Kependudukan, Pengumuman, Pimpinan
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('jumbotron_beranda')
    return render(request, 'myadmin/login.html')

@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required(login_url='user_login')
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

@login_required(login_url='user_login')
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

@login_required(login_url='user_login')
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

@login_required(login_url='user_login')
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
        visi = request.POST.get('visi')
        misi = request.POST.get('misi')
        motto = request.POST.get('motto')
        regulasi = request.POST.get('regulasi')
        program_kerja = request.POST.get('program_kerja')

        if nama: karangtaruna.nama = nama
        if lokasi: karangtaruna.lokasi = lokasi
        if logo: karangtaruna.logo = logo
        if alamat: karangtaruna.alamat = alamat
        if telepon: karangtaruna.telepon = telepon
        if email: karangtaruna.email = email
        if facebook: karangtaruna.facebook = facebook
        if instagram: karangtaruna.instagram = instagram
        if visi: karangtaruna.visi = visi
        if misi: karangtaruna.misi = misi
        if motto: karangtaruna.motto = motto
        if regulasi: karangtaruna.regulasi = regulasi
        if program_kerja: karangtaruna.program_kerja = program_kerja
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

@login_required(login_url='user_login')
def admin_pengumuman(request):
    if request.method == 'POST':
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        foto = request.FILES.get('foto')
        lokasi = request.POST.get('lokasi')

        Pengumuman.objects.create(
            judul=judul,
            deskripsi=deskripsi,
            foto=foto,
            lokasi=lokasi,
        )

    pengumumans = Pengumuman.objects.all()

    context = {
        'pengumumans': pengumumans,
    }
    return render(request, 'myadmin/pengumuman.html', context)

@login_required(login_url='user_login')
def delete_pengumuman(request, id):
    pengumuman = Pengumuman.objects.get(id=id)
    pengumuman.delete()
    return redirect('admin_pengumuman')

@login_required(login_url='user_login')
def pimpinan(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        foto = request.FILES.get('foto')
        telepon = request.POST.get('telepon')
        jabatan = request.POST.get('jabatan')

        Pimpinan.objects.create(
            nama=nama,
            foto=foto,
            telepon=telepon,
            jabatan=jabatan,
        )
    pimpinans = Pimpinan.objects.all()
    context = {
        'pimpinans': pimpinans,
    }
    return render(request, 'myadmin/pimpinan.html', context)

@login_required(login_url='user_login')
def delete_pimpinan(request, id):
    pimpinan = Pimpinan.objects.get(id=id)
    pimpinan.delete()
    return redirect('pimpinan')

@login_required(login_url='user_login')
def anggota(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        foto = request.FILES.get('foto')
        telepon = request.POST.get('telepon')
        jabatan = request.POST.get('jabatan')
        divisi = request.POST.get('divisi')

        Anggota.objects.create(
            nama=nama,
            foto=foto,
            alamat='',
            telepon=telepon,
            jabatan=jabatan,
            divisi=Divisi.objects.get(id=divisi),
        )
    divisis = Divisi.objects.all()
    context = {
        'divisis': divisis,
    }
    return render(request, 'myadmin/anggota.html', context)

@login_required(login_url='user_login')
def delete_anggota(request, id):
    anggota = Anggota.objects.get(id=id)
    anggota.delete()
    return redirect('anggota')

@login_required(login_url='user_login')
def divisi(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        deskripsi = request.POST.get('deskripsi')

        Divisi.objects.create(
            nama=nama,
            deskripsi=deskripsi,
        )

    divisis = Divisi.objects.all()
    context = {
        'divisis': divisis,
    }
    return render(request, 'myadmin/divisi.html', context)

@login_required(login_url='user_login')
def delete_divisi(request, id):
    divisi = Divisi.objects.get(id=id)
    divisi.delete()
    return redirect('divisi')
