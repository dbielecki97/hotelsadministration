from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    PESEL = models.IntegerField('PESEL', null=False, blank=False)
    hotel = models.ForeignKey('hotel.Hotel', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = 'employee'


class Leave(models.Model):
    isPaid = models.BooleanField('Płatny', null=False, blank=False)
    dateOfStart = models.DateField('Początek', null=False, blank=False)
    dateOfEnd = models.DateField('Koniec', null=False, blank=False)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return '{} {}'.format(self.employee, self.pk)


class Contract(models.Model):
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    TRIAL = 'T'
    EMPLOYMENT_TYPES = [
        (FULL_TIME, 'W pełnym wymiarze godzin'),
        (PART_TIME, 'W niepełnym wymiarze godzin'),
        (TRIAL, 'Okres próbny'),
    ]
    isPaid = models.BooleanField('Płatny')
    employmentDate = models.DateField('Data zatrudnienia', blank=False, null=False)
    endOfEmploymentDate = models.DateField('Data zakończenia zatrudnienia', blank=True, null=False)
    type = models.CharField('Type', max_length=2, choices=EMPLOYMENT_TYPES, blank=False, null=False)
    description = models.TextField('Opis', max_length=150, blank=True, null=False)
    hourWage = models.FloatField('Stawka godzinowa', blank=False, null=False)
    position = models.ForeignKey('Position', blank=False, null=False, on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, null=False, blank=False)


class Position(models.Model):
    name = models.CharField('Nazwa stanowiska', max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
