from django import forms
from .models import * 


class ReservationForm(forms.ModelForm):
    number_of_tickets = forms.IntegerField(label='Number of Tickets', min_value=1)

    class Meta:
        model = Reservation
        fields = ['number_of_tickets']

