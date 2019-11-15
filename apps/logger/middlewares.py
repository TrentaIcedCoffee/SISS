from utils.funcs import *
from django.utils import timezone
from .models import Log

def logger_middleware(get_response):
    
    def middleware(request):
        log_data = {
            'ip': ip_of(request),
            'referrer': referrer_of(request),
            'username': username_of(request),
            'method': method_of(request),
            'path': path_of(request),
            'data': data_of(request)
        }
        
        response = get_response(request)
        
        log_data.update({
            'response_status': response.status_code,
            'timestamp': timezone.now()
        })
        
        Log(**log_data).save()
        
        return response
        
    return middleware