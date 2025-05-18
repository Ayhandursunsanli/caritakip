from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(RedirectView.as_view(pattern_name='satinalma:dashboard')), name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('satin-alma/', include('satinalma.urls', namespace='satinalma')),
    path('urunler/', include('urunler.urls', namespace='urunler')),
    path('faturalar/', include('faturalar.urls', namespace='faturalar')),
    path('departmanlar/', include('departmanlar.urls', namespace='departmanlar')),
    path('tedarikciler/', include('tedarikciler.urls', namespace='tedarikciler')),
    path('parametreler/', include('parametreler.urls', namespace='parametreler')),
]

# Development ortamında media dosyaları için
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 