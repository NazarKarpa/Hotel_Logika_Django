from django.contrib import admin

from reservation.models import Room, Reservation, TypeRoom

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'date_start', 'date_end', 'phone_number')
    search_fields = ('date_start', 'phone_number')



admin.site.register(Room)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(TypeRoom)
