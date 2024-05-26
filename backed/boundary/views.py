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

from rest_framework import generics
from .models import District
from .serializers import DistrictSerializer

class DistrictList(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class DistrictDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

