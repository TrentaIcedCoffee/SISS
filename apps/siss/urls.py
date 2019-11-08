from utils.routes import *
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingest/', include(('ingest.urls', 'ingest'), namespace='ingest')),
    path('match/', include(('match.urls', 'match'), namespace='match')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('files/', include(('files.urls', 'files'), namespace='files')),
    path('', include(('home.urls', 'home'), namespace='home')),
]