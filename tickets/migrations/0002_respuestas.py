# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='respuestas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=500)),
                ('imagen', models.ImageField(upload_to=b'%Y/%m/%d', blank=True)),
                ('fecha_creacion', models.DateTimeField(default=datetime.datetime.now)),
                ('usuario_id', models.ForeignKey(to='tickets.users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
