from django.urls import path
from dashboard.views import index
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

