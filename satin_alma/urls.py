from django.urls import path
from . import views

app_name = 'satin_alma'

urlpatterns = [
    path('', views.satin_alma_listesi, name='satin_alma_listesi'),
    path('ekle/', views.satin_alma_ekle, name='satin_alma_ekle'),
    path('<int:pk>/', views.satin_alma_detay, name='satin_alma_detay'),
    path('<int:pk>/duzenle/', views.satin_alma_duzenle, name='satin_alma_duzenle'),
    path('<int:pk>/sil/', views.satin_alma_sil, name='satin_alma_sil'),
] 