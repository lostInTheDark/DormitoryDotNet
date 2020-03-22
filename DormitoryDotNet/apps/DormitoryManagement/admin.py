from django.contrib import admin

from .models import Dormitory, Floor, Room

admin.site.register(Dormitory)
admin.site.register(Floor)
admin.site.register(Room)