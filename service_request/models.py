from django.db import models


# Create your models here.

class ServiceRequest(models.Model):
    description = models.TextField('Opis problemu', max_length=150)
    room = models.ForeignKey('hotel.Room', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return 'Service request {}'.format(self.pk)
