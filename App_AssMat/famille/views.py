
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse

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
       success_url = '/dashboard/'
       
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
    
    def get_queryset(self):
        queryset = ContactUrgence.objects.filter(employeur=self.kwargs['pk'])
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # get the default context data
        context['employeur_id'] = self.kwargs["pk"]
        return context


class ContactUrgenceDetail(DetailView):
    model = ContactUrgence
    context_object_name = "contacts_urgences"
    template_name ='famille/urgence_details.html'
    success_url = '/liste_employeurs/'
    

class ContactUrgenceCreate(CreateView):
    model = ContactUrgence
    form_class = NewContactUrgenceForm
    template_name ='famille/urgence_create.html'
    
    
    def form_valid(self, form):
        form.instance.employeur = Employeur.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("famille:liste_contact_urgence", kwargs={"pk": self.kwargs["pk"]})
    
class ContactUrgenceUpdateView(UpdateView):
    model = ContactUrgence
    form_class = NewContactUrgenceForm
    context_object_name = "contacts_urgences"
    template_name ='famille/urgence_create.html'
    
    
    def get_success_url(self):
        contact_urgence = ContactUrgence.objects.get(id=self.kwargs["pk"])
        employeur = Employeur.objects.get(id=contact_urgence.employeur.id)
        return reverse("famille:liste_contact_urgence", kwargs={"pk": employeur.id})
    
class ContactUrgenceDeleteView(DeleteView):
    model = ContactUrgence
    context_object_name = "contacts_urgences"
    template_name ='famille/urgence_delete.html'
    
    
    def get_success_url(self):
        contact_urgence = ContactUrgence.objects.get(id=self.kwargs["pk"])
        employeur = Employeur.objects.get(id=contact_urgence.employeur.id)
        return reverse("famille:liste_contact_urgence", kwargs={"pk": employeur.id})