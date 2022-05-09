from atexit import register
import re
from django.contrib import admin
from django.utils.html import format_html

from apps import students


from .models import (
    Student,
    
)

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['current_status', 'registration_number', 'surname','firstname', 'gender', 'date_of_birth', 'current_class','date_of_admission', 'passport']
# Register your models here.


