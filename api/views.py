from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets, views
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from tickets.models import tickets, users, respuestas
from api.permissions import IsOwnerOrReadOnly, IsStaffOrTargetUser
from api.serializers import TicketSerializer, UserSerializer, RespuestaSerializer
from api.authentication import QuietBasicAuthentication

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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # allow non-authenticated user to create
        return (permissions.AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),

    def post_save(self, User, *args, **kwargs):
      profile = users(user=User)
      if (rest.request.FILES.get('avatar')):
        profile.avatar=rest.request.FILES.get('avatar')
      profile.save()


class AuthView(views.APIView):
    authentication_classes = (QuietBasicAuthentication,)

    def post(self, request, *args, **kwargs):
        login(request, request.user)
        userSer = UserSerializer(request.user,  context={'request':request})
        return Response(userSer.data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response()
# Create your views here.
