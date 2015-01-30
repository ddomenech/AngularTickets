from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tickets', views.TicketViewSet)
router.register(r'usuarios', views.UserViewSet)
router.register(r'respuestas', views.RespuestaViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
