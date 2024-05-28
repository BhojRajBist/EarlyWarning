from django.db import models

class GeoJSONFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='geojson_files/')

    def __str__(self):
        return self.name
