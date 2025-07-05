from django import forms

from reservation.models import Reservation


class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'date_start',
            'date_end',
            'phone_number',
            'people_quantity'
        ]




