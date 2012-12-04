from django.contrib.auth.models import User
from django.db import models

from skrill.settings import *


class Request(models.Model):
    # custom stuff
    user = models.ForeignKey(User, verbose_name="User")
    time = models.DateTimeField("Time", auto_now_add=True)
    is_test = models.BooleanField("Is test", default=False,
        help_text="If set to True, the request will be send to TEST_API_URL.")

    # merchant details
    transaction_id = models.AutoField("Transaction ID", primary_key=True,
        help_text="Reference or identification number provided by the Merchant. MUST be unique for each payment")
    pay_to_email = models.EmailField("Merchant Email", max_length=50, default=PAY_TO_EMAIL,
        help_text="Email address of the Merchant's moneybookers.com account.")
    recipient_description = models.CharField("Merchant description", max_length=30, blank=True, null=True, default=RECIPIENT_DESCRIPTION,
        help_text="A description of the Merchant, which will be shown on the gateway. If no value is submitted, the pay_to_email value will be shown as the recipient of the payment.")
    return_url = models.URLField("Return URL", max_length=240, blank=True, null=True, default=RETURN_URL,
        help_text="URL to which the customer will be returned when the payment is made. If this field is not filled, the gateway window will simply close automatically at the end of the transaction, so that the customer will be returned to the last page on the Merchant's website where he has been before.")
    return_url_text = models.CharField("Return URL text", max_length=35, blank=True, null=True, default=RETURN_URL_TEXT,
        help_text="The text on the button when the user finishes his payment.")
    return_url_target = models.SmallIntegerField("Return URL target", choices=URL_TARGET_CHOICES, default=DEFAULT_URL_TARGET,
        help_text="Specifies a target in which the return_url value will be called upon successful payment from customer.")
    cancel_url = models.URLField("Cancel URL", max_length=240, blank=True, null=True, default=CANCEL_URL,
        help_text="RL to which the customer will be returned if the payment process is cancelled. If this field is not filled, the gateway window will simply close automatically upon clicking the cancellation button, so the customer will be returned to the last page on the Merchant's website where the customer has been before.")
    cancel_url_target = models.SmallIntegerField("Cancel URL target", choices=URL_TARGET_CHOICES, default=DEFAULT_URL_TARGET,
        help_text="Specifies a target in which the cancel_url value will be called upon cancellation of payment from customer.")
    status_url = models.CharField("Status URL", max_length=255, blank=True, null=True, default=STATUS_URL,
        help_text="URL to which the transaction details will be posted after the payment process is complete. Alternatively, you may specify an email address to which you would like to receive the results.")
    status_url2 = models.CharField("Status URL 2", max_length=255, blank=True, null=True, default=STATUS_URL2,
        help_text="Second URL to which the transaction details will be posted after the payment process is complete. Alternatively, you may specify an email address to which you would like to receive the results.")
    new_window_redirect = models.BooleanField("New window redirect", default=NEW_WINDOW_REDIRECT,
        help_text="Merchants can choose to redirect customers to the Sofortueberweisung payment method in a new window instead of in the same window.")
    language = models.CharField("Language", max_length=2, choices=LANGUAGE_CHOICES, default=LANGUAGE,
        help_text="2-letter code of the language used for Skrill (Moneybookers)' pages.")
    hide_login = models.BooleanField("Hide login", default=False,
        help_text="Merchants can show their customers the gateway page without the prominent login section.")
    confirmation_note = models.CharField("Confirmation note", max_length=240, blank=True, null=True, default=CONFIRMATION_NOTE,
        help_text="Merchant may show to the customer on the confirmation screen - the end step of the process - a note, confirmation number, PIN or any other message. Line breaks <br> may be used for longer messages.")
    logo_url = models.URLField("Logo URL", max_length=240, blank=True, null=True, default=LOGO_URL,
        help_text="The URL of the logo which you would like to appear at the top of the gateway. The logo must be accessible via HTTPS otherwise it will not be shown. For best integration results we recommend that Merchants use logos with dimensions up to 200px in width and 50px in height.")
    prepare_only = models.BooleanField("Prepare only", default=True,
        help_text="Forces only SID to be returned without actual page. Useful when using alternative ways to redirect the customer to the gateway.")
    rid = models.CharField("Referral ID", max_length=100, blank=True, null=True,
        help_text="Merchants can pass the unique referral ID or email of the affiliate from which the customer is referred. The rid value must be included within the actual payment request.")
    ext_ref_id = models.CharField("Extra Referral ID", max_length=100, blank=True, null=True,
        help_text="Merchants can pass additional identifier in this field in order to track affiliates. You MUST inform your account manager about the exact value that will be submitted so that affiliates can be tracked.")
    custom_field_1 = models.CharField("Extra field 1", max_length=240, blank=True, null=True,
        help_text="One of 5 custom fields, see \"merchant_fields\" in the Skrill documentation")
    custom_field_2 = models.CharField("Extra field 2", max_length=240, blank=True, null=True,
        help_text="One of 5 custom fields, see \"merchant_fields\" in the Skrill documentation")
    custom_field_3 = models.CharField("Extra field 3", max_length=240, blank=True, null=True,
        help_text="One of 5 custom fields, see \"merchant_fields\" in the Skrill documentation")
    custom_field_4 = models.CharField("Extra field 4", max_length=240, blank=True, null=True,
        help_text="One of 5 custom fields, see \"merchant_fields\" in the Skrill documentation")
    custom_field_5 = models.CharField("Extra field 5", max_length=240, blank=True, null=True,
        help_text="One of 5 custom fields, see \"merchant_fields\" in the Skrill documentation")

    # customer details
    pay_from_email = models.EmailField("Pay from Email", max_length=100, blank=True, null=True,
        help_text="Email address of the customer who is making the payment. If left empty, the customer has to enter his email address himself.")
    title = models.CharField("Title", max_length=3, choices=TITLE_CHOICES, blank=True, null=True,
        help_text="Customer's title.")
    firstname = models.CharField("First name", max_length=20, blank=True, null=True,
        help_text="Customer's first name.")
    lastname = models.CharField("Last name", max_length=50, blank=True, null=True,
        help_text="Customer's last name.")
    date_of_birth = models.DateField("Date of birth", blank=True, null=True,
        help_text="Date of birth of the customer.")
    address = models.CharField("Address", max_length=100, blank=True, null=True,
        help_text="Customer's address.")
    address2 = models.CharField("Address2", max_length=100, blank=True, null=True,
        help_text="Customer's address.")
    phone_number = models.PositiveIntegerField("Phone number", max_length=20, blank=True, null=True,
        help_text="Customer's phone number. Only numeric values are accepted.")
    postal_code = models.CharField("Postal code", max_length=9, blank=True, null=True,
        help_text="Customer's postal code/ZIP Code. Only alphanumeric values are accepted (no punctuation marks etc.)")
    city = models.CharField("City", max_length=50, blank=True, null=True,
        help_text="Customer's city.")
    state = models.CharField("State", max_length=50, blank=True, null=True,
        help_text="Customer's state or region.")
    country = models.CharField("Country", max_length=3, choices=ISO3166_A3, blank=True, null=True,
        help_text="Customer's country in the 3-digit ISO Code.")

    # payment details
    amount = models.DecimalField("Amount", max_digits=18, decimal_places=2,
        help_text="The total amount payable.")
    currency = models.CharField("Currency", max_length=3, choices=ISO4217,
        help_text="3-letter code of the currency of the amount according to ISO 4217")
    amount2_description = models.CharField("Amount 2 description", max_length=240, blank=True, null=True,
        help_text="Merchant may specify a detailed calculation for the total amount payable. Please note that Skrill (Moneybookers) does not check the validity of these data - they are only displayed in the 'More information' section in the header of the gateway.")
    amount2 = models.DecimalField("Amount 2", max_digits=18, decimal_places=2, blank=True, null=True,
        help_text="This amount in the currency defined in field 'currency' will be shown next to amount2_description.")
    amount3_description = models.CharField("Amount 3 description", max_length=240, blank=True, null=True,
        help_text="Merchant may specify a detailed calculation for the total amount payable. Please note that Skrill (Moneybookers) does not check the validity of these data - they are only displayed in the 'More information' section in the header of the gateway.")
    amount3 = models.DecimalField("Amount 3", max_digits=18, decimal_places=2, blank=True, null=True,
        help_text="This amount in the currency defined in field 'currency' will be shown next to amount3_description.")
    amount4_description = models.CharField("Amount 4 description", max_length=240, blank=True, null=True,
        help_text="Merchant may specify a detailed calculation for the total amount payable. Please note that Skrill (Moneybookers) does not check the validity of these data - they are only displayed in the 'More information' section in the header of the gateway.")
    amount4 = models.DecimalField("Amount 4", max_digits=18, decimal_places=2, blank=True, null=True,
        help_text="This amount in the currency defined in field 'currency' will be shown next to amount4_description.")
    detail1_description = models.CharField("Detail 1 description", max_length=240, blank=True, null=True,
        help_text="Merchant may show up to 5 details about the product or transfer in the 'More information' section in the header of the gateway.")
    detail1_text = models.CharField("Detail 1 text", max_length=240, blank=True, null=True,
        help_text="The detail1_text is shown next to the detail1_description. The detail1_text is also shown to the client in his history at Skrill (Moneybookers)' website.")
    detail2_description = models.CharField("Detail 2 description", max_length=240, blank=True, null=True,
        help_text="Merchant may show up to 5 details about the product or transfer in the 'More information' section in the header of the gateway.")
    detail2_text = models.CharField("Detail 2 text", max_length=240, blank=True, null=True,
        help_text="The detail2_text is shown next to the detail2_description. The detail1_text is also shown to the client in his history at Skrill (Moneybookers)' website.")
    detail3_description = models.CharField("Detail 3 description", max_length=240, blank=True, null=True,
        help_text="Merchant may show up to 5 details about the product or transfer in the 'More information' section in the header of the gateway.")
    detail3_text = models.CharField("Detail 3 text", max_length=240, blank=True, null=True,
        help_text="The detail3_text is shown next to the detail3_description. The detail3_text is also shown to the client in his history at Skrill (Moneybookers)' website.")
    detail4_description = models.CharField("Detail 4 description", max_length=240, blank=True, null=True,
        help_text="Merchant may show up to 5 details about the product or transfer in the 'More information' section in the header of the gateway.")
    detail4_text = models.CharField("Detail 4 text", max_length=240, blank=True, null=True,
        help_text="The detail4_text is shown next to the detail4_description. The detail4_text is also shown to the client in his history at Skrill (Moneybookers)' website.")
    detail5_description = models.CharField("Detail 5 description", max_length=240, blank=True, null=True,
        help_text="Merchant may show up to 5 details about the product or transfer in the 'More information' section in the header of the gateway.")
    detail5_text = models.CharField("Detail 5 text", max_length=240, blank=True, null=True,
        help_text="The detail5_text is shown next to the detail5_description. The detail5_text is also shown to the client in his history at Skrill (Moneybookers)' website.")
