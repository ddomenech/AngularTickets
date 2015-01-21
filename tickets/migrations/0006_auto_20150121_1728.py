# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tickets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20150121_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to=tickets.models.x_file_name, blank=True, default='/imagenes/avatar.png'),
        ),
    ]
