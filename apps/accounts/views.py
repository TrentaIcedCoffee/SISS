from utils.routes import *
from utils.decorators import *
from utils.messages import *
from utils.funcs import *
from django.contrib.auth import authenticate, login as _login, logout as _logout

@allowed_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    if request.method == 'GET':
        return render(request, 'accounts/index.html')
    elif request.method == 'POST':
        data = posted_data(request, ['username', 'password'])
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            messages.error(request, 'invalid username/password')
            return redirect('accounts:login')
        _login(request, user)
        return redirect('home:index')

@allowed_methods(['GET'])
@login_required
def logout(request):
    _logout(request)
    messages.success(request, 'logout success')
    return redirect('accounts:login')