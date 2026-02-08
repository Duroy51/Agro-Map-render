
# PROJET WEB-MAPPING 5GI : Cartographie des Bassins de Production du Cameroun (2025-2026)

## Description du Projet

Ce projet a été réalisé dans le cadre du cursus d'Ingénierie 5GI (Année académique 2025-2026). Il s'agit d'un Système d'Information Géographique (SIG) Web interactif conçu pour visualiser, analyser et comparer les performances économiques des différentes divisions administratives du Cameroun (Régions et Départements).

L'application permet aux décideurs d'identifier les bassins de production majeurs pour trois secteurs clés :
1.  **Agriculture** (Cultures de rente et vivrières).
2.  **Élevage** (Bétail, volaille).
3.  **Pêche** (Maritime et continentale).

## Fonctionnalités Principales

*   **Cartographie Interactive :** Visualisation des 10 régions et 58 départements du Cameroun via Leaflet.js.
*   **Tableau de Bord Dynamique :** Affichage des statistiques de production (volumes en tonnes, répartition par filière) au clic sur une zone administrative.
*   **Comparateur de Bassins :** Outil d'aide à la décision permettant de confronter les performances de deux départements côte à côte via des graphiques comparatifs.
*   **Cartographie Thématique :** Filtrage dynamique par filière (ex: Cacao, Coton, Café) avec gradation des couleurs selon l'intensité de la production.
*   **Moteur de Recherche :** Localisation rapide d'un département avec zoom automatique.

## Architecture Technique

Le projet repose sur une architecture moderne séparant la logique métier (Backend) de l'interface utilisateur (Frontend), communiquant via une API REST.

### Backend (Serveur & API)
*   **Langage :** Python 3.10+
*   **Framework :** Django 5.x
*   **API :** Django REST Framework (DRF) + DRF-GIS
*   **Traitement Spatial :** GeoDjango

### Base de Données (Spatiale)
*   **SGBD :** PostgreSQL 15+
*   **Extension Spatiale :** PostGIS 3.x (Stockage des polygones et calculs spatiaux)

### Frontend (Client)
*   **Structure :** HTML5 / CSS3
*   **Framework CSS :** Bootstrap 5.3 (Design Responsive & Glassmorphism)
*   **Cartographie :** Leaflet.js
*   **Visualisation de Données :** Chart.js (Graphiques circulaires et histogrammes)
*   **Interactivité :** JavaScript (ES6), jQuery, Select2

---

## Guide d'Installation (Déploiement Local)

Ce guide suppose que vous disposez d'un environnement Windows avec Python et PostgreSQL installés.

### 1. Pré-requis Système

Assurez-vous d'avoir installé les outils suivants :
*   **Python** (version 3.9 ou supérieure).
*   **PostgreSQL** (avec l'extension PostGIS installée via StackBuilder).
*   **QGIS** (Recommandé pour les bibliothèques GDAL/GEOS nécessaires à GeoDjango sous Windows).

### 2. Configuration de la Base de Données

Ouvrez pgAdmin ou votre terminal SQL et exécutez les commandes suivantes :

```sql
-- Création de la base de données
CREATE DATABASE cam_agri_db;

-- Connexion à la base (si en ligne de commande)
\c cam_agri_db

-- Activation de l'extension spatiale (Impératif)
CREATE EXTENSION postgis;
```

### 3. Installation du Code Source

Décompressez l'archive du projet et ouvrez un terminal dans le dossier racine.

**a. Création de l'environnement virtuel :**
```bash
python -m venv venv
```

**b. Activation de l'environnement :**
*   Sous Windows : `venv\Scripts\activate`
*   Sous Linux/Mac : `source venv/bin/activate`

**c. Installation des dépendances Python :**
```bash
pip install -r requirements.txt
```

### 4. Configuration de Django

**a. Migrations (Création des tables) :**
```bash
python manage.py makemigrations
python manage.py migrate
```
*Note : Si une erreur GDAL survient sous Windows, le fichier `settings.py` contient déjà une configuration automatique pour détecter QGIS. Assurez-vous simplement que QGIS est installé dans `C:\Program Files` ou `C:\Programmes`.*

**b. Peuplement de la Base de Données (Données Initiales) :**
Le projet inclut des scripts automatisés pour charger la géographie et les données économiques simulées. Exécutez-les dans cet ordre précis :

1.  Chargement des frontières administratives (Shapefiles) :
    ```bash
    python manage.py load_geography
    ```
2.  Chargement des données de production (Statistiques métier) :
    ```bash
    python manage.py load_production
    ```

### 5. Lancement de l'Application

Démarrez le serveur de développement local :

```bash
python manage.py runserver
```

Ouvrez votre navigateur web et accédez à l'adresse suivante :
**http://127.0.0.1:8000/**

---

## Structure du Projet

*   **`backend/`** : Configuration principale du projet Django (`settings.py`, `urls.py`).
*   **`core/`** : Application principale contenant la logique métier.
    *   `models.py` : Définition des modèles de données (Departement, Production).
    *   `views.py` : Logique d'affichage et endpoints API.
    *   `serializers.py` : Transformation des données en GeoJSON.
    *   `management/commands/` : Scripts d'importation des données (ETL).
    *   `templates/` : Fichiers HTML (Interface utilisateur).
*   **`data/`** : Contient les fichiers sources bruts.
    *   `gadm41_CMR_2.shp` : Données vectorielles (GADM).
    *   `production_agri_2025.csv` : Données statistiques consolidées.

## Sources de Données et Méthodologie

Les données exploitées dans ce Système d'Information Géographique proviennent de la consolidation de sources institutionnelles officielles et de rapports sectoriels, harmonisées pour la campagne agricole de référence 2025-2026.

### 1. Données Géographiques (Référentiel Spatial)
*   **Limites Administratives :** Extraction issue de la base **GADM** (Global Administrative Areas), standardisée au niveau 2 (Départements).
*   **Traitement Topologique :** Les couches vectorielles ont été corrigées (nettoyage des géométries, vérification des systèmes de coordonnées WGS84) via QGIS avant intégration dans PostGIS.

### 2. Données Économiques (Attributs Métier)
Les volumes de production intégrés au système résultent du croisement de plusieurs flux d'information :

*   **INS Cameroun (Institut National de la Statistique) :** Données issues des Annuaires Statistiques Régionaux (Chapitre Secteur Primaire).
*   **MINADER (Ministère de l'Agriculture et du Développement Rural) :** Rapports de synthèse des délégations régionales concernant les cultures de rente (Cacao, Café, Coton, Hévéa) et les cultures vivrières (Maïs, Manioc, Plantain).
*   **MINEPIA (Ministère de l'Élevage, des Pêches et des Industries Animales) :** Statistiques annuelles sur le cheptel (Bovins, Ovins, Volaille) et les captures halieutiques (Pêche maritime, continentale et aquaculture).
*   **Organismes de Développement :** Données spécifiques aux filières stratégiques (SODECOTON pour la zone septentrionale, SODECAO pour la zone forestière).

*Note méthodologique : Les données brutes ont fait l'objet d'un traitement ETL (Extract, Transform, Load) pour assurer leur cohérence spatiale avec le découpage administratif de 2025.*
## Auteurs

**Groupe de Projet 5GI - Promotion 2026**
*   [Nom de l'étudiant 1] - Chef de Projet / Backend Lead
*   [Nom de l'étudiant 2] - Architecte Base de Données Spatiale
*   [Nom de l'étudiant 3] - Frontend Developer / UI-UX
*   [Nom de l'étudiant 4] - Analyste de Données
*   [Nom de l'étudiant 5] - Intégrateur & Testeur