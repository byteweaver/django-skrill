from django.contrib import admin

from skrill.models import Request, StatusReport


admin.site.register(Request)
admin.site.register(StatusReport)

