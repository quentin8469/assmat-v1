
from django.views.generic import ListView
from famille.models import Employeur


class EmployeurView(ListView):
    model = Employeur
    context_object_name = 'employeurs'
    tempalte_name = 'famille/liste_famille.html'