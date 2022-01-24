from django.shortcuts import render
from famille.models import Employeur
from contrat.models import (Contrat, 
                            Enfant, 
                            Remuneration, 
                            CongePaye,
                            )


# Create your views here.
def index(request):
    """ """
    employeurs = Employeur.objects.all()
    contrats = Contrat.objects.all()
    enfants = Enfant.objects.all()
    remunerations = Remuneration.objects.all()
    conges = CongePaye.objects.all()
    context = {"employeurs":employeurs,
               "contrats":contrats,
               "enfants":enfants,
               "remunerations":remunerations,
               "conges":conges,
               }
    
    return render(request, "dashboard/base_dashboard.html", context)


def Contrat_Vierge(request):
    """"""
    return render(request, "dashboard/contrat_vierge.html")


