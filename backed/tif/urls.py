from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TiffFileViewSet

router = DefaultRouter()
router.register(r'tiff-files', TiffFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
