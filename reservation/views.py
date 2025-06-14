from django.shortcuts import render

from reservation.models import Room, Reservation, TypeRoom


def room_list(request):
    rooms = Room.objects.all()

    context = {
        'rooms': rooms

    }

    return render(request, template_name='room_list.html', context=context)
