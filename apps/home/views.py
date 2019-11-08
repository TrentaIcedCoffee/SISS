from utils.decorators import *
from utils.routes import *

@allowed_methods(['GET'])
def index(request):
    return redirect('match:index') if request.user.is_authenticated else redirect('accounts:login')