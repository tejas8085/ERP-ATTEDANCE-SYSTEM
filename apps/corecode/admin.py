from atexit import register

from django.contrib import admin
from django.utils.html import format_html


from .models import (
    
    SiteConfig,
)

@admin.register(SiteConfig)
class SiteConfigModelAdmin(admin.ModelAdmin):
    list_display = [ 'key','value']
# Register your models here.


