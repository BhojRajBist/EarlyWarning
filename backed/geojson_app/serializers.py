# from rest_framework import serializers
# from .models import GeoJSONFile

# class GeoJSONFileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GeoJSONFile
#         fields = '__all__'

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import GeoJSONFile

class GeoJSONFileSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = GeoJSONFile
        geo_field = "geom"
        fields = ('id', 'name', 'file', 'geom')
