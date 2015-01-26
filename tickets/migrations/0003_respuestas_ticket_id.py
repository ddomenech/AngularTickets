# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_respuestas'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestas',
            name='ticket_id',
            field=models.ForeignKey(default=1, to='tickets.tickets'),
            preserve_default=False,
        ),
    ]
