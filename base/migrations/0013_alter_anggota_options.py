# Generated by Django 3.2.15 on 2024-02-04 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_pimpinan_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anggota',
            options={'ordering': ['jabatan']},
        ),
    ]
