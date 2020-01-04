from django import forms as forms
from django.contrib.auth.forms import UserCreationForm
from hotel.models import Client
from django.contrib.auth.models import User


class ClientCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=9, label='Numer kontaktowy')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        instance = super().save(commit=True)
        profile = Client(user=instance, phoneNumber=self.cleaned_data['phone_number'])
        profile.save()
        return instance
