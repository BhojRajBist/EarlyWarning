# from rest_framework import generics
# from .models import Province, District, Municipality
# from .serializers import ProvinceSerializer, DistrictSerializer, MunicipalitySerializer

# class ProvinceList(generics.ListAPIView):
#     queryset = Province.objects.all()
#     serializer_class = ProvinceSerializer

# class DistrictList(generics.ListAPIView):
#     queryset = District.objects.all()
#     serializer_class = DistrictSerializer

# class MunicipalityList(generics.ListAPIView):
#     queryset = Municipality.objects.all()
#     serializer_class = MunicipalitySerializer

# spatial_data/views.py
# districts/api/views.py
from rest_framework import viewsets
from .models import GeoJSONFile
from .serializers import GeoJSONFileSerializer

class GeoJSONFileViewSet(viewsets.ModelViewSet):
    queryset = GeoJSONFile.objects.all()
    serializer_class = GeoJSONFileSerializer

