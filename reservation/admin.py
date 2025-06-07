from django.contrib import admin

from reservation.models import Room, Reservation, TypeRoom

admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(TypeRoom)
