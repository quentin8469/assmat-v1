
from django.views.generic import ListView
from famille.models import Employeur


class EmployeurView(ListView):
    model = Employeur
    #queryset = Employeur.objects.all()
    context_object_name = "employeurs"
    