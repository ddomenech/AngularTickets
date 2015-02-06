from rest_framework import serializers
from tickets.models import tickets, users, respuestas
from django.contrib.auth.models import User

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    usuario_id = serializers.Field(source='usuario_id.username')
    imagen = serializers.ImageField(required=False)
    fecha_creacion = serializers.DateTimeField(required=False)
    class Meta:
        model = tickets
        fields = ('url', 'motivo', 'descripcion',
                  'imagen', 'prioridad', 'ticket_padre_id', 'estado', 'fecha_creacion', 'usuario_id', 'hijos', 'respuestastickets')
        read_only_fields=('hijos', 'respuestastickets',)

class RespuestaSerializer(serializers.HyperlinkedModelSerializer):
    usuario_id = serializers.Field(source='usuario_id.username')
    #ticket_id = serializers.HyperlinkedRelatedField(queryset=tickets.objects.all(),view_name='tickets-detail')
    imagen = serializers.ImageField(required=False)
    fecha_creacion = serializers.DateTimeField(required=False)
    class Meta:
        model = respuestas
        fields = ('url', 'titulo', 'descripcion',
                  'imagen',  'usuario_id', 'ticket_id', 'fecha_creacion' )

class UsersSerializers(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False)
    class Meta:
        model = users
        fields = ('avatar',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UsersSerializers()
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'profile', 'usertickets', 'userrespuestas',)
        read_only_fields = ('usertickets', 'userrespuestas',)
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user
