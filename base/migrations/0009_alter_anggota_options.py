# Generated by Django 3.2.15 on 2024-02-04 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20240201_1935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anggota',
            options={'ordering': ['jabatan']},
        ),
    ]
