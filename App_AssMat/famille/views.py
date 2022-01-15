
from django.views.generic import ListView, CreateView


from famille.models import Employeur

from famille.forms import NewEmployeurForm

class EmployeurView(ListView):
    model = Employeur
    #queryset = Employeur.objects.all()
    context_object_name = "employeurs"


class EmployeurCreate(CreateView):
       model = Employeur
       form_class = NewEmployeurForm
       template_name = "famille/employeur_create.html"
       success_url = '/liste_employeurs/'
       
       def form_valid(self, form):
           form.instance.ass_mat = self.request.user
           return super().form_valid(form)
       
       