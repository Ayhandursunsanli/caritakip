"""
URL configuration for satinalma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from satin_alma.views import dashboard, satin_alma_listesi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', satin_alma_listesi, name='satin_alma_listesi'),  # Ana sayfa
    path('satinalma/', include('satin_alma.urls')),
    path('tedarikciler/', include('tedarikciler.urls')),
    path('urunler/', include('urunler.urls')),
    path('departmanlar/', include('departmanlar.urls')),
    path('faturalar/', include('faturalar.urls')),
    path('parametreler/', include('parametreler.urls')),
    path('dashboard/', dashboard, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
