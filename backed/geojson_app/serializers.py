from rest_framework import serializers
from .models import GeoJSONFile

class GeoJSONFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoJSONFile
        fields = '__all__'
