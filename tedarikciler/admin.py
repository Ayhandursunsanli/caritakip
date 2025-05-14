from django.contrib import admin
from .models import Tedarikci

@admin.register(Tedarikci)
class TedarikciAdmin(admin.ModelAdmin):
    list_display = ('ad', 'hizmet', 'yetkili', 'telefon', 'email')
    list_filter = ('hizmet',)
    search_fields = ('ad', 'yetkili', 'telefon', 'email')
    ordering = ('ad',) 