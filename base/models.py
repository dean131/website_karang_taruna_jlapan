from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, nama, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nama=nama,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nama, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            nama=nama,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    nama = models.CharField(max_length=255)
    telepon = models.CharField(max_length=20, null=True, blank=True)
    foto = models.ImageField(upload_to='user', blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nama']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    

class KarangTaruna(models.Model):
    # Halaman utama
    nama = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='karangtaruna', blank=True, null=True)
    # Address
    lokasi = models.TextField(null=True, blank=True)
    alamat = models.CharField(max_length=100, null=True, blank=True)
    # Contact
    telepon = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    # Profile Page
    visi = models.TextField(null=True, blank=True)
    misi = models.TextField(null=True, blank=True)
    regulasi = models.TextField(null=True, blank=True)
    program_kerja = models.TextField(null=True, blank=True)
    motto = models.TextField(null=True, blank=True)


class Pengumuman(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    foto = models.ImageField(upload_to='pengumuman', blank=True)
    lokasi = models.TextField(null=True, blank=True)
    tanggal = models.DateField(auto_now_add=True)


class Kependudukan(models.Model):
    deskripsi = models.TextField()
    foto = models.ImageField(upload_to='kependudukan', blank=True)
    jumlah_penduduk_total = models.IntegerField()
    jumlah_penduduk_pria = models.IntegerField()
    jumlah_penduduk_perempuan = models.IntegerField()


class Divisi(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self) -> str:
        return self.nama

class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='anggota')
    alamat = models.CharField(max_length=100)
    telepon = models.CharField(max_length=20)
    jabatan = models.CharField(max_length=100)
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE)


class Pimpinan(models.Model):
    nama = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='pimpinan')
    telepon = models.CharField(max_length=20)
    jabatan = models.CharField(max_length=100)
    deskripsi = models.TextField()


class Jumbotron(models.Model):
    nama = models.CharField(max_length=30, unique=True)
    judul = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='jumbotron', null=True, blank=True)
    deskripsi = models.TextField()


@receiver(post_save, sender=KarangTaruna)
def lokasi_modifier_karangtaruna(sender, instance, created, **kwargs):
    lokasi = str(instance.lokasi)
    if '<iframe' in lokasi:
        start_index = lokasi.find('src="') + 5
        end_index = lokasi.find('"', start_index)

        iframe_src = lokasi[start_index:end_index]

        print(iframe_src)
        instance.lokasi = iframe_src
        instance.save()

@receiver(post_save, sender=Pengumuman)
def lokasi_modifier_pengumuman(sender, instance, created, **kwargs):
    lokasi = str(instance.lokasi)
    if '<iframe' in lokasi:
        start_index = lokasi.find('src="') + 5
        end_index = lokasi.find('"', start_index)

        iframe_src = lokasi[start_index:end_index]

        print(iframe_src)
        instance.lokasi = iframe_src
        instance.save()