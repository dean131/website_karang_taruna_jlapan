from django.contrib import admin

from .models import (
    User, KarangTaruna, Kependudukan, 
    Pengumuman, Divisi, Anggota, Pimpinan, Jumbotron)


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'nama', 'telepon', 'is_admin')


class KarangTarunaAdmin(admin.ModelAdmin):
    list_display = ('nama',)


class KependudukanAdmin(admin.ModelAdmin):
    list_display = ('jumlah_penduduk_total', 'jumlah_penduduk_pria', 'jumlah_penduduk_perempuan')


class PengumumanAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal')


class DivisiAdmin(admin.ModelAdmin):
    list_display = ('nama',)


class AnggotaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jabatan', 'divisi')


class PimpinanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jabatan')


class JumbotronAdmin(admin.ModelAdmin):
    list_display = ('nama', 'judul',)


admin.site.register(Jumbotron, JumbotronAdmin)
admin.site.register(Pimpinan, PimpinanAdmin)
admin.site.register(Anggota, AnggotaAdmin)
admin.site.register(Divisi, DivisiAdmin)
admin.site.register(Pengumuman, PengumumanAdmin)
admin.site.register(Kependudukan)
admin.site.register(User, UserAdmin)
admin.site.register(KarangTaruna, KarangTarunaAdmin)
