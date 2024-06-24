# from django.shortcuts import render, redirect
# from django.core.files.storage import default_storage
# from .models import FloodRiskZone
# from .utils import classify_raster, apply_color_palette

# def upload_raster(request):
#     if request.method == 'POST':
#         raster_file = request.FILES['raster']
#         path = default_storage.save('rasters/' + raster_file.name, raster_file)
#         full_path = default_storage.path(path)

#         classified, meta = classify_raster(full_path)
#         colored_raster_relative_path = apply_color_palette(classified, meta)

#         zone = FloodRiskZone.objects.create(
#             name='Classified Raster', 
#             raster=path, 
#             classified_raster=colored_raster_relative_path
#         )

#         return redirect('view_raster', pk=zone.pk)

#     return render(request, 'upload_raster.html')

# def view_raster(request, pk):
#     raster = FloodRiskZone.objects.get(pk=pk)
#     return render(request, 'view_raster.html', {'raster_url': raster.classified_raster.url})



# outpot in geojson format
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from .models import FloodRiskZone
from django.conf import settings 
from .utils import classify_and_vectorize_raster, save_vector_data

def upload_raster(request):
    if request.method == 'POST':
        raster_file = request.FILES['raster']
        path = default_storage.save('rasters/' + raster_file.name, raster_file)
        full_path = default_storage.path(path)

        geometries, profile = classify_and_vectorize_raster(full_path)
        vector_file_path = save_vector_data(geometries, profile)

        zone = FloodRiskZone.objects.create(
            name='Classified Zones GeoJSON', 
            raster=path, 
            classified_raster=vector_file_path
        )

        return redirect('view_raster', pk=zone.pk)

    return render(request, 'upload_raster.html')

def view_raster(request, pk):
    raster = FloodRiskZone.objects.get(pk=pk)
    vector_url = f"{settings.MEDIA_URL}{raster.classified_raster}"
    return render(request, 'view_raster.html', {'vector_url': vector_url})
