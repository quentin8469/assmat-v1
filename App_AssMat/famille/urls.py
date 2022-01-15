from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from famille.views import EmployeurView, EmployeurCreate


# Create your views here.
app_name = 'famille'

urlpatterns = [
    path('', EmployeurView.as_view(), name='liste_employeurs'),
    path('creation_employeur/', EmployeurCreate.as_view(), name='creation_employeur'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)