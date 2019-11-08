from django.db import models
from decimal import Decimal
import datetime
from django.contrib.auth.models import User

class KualiEntry(models.Model):
    doc_id = models.CharField(max_length=256, blank=True, null=True)
    tracking_id = models.CharField(max_length=256, blank=True, null=True)
    fullname_kuali = models.CharField(max_length=256, blank=True, null=True)
    firstname_kuali = models.CharField(max_length=256, blank=True, null=True)
    lastname_kuali = models.CharField(max_length=256, blank=True, null=True)
    siss_account = models.CharField(max_length=256, blank=True, null=True)
    dept_account = models.CharField(max_length=256, blank=True, null=True)
    amount_kuali = models.DecimalField(max_digits=128, decimal_places=2, blank=True, null=True)
    date_kuali = models.DateField(blank=True, null=True)
    ref_id = models.IntegerField(blank=True, null=True)
    ref_sunapsis = models.OneToOneField('SunapsisEntry', on_delete=models.SET_NULL, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
class SunapsisEntry(models.Model):
    doc_id = models.CharField(max_length=256, blank=True, null=True)
    sunapsis_id = models.CharField(max_length=256, blank=True, null=True)
    fullname_sunapsis = models.CharField(max_length=256, blank=True, null=True)
    firstname_sunapsis = models.CharField(max_length=256, blank=True, null=True)
    lastname_sunapsis = models.CharField(max_length=256, blank=True, null=True)
    job_title_sunapsis = models.CharField(max_length=256, blank=True, null=True)
    position_id_sunapsis = models.IntegerField(blank=True, null=True)
    dept_name_sunapsis = models.CharField(max_length=256, blank=True, null=True)
    dept_contact_sunapsis = models.CharField(max_length=256, blank=True, null=True)
    visa_amount_sunapsis = models.CharField(max_length=256, blank=True, null=True)
    visa_sunapsis = models.CharField(max_length=256, blank=True, null=True)
    amount_sunapsis = models.DecimalField(max_digits=128, decimal_places=2, blank=True, null=True)
    date_sunapsis = models.DateField(blank=True, null=True)
    ref_id = models.IntegerField(blank=True, null=True)
    ref_kuali = models.OneToOneField('KualiEntry', on_delete=models.SET_NULL, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)