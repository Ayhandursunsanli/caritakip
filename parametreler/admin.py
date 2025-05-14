from django.contrib import admin
from .models import KDV, ParaBirimi, Birim

@admin.register(KDV)
class KDVAdmin(admin.ModelAdmin):
    list_display = ('oran',)
    ordering = ('oran',)

@admin.register(ParaBirimi)
class ParaBirimiAdmin(admin.ModelAdmin):
    list_display = ('kod',)
    ordering = ('kod',)

@admin.register(Birim)
class BirimAdmin(admin.ModelAdmin):
    list_display = ('ad',)
    ordering = ('ad',) 