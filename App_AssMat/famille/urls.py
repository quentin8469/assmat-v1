from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from famille.views import EmployeurView


# Create your views here.
app_name = 'famille'

urlpatterns = [
    path('liste_employeurs/', EmployeurView.as_view(), name='liste_employeurs')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)