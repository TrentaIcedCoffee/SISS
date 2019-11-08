from utils.routes import *
from accounts.views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]