from rest_framework import serializers
from .models import TiffFile

class TiffFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiffFile
        fields = ['id', 'name', 'file', 'uploaded_at']
