# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carregamentos', '0007_caminhao_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caminhao',
            name='volume',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]
