from decimal import Decimal
import hashlib
import random

from django.contrib.auth.models import User

import factory

from skrill.settings import get_secret_word_as_md5
from skrill.models import PaymentRequest, StatusReport
from skrill.settings import *


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: "Test User %s" % n)


class PaymentRequestFactory(factory.Factory):
    FACTORY_FOR = PaymentRequest

    user = UserFactory()
    amount = Decimal(random.randrange(10000))/100
    currency = random.choice(ISO4217)[0]


class StatusReportFactory(factory.Factory):
    FACTORY_FOR = StatusReport

    pay_to_email = PAY_TO_EMAIL
    pay_from_email = "someone@example.com"
    merchant_id = 12345
    payment_request = PaymentRequestFactory()
    mb_transaction_id = 12345
    mb_amount = payment_request.amount
    mb_currency = payment_request.currency
    status = 0
    md5sig = ''
    amount = payment_request.amount
    currency = payment_request.currency

    def _generate_md5_signature(self):
        m = hashlib.md5()
        m.update(str(self.merchant_id))
        m.update(str(self.transaction_id))
        m.update(get_secret_word_as_md5())
        m.update(str(self.mb_amount))
        m.update(self.mb_currency)
        m.update(str(self.status))
        self.md5sig = m.hexdigest().upper()

