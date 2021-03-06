# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 04:54
from __future__ import unicode_literals

from django.db import migrations, models
import webcam.fields
import webcam.storage


class Migration(migrations.Migration):

    dependencies = [
        ('carregamentos', '0002_auto_20160525_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=b'media'),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='photo',
            field=webcam.fields.CameraField(blank=True, null=True, storage=webcam.storage.CameraStorage(), upload_to=b'media', verbose_name=b'foto'),
        ),
    ]
