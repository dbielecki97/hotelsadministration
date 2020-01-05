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
        room = Room.objects.get(pk=self.pk)
        room.isAvailable = False
        room.save()
        receipt = Receipt()
        receipt.total = room.costPerNight * reservation.length
        receipt.save()
        reservation.client = client
        reservation.receipt = receipt
        reservation.room = room
        reservation.save()
        return reservation

    def __init__(self, pk, user, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.pk = pk
        self.user = user


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ('paymentMethod',)
