from django.urls import path
from . import views

app_name = 'departmanlar'

urlpatterns = [
    path('', views.departman_listesi, name='departman_listesi'),
    path('ekle/', views.departman_ekle, name='departman_ekle'),
    path('<int:pk>/', views.departman_detay, name='departman_detay'),
    path('<int:pk>/duzenle/', views.departman_duzenle, name='departman_duzenle'),
    path('<int:pk>/sil/', views.departman_sil, name='departman_sil'),
    path('<int:pk>/excel/', views.departman_excel, name='departman_excel'),
]
 