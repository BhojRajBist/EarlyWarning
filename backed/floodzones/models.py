# models.py
from django.contrib.gis.db import models

class FloodExtent(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='geotiffs/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


