from django.contrib import admin
from .models import Departman

@admin.register(Departman)
class DepartmanAdmin(admin.ModelAdmin):
    list_display = ('ad',)
    search_fields = ('ad',)
    ordering = ('ad',) 