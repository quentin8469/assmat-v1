
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from contrat.views import (ContratView,
                           ContratCreate,
                           )

app_name = "contrat"

urlpatterns = [
    path('', ContratView.as_view() , name='liste_contrats'),
    path('creation_contrat/', ContratCreate.as_view() , name='creation_contrats'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)