from atexit import register

from django.contrib import admin
from django.utils.html import format_html

from apps import students


from .models import (
    Staff,
    
)

@admin.register(Staff)
class StaffModelAdmin(admin.ModelAdmin):
    list_display = ['current_status', 'surname','firstname', 'gender', 'address','mobile_number']
# Register your models here.


