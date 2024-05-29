from django.contrib import admin
from .models import GeoJSONFile

@admin.register(GeoJSONFile)
class GeoJSONFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')

# from django.contrib import admin
# from django.contrib.gis.admin import OSMGeoAdmin
# from .models import GeoJSONFile

# @admin.register(GeoJSONFile)
# class GeoJSONFileAdmin(OSMGeoAdmin):
#     list_display = ('name', 'geom')

