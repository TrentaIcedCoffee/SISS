from utils.routes import *
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingest/', include(('ingest.urls', 'ingest'), namespace='ingest')),
    path('match/', include(('match.urls', 'match'), namespace='match')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('', include(('home.urls', 'home'), namespace='home')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.FILES_URL, document_root=settings.FILES_ROOT)