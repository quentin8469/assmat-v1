from django.urls import path
from django.urls.conf import include, include
from dashboard.views import index, Contrat_Vierge
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dashboard'

urlpatterns = [
    path('', index, name='dashboard'),
    path('contrat_vierge/', Contrat_Vierge , name='contrat_vierge'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

