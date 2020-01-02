from django.contrib import admin

# Register your models here.
from worker.models import Position, Leave, Contract, Worker

admin.site.register(Position)
admin.site.register(Leave)
admin.site.register(Contract)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'first_name',
                    'last_name', 'PESEL', 'hotel', 'contract')
    fieldsets = (
        ('Account', {
            'fields': ('username', 'password')
        }),
        ('Details', {
            'fields': ('first_name', 'last_name', 'PESEL', 'hotel', 'contract')
        })
    )
