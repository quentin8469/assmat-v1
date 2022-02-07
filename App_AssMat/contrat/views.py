
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from contrat.models import Contrat, Enfant, Remuneration, CongePaye
from famille.models import Employeur, ContactUrgence
from contrat.forms import NewContratForm, NewEnfantForm

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


class EnfantCreate(CreateView):
    model = Enfant
    form_class = NewEnfantForm
    template_name = 'contrat/enfant_create.html'
    success_url = '/dashboard/'
    
# details
class EnfantDetail(DetailView):
    model = Enfant
    context_object_name = "enfant"
    template_name = 'contrat/enfant_details.html'
    success_url = '/dashboard/'
    
    def get_context_data(self, **kwargs):
        context = {}
        enfant = Enfant.objects.get(id=self.kwargs["pk"])
        contrat = Contrat.objects.get(id=enfant.contrat.id)
        employeur = Employeur.objects.get(id=contrat.id)
        contacts_urgences = ContactUrgence.objects.filter(employeur=employeur)
        context['contacts_urgences'] = contacts_urgences
        return super().get_context_data(**context) # get the default context data
        
    
# Update
class EnfantUpdateView(UpdateView):
    model = Enfant
    form_class = NewEnfantForm
    context_object_name = "enfants"
    template_name = 'contrat/enfant_create.html'
    success_url = '/dashboard/'

# Delete 
class EnfantDeleteView(DeleteView):
    model = Enfant
    context_object_name = "enfants"
    template_name = 'contrat/enfant_delete.html'
    success_url = '/dashboard/'