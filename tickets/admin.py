from django.contrib import admin

# Register your models here.
from .models import ticket, user

admin.site.register(user)
admin.site.register(ticket)