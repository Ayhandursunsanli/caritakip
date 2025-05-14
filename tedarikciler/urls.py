from django.urls import path
from . import views

app_name = 'tedarikciler'

urlpatterns = [
    path('', views.tedarikci_listesi, name='tedarikci_listesi'),
    path('ekle/', views.tedarikci_ekle, name='tedarikci_ekle'),
    path('<int:pk>/', views.tedarikci_detay, name='tedarikci_detay'),
    path('<int:pk>/duzenle/', views.tedarikci_duzenle, name='tedarikci_duzenle'),
    path('<int:pk>/sil/', views.tedarikci_sil, name='tedarikci_sil'),
    path('<int:pk>/cari/', views.tedarikci_cari, name='tedarikci_cari'),
] 