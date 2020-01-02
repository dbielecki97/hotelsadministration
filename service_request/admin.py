from django.contrib import admin

# Register your models here.
from service_request.models import ServiceRequest

admin.site.register(ServiceRequest)
