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

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import District

class DistrictSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = District
        geo_field = "boundary"
        fields = ('id', 'name', 'boundary')
