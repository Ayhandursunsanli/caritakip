from django.contrib import admin
from .models import Urun

@admin.register(Urun)
class UrunAdmin(admin.ModelAdmin):
    list_display = ('ad', 'sira')
    list_filter = ('sira',)
    search_fields = ('ad',)
    ordering = ('sira', 'ad') 