from functools import wraps
from .errors import method_not_allowed

from django.contrib.auth.decorators import login_required

def allowed_methods(methods):
    def inner_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if args[0].method not in methods:
                return method_not_allowed()
            return f(*args, **kwargs)
        return wrapper
    return inner_function
