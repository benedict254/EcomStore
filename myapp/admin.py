from django.contrib import admin
from .models import *


class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state",)

admin.site.register(City, CityAdmin)
admin.site.register(slider)
admin.site.register(Item)
