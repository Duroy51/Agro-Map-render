from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Departement, Production


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = ['secteur', 'filiere', 'volume_tonnes', 'annee']

# 2. On sérialise le département (le contenant géographique)
class DepartementSerializer(GeoFeatureModelSerializer):

    productions = ProductionSerializer(many=True, read_only=True)

    class Meta:
        model = Departement
        geo_field = "geom" # Le champ qui contient le polygone
        fields = ['id', 'nom_departement', 'nom_region', 'productions']