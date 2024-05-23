from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import TiffFile

@admin.register(TiffFile)
class TiffFileAdmin(LeafletGeoAdmin):
    pass
