from django.contrib import admin
from .models import GeoJSONFile

@admin.register(GeoJSONFile)
class GeoJSONFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')
