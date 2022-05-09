from django.forms import inlineformset_factory, modelformset_factory

from .models import Invoice, Pending_Fees, Receipt

InvoiceItemFormset = inlineformset_factory(
    Invoice, Pending_Fees, fields=["description", "amount"], extra=1, can_delete=True
)

InvoiceReceiptFormSet = inlineformset_factory(
    Invoice,
    Receipt,
    fields=("amount_paid", "date_paid", "comment"),
    extra=0,
    can_delete=True,
)

Invoice = modelformset_factory(Invoice, exclude=(), extra=4)
