from django.contrib import admin

# Register your models here.
from catering.models import Drink, Catering, Course

admin.site.register(Drink)
admin.site.register(Course)
admin.site.register(Catering)
