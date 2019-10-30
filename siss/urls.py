"""siss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from utils.routes import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingest/', include(('ingest.urls', 'ingest'), namespace='ingest')),
    path('match/', include(('match.urls', 'match'), namespace='match')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('files/', include(('files.urls', 'files'), namespace='files')),
    path('', include(('home.urls', 'home'), namespace='home')),
]