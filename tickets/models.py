from django.db import models
from django.utils import timezone
# Create your models here.

class users(models.Model):
    user_name = models.TextField(max_length=200)
    password = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="%Y/%m/%d", blank=True)
    email = models.EmailField()
    
    
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
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
'''
1 - La base de datos tienen nombres en plural, en este caso la tabla la llamaría tickets y usuarios.
2 - Siempre tiene un id que es único y autonumérico.
3 - El id siempre empieza por id_ y el nombre de la base de datos en singular, en este caso sería id_ticket
4 - Las claves foraneas siempre las identifico con el nombre de la base de datos relacionada en singular más el _id, en este caso para la tabla tickets habría una clave foranea de la tabla usuarios y se llamaría usuario_id, otro caso en TicketPadre yo lo llamaría ticket_padre_id.
5 - Los nombre de las tablas y de los campos siempre están en minúsculas para evitar problemas en sistemas unix.
6 - Siempre que el nombre de la tabla o del campo se componga de dos palabras irán separados por un guión bajo, por ejemplo para el campo Fecha_Creacion yo lo llamaría fecha_creacion.

Tabla de Tickets: Tickets_ID - UsuarioID - Motivo - Descripcion - Img - Prioridad ( ALTA-BAJA-MEDIA)- TicketPadre (RECURSIVIDAD) - ESTADO (ABIERTO-CERRADO) - Fecha_Creacion

Tabla Usuarios: UserID - UserName - Passwoord - Avatar - Email
'''
