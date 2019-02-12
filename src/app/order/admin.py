from django.contrib import admin

from .models import Order, Transaction, Outbox


class OrderAdmin(admin.ModelAdmin):
    pass


class TransactionAdmin(admin.ModelAdmin):
    pass


class OutboxAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Outbox, OutboxAdmin)
