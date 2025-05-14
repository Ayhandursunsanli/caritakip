from django.urls import path
from . import views

app_name = 'urunler'

urlpatterns = [
    path('', views.urun_listesi, name='urun_listesi'),
    path('ekle/', views.urun_ekle, name='urun_ekle'),
    path('<int:pk>/', views.urun_detay, name='urun_detay'),
    path('<int:pk>/duzenle/', views.urun_duzenle, name='urun_duzenle'),
    path('<int:pk>/sil/', views.urun_sil, name='urun_sil'),
] 