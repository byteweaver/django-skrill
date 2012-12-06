from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from views import StatusReportView


urlpatterns = patterns('',
    url('^status_report/$', csrf_exempt(StatusReportView.as_view()), name='status_report'),
    url('^cancel/$', TemplateView.as_view(template_name='skrill/cancel.html'), name='cancel'),
    url('^return/$', TemplateView.as_view(template_name='skrill/return.html'), name='return'),
)
