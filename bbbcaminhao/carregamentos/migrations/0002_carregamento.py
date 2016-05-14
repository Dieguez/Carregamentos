# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import webcam.fields
import webcam.storage


class Migration(migrations.Migration):

    dependencies = [
        ('carregamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carregamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(editable=False)),
                ('duracao', models.DurationField()),
                ('path_foto', models.CharField(max_length=2000)),
                ('photo', webcam.fields.CameraField(blank=True, null=True, storage=webcam.storage.CameraStorage(), upload_to=b'pictures', verbose_name=b'CameraPictureField')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(editable=False)),
                ('is_active', models.BooleanField()),
                ('caminhao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carregamentos.Caminhao')),
                ('frente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carregamentos.Frente')),
            ],
        ),
    ]
