# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 04:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carregamentos', '0006_auto_20160517_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carregamento',
            name='duracao',
            field=models.DurationField(default=datetime.timedelta(0), editable=False),
        ),
    ]
