from django.test import TestCase

from skrill.models import StatusReport
from skrill.tests.factories import StatusReportFactory, generate_md5_signature


class StatusReportTestCase(TestCase):
    def test_valid_md5_signature(self):
        status_report = StatusReportFactory()
        status_report.md5sig = generate_md5_signature(status_report)
        status_report.validate_md5sig()

    def test_invalid_md5_signature(self):
        status_report = StatusReportFactory()
        status_report.md5sig = "foobar"
        try:
            status_report.validate_md5sig()
        except StatusReport.InvalidMD5Signature, e:
            str(e)
        else:
            raise Exception("test_invalid_md5_signature failed")
