from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from views import StatusReportView


urlpatterns = patterns('',
    url('^status_report/$', csrf_exempt(StatusReportView.as_view()), name='status_report'),
)
