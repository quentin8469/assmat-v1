
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from contrat.views import (ContratView,
                           ContratCreate,
                           EnfantView,
                           RemunerationView,
                           CongePayeView,
                           
                           )

app_name = "contrat"

urlpatterns = [
    path('', ContratView.as_view() , name='liste_contrats'),
    path('creation_contrat/', ContratCreate.as_view() , name='creation_contrats'),
    path('liste_enfants/', EnfantView.as_view() , name='liste_enfants'),
    path('liste_remunerations/', RemunerationView.as_view(), name='liste_remunerations'),
    path('liste_congepayer/', CongePayeView.as_view() , name='liste_congepayer'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)