from .models import Reservation
from django import forms
from hotel.models import Client, Room
from .models import Receipt


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ('client', 'receipt', 'room',)

    def save(self, commit=True):
        reservation = super(ReservationForm, self).save(commit=False)
        client = Client.objects.get(user=self.user)
        receipt = Receipt()
        receipt.save()
        room = Room.objects.get(pk=self.pk)
        room.isAvailable = False
        room.save()
        reservation.client = client
        reservation.receipt = receipt
        reservation.room = room
        reservation.save()
        super().save_m2m()
        return reservation

    def __init__(self, pk, user, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.pk = pk
        self.user = user
