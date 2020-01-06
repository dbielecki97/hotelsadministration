from django.db import models
from django.utils.timezone import now


# Create your models here.

class ServiceRequest(models.Model):
    description = models.TextField('Opis problemu', max_length=150)
    client = models.ForeignKey('hotel.Client', on_delete=models.SET_NULL, null=True, blank=False)
    date = models.DateTimeField('Data', null=False, blank=False, default=now)
    reservation = models.ForeignKey('reservation.Reservation', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return 'Service request {}'.format(self.pk)
