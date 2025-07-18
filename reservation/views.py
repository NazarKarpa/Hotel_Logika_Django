from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from reservation.forms import *
from reservation.models import Room, Reservation, TypeRoom


def room_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms

    }
    return render(request, template_name='room_list.html', context=context)



@login_required
def booking(request, id_room):
    room = get_object_or_404(Room, id=id_room)
    form = BookingForm(room=room)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room
            reservation.user = request.user
            #form.full_clean()
            reservation.save()
            return redirect('room-list')

    context = {
        'room': room,
        'form': form,

    }


    return render(request, template_name='booking.html', context=context)