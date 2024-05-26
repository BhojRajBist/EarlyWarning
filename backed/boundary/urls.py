# spatial_data/urls.py

from django.urls import path
from .views import DistrictList, DistrictDetail

urlpatterns = [
    path('districts/', DistrictList.as_view(), name='district-list'),
    path('districts/<int:pk>/', DistrictDetail.as_view(), name='district-detail'),
]
