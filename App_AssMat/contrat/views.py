
from django.views.generic import ListView, CreateView

from contrat.models import Contrat
from contrat.forms import NewContratForm

# Contrat CRUD

class ContratView(ListView):
    model = Contrat
    context_object_name = 'contrats'
    template_name = 'contrat/contrat_list.html'
    
class ContratCreate(CreateView):
    model = Contrat
    form_class = NewContratForm
    template_name = 'contrat/contrat_create.html'
    success_url = '/dashboard/'
