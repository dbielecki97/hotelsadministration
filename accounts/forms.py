from django import forms as forms
from django.contrib.auth.forms import UserCreationForm
from hotel.models import Client, Address


class ClientCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=9, label='Numer kontaktowy')
    street = forms.CharField(max_length=50, required=True, label='Ulica')
    houseNumber = forms.CharField(max_length=10, required=True, label='Numer domu')
    postalCode = forms.CharField(max_length=6, required=True, label='Kod pocztowy')
    city = forms.CharField(max_length=50, required=True, label='Miasto')

    def save(self, commit=True):
        instance = super().save(commit=True)
        address_instance = Address(city=self.cleaned_data['city'],
                                   postalCode=self.cleaned_data['postalCode'],
                                   houseNumber=self.cleaned_data['houseNumber'],
                                   street=self.cleaned_data['street'])
        address_instance.save()
        profile = Client(user=instance, phoneNumber=self.cleaned_data['phone_number'], address=address_instance)
        profile.save()
        return instance
