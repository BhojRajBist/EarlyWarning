from django.contrib import admin
from .models import TiffFile

@admin.register(TiffFile)
class TiffFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at')
