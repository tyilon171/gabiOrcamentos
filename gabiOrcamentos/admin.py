from django.contrib import admin

from gabiOrcamentos.models import Client, Location, Schedule

# Register your models here.
admin.site.register(Location)
admin.site.register(Client)
admin.site.register(Schedule)