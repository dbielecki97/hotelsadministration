from django.db import models


class Catering(models.Model):
    total = models.FloatField('Kwota')
    reservation = models.ForeignKey('reservation.Reservation', on_delete=models.CASCADE, null=False, blank=False)
    drinks = models.ManyToManyField('Drink')
    courses = models.ManyToManyField('Course')

    def __str__(self):
        return 'Catering {}'.format(self.pk)


class Drink(models.Model):
    FIZZY = 'F'
    FLAT = 'FL'
    ALCOHOL = 'A'
    DRING_TYPES = [(FIZZY, 'gazowany'), (FLAT, 'niegazowany'), (ALCOHOL, 'alkoholowy'), ]

    name = models.CharField('Nazwa', blank=False, null=False, max_length=50)
    price = models.FloatField('Cena', blank=False, null=False)
    type = models.CharField('Typ', max_length=2, choices=DRING_TYPES, null=False, blank=False)

    def __str__(self):
        return self.name


class Course(models.Model):
    CANDY = 'C'
    DESSERT = 'D'
    MAIN_COURSE = 'MC'
    SOUP = 'S'
    STARTER = 'ST'
    COURSE_TYPES = [(MAIN_COURSE, 'danie główne'), (STARTER, 'przystawka'), (SOUP, 'zupa'), (CANDY, 'słodycz'),
                    (DESSERT, 'deser'),

                    ]
    name = models.CharField('Nazwa', max_length=50, blank=False, null=False)
    price = models.FloatField('Cena', blank=False, null=False)
    type = models.CharField('typ', max_length=2, choices=COURSE_TYPES, blank=False, null=False)

    def __str__(self):
        return self.name
