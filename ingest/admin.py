from django.contrib import admin
from ingest.models import KualiEntry, SunapsisEntry

admin.site.register(KualiEntry)
admin.site.register(SunapsisEntry)