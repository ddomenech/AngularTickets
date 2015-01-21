# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20150121_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='imagenes/avatar.png', blank=True, upload_to='imagenes/%user_id/%Y/%m/%d'),
        ),
    ]
