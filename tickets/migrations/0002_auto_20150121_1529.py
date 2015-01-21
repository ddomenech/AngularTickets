# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=400)),
                ('imagen', models.ImageField(upload_to='%Y/%m/%d', blank=True)),
                ('prioridad', models.CharField(default='BAJA', max_length=5, choices=[('ALTA', '1'), ('MEDIA', '2'), ('BAJA', '3')])),
                ('estado', models.CharField(default='A', max_length=1, choices=[('A', 'ABIERTO'), ('C', 'CERRADO')])),
                ('fecha_creacion', models.DateTimeField(default=datetime.datetime.now)),
                ('ticket_padre_id', models.ForeignKey(null=True, blank=True, to='tickets.ticket')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='%Y/%m/%d', blank=True)),
                ('user', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='ticket_padre_id',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='usuario_id',
        ),
        migrations.DeleteModel(
            name='tickets',
        ),
        migrations.DeleteModel(
            name='users',
        ),
        migrations.AddField(
            model_name='ticket',
            name='usuario_id',
            field=models.ForeignKey(to='tickets.user'),
            preserve_default=True,
        ),
    ]
