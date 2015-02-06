# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tickets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20150201_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestas',
            name='fecha_creacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 2, 3, 2, 1, 21, 948767)),
        ),
        migrations.AlterField(
            model_name='respuestas',
            name='imagen',
            field=models.ImageField(upload_to='imagenes/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='fecha_creacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 2, 3, 2, 1, 21, 947767)),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='imagen',
            field=models.ImageField(upload_to='imagenes/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.ImageField(upload_to=tickets.models.x_file_name, blank=True, default='imagenes/avatar.png'),
        ),
    ]
