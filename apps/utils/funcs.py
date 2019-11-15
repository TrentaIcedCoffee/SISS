from django.shortcuts import get_object_or_404

posted_data = lambda request, keys: {key: request.POST.get(key, None) for key in keys}

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