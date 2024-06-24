from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_raster, name='upload_raster'),
    path('raster/<int:pk>/', views.view_raster, name='view_raster'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


