# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carregamentos', '0009_auto_20160601_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to=b'media'),
        ),
    ]
