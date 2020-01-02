from django.contrib import admin

# Register your models here.
from reservation.models import Receipt, Reservation

admin.site.register(Receipt)
admin.site.register(Reservation)
