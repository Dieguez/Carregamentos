# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 03:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carregamentos', '0016_auto_20160603_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caminhao',
            old_name='altura',
            new_name='profundidade',
        ),
    ]
