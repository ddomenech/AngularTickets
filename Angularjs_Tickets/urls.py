from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tickets', views.TicketViewSet)
router.register(r'usuarios', views.UserViewSet)
router.register(r'respuestas', views.RespuestaViewSet)

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^api/', include(router.urls)),
    url(r'^api/auth/$', views.AuthView.as_view(), name='authenticate'),
    url(r'^admin/', include(admin.site.urls)),

)
