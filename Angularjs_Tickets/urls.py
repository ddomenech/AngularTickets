from django.conf.urls import patterns, include, url
from django.contrib import admin
from Angularjs_Tickets.views import IndexView
from api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tickets', views.TicketViewSet)
router.register(r'usuarios', views.UserViewSet)
router.register(r'respuestas', views.RespuestaViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api/auth/$', views.AuthView.as_view(), name='authenticate'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', IndexView.as_view(), name='index')
)
