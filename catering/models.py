from django.db import models


class Catering(models.Model):
    total = models.FloatField('Kwota')
    reservation = models.ForeignKey('reservation.Reservation', on_delete=models.CASCADE, null=False, blank=False)
    drinks = models.ManyToManyField('Drink')
    courses = models.ManyToManyField('Course')

    def __str__(self):
        return 'Catering {}'.format(self.pk)


class Drink(models.Model):
    name = models.CharField('Nazwa', blank=False, null=False, max_length=50)
    price = models.FloatField('Cena', blank=False, null=False)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField('Nazwa', max_length=50, blank=False, null=False)
    price = models.FloatField('Cena', blank=False, null=False)

    def __str__(self):
        return self.name
