from django.contrib import admin

from skrill.models import PaymentRequest, StatusReport


class PaymentRequestAdmin(admin.ModelAdmin):
    list_display = ('time', 'user', 'amount', 'currency', 'test')
    list_filter = ('time',)
    search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name')

class StatusReportAdmin(admin.ModelAdmin):
    list_display = ('time', 'status', 'amount', 'currency', 'mb_transaction_id', 'valid', 'signal_sent',)
    list_filter = ('time', 'status', 'valid', 'signal_sent')
    search_fields = ('payment_request__user__email', 'payment_request__user__username', 'payment_request__user__first_name', 'payment_request__user__last_name', 'mb_transaction_id')

admin.site.register(PaymentRequest, PaymentRequestAdmin)
admin.site.register(StatusReport, StatusReportAdmin)

