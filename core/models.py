from django.contrib.gis.db import models


# 1. Le Contenant : Le Département (Géographie)
class Departement(models.Model):
    # Les noms doivent correspondre aux champs de ton Shapefile pour faciliter l'import
    nom_departement = models.CharField(max_length=100)  # Correspondra à NAME_2
    nom_region = models.CharField(max_length=100)  # Correspondra à NAME_1

    # La géométrie. MultiPolygon est plus sûr que Polygon (gère les enclaves)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return f"{self.nom_departement} ({self.nom_region})"


# 2. Le Contenu : La Production (Données Métier)
class Production(models.Model):
    SECTEURS = (
        ('AGRICULTURE', 'Agriculture'),
        ('ELEVAGE', 'Elevage'),
        ('PECHE', 'Pêche'),
    )

    # Clé étrangère vers le département (Liaison Spatiale <-> Données)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='productions')

    secteur = models.CharField(max_length=20, choices=SECTEURS)
    filiere = models.CharField(max_length=100)  # ex: Cacao, Coton
    volume_tonnes = models.FloatField()
    annee = models.IntegerField(default=2025)

    def __str__(self):
        return f"{self.filiere} - {self.departement.nom_departement}"