from utils.routes import *
from ingest import views

urlpatterns = [
    path('', views.index, name='index'),
]