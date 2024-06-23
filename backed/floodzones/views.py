# views.py
import os
import rasterio
from django.shortcuts import render
from django.http import JsonResponse
from .models import FloodExtent

def analyze_flood_extent(request, floodextent_id):
    try:
        flood_extent = FloodExtent.objects.get(pk=floodextent_id)
        file_path = flood_extent.file.path

        # Open GeoTIFF file for analysis
        with rasterio.open(file_path) as src:
            # Read raster data
            data = src.read(1)  # Assuming it's a single band raster

            # Perform analysis to classify zones (example)
            high_risk_threshold = 0.8 * data.max()  # Example threshold for high risk
            medium_risk_threshold = 0.5 * data.max()  # Example threshold for medium risk

            # Classify zones based on pixel values
            high_risk_zone = (data >= high_risk_threshold).astype(int)
            medium_risk_zone = ((data < high_risk_threshold) & (data >= medium_risk_threshold)).astype(int)
            low_risk_zone = (data < medium_risk_threshold).astype(int)

            # Prepare response data
            response_data = {
                'high_risk_zone': high_risk_zone.tolist(),  # Convert numpy array to list
                'medium_risk_zone': medium_risk_zone.tolist(),
                'low_risk_zone': low_risk_zone.tolist(),
            }

            return JsonResponse(response_data)
    except FloodExtent.DoesNotExist:
        return JsonResponse({'error': 'FloodExtent not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def flood_zones_map(request, floodextent_id):
    return render(request, 'floodzones/map.html', {'floodextent_id': floodextent_id})


