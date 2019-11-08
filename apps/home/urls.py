from utils.routes import *
from home.views import *

urlpatterns = [
    path('', index, name='index'),
]