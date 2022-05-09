from atexit import register

from django.contrib import admin
from django.utils.html import format_html


from .models import (
    Result,
    AcademicSession,
    AcademicTerm,
    StudentClass,
    Subject,
)

@admin.register(Result)
class ResultModelAdmin(admin.ModelAdmin):
    list_display = ['student', 'session','term', 'current_class', 'subject', 'Insem','Endsem']
# Register your models here.


