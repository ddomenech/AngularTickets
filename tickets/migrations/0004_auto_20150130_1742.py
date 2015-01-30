# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_respuestas_ticket_id'),
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
            model_name='respuestas',
            name='ticket_id',
            field=models.ForeignKey(related_name='respuestastickets', to='tickets.tickets'),
        ),
        migrations.AlterField(
            model_name='respuestas',
            name='usuario_id',
            field=models.ForeignKey(related_name='userrespuestas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='ticket_padre_id',
            field=models.ForeignKey(blank=True, null=True, related_name='hijos', to='tickets.tickets'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='usuario_id',
            field=models.ForeignKey(related_name='usertickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='profile', unique=True),
        ),
    ]
