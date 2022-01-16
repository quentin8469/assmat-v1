
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


from famille.models import Employeur

from famille.forms import NewEmployeurForm

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
    pass

class EmployeurDeleteView(DeleteView):
    model = Employeur
    context_object_name = "employeur"
    template_name ='famille/employeur_delete.html'
    success_url = '/liste_employeurs/'
    