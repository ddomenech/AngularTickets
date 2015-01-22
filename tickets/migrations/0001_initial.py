# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import tickets.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tickets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('motivo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=400)),
                ('imagen', models.ImageField(blank=True, upload_to='%Y/%m/%d')),
                ('prioridad', models.CharField(max_length=5, choices=[('ALTA', '1'), ('MEDIA', '2'), ('BAJA', '3')], default='BAJA')),
                ('estado', models.CharField(max_length=1, choices=[('A', 'ABIERTO'), ('C', 'CERRADO')], default='A')),
                ('fecha_creacion', models.DateTimeField(default=datetime.datetime.now)),
                ('ticket_padre_id', models.ForeignKey(to='tickets.tickets', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to=tickets.models.x_file_name, blank=True, default='/imagenes/avatar.png')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tickets',
            name='usuario_id',
            field=models.ForeignKey(to='tickets.users'),
            preserve_default=True,
        ),
    ]
