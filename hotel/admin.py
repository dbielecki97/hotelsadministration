from django.contrib import admin

from hotel.models import Address, Hotel, Client, Opinion, Room

# Register your models here.
admin.site.register(Address)

admin.site.register(Hotel)
admin.site.register(Client)
admin.site.register(Opinion)
admin.site.register(Room)
