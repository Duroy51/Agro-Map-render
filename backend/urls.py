from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Route pour l'administration (http://127.0.0.1:8000/admin/)
    path('admin/', admin.site.urls),

    # Route pour ton API (http://127.0.0.1:8000/api/departements/)
    # On délègue tout ce qui commence par 'api/' au fichier urls.py de l'app 'core'
    path('', include('core.urls')),
]