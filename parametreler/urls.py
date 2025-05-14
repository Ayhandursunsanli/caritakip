from django.urls import path
from . import views

app_name = 'parametreler'

urlpatterns = [
    path('', views.parametre_listesi, name='parametre_listesi'),
    path('kdv/', views.kdv_listesi, name='kdv_listesi'),
    path('kdv/ekle/', views.kdv_ekle, name='kdv_ekle'),
    path('kdv/<int:pk>/duzenle/', views.kdv_duzenle, name='kdv_duzenle'),
    path('kdv/<int:pk>/sil/', views.kdv_sil, name='kdv_sil'),
    
    path('para-birimi/', views.para_birimi_listesi, name='para_birimi_listesi'),
    path('para-birimi/ekle/', views.para_birimi_ekle, name='para_birimi_ekle'),
    path('para-birimi/<int:pk>/duzenle/', views.para_birimi_duzenle, name='para_birimi_duzenle'),
    path('para-birimi/<int:pk>/sil/', views.para_birimi_sil, name='para_birimi_sil'),
    
    path('birim/', views.birim_listesi, name='birim_listesi'),
    path('birim/ekle/', views.birim_ekle, name='birim_ekle'),
    path('birim/<int:pk>/duzenle/', views.birim_duzenle, name='birim_duzenle'),
    path('birim/<int:pk>/sil/', views.birim_sil, name='birim_sil'),
] 