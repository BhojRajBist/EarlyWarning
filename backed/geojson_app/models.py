from django.db import models

class GeoJSONFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='geojson_files/')

    def __str__(self):
        return self.name

# from django.contrib.gis.db import models

# class GeoJSONFile(models.Model):
#     name = models.CharField(max_length=255)
#     file = models.FileField(upload_to='geojson_files/')
#     geom = models.GeometryField(null=True, blank=True)  # Field to store the geometry

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         import json
#         from django.contrib.gis.geos import GEOSGeometry

#         if self.file:
#             geojson_data = self.file.read()
#             geojson_dict = json.loads(geojson_data)
#             self.geom = GEOSGeometry(json.dumps(geojson_dict['features'][0]['geometry']))
#         super().save(*args, **kwargs)

