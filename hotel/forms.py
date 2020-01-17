from django.forms import ModelForm

from hotel.models import Address, Opinion, Hotel


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'houseNumber', 'postalCode', 'city']


class CreateOpinionForm(ModelForm):
    class Meta:
        model = Opinion
        fields = ['message', ]

    def save(self, commit=True):
        opinion = super(CreateOpinionForm, self).save(commit=False)
        opinion.hotel = Hotel.objects.get(pk=self.hotel_pk)
        opinion.save()
        return opinion

    def __init__(self, pk, *args, **kwargs):
        super(CreateOpinionForm, self).__init__(*args, **kwargs)
        self.hotel_pk = pk
