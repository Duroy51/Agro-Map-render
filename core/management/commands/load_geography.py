import os
from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
from core.models import Departement


class Command(BaseCommand):
    help = 'Charge les départements du Cameroun dans PostGIS'

    def handle(self, *args, **kwargs):

        shp_path = os.path.join(os.getcwd(), 'data', 'gadm41_CMR_2.shp')
        mapping = {
            'nom_departement': 'NAME_2',
            'nom_region': 'NAME_1',
            'geom': 'MULTIPOLYGON',
        }

        print(f"🔄 Chargement de {shp_path}...")

        try:
            lm = LayerMapping(Departement, shp_path, mapping, transform=False, encoding='utf-8')
            lm.save(strict=True, verbose=True)
            self.stdout.write(self.style.SUCCESS(f"✅ SUCCÈS : Départements importés !"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ ERREUR : {e}"))