# districts/management/commands/load_districts.py
from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
from .models import District

class Command(BaseCommand):
    help = 'Load districts from GeoJSON file'

    def handle(self, *args, **options):
        mapping = {
            'name': 'DISTRICT', # Assuming 'DISTRICT' is the property in GeoJSON representing district names
            'boundary': 'MULTIPOLYGON'  # Assuming 'MULTIPOLYGON' is the geometry field in GeoJSON
        }
        geojson_file = '/home/bhoj/Desktop/EarlyWarning/backed/data/nepal-districts.geojson'
        layer_mapping = LayerMapping(District, geojson_file, mapping)
        layer_mapping.save(verbose=True)
