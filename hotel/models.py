from django.contrib.auth.models import User
from django.db import models


class Hotel(models.Model):
    name = models.CharField('Nazwa', max_length=50, null=False, blank=False)
    address = models.ForeignKey('Address', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Opinion(models.Model):
    message = models.TextField(max_length=150, blank=True, null=False)
    hotel = models.ForeignKey('Hotel', on_delete=models.DO_NOTHING, blank=False, null=False)

    def __str__(self):
        return 'Opinia{}'.format(self.pk)


class Room(models.Model):
    hotel = models.ForeignKey('Hotel', blank=False, null=False, on_delete=models.CASCADE)
    numberOfBeds = models.IntegerField('Ilość łóżek', default=1, blank=False, null=False)
    standard = models.CharField('Standard', max_length=50)
    roomNumber = models.IntegerField('Numer pokoju', null=False, blank=False)

    def __str__(self):
        return '{}: {}'.format(self.hotel, self.roomNumber)


class Client(User):
    name = models.CharField('Imię', max_length=50, null=False, blank=False)
    surname = models.CharField('Surname', max_length=50, null=False, blank=False)
    phoneNumber = models.IntegerField("Numer kontaktowy", null=False, blank=False)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{}:{} {}'.format(self.username, self.name, self.surname)

    class Meta:
        verbose_name = "client"


class Address(models.Model):
    city = models.CharField('Miasto', max_length=50, null=False, blank=False)
    postalCode = models.CharField('Kod pocztowy', max_length=6, null=False, blank=False)
    street = models.CharField('Ulica', max_length=50, null=False, blank=False)
    houseNumber = models.CharField('Numer domu', max_length=10, null=False, blank=False)

    def __str__(self):
        return '{} {}, {}, {}'.format(self.street, self.houseNumber, self.city, self.postalCode)

    class Meta:
        verbose_name_plural = "addresses"
