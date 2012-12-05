import hashlib

from django.test import TestCase
from django.core.urlresolvers import reverse

from skrill.settings import get_secret_word_as_md5
from skrill.tests.factories import PaymentRequestFactory
from skrill.settings import *


class StatusReportTestCase(TestCase):
    def generate_md5_signature(self):
        m = hashlib.md5()
        m.update(str(self.data['merchant_id']))
        m.update(str(self.data['transaction_id']))
        m.update(get_secret_word_as_md5())
        m.update(str(self.data['mb_amount']))
        m.update(self.data['mb_currency'])
        m.update(str(self.data['status']))
        self.data['md5sig'] = m.hexdigest().upper()

    def setUp(self):
        self.payment_request = PaymentRequestFactory()
        self.data = {
            'pay_to_email': PAY_TO_EMAIL,
            'pay_from_email': 'someone@example.com',
            'merchant_id': 12345,
            'transaction_id': self.payment_request.pk,
            'mb_transaction_id': 12345,
            'mb_amount': self.payment_request.amount,
            'mb_currency': self.payment_request.currency,
            'status': 0,
            'amount': self.payment_request.amount,
            'currency': self.payment_request.currency,
        }
        self.generate_md5_signature()

    def test_pending(self):
        resp = self.client.post(reverse('skrill:status_report'), self.data)
        self.assertEqual(resp.status_code, 200)

