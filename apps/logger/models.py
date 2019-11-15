from django.utils import timezone

from django.db import models

TO_TZ = timezone.get_default_timezone()

class Log(models.Model):
    ip = models.CharField(max_length=128, blank=False, null=False)
    referrer = models.CharField(max_length=512, blank=True, null=False)
    username = models.CharField(max_length=256, blank=True, null=False)
    method = models.CharField(max_length=16, blank=False, null=False)
    path = models.CharField(max_length=128, blank=False, null=False)
    data = models.TextField(blank=True, null=False)
    response_status = models.IntegerField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    highlight = models.CharField(max_length=128, unique=False, blank=False, null=False)

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.highlight = f'{self.timestamp.astimezone(TO_TZ).strftime("%Y-%m-%d %H:%M")},{self.ip},{self.username},{self.method},{self.path},{self.response_status}'

    def __str__(self):
    	return str(self.highlight)