from django.contrib import admin

from skrill.models import PaymentRequest, StatusReport


admin.site.register(PaymentRequest)
admin.site.register(StatusReport)

