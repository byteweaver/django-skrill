from django import http
from django.views.generic.base import View

from skrill.models import PaymentRequest, StatusReport


class StatusReportView(View):
    def post(self, request, *args, **kwargs):
        payment_request = PaymentRequest.objects.get(pk=request.POST['transaction_id'])
        report = StatusReport()
        report.payment_request = payment_request
        report.pay_to_email = request.POST['pay_to_email']
        report.pay_from_email = request.POST['pay_from_email']
        report.merchant_id = request.POST['merchant_id']
        report.customer_id = request.POST.get('customer_id', None)
        report.mb_transaction_id = request.POST['mb_transaction_id']
        report.mb_amount = request.POST['mb_amount']
        report.mb_currency = request.POST['mb_currency']
        report.status = request.POST['status']
        report.failed_reason_code = request.POST.get('failed_reason_code', None)
        report.md5sig = request.POST['md5sig']
        report.sha2sig = request.POST.get('sha2sig', None)
        report.amount = request.POST['amount']
        report.currency = request.POST['currency']
        report.payment_type = request.POST.get('payment_type', None)
        report.custom_field_1 = request.POST.get('custom_field_1', None)
        report.custom_field_2 = request.POST.get('custom_field_2', None)
        report.custom_field_3 = request.POST.get('custom_field_3', None)
        report.custom_field_4 = request.POST.get('custom_field_4', None)
        report.custom_field_5 = request.POST.get('custom_field_5', None)
        report.save()
        report.validate_md5sig()
        report.valid = True
        report.save()
        report.send_signal()
        return http.HttpResponse()

