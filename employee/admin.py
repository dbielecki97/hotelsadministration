from django.contrib import admin

# Register your models here.
from employee.models import Position, Leave, Contract, Employee
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Position)
admin.site.register(Leave)
admin.site.register(Contract)
admin.site.register(Employee)

# class EmployeeInline(admin.TabularInline):
#     model = Employee
#
#
# class EmployeeAdmin(UserAdmin):
#     inlines = [
#         EmployeeInline,
#     ]
#
#
# admin.site.register(User, EmployeeAdmin)
