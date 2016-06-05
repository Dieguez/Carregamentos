# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django_boto.s3.storage
import webcam.fields


class Migration(migrations.Migration):

    dependencies = [
        ('carregamentos', '0011_auto_20160602_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='foto',
            field=models.FileField(storage=django_boto.s3.storage.S3Storage(), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='carregamento',
            name='photo',
            field=webcam.fields.CameraField(storage=django_boto.s3.storage.S3Storage(), upload_to=b'', verbose_name=b'foto'),
        ),
    ]