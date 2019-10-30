from django import forms
from ingest.models import *

def unpack_visa_amount_sunapsis(s):
    ''' J-1 Initial (490.00) -> Tuple['J-1 Initial', 490.0] '''
    if not s:
        return '', ''
    s = s.strip()
    is_digit, start = True, len(s)-1
    while start >= 0 and (s[start].isdigit() or s[start] in set('().')):
        start -= 1
    digit_start, digit_end = start+1, len(s)-1
    if digit_start < len(s) and s[digit_start] == '(':
        digit_start += 1
    if digit_end >= 0 and s[digit_end] == ')':
        digit_end -= 1
    return s[:start+1].strip(), s[digit_start:digit_end+1]

class KualiForm(forms.ModelForm):
    date_kuali = forms.DateField(required=False, input_formats=['%Y-%m-%d'])
    class Meta:
        model = KualiEntry
        fields = (
            'doc_id,tracking_id,fullname_kuali,firstname_kuali,lastname_kuali,'
            'siss_account,dept_account,amount_kuali,ref_id'
        ).split(',')
        
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['fullname_kuali'] and \
           not cleaned_data['firstname_kuali'] and not cleaned_data['lastname_kuali']:
            lst = cleaned_data['fullname_kuali'].split(' ')
            if len(lst) == 2:
                cleaned_data['firstname_kuali'] = lst[0]
                cleaned_data['lastname_kuali'] = lst[-1]
        if not cleaned_data['fullname_kuali'] and \
           cleaned_data['firstname_kuali'] and cleaned_data['lastname_kuali']:
            cleaned_data['fullname_kuali'] = (
                f'{cleaned_data["firstname_kuali"]} '
                f'{cleaned_data["lastname_kuali"]}'
            )
            
    def save(self, commit=True):
        ins = super().save(commit=False)
        ins.date_kuali = self.cleaned_data['date_kuali']
        if commit:
            ins.save()
        return ins
        
class SunapsisForm(forms.ModelForm):
    date_sunapsis = forms.DateField(required=False, input_formats=['%Y-%m-%d'])
    class Meta:
        model = SunapsisEntry
        fields = (
            'doc_id,sunapsis_id,fullname_sunapsis,firstname_sunapsis,'
            'lastname_sunapsis,job_title_sunapsis,position_id_sunapsis,'
            'dept_name_sunapsis,dept_contact_sunapsis,visa_amount_sunapsis,'
            'visa_sunapsis,amount_sunapsis,ref_id'    
        ).split(',')
        
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['fullname_sunapsis'] and \
           not cleaned_data['firstname_sunapsis'] and not cleaned_data['lastname_sunapsis']:
            lst = cleaned_data['fullname_sunapsis'].split(' ')
            if len(lst) == 2:
                cleaned_data['firstname_sunapsis'] = lst[0]
                cleaned_data['lastname_sunapsis'] = lst[-1]
        if not cleaned_data['fullname_sunapsis'] and \
           cleaned_data['firstname_sunapsis'] and cleaned_data['lastname_sunapsis']:
            cleaned_data['fullname_sunapsis'] = (
                f'{cleaned_data["firstname_sunapsis"]} '
                f'{cleaned_data["lastname_sunapsis"]}'
            )
        if cleaned_data['visa_amount_sunapsis'] and \
           not cleaned_data['visa_sunapsis'] and not cleaned_data['amount_sunapsis']:
            cleaned_data['visa_sunapsis'], cleaned_data['amount_sunapsis'] = \
                unpack_visa_amount_sunapsis(cleaned_data['visa_amount_sunapsis'])
        
    def save(self, commit=True):
        ins = super().save(commit=False)
        ins.date_sunapsis = self.cleaned_data['date_sunapsis']
        if commit:
            ins.save()
        return ins