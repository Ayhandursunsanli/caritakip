from django.contrib import admin
from .models import Fatura

@admin.register(Fatura)
class FaturaAdmin(admin.ModelAdmin):
    list_display = ('tedarikci', 'fatura_no', 'fatura_tarihi', 'odeme_tarihi', 'tutar')
    list_filter = ('tedarikci', 'fatura_tarihi', 'odeme_tarihi')
    search_fields = ('tedarikci__ad', 'fatura_no')
    date_hierarchy = 'fatura_tarihi'
    ordering = ('-fatura_tarihi',)
    filter_horizontal = ('satinalmalar',) 