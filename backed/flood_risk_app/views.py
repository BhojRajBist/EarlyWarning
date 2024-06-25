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
# from django.shortcuts import render, redirect
# from django.core.files.storage import default_storage
# from .models import FloodRiskZone
# from django.conf import settings 
# from .utils import classify_and_vectorize_raster, save_vector_data

# def upload_raster(request):
#     if request.method == 'POST':
#         raster_file = request.FILES['raster']
#         path = default_storage.save('rasters/' + raster_file.name, raster_file)
#         full_path = default_storage.path(path)

#         geometries, profile = classify_and_vectorize_raster(full_path)
#         vector_file_path = save_vector_data(geometries, profile)

#         zone = FloodRiskZone.objects.create(
#             name='Classified Zones GeoJSON', 
#             raster=path, 
#             classified_raster=vector_file_path
#         )

#         return redirect('view_raster', pk=zone.pk)

#     return render(request, 'upload_raster.html')

# def view_raster(request, pk):
#     raster = FloodRiskZone.objects.get(pk=pk)
#     vector_url = f"{settings.MEDIA_URL}{raster.classified_raster}"
#     return render(request, 'view_raster.html', {'vector_url': vector_url})



#views for rest api


import os
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.conf import settings
from .models import FloodRiskZone
from .utils import classify_and_vectorize_raster, save_vector_data

def upload_raster(request):
    if request.method == 'POST':
        raster_file = request.FILES['raster']
        path = default_storage.save('rasters/' + raster_file.name, raster_file)
        full_path = default_storage.path(path)

        geometries, profile, min_value, max_value = classify_and_vectorize_raster(full_path)
        vector_file_path = save_vector_data(geometries, profile)

        zone = FloodRiskZone.objects.create(
            name='Classified Zones GeoJSON', 
            raster=path, 
            classified_raster=vector_file_path,
            min_value=min_value,
            max_value=max_value
        )

        return redirect('view_raster', pk=zone.pk)

    return render(request, 'upload_raster.html')

def view_raster(request, pk):
    raster = FloodRiskZone.objects.get(pk=pk)
    vector_url = f"{settings.MEDIA_URL}{raster.classified_raster}"
    return render(request, 'view_raster.html', {'vector_url': vector_url})

def get_flood_zones_geojson(request):
    if request.method == 'GET':
        try:
            # Fetch the latest uploaded raster data
            raster = FloodRiskZone.objects.latest('id')

            # Get the path to the classified GeoJSON file
            vector_file_path = raster.classified_raster.name  # Use .name to get the file path

            # Construct full path to GeoJSON file
            geojson_file_path = default_storage.path(vector_file_path)

            with open(geojson_file_path, 'r') as geojson_file:
                geojson_data = json.load(geojson_file)

            # Include the min and max values in the response
            response_data = {
                'geojson_data': geojson_data,
                'min_value': raster.min_value,
                'max_value': raster.max_value
            }

            return JsonResponse(response_data)

        except FloodRiskZone.DoesNotExist:
            return JsonResponse({'error': 'No classified raster found.'}, status=404)
        except FileNotFoundError:
            return JsonResponse({'error': 'GeoJSON file not found.'}, status=404)

    return JsonResponse({'error': 'Method not allowed.'}, status=405)


