# # floodzones/management/commands/load_raster.py

# import os
# from django.core.management.base import BaseCommand
# from django.contrib.gis.gdal import GDALException
# from osgeo import gdal
# from floodzones.models import FloodZone

# class Command(BaseCommand):
#     help = 'Load raster data into the FloodZone model'

#     def handle(self, *args, **kwargs):
#         raster_path = '/home/bhoj/Desktop/5yr_flood_extent_koshi.geotif'

#         # Verify the file path
#         self.stdout.write('Checking file path: {}'.format(raster_path))
#         if not os.path.isfile(raster_path):
#             self.stderr.write(self.style.ERROR('File not found: {}'.format(raster_path)))
#             return

#         try:
#             # Set GDAL configuration option
#             gdal.SetConfigOption('GTIFF_HONOUR_NEGATIVE_SCALEY', 'YES')

#             # Open the raster file
#             ds = gdal.Open(raster_path, gdal.GA_ReadOnly)
#             self.stdout.write('GDAL open result: {}'.format(ds))
#             if ds is None:
#                 self.stderr.write(self.style.ERROR('Could not open the datasource at "{}"'.format(raster_path)))
#                 return

#             band = ds.GetRasterBand(1)
#             min_value, max_value = band.ComputeRasterMinMax()
#             self.stdout.write('Min value: {}, Max value: {}'.format(min_value, max_value))

#             # Determine risk level based on max value
#             if max_value >= 100:
#                 risk_level = 'High Risk'
#             elif max_value >= 50:
#                 risk_level = 'Medium Risk'
#             else:
#                 risk_level = 'Low Risk'

#             # Create a new FloodZone entry
#             FloodZone.objects.create(
#                 name='Flood Zone',
#                 rast=raster_path,  # Storing the path for simplicity; modify as needed
#                 risk_level=risk_level
#             )
#             self.stdout.write(self.style.SUCCESS('Successfully loaded raster data'))
#         except GDALException as e:
#             self.stderr.write(self.style.ERROR('Could not open the datasource: {}'.format(e)))
#             return


# floodzones/management/commands/load_raster.py

# management/commands/load_geotiff.py
import os
from django.core.management.base import BaseCommand
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
from django.conf import settings
from yourapp.models import FloodZone

class Command(BaseCommand):
    help = 'Load GeoTIFF file, perform analysis, and save results.'

    def handle(self, *args, **kwargs):
        geotiff_path = '/path/to/your/geotiff/file.tif'  # Replace with your GeoTIFF file path
        name = 'Flood Zone Map'  # Example name

        try:
            # Open the GeoTIFF file
            ds = DataSource(geotiff_path)

            # Assume your GeoTIFF has a single band with flood extent values
            band = ds[0]
            extent = band.extent  # Get the extent of the raster

            # Perform analysis to classify zones
            high_risk_zone = None
            medium_risk_zone = None
            low_risk_zone = None

            # Example classification based on flood extent values (adjust as per your analysis)
            for feature in ds[0]:
                geom = feature.geom
                value = feature.get_value()

                if value >= 20:  # Example threshold for high risk zone
                    if high_risk_zone:
                        high_risk_zone = high_risk_zone.union(geom)
                    else:
                        high_risk_zone = geom
                elif value >= 10:  # Example threshold for medium risk zone
                    if medium_risk_zone:
                        medium_risk_zone = medium_risk_zone.union(geom)
                    else:
                        medium_risk_zone = geom
                else:  # Example threshold for low risk zone
                    if low_risk_zone:
                        low_risk_zone = low_risk_zone.union(geom)
                    else:
                        low_risk_zone = geom

            # Save results to database
            flood_zone = FloodZone.objects.create(
                name=name,
                rast=os.path.basename(geotiff_path),  # Store the filename or actual raster data if using RasterField
                high_risk_zone=GEOSGeometry(high_risk_zone.wkt) if high_risk_zone else None,
                medium_risk_zone=GEOSGeometry(medium_risk_zone.wkt) if medium_risk_zone else None,
                low_risk_zone=GEOSGeometry(low_risk_zone.wkt) if low_risk_zone else None,
            )

            self.stdout.write(self.style.SUCCESS('GeoTIFF file loaded and analyzed successfully.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading GeoTIFF file: {str(e)}'))

