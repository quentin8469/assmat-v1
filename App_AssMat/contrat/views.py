
from django.views.generic import ListView, CreateView

from contrat.models import Contrat, Enfant, Remuneration, CongePaye
from contrat.forms import NewContratForm

# Liste

class ContratView(ListView):
    model = Contrat
    context_object_name = 'contrats'
    template_name = 'contrat/contrat_list.html'


class EnfantView(ListView):
    model = Enfant
    context_object_name = 'enfants'
    template_name = 'contrat/enfant_list.html'


class RemunerationView(ListView):
    model = Remuneration
    context_object_name = 'remunerations'
    template_name = 'contrat/remuneration_list.html'

    
class CongePayeView(ListView):
    model = CongePaye
    context_object_name = 'conges'
    template_name = 'contrat/conge_list.html'
    
# Create   
class ContratCreate(CreateView):
    model = Contrat
    form_class = NewContratForm
    template_name = 'contrat/contrat_create.html'
    success_url = '/dashboard/'