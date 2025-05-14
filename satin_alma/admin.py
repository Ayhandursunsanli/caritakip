from django.contrib import admin
from .models import SatinAlma

@admin.register(SatinAlma)
class SatinAlmaAdmin(admin.ModelAdmin):
    list_display = ('tedarikci', 'urun', 'departman', 'tarih', 'miktar', 'birim', 'birim_fiyat', 'kdv', 'para_birimi', 'faturaya_baglandi')
    list_filter = ('tedarikci', 'departman', 'kdv', 'para_birimi', 'faturaya_baglandi')
    search_fields = ('tedarikci__ad', 'urun__ad')
    date_hierarchy = 'tarih'
    ordering = ('-tarih',) 