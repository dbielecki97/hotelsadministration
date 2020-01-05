from django.contrib.auth.models import User
from django.db import models


class Hotel(models.Model):
    name = models.CharField('Nazwa', max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.CharField('Miasto', max_length=50, null=False, blank=True)
    postalCode = models.CharField('Kod pocztowy', max_length=6, null=False, blank=True)
    street = models.CharField('Ulica', max_length=50, null=False, blank=True)
    houseNumber = models.CharField('Numer domu', max_length=10, null=False, blank=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return '{} {}, {}, {}'.format(self.street, self.houseNumber, self.city, self.postalCode)

    class Meta:
        verbose_name_plural = "addresses"


class Opinion(models.Model):
    message = models.TextField(max_length=150, blank=True, null=False)
    hotel = models.ForeignKey('Hotel', on_delete=models.DO_NOTHING, blank=False, null=False)

    def __str__(self):
        return 'Opinia{}'.format(self.pk)


class Room(models.Model):
    STANDARD = 'ST'
    APARTAMENT = 'APT'
    FAMILY = 'FAM'
    ROOM_STANDARDS = [
        (STANDARD, 'standard'),
        (FAMILY, 'rodzinny'),
        (APARTAMENT, 'apartament'),
    ]

    numberOfBeds = models.IntegerField('Ilość łóżek', default=1, blank=False, null=False)
    standard = models.CharField('Standard', max_length=3, choices=ROOM_STANDARDS, default=STANDARD)
    roomNumber = models.IntegerField('Numer pokoju', null=False, blank=False)
    isAvailable = models.BooleanField('Dostępny', default=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, blank=False, null=False)
    costPerNight = models.FloatField('Cena za noc', blank=False, null=False)

    def __str__(self):
        return '{}: {}'.format(self.hotel, self.roomNumber)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.IntegerField("Numer kontaktowy", null=False, blank=False)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = "client"
