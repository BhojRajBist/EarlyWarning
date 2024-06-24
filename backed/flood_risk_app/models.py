# models.py
from django.db import models

class FloodRiskZone(models.Model):
    name = models.CharField(max_length=100)
    raster = models.FileField(upload_to='rasters/')
    classified_raster = models.ImageField(upload_to='classified_rasters/')
    created_at = models.DateTimeField(auto_now_add=True)  # Add this line
