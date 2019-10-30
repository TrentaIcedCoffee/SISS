from functools import wraps
from .res import *

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not args[0].user.is_authenticated:
            return forbidden()
        return f(*args, **kwargs)
    return wrapper
    
def allowed_methods(methods):
    def inner_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if args[0].method not in methods:
                return method_not_allowed()
            return f(*args, **kwargs)
        return wrapper
    return inner_function