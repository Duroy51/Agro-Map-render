from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartementViewSet, index

# Création du routeur automatique
router = DefaultRouter()
# On enregistre la route "departements"
router.register(r'departements', DepartementViewSet)

urlpatterns = [
    path('api/', include(router.urls)), # L'API reste accessible sur /api/
    path('', index, name='home'),       # La page d'accueil (racine du site)
]