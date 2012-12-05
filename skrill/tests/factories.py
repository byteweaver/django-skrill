from decimal import Decimal
import random

from django.contrib.auth.models import User

import factory

from skrill.models import PaymentRequest
from skrill.settings import ISO4217


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: "Test User %s" % n)


class PaymentRequestFactory(factory.Factory):
    FACTORY_FOR = PaymentRequest

    user = UserFactory()
    amount = Decimal(random.randrange(10000))/100
    currency = random.choice(ISO4217)[0]

