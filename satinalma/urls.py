from django.urls import path
from . import views

app_name = 'satinalma'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('satin-alma-listesi/', views.satin_alma_listesi, name='satin_alma_listesi'),
    path('satin-alma-ekle/', views.satin_alma_ekle, name='satin_alma_ekle'),
    path('satin-alma/<int:pk>/', views.satin_alma_detay, name='satin_alma_detay'),
    path('satin-alma/<int:pk>/duzenle/', views.satin_alma_duzenle, name='satin_alma_duzenle'),
    path('satin-alma/<int:pk>/sil/', views.satin_alma_sil, name='satin_alma_sil'),
] 