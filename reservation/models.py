from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Receipt(models.Model):
    CASH = 'C'
    CARD = 'CD'
    PAYMENT_METHODS = [
        (CASH, 'Karta'),
        (CARD, 'Gotówka'),
    ]
    total = models.FloatField('Kwota', null=False, blank=False, default=0)
    accomodationCost = models.FloatField('Kosz noclegu', null=False, blank=False, default=0)
    cateringCosts = models.FloatField('Kosz cateringu', null=False, blank=False, default=0)
    paymentMethod = models.CharField('Metoda płatności',
                                     max_length=2, null=False, blank=False,
                                     choices=PAYMENT_METHODS, default=CASH)

    def __str__(self):
        return 'Rachunek {}'.format(self.pk)

    def update_costs(self):
        reservation = Reservation.objects.get(receipt=self)
        if reservation.isRegistered:
            self.cateringCosts = 0
            items = reservation.catering.foodquantity_set.all()
            for item in items:
                self.cateringCosts += item.quantity * item.foodItem.price

        self.accomodationCost = reservation.room.costPerNight * reservation.length
        self.total = 50 + self.accomodationCost + self.cateringCosts \
            if reservation.isParkingSpotNeeded \
            else self.accomodationCost + self.cateringCosts
        self.save()


class Reservation(models.Model):
    start = models.DateField('Rozpoczęcie', null=False, blank=False)
    length = models.IntegerField('Długość', null=False, blank=False)
    notes = models.TextField('Notatki', max_length=150, blank=True, null=False)
    isParkingSpotNeeded = models.BooleanField('Miejsce parkingowe', null=False, blank=False)
    client = models.ForeignKey('hotel.Client', on_delete=models.CASCADE, null=False, blank=False)
    room = models.ForeignKey('hotel.Room', on_delete=models.CASCADE, null=False, blank=False, related_name='room')
    receipt = models.ForeignKey('Receipt', on_delete=models.CASCADE, null=False, blank=False)
    catering = models.ForeignKey('catering.Catering', on_delete=models.SET_NULL, null=True, blank=False)
    isRegistered = models.BooleanField('Zameldowano', null=False, blank=False, default=False)
    isCheckedOut = models.BooleanField('Wymeldowano', null=False, blank=False, default=False)

    def __str__(self):
        return 'Rezerwacja{} - {}'.format(self.pk, self.room)


@receiver(post_save, sender=Reservation)
def update_receipt(sender, instance, created, **kwargs):
    if created:
        instance.receipt.update_costs()
        instance.receipt.save()


post_save.connect(update_receipt, sender=Reservation)
