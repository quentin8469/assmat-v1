from django.urls import path
from dashboard.views import index

urlpatterns = [
    path('dashboard/', index)
]

