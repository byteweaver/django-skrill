from django.contrib import admin

from skrill.models import PaymentRequest, StatusReport


class StatusReportAdmin(admin.ModelAdmin):
    list_display = ('time', 'status', 'amount', 'currency', 'valid', 'signal_sent',)
    list_filter = ('time', 'status', 'valid', 'signal_sent',)

admin.site.register(PaymentRequest)
admin.site.register(StatusReport, StatusReportAdmin)

