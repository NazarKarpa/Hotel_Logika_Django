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
        widgets = {
            'date_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_end': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'




