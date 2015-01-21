# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=400)),
                ('imagen', models.ImageField(blank=True, upload_to='%Y/%m/%d')),
                ('prioridad', models.CharField(max_length=5, choices=[('ALTA', '1'), ('MEDIA', '2'), ('BAJA', '3')], default='BAJA')),
                ('estado', models.CharField(max_length=1, choices=[('A', 'ABIERTO'), ('C', 'CERRADO')], default='A')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('ticket_padre_id', models.ForeignKey(blank=True, null=True, to='tickets.tickets')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('avatar', models.ImageField(blank=True, upload_to='%Y/%m/%d')),
                ('email', models.EmailField(max_length=75)),
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
