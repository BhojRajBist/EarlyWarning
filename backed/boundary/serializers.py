# from rest_framework_gis.serializers import GeoFeatureModelSerializer
# from .models import Province, District, Municipality

# class ProvinceSerializer(GeoFeatureModelSerializer):
#     class Meta:
#         model = Province
#         geo_field = "boundary"
#         fields = "__all__"

# class DistrictSerializer(GeoFeatureModelSerializer):
#     class Meta:
#         model = District
#         geo_field = "boundary"
#         fields = "__all__"

# class MunicipalitySerializer(GeoFeatureModelSerializer):
#     class Meta:
#         model = Municipality
#         geo_field = "boundary"
#         fields = "__all__"

# spatial_data/serializers.py

# districts/api/serializers.py
from rest_framework import serializers
from .models import GeoJSONFile

class GeoJSONFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoJSONFile
        fields = '__all__'

