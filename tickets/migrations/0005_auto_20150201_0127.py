# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20150130_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestas',
            name='imagen',
            field=models.ImageField(upload_to='/imagenes/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='imagen',
            field=models.ImageField(upload_to='/imagenes/%Y/%m/%d', blank=True),
        ),
    ]
