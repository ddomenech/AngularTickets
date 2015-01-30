from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from tickets.models import tickets, users, respuestas
from api.permissions import IsOwnerOrReadOnly
from api.serializers import TicketSerializer, UserSerializer, RespuestaSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = tickets.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def pre_save(self, obj):
        obj.usuario_id = self.request.user
    
class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = respuestas.objects.all()
    serializer_class = RespuestaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def pre_save(self, obj):
        obj.usuario_id = self.request.user    
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
