
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


from famille.models import Employeur, ContactUrgence

from famille.forms import NewEmployeurForm, NewContactUrgenceForm


# Employeur class CRUD

class EmployeurView(ListView):
    model = Employeur
    #queryset = Employeur.objects.all()
    context_object_name = "employeurs"
    template_name = "famille/employeur_list.html"


class EmployeurCreate(CreateView):
       model = Employeur
       form_class = NewEmployeurForm
       template_name = "famille/employeur_create.html"
       success_url = '/liste_employeurs/'
       
       def form_valid(self, form):
           form.instance.ass_mat = self.request.user
           return super().form_valid(form)
       

class EmployeurDetail(DetailView):
    model = Employeur
    template_name = "famille/employeur_details.html"
    context_object_name = "employeur"
    

class EmployeurUpdateView(UpdateView):
    model = Employeur
    form_class = NewEmployeurForm
    template_name = "famille/employeur_create.html"
    success_url = '/liste_employeurs/'
    

class EmployeurDeleteView(DeleteView):
    model = Employeur
    context_object_name = "employeur"
    template_name ='famille/employeur_delete.html'
    success_url = '/liste_employeurs/'


#Contact Urgence CRUD
   
class ContactUrgenceView(ListView):
    model = ContactUrgence
    context_object_name = "contacts_urgences"
    template_name ='famille/urgence_list.html'
    success_url = '/liste_employeurs/'
    

class ContactUrgenceDetail(DetailView):
    model = ContactUrgence
    context_object_name = "contacts_urgences"
    template_name ='famille/urgence_details.html'
    success_url = '/liste_employeurs/'
    

class ContactUrgenceCreate(CreateView):
    model = ContactUrgence
    form_class = NewContactUrgenceForm
    template_name ='famille/urgence_create.html'
    success_url = '/liste_employeurs/'
    
    def form_valid(self, form):

        form.instance.ContactUrgence = self.kwargs['employeur']
        return super().form_valid(form)

class ContactUrgenceUpdateView(UpdateView):
    model = ContactUrgence
    context_object_name = "contacts_urgences"
    template_name ='famille/urgence_create.html'
    success_url = '/liste_employeurs/'
    

class ContactUrgenceDeleteView(DeleteView):
    model = ContactUrgence
    context_object_name = "contacts_urgences"
    template_name ='famille/urgence_delete.html'
    success_url = '/liste_employeurs/'
    