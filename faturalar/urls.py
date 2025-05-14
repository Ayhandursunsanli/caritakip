from django.urls import path
from . import views

app_name = 'faturalar'

urlpatterns = [
    path('', views.fatura_listesi, name='fatura_listesi'),
    path('ekle/', views.fatura_ekle, name='fatura_ekle'),
    path('<int:pk>/', views.fatura_detay, name='fatura_detay'),
    path('<int:pk>/duzenle/', views.fatura_duzenle, name='fatura_duzenle'),
    path('<int:pk>/sil/', views.fatura_sil, name='fatura_sil'),
    path('excel/', views.fatura_listesi_excel, name='fatura_listesi_excel'),
] 