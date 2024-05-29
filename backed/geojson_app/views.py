# from rest_framework import viewsets
# from .models import GeoJSONFile
# from .serializers import GeoJSONFileSerializer

# class GeoJSONFileViewSet(viewsets.ModelViewSet):
#     queryset = GeoJSONFile.objects.all()
#     serializer_class = GeoJSONFileSerializer


from rest_framework import viewsets
from .models import GeoJSONFile
from .serializers import GeoJSONFileSerializer

class GeoJSONFileViewSet(viewsets.ModelViewSet):
    queryset = GeoJSONFile.objects.all()
    serializer_class = GeoJSONFileSerializer
