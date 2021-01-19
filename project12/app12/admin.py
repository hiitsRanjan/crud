from django.contrib import admin
from .models import Employeemodel,Availablejobs

@admin.register(Employeemodel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email_id','phone_num']


@admin.register(Availablejobs)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name']


