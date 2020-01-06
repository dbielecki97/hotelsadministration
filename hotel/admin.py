from django.contrib import admin

from hotel.models import Room, Hotel, Opinion, Address, Client

# Register your models here.
admin.site.register(Address)
admin.site.register(Client)
admin.site.register(Opinion)
admin.site.register(Room)


class RoomTabular(admin.TabularInline):
    model = Room
    extra = 0
    fieldsets = ((
                     'Room', {
                         'fields': ('roomNumber', 'standard', 'numberOfBeds', 'costPerNight',)
                     }),
    )


class AddressTabular(admin.StackedInline):
    model = Address
    max_num = 1
    verbose_name_plural = 'address'


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (AddressTabular, RoomTabular,)

    fieldsets = (
        ('General', {
            'fields': ('name',)
        }),
    )
