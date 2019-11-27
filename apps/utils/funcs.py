from typing import *

from django.shortcuts import get_object_or_404

def posted_data(request, lst_key_opname):
    ''' extract posted data from request with error message as single string
        request, [('key_hit', 'username'), ('key_miss', 'birthdate'), 'another_key_miss'] ->
        ('missing birthdate, another_key_miss', {'key_hit': 'value_hit'})
    '''
    missings, data = [], {}
    for e in lst_key_opname:
        key, name = e if type(e) == tuple else (e, e)
        if not request.POST.get(key, ''):
            missings.append(name)
        else:
            data[key] = request.POST[key]
    return (f'missing {", ".join(missings)}' if missings else '', data)

def ip_of(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
    return ip    
    
def username_of(request):
    return request.user.username if request.user.is_authenticated else 'anonymous'
    
def referrer_of(request):
    return request.META.get('HTTP_REFERER', '')
    
def method_of(request):
    return request.method
    
def path_of(request):
    return request.path
    
def data_of(request):
    data = {
        'GET': dict(request.GET.copy()),
        'POST': dict(request.POST.copy())
    }
    return data
    
def post_captcha(secret, ip, g_recaptcha_response):
    import requests
    URL = 'https://www.google.com/recaptcha/api/siteverify'
    url = f'{URL}?secret={secret}&response={g_recaptcha_response}&remoteip={ip}'
    return requests.get(url).json()
