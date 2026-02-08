import csv
import os
from django.core.management.base import BaseCommand
from core.models import Departement, Production


class Command(BaseCommand):
    help = 'Charge les données de production depuis le CSV'

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(os.getcwd(), 'data', 'production_agri_2025.csv')

        if not os.path.exists(csv_path):
            self.stdout.write(self.style.ERROR("Fichier CSV introuvable !"))
            return

        print("🔄 Chargement des productions...")

        Production.objects.all().delete()

        compteur = 0
        erreurs = 0

        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:

                    dept = Departement.objects.get(
                        nom_departement=row['departement'],
                        nom_region=row['region']
                    )


                    Production.objects.create(
                        departement=dept,
                        secteur=row['secteur'],
                        filiere=row['filiere'],
                        volume_tonnes=float(row['volume_tonnes']),
                        annee=int(row['annee'])
                    )
                    compteur += 1

                except Departement.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"⚠️ Département inconnu : {row['departement']}"))
                    erreurs += 1
                except Exception as e:
                    print(f"Erreur ligne : {e}")

        self.stdout.write(self.style.SUCCESS(f"✅ Terminé ! {compteur} lignes importées. ({erreurs} erreurs)"))