from atexit import register

from django.contrib import admin
from django.utils.html import format_html

from apps import students


from .models import (
    Invoice,
    Pending_Fees,
    Receipt,
    
)

@admin.register(Invoice)
class InvoiceModelAdmin(admin.ModelAdmin):
    list_display = ['student', 'session','term', 'class_for', 'balance_from_previous_term','status']

@admin.register(Pending_Fees)
class Pending_FeesModelAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'description','amount']
# Register your models here.

# @admin.register(InvoiceItem)
# class InvoiceItemModelAdmin(admin.ModelAdmin):
#     list_display = ['invoice', 'description','amount']


@admin.register(Receipt)
class ReceiptItemModelAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'amount_paid','date_paid','comment']
# Register your models here.


