
# Create your models here.
from django.contrib.gis.db import models

class TiffFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='tiff_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name