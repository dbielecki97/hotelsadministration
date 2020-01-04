from django.db import models


# Create your models here.

class Receipt(models.Model):
    CASH = 'C'
    CARD = 'CD'
    PAYMENT_METHODS = [
        (CASH, 'Karta'),
        (CARD, 'Gotówka'),
    ]
    total = models.FloatField('Kwota', null=False, blank=True, default=0)
    paymentMethod = models.CharField('Metoda płatności',
                                     max_length=2, null=False, blank=False,
                                     choices=PAYMENT_METHODS, default=CASH)

    def __str__(self):
        return 'Receipt {}'.format(self.pk)


class Reservation(models.Model):
    start = models.DateField('Rozpoczęcie', null=False, blank=False)
    length = models.IntegerField('Długość', null=False, blank=False)
    notes = models.TextField('Notatki', max_length=150, blank=True, null=False)
    isParkingSpotNeeded = models.BooleanField('Miejsce parkingowe', null=False, blank=False)
    client = models.ForeignKey('hotel.Client', on_delete=models.CASCADE, null=False, blank=False)
    room = models.ForeignKey('hotel.Room', on_delete=models.CASCADE, null=False, blank=False)
    receipt = models.ForeignKey('Receipt', on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return 'Reservation {}.{}'.format(self.room, self.pk)
