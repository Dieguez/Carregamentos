# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carregamentos', '0004_auto_20160514_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carregamento',
            name='path_foto',
        ),
    ]
