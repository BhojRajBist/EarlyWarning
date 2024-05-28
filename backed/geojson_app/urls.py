from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeoJSONFileViewSet

router = DefaultRouter()
router.register(r'geojson', GeoJSONFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
