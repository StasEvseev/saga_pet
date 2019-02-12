from django.contrib import admin

from .models import Customer, Payment, Transaction, Outbox


class CustomerAdmin(admin.ModelAdmin):
    pass


class PaymentAdmin(admin.ModelAdmin):
    pass


class TransactionAdmin(admin.ModelAdmin):
    pass


class OutboxAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Outbox, OutboxAdmin)
