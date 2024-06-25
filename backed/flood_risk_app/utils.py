# import os
# import numpy as np
# import rasterio
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from django.conf import settings

# def classify_raster(file_path):
#     with rasterio.open(file_path) as src:
#         raster = src.read(1)
#         classified = np.zeros_like(raster, dtype=np.uint8)

#         # Example classification
#         classified[raster <= 0.5] = 1  # Low risk
#         classified[(raster > 0.5) & (raster <= 1.5)] = 2  # Medium risk
#         classified[raster > 1.5] = 3  # High risk

#         return classified, src.meta

# def apply_color_palette(classified_raster, meta):
#     # Define color palette
#     colors = ['#00ff00', '#ffff00', '#ff0000']  # Green, Yellow, Red
#     cmap = ListedColormap(colors)

#     # Create colored image
#     plt.imshow(classified_raster, cmap=cmap)
#     plt.axis('off')

#     # Ensure the directory exists
#     classified_raster_dir = os.path.join(settings.MEDIA_ROOT, 'classified_rasters')
#     os.makedirs(classified_raster_dir, exist_ok=True)

#     # Save the image
#     output_filename = 'colored_raster.png'
#     output_path = os.path.join(classified_raster_dir, output_filename)
#     plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
#     plt.close()

#     return os.path.join('classified_rasters', output_filename)


# To convert the image in geojson
# import os
# import json
# import numpy as np
# import rasterio
# from shapely.geometry import shape, mapping
# from rasterio.features import shapes
# from rasterio.warp import transform_geom
# from django.conf import settings

# def classify_and_vectorize_raster(file_path):
#     with rasterio.open(file_path) as src:
#         raster = src.read(1)
#         profile = src.profile  # Get the raster profile for metadata
#         transform = src.transform

#         # Example classification (adjust as per your classification logic)
#         low_risk = raster <= 0.5
#         medium_risk = (raster > 0.5) & (raster <= 1.5)
#         high_risk = raster > 1.5

#         # Create an empty mask with the same shape as the raster
#         classification = np.zeros_like(raster, dtype=np.uint8)

#         # Assign classification values
#         classification[low_risk] = 1
#         classification[medium_risk] = 2
#         classification[high_risk] = 3

#         # Define classification mapping
#         class_mapping = {
#             1: 'low',
#             2: 'medium',
#             3: 'high'
#         }

#         # Extract polygons for each class
#         geometries = []
#         for class_value, class_name in class_mapping.items():
#             mask = classification == class_value
#             shapes_generator = shapes(mask.astype(np.int16), mask=mask, transform=transform)
            
#             for geom, val in shapes_generator:
#                 geom_transformed = transform_geom(src.crs, 'EPSG:4326', geom)
#                 geometries.append({
#                     'type': 'Feature',
#                     'geometry': geom_transformed,
#                     'properties': {
#                         'classification': class_name
#                     }
#                 })

#     return geometries, profile

# def save_vector_data(geometries, profile):
#     vector_dir = os.path.join(settings.MEDIA_ROOT, 'vector_data')
#     os.makedirs(vector_dir, exist_ok=True)

#     output_path = os.path.join(vector_dir, 'classified_zones.geojson')
#     with open(output_path, 'w') as f:
#         geojson = {
#             'type': 'FeatureCollection',
#             'features': geometries
#         }
#         json.dump(geojson, f)

#     relative_path = os.path.relpath(output_path, settings.MEDIA_ROOT)
#     return relative_path




# This is the updated code as in PDRA GEE


# import os
# import json
# import numpy as np
# import rasterio
# from shapely.geometry import shape, mapping
# from rasterio.features import shapes
# from rasterio.warp import transform_geom
# from django.conf import settings

# def classify_and_vectorize_raster(file_path):
#     with rasterio.open(file_path) as src:
#         raster = src.read(1)
#         profile = src.profile  # Get the raster profile for metadata
#         transform = src.transform

#         # Example classification (adjust as per your classification logic)
#         shallow_threshold = 0.5
#         moderate_threshold = 1.5

#         # Create an empty mask with the same shape as the raster
#         classification = np.zeros_like(raster, dtype=np.uint8)

#         # Assign classification values based on flood depth thresholds
#         classification[raster > moderate_threshold] = 3  # Deep flood zones
#         classification[(raster > shallow_threshold) & (raster <= moderate_threshold)] = 2  # Moderate risk zones
#         classification[raster <= shallow_threshold] = 1  # Low risk zones

#         # Define classification mapping
#         class_mapping = {
#             1: 'low',
#             2: 'medium',
#             3: 'high'
#         }

#         # Extract polygons for each class
#         geometries = []
#         for class_value, class_name in class_mapping.items():
#             mask = classification == class_value
#             shapes_generator = shapes(mask.astype(np.int16), mask=mask, transform=transform)
            
#             for geom, val in shapes_generator:
#                 geom_transformed = transform_geom(src.crs, 'EPSG:4326', geom)
#                 geometries.append({
#                     'type': 'Feature',
#                     'geometry': geom_transformed,
#                     'properties': {
#                         'classification': class_name
#                     }
#                 })

#     return geometries, profile

# def save_vector_data(geometries, profile):
#     vector_dir = os.path.join(settings.MEDIA_ROOT, 'vector_data')
#     os.makedirs(vector_dir, exist_ok=True)

#     output_path = os.path.join(vector_dir, 'classified_zones.geojson')
#     with open(output_path, 'w') as f:
#         geojson = {
#             'type': 'FeatureCollection',
#             'features': geometries
#         }
#         json.dump(geojson, f)

#     relative_path = os.path.relpath(output_path, settings.MEDIA_ROOT)
#     return relative_path



# min and maximum value is given

# import os
# import json
# import numpy as np
# import rasterio
# from shapely.geometry import shape, mapping
# from rasterio.features import shapes
# from rasterio.warp import transform_geom
# from django.conf import settings

# def classify_and_vectorize_raster(file_path):
#     with rasterio.open(file_path) as src:
#         raster = src.read(1)
#         profile = src.profile  # Get the raster profile for metadata
#         transform = src.transform

#         # Get the minimum and maximum values in the raster
#         min_value = float(raster.min())  # Convert to float for JSON serialization
#         max_value = float(raster.max())  # Convert to float for JSON serialization

#         # Example classification (adjust as per your classification logic)
#         shallow_threshold = 0.5
#         moderate_threshold = 1.5

#         # Create an empty mask with the same shape as the raster
#         classification = np.zeros_like(raster, dtype=np.uint8)

#         # Assign classification values based on flood depth thresholds
#         classification[raster > moderate_threshold] = 3  # Deep flood zones
#         classification[(raster > shallow_threshold) & (raster <= moderate_threshold)] = 2  # Moderate risk zones
#         classification[raster <= shallow_threshold] = 1  # Low risk zones

#         # Define classification mapping
#         class_mapping = {
#             1: 'low',
#             2: 'medium',
#             3: 'high'
#         }

#         # Extract polygons for each class
#         geometries = []
#         for class_value, class_name in class_mapping.items():
#             mask = classification == class_value
#             shapes_generator = shapes(mask.astype(np.int16), mask=mask, transform=transform)
            
#             for geom, val in shapes_generator:
#                 geom_transformed = transform_geom(src.crs, 'EPSG:4326', geom)
#                 geometries.append({
#                     'type': 'Feature',
#                     'geometry': geom_transformed,
#                     'properties': {
#                         'classification': class_name
#                     }
#                 })

#     return geometries, profile, min_value, max_value

# def save_vector_data(geometries, profile):
#     vector_dir = os.path.join(settings.MEDIA_ROOT, 'vector_data')
#     os.makedirs(vector_dir, exist_ok=True)

#     output_path = os.path.join(vector_dir, 'classified_zones.geojson')
#     with open(output_path, 'w') as f:
#         geojson = {
#             'type': 'FeatureCollection',
#             'features': geometries
#         }
#         json.dump(geojson, f)

#     relative_path = os.path.relpath(output_path, settings.MEDIA_ROOT)
#     return relative_path






import os
import json
import numpy as np
import rasterio
from shapely.geometry import shape, mapping
from rasterio.features import shapes
from rasterio.warp import transform_geom
from django.conf import settings

def classify_and_vectorize_raster(file_path):
    with rasterio.open(file_path) as src:
        raster = src.read(1)
        profile = src.profile  # Get the raster profile for metadata
        transform = src.transform

        # Get the minimum and maximum values in the raster
        min_value = float(raster.min())  # Convert to float for JSON serialization
        max_value = float(raster.max())  # Convert to float for JSON serialization

        # Define classification thresholds
        shallow_threshold = 0.5
        moderate_threshold = 1.5
        deep_threshold = 3.0

        # Create an empty mask with the same shape as the raster
        classification = np.zeros_like(raster, dtype=np.uint8)

        # Assign classification values based on flood depth thresholds
        classification = np.where(raster > 0, 0, classification)  # No flood
        classification = np.where(raster > shallow_threshold, 1, classification)  # Shallow flood
        classification = np.where(raster > moderate_threshold, 2, classification)  # Moderate flood
        classification = np.where(raster > deep_threshold, 3, classification)  # Deep flood

        # Define classification mapping
        class_mapping = {
            0: 'no_flood',
            1: 'shallow',
            2: 'moderate',
            3: 'deep'
        }

        # Extract polygons for each class
        geometries = []
        for class_value, class_name in class_mapping.items():
            mask = classification == class_value
            shapes_generator = shapes(mask.astype(np.int16), mask=mask, transform=transform)
            
            for geom, val in shapes_generator:
                geom_transformed = transform_geom(src.crs, 'EPSG:4326', geom)
                geometries.append({
                    'type': 'Feature',
                    'geometry': geom_transformed,
                    'properties': {
                        'classification': class_name
                    }
                })

    return geometries, profile, min_value, max_value

def save_vector_data(geometries, profile):
    vector_dir = os.path.join(settings.MEDIA_ROOT, 'vector_data')
    os.makedirs(vector_dir, exist_ok=True)

    output_path = os.path.join(vector_dir, 'classified_zones.geojson')
    with open(output_path, 'w') as f:
        geojson = {
            'type': 'FeatureCollection',
            'features': geometries
        }
        json.dump(geojson, f)

    relative_path = os.path.relpath(output_path, settings.MEDIA_ROOT)
    return relative_path
