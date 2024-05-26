import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
from boundary.models import District

class Command(BaseCommand):
    help = 'Load districts from a GeoJSON file'

    def add_arguments(self, parser):
        parser.add_argument('geojson_file', type=str, help='The path to the GeoJSON file')

    def handle(self, *args, **kwargs):
        geojson_file = kwargs['geojson_file']

        with open(geojson_file, 'r') as file:
            data = json.load(file)

            for feature in data['features']:
                properties = feature.get('properties', {})
                geometry = feature.get('geometry', None)

                if not geometry:
                    self.stdout.write(self.style.ERROR('Missing geometry in feature'))
                    continue

                name = properties.get('name', None)

                if not name:
                    self.stdout.write(self.style.ERROR('Missing name in feature properties'))
                    continue

                boundary = GEOSGeometry(json.dumps(geometry))

                district, created = District.objects.get_or_create(name=name, boundary=boundary)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created district: {name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'District already exists: {name}'))
