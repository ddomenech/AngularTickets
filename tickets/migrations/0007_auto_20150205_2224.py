# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tickets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20150203_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestas',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='respuestas',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.ImageField(upload_to=tickets.models.x_file_name, blank=True, default='/imagenes/avatar.png'),
        ),
    ]
