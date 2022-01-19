from django.shortcuts import render
from famille.models import Employeur
from contrat.models import Contrat


# Create your views here.
def index(request):
    """ """
    employeurs = Employeur.objects.all()
    contrats = Contrat.objects.all()
    context = {"employeurs":employeurs,
               "contrats":contrats}
    
    return render(request, "dashboard/base_dashboard.html", context)


