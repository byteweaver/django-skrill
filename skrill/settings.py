# -*- coding: utf-8 -*-
import hashlib

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.functional import lazy


def get_url(unicode):
    return "http://%s%s" % (Site.objects.get_current().domain, reverse(unicode))
get_url_lazy = lazy(get_url, unicode)

# settings that normaly need no change
API_URL = getattr(settings, "SKRILL_API_URL", "https://www.moneybookers.com/app/payment.pl")

# mandatory settings
PAY_TO_EMAIL = getattr(settings, "SKRILL_PAY_TO_EMAIL", None)
SECRET_WORD = getattr(settings, "SKRILL_SECRET_WORD", '')

def get_secret_word_as_md5():
    """returns md5 hash of SECRET_WORD in upper case"""
    m = hashlib.md5()
    m.update(SECRET_WORD)
    return m.hexdigest().upper()

# optional default settings
RECIPIENT_DESCRIPTION = getattr(settings, "SKRILL_RECIPIENT_DESCRIPTION", None)
RETURN_URL = getattr(settings, "SKRILL_RETURN_URL", get_url_lazy('skrill:return'))
RETURN_URL_TEXT = getattr(settings, "SKRILL_RETURN_URL_TEXT", None)
CANCEL_URL = getattr(settings, "SKRILL_CANCEL_URL", get_url_lazy('skrill:cancel'))
STATUS_URL = getattr(settings, "SKRILL_STATUS_URL", get_url_lazy('skrill:status_report'))
STATUS_URL2 = getattr(settings, "SKRILL_STATUS_URL2", None)
NEW_WINDOW_REDIRECT = getattr(settings, "SKRILL_NEW_WINDOW_REDIRECT", False)
LANGUAGE = getattr(settings, "SKRILL_LANGUAGE", settings.LANGUAGES[0][0].upper())
CONFIRMATION_NOTE = getattr(settings, "SKRILL_CONFIRMATION_NOTE", None)
LOGO_URL = getattr(settings, "SKRILL_LOGO_URL", None)
DEFAULT_URL_TARGET = getattr(settings, "SKRILL_DEFAULT_URL_TARGET", 1)
DEFAULT_CURRENCY = getattr(settings, "SKRILL_DEFAULT_CURRENCY", None)

URL_TARGET_CHOICES = (
    (1,"_top"),
    (2,"_parent"),
    (3,"_self"),
    (4,"_blank"),
)

LANGUAGE_CHOICES = (
    ('EN', "EN"),
    ('DE', "DE"),
    ('ES', "ES"),
    ('FR', "FR"),
    ('IT', "IT"),
    ('PL', "PL"),
    ('GR', "GR"),
    ('RO', "RO"),
    ('RU', "RU"),
    ('TR', "TR"),
    ('CN', "CN"),
    ('CZ', "CZ"),
    ('NL', "NL"),
    ('DA', "DA"),
    ('SV', "SV"),
    ('FI', "FI"),
)

TITLE_CHOICES = (
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
)

STATUS_CHOICES = (
    (-3, 'Chargeback'),
    (-2, 'Failed'),
    (-1, 'Cancelled'),
    (0, 'Pending'),
    (2, 'Processed'),
)

# Thanks to https://github.com/mikery/django-moneybookers for the following lists
ISO4217 = (
    ('EUR', 'Euro'),
    ('TWD', 'Taiwan Dollar'),
    ('USD', 'U.S. Dollar'),
    ('THB', 'Thailand Baht'),
    ('GBP', 'British Pound'),
    ('CZK', 'Czech Koruna'),
    ('HKD', 'Hong Kong Dollar'),
    ('HUF', 'Hungarian Forint'),
    ('SGD', 'Singapore Dollar'),
    ('SKK', 'Slovakian Koruna'),
    ('JPY', 'Japanese Yen'),
    ('EEK', 'Estonian Kroon'),
    ('CAD', 'Canadian Dollar'),
    ('BGN', 'Bulgarian Leva'),
    ('AUD', 'Australian Dollar'),
    ('PLN', 'Polish Zloty'),
    ('CHF', 'Swiss Franc'),
    ('ISK', 'Iceland Krona'),
    ('DKK', 'Danish Krone'),
    ('INR', 'Indian Rupee'),
    ('SEK', 'Swedish Krona'),
    ('LVL', 'Latvian Lat'),
    ('NOK', 'Norwegian Krone'),
    ('KRW', 'South-Korean Won'),
    ('ILS', 'Israeli Shekel'),
    ('ZAR', 'South-African Rand'),
    ('MYR', 'Malaysian Ringgit'),
    ('RON', 'Romanian Leu New'),
    ('NZD', 'New Zealand Dollar'),
    ('HRK', 'Croatian Kuna'),
    ('TRY', 'New Turkish Lira'),
    ('LTL', 'Lithuanian Litas'),
    ('AED', 'Utd. Arab Emir. Dirham'),
    ('JOD', 'Jordanian Dinar'),
    ('MAD', 'Moroccan Dirham'),
    ('OMR', 'Omani Rial'),
    ('QAR', 'Qatari Rial'),
    ('RSD', 'Serbian dinar'),
    ('SAR', 'Saudi Riyal'),
    ('TND', 'Tunisian Dinar'),
)

GATEWAY_PAYMENT_CODES = (
    ('', 'Moneybookers Wallet'), # ALL
    ('ACC', 'All Card Types'), # ALL
    ('VSA', 'Visa'), # ALL
    ('MSC', 'MasterCard'), # ALL
    ('VSD', 'Visa Delta/Debit'), # United Kingdom
    ('VSE', 'Visa Electron'), # ALL
    ('MAE', 'Maestro'), # United Kingdom, Spain & Austria
    ('SLO', 'Solo'), # United Kingdom
    ('AMX', 'American Express'), # ALL
    ('DIN', 'Diners'), # ALL
    ('JCB', 'JCB'), # ALL
    ('LSR', 'Laser'), # Rep. of Ireland
    ('GCB', 'Carte Bleue'), # France
    ('DNK', 'Dankort'), # Denmark
    ('PSP', 'PostePay'), # Italy
    ('CSI', 'CartaSi'), # Italy
    ('OBT', 'Online Bank Transfer'), # Germany, United Kingdom, Denmark, Finland, Sweden, Poland, Estonia, Latvia, Lithuania
    ('GIR', 'Giropay'), # Germany
    ('DID', 'Direct Debit / ELV'), # Germany
    ('SFT', 'Sofortueberweisung'), # Germany, Austria, Belgium, Netherlands, Switzerland & United Kingdom
    ('ENT', 'eNETS'), # Singapore
    ('EBT', 'Nordea Solo'), # Sweden
    ('SO2', 'Nordea Solo'), # Finland
    ('IDL', 'iDEAL'), # Netherlands
    ('NPY', 'EPS (Netpay)'), # Austria
    ('PLI', 'POLi'), # Australia
    ('PWY', 'All Polish Banks'), # Poland
    ('PWY5', 'ING Bank Śląski'), # Poland
    ('PWY6', 'PKO BP (PKO Inteligo)'), # Poland
    ('PWY7', 'Multibank (Multitransfer)'), # Poland
    ('PWY14', 'Lukas Bank'), # Poland
    ('PWY15', 'Bank BPH'), # Poland
    ('PWY17', 'InvestBank'), # Poland
    ('PWY18', 'PeKaO S.A.'), # Poland
    ('PWY19', 'Citibank handlowy'), # Poland
    ('PWY20', 'Bank Zachodni WBK (Przelew24)'), # Poland
    ('PWY21', 'BGŻ'), # Poland
    ('PWY22', 'Millenium'), # Poland
    ('PWY25', 'mBank (mTransfer)'), # Poland
    ('PWY26', 'Płacę z Inteligo'), # Poland
    ('PWY28', 'Bank Ochrony Środowiska'), # Poland
    ('PWY32', 'Nordea'), # Poland
    ('PWY33', 'Fortis Bank'), # Poland
    ('PWY36', 'Deutsche Bank PBC S.A.'), # Poland
    ('EPY', 'ePay.bg'), # Bulgaria
)

ISO3166_A3 = (
    ('AFG', 'Afghanistan'),
    ('ALA', 'Åland Islands'),
    ('ALB', 'Albania'),
    ('DZA', 'Algeria'),
    ('ASM', 'American Samoa'),
    ('AND', 'Andorra'),
    ('AGO', 'Angola'),
    ('AIA', 'Anguilla'),
    ('ATA', 'Antarctica'),
    ('ATG', 'Antigua and Barbuda'),
    ('ARG', 'Argentina'),
    ('ARM', 'Armenia'),
    ('ABW', 'Aruba'),
    ('AUS', 'Australia'),
    ('AUT', 'Austria'),
    ('AZE', 'Azerbaijan'),
    ('BHS', 'Bahamas, The'),
    ('BHR', 'Bahrain'),
    ('BGD', 'Bangladesh'),
    ('BRB', 'Barbados'),
    ('BLR', 'Belarus'),
    ('BEL', 'Belgium'),
    ('BLZ', 'Belize'),
    ('BEN', 'Benin'),
    ('BMU', 'Bermuda'),
    ('BTN', 'Bhutan'),
    ('BOL', 'Bolivia'),
    ('BIH', 'Bosnia and Herzegovina'),
    ('BWA', 'Botswana'),
    ('BVT', 'Bouvet Island'),
    ('BRA', 'Brazil'),
    ('IOT', 'British Indian Ocean Territory'),
    ('VGB', 'British Virgin Islands'),
    ('BRN', 'Brunei'),
    ('BGR', 'Bulgaria'),
    ('BFA', 'Burkina Faso'),
    ('MMR', 'Burma'),
    ('BDI', 'Burundi'),
    ('KHM', 'Cambodia'),
    ('CMR', 'Cameroon'),
    ('CAN', 'Canada'),
    ('CPV', 'Cape Verde'),
    ('CYM', 'Cayman Islands'),
    ('CAF', 'Central African Republic'),
    ('TCD', 'Chad'),
    ('CHL', 'Chile'),
    ('CHN', 'China'),
    ('CXR', 'Christmas Island'),
    ('CCK', 'Cocos (Keeling) Islands'),
    ('COL', 'Colombia'),
    ('COM', 'Comoros'),
    ('COD', 'Congo, Democratic Republic of the'),
    ('COG', 'Congo, Republic of the'),
    ('COK', 'Cook Islands'),
    ('CRI', 'Costa Rica'),
    ('CIV', "Cote d'Ivoire"),
    ('HRV', 'Croatia'),
    ('CUB', 'Cuba'),
    ('CYP', 'Cyprus'),
    ('CZE', 'Czech Republic'),
    ('DNK', 'Denmark'),
    ('DJI', 'Djibouti'),
    ('DMA', 'Dominica'),
    ('DOM', 'Dominican Republic'),
    ('ECU', 'Ecuador'),
    ('EGY', 'Egypt'),
    ('SLV', 'El Salvador'),
    ('GNQ', 'Equatorial Guinea'),
    ('ERI', 'Eritrea'),
    ('EST', 'Estonia'),
    ('ETH', 'Ethiopia'),
    ('FLK', 'Falkland Islands (Islas Malvinas)'),
    ('FRO', 'Faroe Islands'),
    ('FJI', 'Fiji'),
    ('FIN', 'Finland'),
    ('FRA', 'France'),
    ('GUF', 'French Guiana'),
    ('PYF', 'French Polynesia'),
    ('ATF', 'French Southern and Antarctic Lands'),
    ('GAB', 'Gabon'),
    ('GMB', 'Gambia, The'),
    ('PSE', 'Gaza Strip'),
    ('GEO', 'Georgia'),
    ('DEU', 'Germany'),
    ('GHA', 'Ghana'),
    ('GIB', 'Gibraltar'),
    ('GRC', 'Greece'),
    ('GRL', 'Greenland'),
    ('GRD', 'Grenada'),
    ('GLP', 'Guadeloupe'),
    ('GUM', 'Guam'),
    ('GTM', 'Guatemala'),
    ('GGY', 'Guernsey'),
    ('GIN', 'Guinea'),
    ('GNB', 'GuineaBissau'),
    ('GUY', 'Guyana'),
    ('HTI', 'Haiti'),
    ('HMD', 'Heard Island and McDonald Islands'),
    ('VAT', 'Holy See (Vatican City)'),
    ('HND', 'Honduras'),
    ('HKG', 'Hong Kong'),
    ('HUN', 'Hungary'),
    ('ISL', 'Iceland'),
    ('IND', 'India'),
    ('IDN', 'Indonesia'),
    ('IRN', 'Iran'),
    ('IRQ', 'Iraq'),
    ('IRL', 'Ireland'),
    ('IMN', 'Isle of Man'),
    ('ISR', 'Israel'),
    ('ITA', 'Italy'),
    ('JAM', 'Jamaica'),
    ('JPN', 'Japan'),
    ('JEY', 'Jersey'),
    ('JOR', 'Jordan'),
    ('KAZ', 'Kazakhstan'),
    ('KEN', 'Kenya'),
    ('KIR', 'Kiribati'),
    ('PRK', 'Korea, North'),
    ('KOR', 'Korea, South'),
    ('KWT', 'Kuwait'),
    ('KGZ', 'Kyrgyzstan'),
    ('LAO', 'Laos'),
    ('LVA', 'Latvia'),
    ('LBN', 'Lebanon'),
    ('LSO', 'Lesotho'),
    ('LBR', 'Liberia'),
    ('LBY', 'Libya'),
    ('LIE', 'Liechtenstein'),
    ('LTU', 'Lithuania'),
    ('LUX', 'Luxembourg'),
    ('MAC', 'Macau'),
    ('MKD', 'Macedonia'),
    ('MDG', 'Madagascar'),
    ('MWI', 'Malawi'),
    ('MYS', 'Malaysia'),
    ('MDV', 'Maldives'),
    ('MLI', 'Mali'),
    ('MLT', 'Malta'),
    ('MHL', 'Marshall Islands'),
    ('MTQ', 'Martinique'),
    ('MRT', 'Mauritania'),
    ('MUS', 'Mauritius'),
    ('MYT', 'Mayotte'),
    ('MEX', 'Mexico'),
    ('FSM', 'Micronesia, Federated States of'),
    ('MDA', 'Moldova'),
    ('MCO', 'Monaco'),
    ('MNG', 'Mongolia'),
    ('MNE', 'Montenegro'),
    ('MSR', 'Montserrat'),
    ('MAR', 'Morocco'),
    ('MOZ', 'Mozambique'),
    ('NAM', 'Namibia'),
    ('NRU', 'Nauru'),
    ('NPL', 'Nepal'),
    ('NLD', 'Netherlands'),
    ('ANT', 'Netherlands Antilles'),
    ('NCL', 'New Caledonia'),
    ('NZL', 'New Zealand'),
    ('NIC', 'Nicaragua'),
    ('NER', 'Niger'),
    ('NGA', 'Nigeria'),
    ('NIU', 'Niue'),
    ('NFK', 'Norfolk Island'),
    ('MNP', 'Northern Mariana Islands'),
    ('NOR', 'Norway'),
    ('OMN', 'Oman'),
    ('PAK', 'Pakistan'),
    ('PLW', 'Palau'),
    ('PAN', 'Panama'),
    ('PNG', 'Papua New Guinea'),
    ('PRY', 'Paraguay'),
    ('PER', 'Peru'),
    ('PHL', 'Philippines'),
    ('PCN', 'Pitcairn Islands'),
    ('POL', 'Poland'),
    ('PRT', 'Portugal'),
    ('PRI', 'Puerto Rico'),
    ('QAT', 'Qatar'),
    ('REU', 'Reunion'),
    ('ROU', 'Romania'),
    ('RUS', 'Russia'),
    ('RWA', 'Rwanda'),
    ('BLM', 'Saint Barthelemy'),
    ('SHN', 'Saint Helena'),
    ('KNA', 'Saint Kitts and Nevis'),
    ('LCA', 'Saint Lucia'),
    ('MAF', 'Saint Martin'),
    ('SPM', 'Saint Pierre and Miquelon'),
    ('VCT', 'Saint Vincent and the Grenadines'),
    ('WSM', 'Samoa'),
    ('SMR', 'San Marino'),
    ('STP', 'Sao Tome and Principe'),
    ('SAU', 'Saudi Arabia'),
    ('SEN', 'Senegal'),
    ('SRB', 'Serbia'),
    ('SYC', 'Seychelles'),
    ('SLE', 'Sierra Leone'),
    ('SGP', 'Singapore'),
    ('SVK', 'Slovakia'),
    ('SVN', 'Slovenia'),
    ('SLB', 'Solomon Islands'),
    ('SOM', 'Somalia'),
    ('ZAF', 'South Africa'),
    ('SGS', 'South Georgia and the South Sandwich Islands'),
    ('ESP', 'Spain'),
    ('LKA', 'Sri Lanka'),
    ('SDN', 'Sudan'),
    ('SUR', 'Suriname'),
    ('SJM', 'Svalbard'),
    ('SWZ', 'Swaziland'),
    ('SWE', 'Sweden'),
    ('CHE', 'Switzerland'),
    ('SYR', 'Syria'),
    ('TWN', 'Taiwan'),
    ('TJK', 'Tajikistan'),
    ('TZA', 'Tanzania'),
    ('THA', 'Thailand'),
    ('TLS', 'TimorLeste'),
    ('TGO', 'Togo'),
    ('TKL', 'Tokelau'),
    ('TON', 'Tonga'),
    ('TTO', 'Trinidad and Tobago'),
    ('TUN', 'Tunisia'),
    ('TUR', 'Turkey'),
    ('TKM', 'Turkmenistan'),
    ('TCA', 'Turks and Caicos Islands'),
    ('TUV', 'Tuvalu'),
    ('UGA', 'Uganda'),
    ('UKR', 'Ukraine'),
    ('ARE', 'United Arab Emirates'),
    ('GBR', 'United Kingdom'),
    ('USA', 'United States'),
    ('UMI', 'United States Minor Outlying Islands'),
    ('URY', 'Uruguay'),
    ('UZB', 'Uzbekistan'),
    ('VUT', 'Vanuatu'),
    ('VEN', 'Venezuela'),
    ('VNM', 'Vietnam'),
    ('VIR', 'Virgin Islands'),
    ('WLF', 'Wallis and Futuna'),
    ('PSE', 'West Bank'),
    ('ESH', 'Western Sahara'),
    ('YEM', 'Yemen'),
    ('ZMB', 'Zambia'),
    ('ZWE', 'Zimbabwe'),
)

FAILED_REASON_CODES = (
    ('01', '01 - Referred'),
    ('02', '02 - Invalid Merchant Number'),
    ('03', '03 - Pick-up card'),
    ('04', '04 - Authorisation Declined'),
    ('05', '05 - Other Error'),
    ('06', '06 - CVV is mandatory, but not set or invalid'),
    ('07', '07 - Approved authorisation, honour with identification'),
    ('08', '08 - Delayed Processing'),
    ('09', '09 - Invalid Transaction'),
    ('10', '10 - Invalid Currency'),
    ('11', '11 - Invalid Amount/Available Limit Exceeded/Amount too high'),
    ('12', '12 - Invalid credit card or bank account'),
    ('13', '13 - Invalid Card Issuer'),
    ('14', '14 - Annulation by client'),
    ('15', '15 - Duplicate transaction'),
    ('16', '16 - Acquirer Error'),
    ('17', '17 - Reversal not processed, matching authorisation not found'),
    ('18', '18 - File Transfer not available/unsuccessful'),
    ('19', '19 - Reference number error'),
    ('20', '20 - Access Denied'),
    ('21', '21 - File Transfer failed'),
    ('22', '22 - Format Error'),
    ('23', '23 - Unknown Acquirer'),
    ('24', '24 - Card expired'),
    ('25', '25 - Fraud Suspicion'),
    ('26', '26 - Security code expired'),
    ('27', '27 - Requested function not available'),
    ('28', '28 - Lost/Stolen card'),
    ('29', '29 - Stolen card, Pick up'),
    ('30', '30 - Duplicate Authorisation'),
    ('31', '31 - Limit Exceeded'),
    ('32', '32 - Invalid Security Code'),
    ('33', '33 - Unknown or Invalid Card/Bank account'),
    ('34', '34 - Illegal Transaction'),
    ('35', '35 - Transaction Not Permitted'),
    ('36', '36 - Card blocked in local blacklist'),
    ('37', '37 - Restricted card/bank account'),
    ('38', '38 - Security Rules Violation'),
    ('39', '39 - The transaction amount of the referencing transaction is higher than the transaction amount of the original transaction'),
    ('40', '40 - Transaction frequency limit exceeded, override is possible'),
    ('41', '41 - Incorrect usage count in the Authorisation System exceeded'),
    ('42', '42 - Card blocked'),
    ('43', '43 - Rejected by Credit Card Issuer'),
    ('44', '44 - Card Issuing Bank or Network is not available'),
    ('45', '45 - The card type is not processed by the authorisation centre / Authorisation System has determined incorrect Routing'),
    ('47', '47 - Processing temporarily not possible'),
    ('48', '48 - Security Breach'),
    ('49', '49 - Date / time not plausible, trace-no. not increasing'),
    ('50', '50 - Error in PAC encryption detected'),
    ('51', '51 - System Error'),
    ('52', '52 - MB Denied - potential fraud'),
    ('53', '53 - Mobile verification failed'),
    ('54', '54 - Failed due to internal security restrictions'),
    ('55', '55 - Communication or verification problem'),
    ('56', '56 - 3D verification failed'),
    ('57', '57 - AVS check failed'),
    ('58', '58 - Invalid bank code'),
    ('59', '59 - Invalid account code'),
    ('60', '60 - Card not authorised'),
    ('61', '61 - No credit worthiness'),
    ('62', '62 - Communication error'),
    ('63', '63 - Transaction not allowed for cardholder'),
    ('64', '64 - Invalid Data in Request'),
    ('65', '65 - Blocked bank code'),
    ('66', '66 - CVV2/CVC2 Failure'),
    ('99', '99 - General error'),
)

