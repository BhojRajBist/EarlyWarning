# # views.py
# import os
# import rasterio
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import FloodExtent

# def analyze_flood_extent(request, floodextent_id):
#     try:
#         flood_extent = FloodExtent.objects.get(pk=floodextent_id)
#         file_path = flood_extent.file.path

#         # Open GeoTIFF file for analysis
#         with rasterio.open(file_path) as src:
#             # Read raster data
#             data = src.read(1)  # Assuming it's a single band raster

#             # Perform analysis to classify zones (example)
#             high_risk_threshold = 0.8 * data.max()  # Example threshold for high risk
#             medium_risk_threshold = 0.5 * data.max()  # Example threshold for medium risk

#             # Classify zones based on pixel values
#             high_risk_zone = (data >= high_risk_threshold).astype(int)
#             medium_risk_zone = ((data < high_risk_threshold) & (data >= medium_risk_threshold)).astype(int)
#             low_risk_zone = (data < medium_risk_threshold).astype(int)

#             # Prepare response data
#             response_data = {
#                 'high_risk_zone': high_risk_zone.tolist(),  # Convert numpy array to list
#                 'medium_risk_zone': medium_risk_zone.tolist(),
#                 'low_risk_zone': low_risk_zone.tolist(),
#             }

#             return JsonResponse(response_data)
#     except FloodExtent.DoesNotExist:
#         return JsonResponse({'error': 'FloodExtent not found'}, status=404)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)
    
# def flood_zones_map(request, floodextent_id):
#     return render(request, 'floodzones/map.html', {'floodextent_id': floodextent_id})


# import os
# import rasterio
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import FloodExtent

# def analyze_flood_extent(request, floodextent_id):
#     try:
#         flood_extent = FloodExtent.objects.get(pk=floodextent_id)
#         file_path = flood_extent.file.path

#         if not os.path.exists(file_path):
#             return JsonResponse({'error': 'File not found'}, status=404)

#         # Open GeoTIFF file for analysis
#         with rasterio.open(file_path) as src:
#             data = src.read(1)  # Assuming it's a single band raster

#             # Perform analysis to classify zones
#             high_risk_threshold = 0.8 * data.max()  # Example threshold for high risk
#             medium_risk_threshold = 0.5 * data.max()  # Example threshold for medium risk

#             # Classify zones based on pixel values
#             high_risk_zone = (data >= high_risk_threshold).astype(int)
#             medium_risk_zone = ((data < high_risk_threshold) & (data >= medium_risk_threshold)).astype(int)
#             low_risk_zone = (data < medium_risk_threshold).astype(int)

#             # Prepare response data
#             response_data = {
#                 'high_risk_zone': high_risk_zone.tolist(),
#                 'medium_risk_zone': medium_risk_zone.tolist(),
#                 'low_risk_zone': low_risk_zone.tolist(),
#             }

#             return JsonResponse(response_data)

#     except FloodExtent.DoesNotExist:
#         return JsonResponse({'error': 'FloodExtent not found'}, status=404)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# def flood_zones_map(request):
#     return render(request, 'map.html', {})



                      #Output as AAA
# import os
# import rasterio
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# import base64
# from .models import FloodExtent

# def home(request):
#     first_flood_extent = FloodExtent.objects.first()
#     if first_flood_extent:
#         return redirect('flood_zones_map', floodextent_id=first_flood_extent.id)
#     return JsonResponse({'error': 'No flood extents available'}, status=404)

# def flood_zones_map(request, floodextent_id):
#     return render(request, 'map.html', {'floodextent_id': floodextent_id})

# def analyze_flood_extent(request, floodextent_id):
#     try:
#         flood_extent = FloodExtent.objects.get(pk=floodextent_id)
#         file_path = flood_extent.file.path

#         with rasterio.open(file_path) as src:
#             data = src.read(1)

#             high_risk_threshold = 0.8 * data.max()
#             medium_risk_threshold = 0.5 * data.max()

#             high_risk_zone = (data >= high_risk_threshold).astype(int)
#             medium_risk_zone = ((data < high_risk_threshold) & (data >= medium_risk_threshold)).astype(int)
#             low_risk_zone = (data < medium_risk_threshold).astype(int)

#             high_risk_zone_base64 = base64.b64encode(high_risk_zone.tobytes()).decode('utf-8')
#             medium_risk_zone_base64 = base64.b64encode(medium_risk_zone.tobytes()).decode('utf-8')
#             low_risk_zone_base64 = base64.b64encode(low_risk_zone.tobytes()).decode('utf-8')

#             response_data = {
#                 'high_risk_zone': high_risk_zone_base64,
#                 'medium_risk_zone': medium_risk_zone_base64,
#                 'low_risk_zone': low_risk_zone_base64,
#             }

#             return JsonResponse(response_data)
#     except FloodExtent.DoesNotExist:
#         return JsonResponse({'error': 'FloodExtent not found'}, status=404)
#     except Exception as e:
#         print(f"Error analyzing flood extent: {str(e)}")
#         return JsonResponse({'error': str(e)}, status=500)





#    this ONE IS WORKING BUT THE RESPOSE IS BIG
# import os
# import rasterio
# import base64
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from .models import FloodExtent

# def home(request):
#     first_flood_extent = FloodExtent.objects.first()
#     if first_flood_extent:
#         return redirect('flood_zones_map', floodextent_id=first_flood_extent.id)
#     return JsonResponse({'error': 'No flood extents available'}, status=404)

# def flood_zones_map(request, floodextent_id):
#     return render(request, 'map.html', {'floodextent_id': floodextent_id})

# def analyze_flood_extent(request, floodextent_id):
#     try:
#         flood_extent = FloodExtent.objects.get(pk=floodextent_id)
#         file_path = flood_extent.file.path

#         with rasterio.open(file_path) as src:
#             data = src.read(1)

#             high_risk_threshold = 0.8 * data.max()
#             medium_risk_threshold = 0.5 * data.max()

#             high_risk_zone = (data >= high_risk_threshold).astype(int)
#             medium_risk_zone = ((data < high_risk_threshold) & (data >= medium_risk_threshold)).astype(int)
#             low_risk_zone = (data < medium_risk_threshold).astype(int)

#             high_risk_zone_base64 = base64.b64encode(high_risk_zone.tobytes()).decode('utf-8')
#             medium_risk_zone_base64 = base64.b64encode(medium_risk_zone.tobytes()).decode('utf-8')
#             low_risk_zone_base64 = base64.b64encode(low_risk_zone.tobytes()).decode('utf-8')

#             response_data = {
#                 'high_risk_zone': high_risk_zone_base64,
#                 'medium_risk_zone': medium_risk_zone_base64,
#                 'low_risk_zone': low_risk_zone_base64,
#                 'width': data.shape[1],  # width of the raster
#                 'height': data.shape[0]  # height of the raster
#             }

#             return JsonResponse(response_data)
#     except FloodExtent.DoesNotExist:
#         return JsonResponse({'error': 'FloodExtent not found'}, status=404)
#     except Exception as e:
#         print(f"Error analyzing flood extent: {str(e)}")
#         return JsonResponse({'error': str(e)}, status=500)




# 1/10 of the raster is taken


import os
import rasterio
import base64
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from .models import FloodExtent

def analyze_flood_extent(request, floodextent_id):
    try:
        flood_extent = FloodExtent.objects.get(pk=floodextent_id)
        file_path = flood_extent.file.path

        # Open GeoTIFF file for analysis
        with rasterio.open(file_path) as src:
            # Define the window to read (10% of the original raster)
            height, width = src.shape
            window = rasterio.windows.Window(0, 0, width // 10, height // 10)
            data = src.read(1, window=window)

            # Perform analysis to classify zones (example)
            high_risk_threshold = 0.8 * data.max()  # Example threshold for high risk
            medium_risk_threshold = 0.5 * data.max()  # Example threshold for medium risk

            # Classify zones based on pixel values
            high_risk_zone = (data >= high_risk_threshold).astype(np.uint8)
            medium_risk_zone = ((data < high_risk_threshold) & (data >= medium_risk_threshold)).astype(np.uint8)
            low_risk_zone = (data < medium_risk_threshold).astype(np.uint8)

            # Encode zones to base64
            high_risk_zone_base64 = base64.b64encode(high_risk_zone.tobytes()).decode('utf-8')
            medium_risk_zone_base64 = base64.b64encode(medium_risk_zone.tobytes()).decode('utf-8')
            low_risk_zone_base64 = base64.b64encode(low_risk_zone.tobytes()).decode('utf-8')

            # Prepare response data
            response_data = {
                'high_risk_zone': high_risk_zone_base64,
                'medium_risk_zone': medium_risk_zone_base64,
                'low_risk_zone': low_risk_zone_base64,
                'width': window.width,  # width of the window
                'height': window.height  # height of the window
            }

            return JsonResponse(response_data)
    except FloodExtent.DoesNotExist:
        return JsonResponse({'error': 'FloodExtent not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def flood_zones_map(request, floodextent_id):
    return render(request, 'map.html', {'floodextent_id': floodextent_id})
