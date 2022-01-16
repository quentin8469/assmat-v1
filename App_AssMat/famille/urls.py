from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from famille.views import EmployeurView, EmployeurCreate, EmployeurDetail, EmployeurDeleteView, EmployeurUpdateView


# Create your views here.
app_name = 'famille'

urlpatterns = [
    path('', EmployeurView.as_view(), name='liste_employeurs'),
    path('creation_employeur/', EmployeurCreate.as_view(), name='creation_employeur'),
    path('<int:pk>/', EmployeurDetail.as_view(), name='details_employeur'),
    path('<int:pk>/edit/', EmployeurUpdateView.as_view(), name='editter_employeur'),
    path('<int:pk>/delete/', EmployeurDeleteView.as_view(), name='effacer_employeur'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)