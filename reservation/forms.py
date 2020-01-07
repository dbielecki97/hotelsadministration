from django import forms

from catering.models import Catering
from hotel.models import Client, Room
from .models import Receipt
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ('client', 'receipt', 'room', 'catering', 'isRegistered', 'isCheckedOut',)

    def save(self, commit=True):
        reservation = super(ReservationForm, self).save(commit=False)
        client = Client.objects.get(user=self.user)
        room = Room.objects.get(pk=self.pk)
        receipt = Receipt()
        receipt.save()
        reservation.client = client
        reservation.receipt = receipt
        reservation.room = room
        catering = Catering()
        catering.save()
        reservation.catering = catering
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
