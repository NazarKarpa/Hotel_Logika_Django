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
        self.room = kwargs.pop('room',None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        date_start = cleaned_data.get('date_start')
        date_end = cleaned_data.get('date_end')

        if date_start and date_end:
            if self.room:
                ex_booking = Reservation.objects.filter(
                    room = self.room,
                    date_start__lt=date_end,
                    date_end__gt=date_start
                )
                if ex_booking.exists():
                    raise forms.ValidationError("KiMiara Bже заброньована на цей період")

        return cleaned_data



