# from django.contrib.gis.db import models

# class Province(models.Model):
#     name = models.CharField(max_length=100)
#     boundary = models.MultiPolygonField()

# class District(models.Model):
#     name = models.CharField(max_length=100)
#     boundary = models.MultiPolygonField()

# class Municipality(models.Model):
#     name = models.CharField(max_length=100)
#     boundary = models.MultiPolygonField()

from django.contrib.gis.db import models

class District(models.Model):
    name = models.CharField(max_length=100)
    boundary = models.MultiPolygonField()

    def __str__(self):
        return self.name
