from django import forms

from hotel.models import Client
from reservation.models import Reservation
from service_request.models import ServiceRequest


class NewServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ('description',)

    def save(self, commit=True):
        service_request = super(NewServiceRequestForm, self).save(commit=False)
        service_request.client = Client.objects.get(user=self.user)
        service_request.reservation = Reservation.objects.get(pk=self.pk)
        service_request.save()
        return service_request

    def __init__(self, pk, user, *args, **kwargs):
        super(NewServiceRequestForm, self).__init__(*args, **kwargs)
        self.pk = pk
        self.user = user
