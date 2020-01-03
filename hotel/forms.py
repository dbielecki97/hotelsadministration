from django.forms import ModelForm
from hotel.models import Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'houseNumber', 'postalCode', 'city']
