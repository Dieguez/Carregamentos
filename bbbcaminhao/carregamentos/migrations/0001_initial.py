# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 02:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import webcam.fields
import webcam.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caminhao',
            fields=[
                ('placa', models.CharField(max_length=7)),
                ('largura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('profundidade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('motorista', models.CharField(max_length=500)),
                ('data_criacao', models.DateTimeField(editable=False)),
                ('data_alteracao', models.DateTimeField(editable=False)),
                ('codigo_barras', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Caminhao',
                'verbose_name_plural': 'Caminhoes',
            },
        ),
        migrations.CreateModel(
            name='Carregamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(editable=False)),
                ('duracao', models.DurationField(default=datetime.timedelta(0), editable=False)),
                ('photo', webcam.fields.CameraField(blank=True, null=True, storage=webcam.storage.CameraStorage(), upload_to=b'carregamentos-photo', verbose_name=b'foto')),
                ('foto', models.FileField(blank=True, null=True, upload_to=b'carregamentos-photo')),
                ('data_criacao', models.DateTimeField(editable=False)),
                ('data_alteracao', models.DateTimeField(editable=False)),
                ('id_caminhao', models.CharField(max_length=100)),
                ('caminhao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carregamentos.Caminhao')),
            ],
        ),
        migrations.CreateModel(
            name='Frente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=2000)),
                ('data_criacao', models.DateTimeField(editable=False)),
                ('data_alteracao', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='carregamento',
            name='frente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carregamentos.Frente'),
        ),
    ]
