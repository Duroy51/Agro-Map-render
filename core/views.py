from rest_framework import viewsets
from .models import Departement
from .serializers import DepartementSerializer
from django.shortcuts import render

class DepartementViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint qui permet de voir les départements et leurs productions.
    ReadOnlyModelViewSet = On peut lire, mais pas modifier (sécurité).
    """
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer


def index(request):
    return render(request, 'core/index.html')