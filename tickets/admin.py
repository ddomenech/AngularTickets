from django.contrib import admin

# Register your models here.
from .models import tickets, users, respuestas

admin.site.register(users)
admin.site.register(tickets)
admin.site.register(respuestas)