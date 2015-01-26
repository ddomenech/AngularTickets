# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

def x_file_name(instance, filename):
    return '/'.join(['imagenes', instance.user.username, filename])
 
class users(models.Model):
    user = models.ForeignKey(User,unique=True)
    avatar = models.ImageField(upload_to=x_file_name, default="/imagenes/avatar.png", blank=True)
    
class tickets(models.Model):
    usuario_id = models.ForeignKey('users')
    motivo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400)
    imagen = models.ImageField(upload_to="%Y/%m/%d", blank=True)
    prioridad_opciones = (
        ('ALTA', '1'), ('MEDIA', '2'), ('BAJA', '3')
    )
    prioridad = models.CharField(max_length=5,choices=prioridad_opciones,default='BAJA')
    ticket_padre_id = models.ForeignKey('self', blank=True, null=True)
    estado_opciones = (
        ('A', 'ABIERTO'),
        ('C', 'CERRADO')
    )
    estado = models.CharField(max_length=1, choices=estado_opciones, default='A')
    fecha_creacion = models.DateTimeField(default=datetime.now)
    def __unicode__(self):
        return self.motivo

class respuestas(models.Model):
    usuario_id = models.ForeignKey('users')
    ticket_id = models.ForeignKey('tickets',null=False)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to="%Y/%m/%d", blank=True)
    fecha_creacion = models.DateTimeField(default=datetime.now)
    def __unicode__(self):
        return self.titulo


