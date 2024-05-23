from rest_framework import viewsets
from .models import TiffFile
from .serializers import TiffFileSerializer

class TiffFileViewSet(viewsets.ModelViewSet):
    queryset = TiffFile.objects.all()
    serializer_class = TiffFileSerializer
